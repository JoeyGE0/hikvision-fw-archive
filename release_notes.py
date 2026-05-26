#!/usr/bin/env python3
"""Fetch and summarize Hikvision release-note PDFs."""
from __future__ import annotations

import io
import logging
import re
from typing import Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)

# Order matters: longer / more specific patterns first.
SECTION_HEADERS = (
    r'new\s*(?:&\s*)?optimized\s*features',
    r'new\s+features?',
    r'modified\s+features',
    r'modify\s+features',
    r'modify\s+function',
    r'improved\s+functionality',
    r'bug\s+fixes?',
    r'issues?\s*fixes?',
    r'features?',
    r'improvements?',
    r'enhancements?',
    r'changes?',
)

STOP_HEADERS = (
    r'customer\s+impact',
    r'recommended\s+action',
    r'supported\s+product',
    r'product\s+category',
    r'model\s+number',
    r'firmware\s+basic\s+information',
    r'firmware\s+version',
    r'release\s+note',
    r'remarks:?',
    r'note',
    r'hikvision\s+digital',
    r'tel:',
    r'email:',
    r'no\.\s*\d+.*road',
)

# Leading bullets, numbering (1), 1.1), and CJK colon variants.
LINE_PREFIX_RE = re.compile(
    r'^[\s•\u2022\uf06c\uf0b7\-*]+|'
    r'^(?:\d+(?:\.\d+)*)[\).\s：:]+',
    re.IGNORECASE,
)

SECTION_START_RE = re.compile(
    rf'^({"|".join(SECTION_HEADERS)})\s*(?:[：:].*)?$',
    re.IGNORECASE,
)
STOP_RE = re.compile(
    rf'^({"|".join(STOP_HEADERS)})\b',
    re.IGNORECASE,
)

# Section titles echoed as content — skip these lines.
_SECTION_TITLE_ONLY = re.compile(
    rf'^({"|".join(SECTION_HEADERS)})\s*(?:[：:])?\s*$',
    re.IGNORECASE,
)

_VERSION_LINE = re.compile(
    r'^v?\d+\.\d+',
    re.IGNORECASE,
)

_SKIP_CONTENT_LINE = re.compile(
    r'release\s+note|product\s+category|model\s+number|'
    r'firmware\s+basic|firmware\s+version|'
    r'\bDS-[A-Z0-9]{2,}',
    re.IGNORECASE,
)


def normalize_pdf_text(text: str) -> str:
    if not text:
        return ''
    text = text.replace('\r', '\n')
    text = re.sub(r'[\x00-\x08\x0b\x0c\x0e-\x1f]', ' ', text)
    text = re.sub(r'[ \t]+', ' ', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def strip_line_prefix(line: str) -> str:
    """Remove PDF bullets and numbered list prefixes from a line."""
    line = (line or '').strip()
    while line:
        new = LINE_PREFIX_RE.sub('', line, count=1).strip()
        if new == line:
            break
        line = new
    return line


def _clean_content_line(line: str) -> str:
    line = strip_line_prefix(line)
    line = line.strip(' •\t\u2022\uf06c\uf0b7-*')
    line = re.sub(r'\s+', ' ', line).strip()
    return line


def _is_section_header(line: str) -> bool:
    return bool(SECTION_START_RE.match(line))


def _is_stop_header(line: str) -> bool:
    return bool(STOP_RE.match(line))


def _collect_section_lines(text: str) -> List[List[str]]:
    """Return change lines grouped by detected section."""
    sections: List[List[str]] = []
    current: Optional[List[str]] = None

    for raw in text.split('\n'):
        line = _clean_content_line(raw)
        if not line:
            continue
        if _VERSION_LINE.match(line):
            continue
        if _is_stop_header(line):
            if current:
                sections.append(current)
            current = None
            continue
        if _is_section_header(line):
            if current:
                sections.append(current)
            current = []
            continue
        if _SECTION_TITLE_ONLY.match(line):
            continue
        if len(line) < 8:
            continue
        if _SKIP_CONTENT_LINE.search(line):
            continue
        if current is not None:
            current.append(line)

    if current:
        sections.append(current)
    return sections


def _fallback_chunks(text: str) -> List[str]:
    """Last resort when no section headers matched."""
    patterns = (
        r'(?:New\s*(?:&\s*)?Optimized\s*)?Features?\s*(.{20,280}?)(?:Customer\s+Impact|Supported\s+Product|Note\b|$)',
        r'Modify\s+(?:Function|Features)\s*(.{15,280}?)(?:Customer\s+Impact|Supported\s+Product|Note\b|$)',
        r'Modified\s+Features\s*(.{15,200}?)(?:Customer\s+Impact|Supported\s+Product|$)',
        r'Issues?\s*fixes?\s*[：:]?\s*(.{15,200}?)(?:Customer\s+Impact|Supported\s+Product|$)',
        r'(Fixed\s+[^.]{15,200}\.)',
        r'(Fix(?:ed)?\s+[^.]{12,200}\.)',
        r'(Improve[^.]{10,200}\.)',
    )
    for pattern in patterns:
        m = re.search(pattern, text, re.IGNORECASE | re.DOTALL)
        if not m:
            continue
        snippet = re.sub(r'\s+', ' ', m.group(1)).strip(' •\t-')
        snippet = re.sub(
            r'^(?:\d+[\).]\s*)+',
            '',
            snippet,
            flags=re.IGNORECASE,
        ).strip()
        if len(snippet) >= 12 and not _is_stop_header(snippet):
            return [snippet]
    return []


def extract_changes_summary(text: str, max_len: int = 420) -> str:
    """Pull short change bullets from release-note PDF plain text."""
    text = normalize_pdf_text(text)
    if not text:
        return ''

    chunks: List[str] = []
    for section_lines in _collect_section_lines(text):
        for line in section_lines[:5]:
            if _is_section_header(line) or _is_stop_header(line):
                continue
            chunks.append(line)
            if len(chunks) >= 6:
                break
        if len(chunks) >= 6:
            break

    if not chunks:
        chunks = _fallback_chunks(text)

    if not chunks:
        return ''

    seen: set[str] = set()
    unique: List[str] = []
    for c in chunks:
        key = c.lower()
        if key in seen:
            continue
        seen.add(key)
        unique.append(c)

    summary = ' · '.join(unique[:4])
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
