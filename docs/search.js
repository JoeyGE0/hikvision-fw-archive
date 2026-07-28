(function () {
  "use strict";

  var data = null;
  var catalog = []; // { name, compact, tokens, latestByHw }
  var lastHits = [];

  var q = document.getElementById("q");
  var clearBtn = document.getElementById("clear");
  var statusEl = document.getElementById("status");
  var hitsSection = document.getElementById("hits");
  var hitsTitle = document.getElementById("hits-title");
  var hitsCount = document.getElementById("hits-count");
  var hitList = document.getElementById("hit-list");
  var detail = document.getElementById("detail");
  var emptyHint = document.getElementById("empty-hint");
  var detailModel = document.getElementById("detail-model");
  var detailMeta = document.getElementById("detail-meta");
  var hwSelect = document.getElementById("hw");
  var rows = document.getElementById("rows");
  var backBtn = document.getElementById("back");
  var footMeta = document.getElementById("foot-meta");

  function setStatus(text, isError) {
    statusEl.textContent = text || "";
    statusEl.className = isError ? "status error" : "status";
  }

  function compact(s) {
    return String(s || "")
      .toUpperCase()
      .replace(/[^A-Z0-9]/g, "");
  }

  function tokens(s) {
    return String(s || "")
      .toUpperCase()
      .match(/[A-Z]+|\d+/g) || [];
  }

  function latestForEntry(entry) {
    var hw = entry.hw || {};
    var best = null;
    Object.keys(hw).forEach(function (h) {
      var builds = hw[h] || [];
      if (!builds.length) return;
      var cand = { hw: h, build: builds[0] };
      if (!best) {
        best = cand;
        return;
      }
      // Prefer IPC_* hardware, then newer-looking version string length/date
      var preferHw =
        cand.hw.indexOf("IPC_") === 0 && best.hw.indexOf("IPC_") !== 0;
      if (preferHw) {
        best = cand;
        return;
      }
      if ((cand.build.d || "") > (best.build.d || "")) best = cand;
    });
    return best;
  }

  function buildCatalog(models) {
    catalog = Object.keys(models).map(function (name) {
      var entry = models[name];
      return {
        name: name,
        compact: compact(name),
        tokens: tokens(name),
        latest: latestForEntry(entry),
        entry: entry,
      };
    });
  }

  function scoreMatch(query, item) {
    var raw = String(query || "").trim();
    if (!raw) return 0;

    var qCompact = compact(raw);
    var qTokens = tokens(raw);
    if (!qCompact && !qTokens.length) return 0;

    var score = 0;
    var name = item.name.toUpperCase();
    var c = item.compact;
    var nameTokens = item.tokens;

    if (c === qCompact) return 10000;
    if (c.indexOf(qCompact) === 0) score += 5000 - Math.min(c.length, 400);
    else if (name.indexOf(raw.toUpperCase()) === 0) score += 4500;
    else if (
      c.indexOf(qCompact) > -1 &&
      qTokens.length <= 1 &&
      !/^\d+$/.test(qCompact)
    ) {
      // Letter-ish queries (LIS2UY) can use compact substring; bare digits cannot
      // (otherwise 4238-7 falsely matches 2387).
      score += 2500 - Math.min(c.indexOf(qCompact), 400);
    }

    if (qTokens.length) {
      for (var i = 0; i < qTokens.length; i++) {
        var t = qTokens[i];
        var isDigits = /^\d+$/.test(t);
        var hit = false;

        if (isDigits) {
          for (var j = 0; j < nameTokens.length; j++) {
            var nt = nameTokens[j];
            if (!/^\d+$/.test(nt)) continue;
            if (
              nt === t ||
              nt.indexOf(t) === 0 ||
              (t.indexOf(nt) === 0 && nt.length >= 3)
            ) {
              hit = true;
              score += 120 + t.length * 15;
              if (nt === t) score += 200;
              break;
            }
          }
        } else if (c.indexOf(t) > -1 || name.indexOf(t) > -1) {
          hit = true;
          score += t.length >= 3 ? 90 + t.length * 10 : 25;
        }

        if (!hit) return 0;
      }
    } else if (score === 0) {
      return 0;
    }

    score += Math.max(0, 140 - Math.min(item.name.length, 140));
    if (item.name.indexOf("(") === -1) score += 30;
    return score;
  }

  function findMatches(query, limit) {
    limit = limit || 40;
    var scored = [];
    for (var i = 0; i < catalog.length; i++) {
      var item = catalog[i];
      var sc = scoreMatch(query, item);
      if (sc > 0) scored.push({ item: item, score: sc });
    }
    scored.sort(function (a, b) {
      if (b.score !== a.score) return b.score - a.score;
      return a.item.name.localeCompare(b.item.name);
    });
    return scored.slice(0, limit);
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function highlight(name, query) {
    var qTokens = tokens(query).filter(function (t) {
      return t.length >= 2;
    });
    if (!qTokens.length) return escapeHtml(name);

    // Highlight compact-insensitive chunks by scanning original string
    var upper = name.toUpperCase();
    var marks = [];
    qTokens.forEach(function (t) {
      var start = 0;
      while (true) {
        var idx = upper.indexOf(t, start);
        if (idx < 0) break;
        marks.push([idx, idx + t.length]);
        start = idx + t.length;
      }
    });
    if (!marks.length) return escapeHtml(name);

    marks.sort(function (a, b) {
      return a[0] - b[0];
    });
    var merged = [];
    marks.forEach(function (m) {
      var last = merged[merged.length - 1];
      if (!last || m[0] > last[1]) merged.push(m.slice());
      else last[1] = Math.max(last[1], m[1]);
    });

    var out = "";
    var cursor = 0;
    merged.forEach(function (m) {
      out += escapeHtml(name.slice(cursor, m[0]));
      out += "<mark>" + escapeHtml(name.slice(m[0], m[1])) + "</mark>";
      cursor = m[1];
    });
    out += escapeHtml(name.slice(cursor));
    return out;
  }

  function showHits(items, query) {
    lastHits = items;
    hitList.innerHTML = "";
    if (!items.length) {
      hitsSection.hidden = true;
      return;
    }

    items.forEach(function (row) {
      var item = row.item;
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "hit";
      btn.dataset.model = item.name;

      var left = document.createElement("div");
      var title = document.createElement("div");
      title.className = "hit-title";
      title.innerHTML = highlight(item.name, query);
      var sub = document.createElement("div");
      sub.className = "hit-sub";
      if (item.latest && item.latest.build) {
        sub.textContent =
          (item.latest.hw || "—") +
          " · Latest V" +
          (item.latest.build.v || "?") +
          (item.latest.build.d ? " · " + item.latest.build.d : "");
      } else {
        sub.textContent = "Firmware available";
      }
      left.appendChild(title);
      left.appendChild(sub);

      var cta = document.createElement("span");
      cta.className = "hit-cta";
      cta.textContent = "View";

      btn.appendChild(left);
      btn.appendChild(cta);
      btn.addEventListener("click", function () {
        openDetail(item.name);
      });
      hitList.appendChild(btn);
    });

    hitsTitle.textContent = "Matching products";
    hitsCount.textContent =
      items.length + (items.length >= 40 ? "+" : "") + " shown";
    hitsSection.hidden = false;
  }

  function countBuilds(entry) {
    var total = 0;
    var hw = entry.hw || {};
    Object.keys(hw).forEach(function (k) {
      total += (hw[k] || []).length;
    });
    return total;
  }

  function openDetail(model) {
    var entry = data.models[model];
    if (!entry) return;

    q.value = model;
    clearBtn.hidden = false;
    hitsSection.hidden = true;
    emptyHint.hidden = true;
    detail.hidden = false;
    setStatus("");

    var hwNames = Object.keys(entry.hw || {}).sort();
    detailModel.textContent = model;
    detailMeta.textContent =
      countBuilds(entry) +
      " build" +
      (countBuilds(entry) === 1 ? "" : "s") +
      " across " +
      hwNames.length +
      " hardware line" +
      (hwNames.length === 1 ? "" : "s");

    hwSelect.innerHTML = "";
    hwNames.forEach(function (h) {
      var opt = document.createElement("option");
      opt.value = h;
      opt.textContent = h;
      hwSelect.appendChild(opt);
    });
    var preferred = hwNames.find(function (h) {
      return h.indexOf("IPC_") === 0;
    });
    if (preferred) hwSelect.value = preferred;

    renderRows(model, hwSelect.value);

    var url = new URL(window.location.href);
    url.searchParams.set("model", model);
    url.searchParams.set("hw", hwSelect.value);
    history.replaceState(null, "", url);
  }

  function renderRows(model, hw) {
    rows.innerHTML = "";
    var builds = (((data.models[model] || {}).hw || {})[hw] || []).slice();
    if (!builds.length) {
      rows.innerHTML =
        '<tr><td colspan="4">No firmware for this hardware line.</td></tr>';
      return;
    }

    builds.forEach(function (b, i) {
      var tr = document.createElement("tr");
      if (i === 0) tr.className = "latest";

      var ver = document.createElement("td");
      ver.textContent = b.v ? "V" + b.v : "—";
      if (i === 0) {
        var tag = document.createElement("span");
        tag.className = "tag";
        tag.textContent = "Latest";
        ver.appendChild(tag);
      }

      var date = document.createElement("td");
      date.textContent = b.d || "—";

      var file = document.createElement("td");
      file.className = "file";
      file.textContent = b.f || "—";

      var action = document.createElement("td");
      if (b.u) {
        var a = document.createElement("a");
        a.className = "dl";
        a.href = b.u;
        a.textContent = "Download";
        a.rel = "noopener";
        action.appendChild(a);
      } else {
        action.textContent = "—";
      }

      tr.appendChild(ver);
      tr.appendChild(date);
      tr.appendChild(file);
      tr.appendChild(action);
      rows.appendChild(tr);
    });
  }

  function resetToSearch() {
    detail.hidden = true;
    var value = q.value.trim();
    if (!value) {
      hitsSection.hidden = true;
      emptyHint.hidden = false;
      setStatus(
        catalog.length.toLocaleString() +
          " products indexed. Type any part of a model number."
      );
      history.replaceState(null, "", window.location.pathname);
      return;
    }
    emptyHint.hidden = true;
    var matches = findMatches(value, 40);
    showHits(matches, value);
    if (!matches.length) {
      setStatus('No products match “' + value + '”. Try a shorter fragment.', true);
    } else {
      setStatus("");
    }
    var url = new URL(window.location.href);
    url.searchParams.delete("model");
    url.searchParams.delete("hw");
    if (value) url.searchParams.set("q", value);
    history.replaceState(null, "", url);
  }

  var debounceTimer = null;
  function onQueryInput() {
    clearBtn.hidden = !q.value;
    if (!data) return;
    clearTimeout(debounceTimer);
    debounceTimer = setTimeout(function () {
      detail.hidden = true;
      var value = q.value.trim();
      if (value.length < 2) {
        hitsSection.hidden = true;
        emptyHint.hidden = false;
        setStatus(
          value
            ? "Keep typing… (2+ characters)"
            : catalog.length.toLocaleString() +
                " products indexed. Type any part of a model number."
        );
        return;
      }
      emptyHint.hidden = true;
      var matches = findMatches(value, 40);
      showHits(matches, value);
      if (!matches.length) {
        setStatus(
          'No products match “' + value + '”. Try digits like 2387 or 1383.',
          true
        );
      } else {
        setStatus("");
      }
    }, 80);
  }

  q.addEventListener("input", onQueryInput);

  q.addEventListener("keydown", function (ev) {
    if (ev.key === "Enter") {
      ev.preventDefault();
      if (lastHits.length) openDetail(lastHits[0].item.name);
    } else if (ev.key === "Escape") {
      q.value = "";
      clearBtn.hidden = true;
      resetToSearch();
    }
  });

  clearBtn.addEventListener("click", function () {
    q.value = "";
    clearBtn.hidden = true;
    resetToSearch();
    q.focus();
  });

  backBtn.addEventListener("click", function () {
    resetToSearch();
    q.focus();
  });

  hwSelect.addEventListener("change", function () {
    var model = detailModel.textContent;
    renderRows(model, hwSelect.value);
    var url = new URL(window.location.href);
    url.searchParams.set("model", model);
    url.searchParams.set("hw", hwSelect.value);
    history.replaceState(null, "", url);
  });

  fetch("search-data.json", { cache: "no-cache" })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (json) {
      data = json;
      buildCatalog(data.models || {});
      var when = data.generated_at
        ? String(data.generated_at).slice(0, 19).replace("T", " ") + " UTC"
        : "unknown";
      footMeta.textContent =
        catalog.length.toLocaleString() + " products · updated " + when;

      var params = new URLSearchParams(window.location.search);
      var presetModel = params.get("model");
      var presetQ = params.get("q");

      if (presetModel && data.models[presetModel]) {
        openDetail(presetModel);
        if (params.get("hw") && data.models[presetModel].hw[params.get("hw")]) {
          hwSelect.value = params.get("hw");
          renderRows(presetModel, hwSelect.value);
        }
      } else if (presetQ) {
        q.value = presetQ;
        clearBtn.hidden = false;
        onQueryInput();
      } else {
        setStatus(
          catalog.length.toLocaleString() +
            " products indexed. Type any part of a model number."
        );
      }
    })
    .catch(function (err) {
      setStatus("Could not load search index (" + err.message + ").", true);
    });
})();
