(function () {
  "use strict";

  var data = null;
  var modelNames = [];
  var activeIndex = -1;

  var q = document.getElementById("q");
  var clearBtn = document.getElementById("clear");
  var suggestions = document.getElementById("suggestions");
  var statusEl = document.getElementById("status");
  var result = document.getElementById("result");
  var resultModel = document.getElementById("result-model");
  var resultMeta = document.getElementById("result-meta");
  var hwSelect = document.getElementById("hw");
  var rows = document.getElementById("rows");
  var footMeta = document.getElementById("foot-meta");

  function setStatus(text, isError) {
    statusEl.textContent = text || "";
    statusEl.className = isError ? "status error" : "status";
  }

  function normalize(s) {
    return String(s || "")
      .toUpperCase()
      .replace(/\s+/g, " ")
      .trim();
  }

  function scoreMatch(query, name) {
    var qn = normalize(query);
    var nn = normalize(name);
    if (!qn) return 0;
    if (nn === qn) return 1000;
    if (nn.indexOf(qn) === 0) return 800 - Math.min(nn.length, 200);
    var idx = nn.indexOf(qn);
    if (idx > 0) return 500 - idx;
    // loose: ignore some punctuation differences
    var q2 = qn.replace(/[()/.-]/g, "");
    var n2 = nn.replace(/[()/.-]/g, "");
    if (n2.indexOf(q2) === 0) return 450;
    if (n2.indexOf(q2) > -1) return 200;
    return 0;
  }

  function findMatches(query, limit) {
    limit = limit || 20;
    var scored = [];
    for (var i = 0; i < modelNames.length; i++) {
      var name = modelNames[i];
      var sc = scoreMatch(query, name);
      if (sc > 0) scored.push({ name: name, score: sc });
    }
    scored.sort(function (a, b) {
      if (b.score !== a.score) return b.score - a.score;
      return a.name.localeCompare(b.name);
    });
    return scored.slice(0, limit);
  }

  function hideSuggestions() {
    suggestions.hidden = true;
    suggestions.innerHTML = "";
    activeIndex = -1;
  }

  function renderSuggestions(items) {
    if (!items.length) {
      hideSuggestions();
      return;
    }
    suggestions.innerHTML = "";
    for (var i = 0; i < items.length; i++) {
      var li = document.createElement("li");
      li.setAttribute("role", "option");
      var btn = document.createElement("button");
      btn.type = "button";
      btn.textContent = items[i].name;
      btn.dataset.model = items[i].name;
      btn.addEventListener("mousedown", function (ev) {
        ev.preventDefault();
        selectModel(ev.currentTarget.dataset.model);
      });
      li.appendChild(btn);
      suggestions.appendChild(li);
    }
    suggestions.hidden = false;
    activeIndex = -1;
  }

  function highlightSuggestion(idx) {
    var buttons = suggestions.querySelectorAll("button");
    for (var i = 0; i < buttons.length; i++) {
      buttons[i].classList.toggle("active", i === idx);
    }
  }

  function countBuilds(entry) {
    var total = 0;
    var hw = entry && entry.hw ? entry.hw : {};
    Object.keys(hw).forEach(function (k) {
      total += (hw[k] || []).length;
    });
    return total;
  }

  function selectModel(model) {
    if (!data || !data.models[model]) {
      setStatus("Model not in archive.", true);
      result.hidden = true;
      return;
    }

    q.value = model;
    clearBtn.hidden = false;
    hideSuggestions();

    var entry = data.models[model];
    var hwNames = Object.keys(entry.hw || {}).sort();
    resultModel.textContent = model;
    resultMeta.textContent =
      countBuilds(entry) +
      " firmware build" +
      (countBuilds(entry) === 1 ? "" : "s") +
      " · " +
      hwNames.length +
      " hardware line" +
      (hwNames.length === 1 ? "" : "s");

    hwSelect.innerHTML = "";
    for (var i = 0; i < hwNames.length; i++) {
      var opt = document.createElement("option");
      opt.value = hwNames[i];
      opt.textContent = hwNames[i];
      hwSelect.appendChild(opt);
    }

    // Prefer IPC_* if present
    var preferred = hwNames.find(function (h) {
      return h.indexOf("IPC_") === 0;
    });
    if (preferred) hwSelect.value = preferred;

    result.hidden = false;
    setStatus("");
    renderRows(model, hwSelect.value);

    var url = new URL(window.location.href);
    url.searchParams.set("model", model);
    if (hwSelect.value) url.searchParams.set("hw", hwSelect.value);
    else url.searchParams.delete("hw");
    history.replaceState(null, "", url);
  }

  function renderRows(model, hw) {
    rows.innerHTML = "";
    var builds = (((data.models[model] || {}).hw || {})[hw] || []).slice();
    if (!builds.length) {
      var empty = document.createElement("tr");
      empty.innerHTML =
        '<td colspan="4">No firmware for this hardware line.</td>';
      rows.appendChild(empty);
      return;
    }

    for (var i = 0; i < builds.length; i++) {
      var b = builds[i];
      var tr = document.createElement("tr");
      if (i === 0) tr.className = "latest";

      var ver = document.createElement("td");
      ver.textContent = b.v || "—";
      if (i === 0) {
        var tag = document.createElement("span");
        tag.className = "tag";
        tag.textContent = "latest";
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
    }
  }

  function onQueryInput() {
    var value = q.value.trim();
    clearBtn.hidden = !value;
    if (!data) return;

    if (!value) {
      hideSuggestions();
      result.hidden = true;
      setStatus(
        modelNames.length.toLocaleString() +
          " models indexed. Start typing a model number."
      );
      return;
    }

    var matches = findMatches(value, 20);
    renderSuggestions(matches);
    if (!matches.length) {
      setStatus("No models match “" + value + "”.", true);
      result.hidden = true;
    } else {
      setStatus(matches.length + " match" + (matches.length === 1 ? "" : "es"));
    }
  }

  q.addEventListener("input", onQueryInput);

  q.addEventListener("keydown", function (ev) {
    var buttons = suggestions.querySelectorAll("button");
    if (ev.key === "ArrowDown" && buttons.length) {
      ev.preventDefault();
      activeIndex = (activeIndex + 1) % buttons.length;
      highlightSuggestion(activeIndex);
    } else if (ev.key === "ArrowUp" && buttons.length) {
      ev.preventDefault();
      activeIndex = (activeIndex - 1 + buttons.length) % buttons.length;
      highlightSuggestion(activeIndex);
    } else if (ev.key === "Enter") {
      ev.preventDefault();
      if (activeIndex >= 0 && buttons[activeIndex]) {
        selectModel(buttons[activeIndex].dataset.model);
      } else {
        var matches = findMatches(q.value, 1);
        if (matches.length) selectModel(matches[0].name);
      }
    } else if (ev.key === "Escape") {
      hideSuggestions();
    }
  });

  clearBtn.addEventListener("click", function () {
    q.value = "";
    clearBtn.hidden = true;
    hideSuggestions();
    result.hidden = true;
    setStatus(
      modelNames.length.toLocaleString() +
        " models indexed. Start typing a model number."
    );
    history.replaceState(null, "", window.location.pathname);
    q.focus();
  });

  hwSelect.addEventListener("change", function () {
    var model = resultModel.textContent;
    renderRows(model, hwSelect.value);
    var url = new URL(window.location.href);
    url.searchParams.set("model", model);
    url.searchParams.set("hw", hwSelect.value);
    history.replaceState(null, "", url);
  });

  document.addEventListener("click", function (ev) {
    if (!suggestions.contains(ev.target) && ev.target !== q) {
      hideSuggestions();
    }
  });

  fetch("search-data.json", { cache: "no-cache" })
    .then(function (res) {
      if (!res.ok) throw new Error("HTTP " + res.status);
      return res.json();
    })
    .then(function (json) {
      data = json;
      modelNames = Object.keys(data.models || {}).sort();
      var when = data.generated_at ? String(data.generated_at).slice(0, 19).replace("T", " ") + " UTC" : "unknown";
      footMeta.textContent =
        modelNames.length.toLocaleString() +
        " models · index " +
        when;
      setStatus(
        modelNames.length.toLocaleString() +
          " models indexed. Start typing a model number."
      );

      var params = new URLSearchParams(window.location.search);
      var preset = params.get("model");
      if (preset && data.models[preset]) {
        selectModel(preset);
        if (params.get("hw") && data.models[preset].hw[params.get("hw")]) {
          hwSelect.value = params.get("hw");
          renderRows(preset, hwSelect.value);
        }
      }
    })
    .catch(function (err) {
      setStatus("Could not load search-data.json (" + err.message + ").", true);
    });
})();
