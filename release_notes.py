#!/usr/bin/env python3
"""Fetch and summarize Hikvision release-note PDFs."""
from __future__ import annotations

import io
import logging
import re
from typing import Dict, Optional

logger = logging.getLogger(__name__)

# Section headers we care about (case-insensitive line starts)
SECTION_HEADERS = (
    r'new features?',
    r'modify function',
    r'features?',
    r'improvements?',
    r'improved functionality',
    r'bug fixes?',
    r'fixed',
    r'changes?',
    r'enhancements?',
)

STOP_HEADERS = (
    r'customer impact',
    r'recommended action',
    r'supported product',
    r'product category',
    r'model number',
    r'remarks:?',
    r'hikvision digital',
    r'firmware basic information',
    r'tel:',
    r'email:',
    r'no\.\s*\d+.*road',
)

SECTION_START_RE = re.compile(
    rf'^({"|".join(SECTION_HEADERS)})\b',
    re.IGNORECASE | re.MULTILINE,
)
STOP_RE = re.compile(
    rf'^({"|".join(STOP_HEADERS)})\b',
    re.IGNORECASE | re.MULTILINE,
)


def normalize_pdf_text(text: str) -> str:
    if not text:
        return ''
    text = text.replace('\r', '\n')
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', ' ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def extract_changes_summary(text: str, max_len: int = 420) -> str:
    """Pull short change bullets from release-note PDF plain text."""
    text = normalize_pdf_text(text)
    if not text:
        return ''

    chunks: list[str] = []
    for match in SECTION_START_RE.finditer(text):
        start = match.end()
        rest = text[start:]
        stop = STOP_RE.search(rest)
        section_body = rest[: stop.start() if stop else len(rest)]
        section_body = normalize_pdf_text(section_body)
        if not section_body:
            continue
        lines = []
        for line in section_body.split('\n'):
            line = line.strip(' •\t\u2022\uf06c\uf0b7-*')
            line = re.sub(r'\s+', ' ', line).strip()
            if len(line) < 8:
                continue
            if STOP_RE.match(line):
                break
            if SECTION_START_RE.match(line):
                break
            if re.match(r'^v?\d+\.\d+', line, re.I):
                continue
            lines.append(line)
        if lines:
            chunks.extend(lines[:4])

    if not chunks:
        # Fallback: grab first substantive sentence after "Modify Function" style keywords inline
        for pattern in (
            r'(?:New Features|Modify Function|Features)\s*(.{20,220}?)(?:Customer Impact|Supported Product|$)',
            r'(Fixed [^.]{15,200}\.)',
            r'(Improve[^.]{10,200}\.)',
        ):
            m = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
            if m:
                snippet = re.sub(r'\s+', ' ', m.group(1)).strip()
                if snippet:
                    chunks.append(snippet)
                    break

    if not chunks:
        return ''

    seen: set[str] = set()
    unique: list[str] = []
    for c in chunks:
        key = c.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(c)

    summary = ' · '.join(unique[:3])
    summary = re.sub(r'\s+', ' ', summary).strip()
    if len(summary) > max_len:
        summary = summary[: max_len - 1].rsplit(' ', 1)[0] + '…'
    return summary


def pdf_text_from_bytes(data: bytes) -> str:
    try:
        from pypdf import PdfReader
    except ImportError:
        logger.warning('pypdf not installed — cannot parse release-note PDFs')
        return ''
    try:
        reader = PdfReader(io.BytesIO(data))
        parts = []
        for page in reader.pages[:6]:
            parts.append(page.extract_text() or '')
        return '\n'.join(parts)
    except Exception as exc:
        logger.debug('PDF parse failed: %s', exc)
        return ''


def fetch_pdf_summary(
    url: str,
    cache: Dict[str, Dict],
    headers: Optional[Dict[str, str]] = None,
    timeout: int = 45,
) -> str:
    """Download PDF (with cache), return short changes summary."""
    url = (url or '').strip()
    if not url or not url.lower().endswith('.pdf'):
        return ''
    if url in cache and cache[url].get('changes'):
        return cache[url]['changes']

    try:
        import requests
    except ImportError:
        return ''

    try:
        resp = requests.get(url, headers=headers or {}, timeout=timeout)
        resp.raise_for_status()
        if 'pdf' not in (resp.headers.get('content-type') or '').lower() and not resp.content[:4] == b'%PDF':
            return ''
        text = pdf_text_from_bytes(resp.content)
        summary = extract_changes_summary(text)
        if summary:
            cache[url] = {'changes': summary, 'source': 'pdf'}
        return summary
    except Exception as exc:
        logger.debug('Release notes fetch failed for %s: %s', url[:80], exc)
        return ''
