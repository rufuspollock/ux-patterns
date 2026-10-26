/* Reading System v0.1: optional behaviour for reading.css.
   - turns Markdown (GFM) footnotes into sidenotes: margin notes on wide screens, tap-to-open on phones
   - marks the first paragraph of each chapter (for drop caps and small caps)
   - fills an empty contents list from the headings
   - chapter bar: current section, progress line, contents drawer
   - copy buttons: <button data-rs-copy="#cite-text">
   Without it, the page still reads well: footnotes stay at the end.
   Usage: <script src="reading.js" defer></script>  (runs on every .rs on the page)
          ReadingSystem.refresh() after changing layout (e.g. moving the page into a scrolling box). */
(function () {
  "use strict";

  function slug(s) { return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-|-$/g, "").slice(0, 48); }

  function sidenotes(root) {
    var refs = root.querySelectorAll(".rs-text a[data-footnote-ref], .rs-text sup a.footnote-ref, .rs-text sup > a[href^='#fn']");
    var used = [];
    refs.forEach(function (a) {
      var id = decodeURIComponent((a.getAttribute("href") || "").slice(1));
      var li = id && root.querySelector("[id='" + id.replace(/'/g, "\\'") + "']");
      if (!li) return;
      var n = (a.textContent || "").trim();
      var body = li.cloneNode(true);
      body.querySelectorAll("a[data-footnote-backref], .footnote-backref, a[href^='#fnref']").forEach(function (b) { b.remove(); });
      var inner = body.innerHTML.replace(/^\s*<p>/, "").replace(/<\/p>\s*$/, "").replace(/<\/p>\s*<p>/g, "<br><br>").trim();
      var sn = document.createElement("span");
      sn.className = "rs-sn";
      var noteId = "rs-sn-" + slug(id);
      sn.innerHTML = '<button type="button" class="rs-sn-ref" aria-expanded="false" aria-controls="' + noteId + '" aria-label="Note ' + n + '">' + n + "</button>" +
        '<span class="rs-sn-note" id="' + noteId + '" role="note"><span class="rs-sn-n">' + n + "</span> " + inner + "</span>";
      var sup = a.closest("sup") || a;
      // keep the number with the word before it
      var prev = sup.previousSibling;
      var wrap = document.createElement("span");
      wrap.className = "rs-nw";
      wrap.id = sup.id || a.id || "";
      if (prev && prev.nodeType === 3) {
        var m = prev.nodeValue.match(/(\S+)$/);
        if (m) { prev.nodeValue = prev.nodeValue.slice(0, -m[1].length); wrap.appendChild(document.createTextNode(m[1])); }
      }
      sup.parentNode.insertBefore(wrap, sup);
      wrap.appendChild(sn);
      sup.remove();
      used.push(li);
    });
    if (!used.length) return;
    // move the footnote list into the end matter slot if there is one, else hide it on screen
    var section = used[0].closest("section, .footnotes, ol");
    var slot = root.querySelector("[data-rs-notes-slot]");
    var list = used[0].closest("ol");
    if (slot && list) { list.classList.add("rs-notes"); slot.appendChild(list); if (section && section !== list && !section.querySelector("li")) section.remove(); }
    else if (section) section.setAttribute("data-rs-sidenoted", "");
    root.querySelectorAll(".rs-sn-ref").forEach(function (b) {
      b.addEventListener("click", function () { var open = b.parentNode.classList.toggle("rs-open"); b.setAttribute("aria-expanded", String(open)); });
    });
  }

  function firstParagraphs(root) {
    root.querySelectorAll(".rs-text h2").forEach(function (h) {
      if (h.closest(".footnotes, [data-footnotes]")) return;
      var el = h.nextElementSibling;
      while (el && !(el.tagName === "P" && !el.classList.contains("rs-inbrief"))) {
        if (el.tagName === "H2") return;
        el = el.nextElementSibling;
      }
      if (el) el.classList.add("rs-first");
    });
  }

  function contents(root) {
    var heads = Array.prototype.slice.call(root.querySelectorAll(".rs-text h2, .rs-text h3")).filter(function (h) { return !h.closest(".footnotes, [data-footnotes], [data-rs-sidenoted]"); });
    heads.forEach(function (h) { if (!h.id) h.id = slug(h.textContent); });
    root.querySelectorAll(".rs-toc[data-rs-auto]").forEach(function (ol) {
      if (ol.children.length) return;
      heads.forEach(function (h) {
        var li = document.createElement("li");
        li.className = h.tagName === "H2" ? "rs-l2" : "rs-l3";
        var a = document.createElement("a");
        a.href = "#" + h.id;
        a.textContent = label(h);
        li.appendChild(a); ol.appendChild(li);
      });
    });
    return heads;
  }

  function label(h) {
    var num = h.querySelector(".rs-num");
    var name = h.cloneNode(true); var n2 = name.querySelector(".rs-num"); if (n2) n2.remove();
    return (num && num.textContent ? num.textContent + ". " : "") + name.textContent.trim();
  }

  function scrollerOf(el) {
    for (var p = el.parentElement; p; p = p.parentElement) {
      var o = getComputedStyle(p).overflowY;
      if ((o === "auto" || o === "scroll") && p.scrollHeight > p.clientHeight) return p;
    }
    return null;
  }

  var pages = [];
  function bar(root, heads) {
    var current = root.querySelector(".rs-bar-current");
    var progress = root.querySelector(".rs-progress");
    var text = root.querySelector(".rs-text");
    var title = current ? current.textContent : "";
    var state = { root: root, scroller: null };
    function update() {
      var sc = state.scroller;
      var top = sc ? sc.getBoundingClientRect().top : 0;
      var vh = sc ? sc.clientHeight : window.innerHeight;
      var line = top + 90 + (parseFloat(getComputedStyle(root).getPropertyValue("--rs-sticky-top")) || 0), id = null, lab = title;
      heads.forEach(function (h) { if (!h.offsetParent) return; if (h.getBoundingClientRect().top < line) { id = h.id; lab = label(h); } });
      if (current) current.textContent = lab;
      root.querySelectorAll(".rs-toc li").forEach(function (li) { var a = li.querySelector("a"); li.classList.toggle("rs-active", !!a && a.getAttribute("href") === "#" + id); });
      if (progress && text) {
        var r = text.getBoundingClientRect();
        progress.style.width = Math.min(100, Math.max(0, (line - r.top) / Math.max(1, r.height - vh / 2) * 100)) + "%";
      }
    }
    function attach() {
      if (state.scroller) state.scroller.removeEventListener("scroll", update);
      state.scroller = scrollerOf(root);
      if (state.scroller) state.scroller.addEventListener("scroll", update, { passive: true });
      update();
    }
    window.addEventListener("scroll", update, { passive: true });
    window.addEventListener("resize", update);
    state.update = update; state.attach = attach;
    attach();
    // drawer
    var toggle = root.querySelector(".rs-bar-toggle"), drawer = root.querySelector(".rs-drawer");
    if (toggle && drawer) {
      toggle.addEventListener("click", function () { var open = drawer.hidden; drawer.hidden = !open; toggle.setAttribute("aria-expanded", String(open)); });
      drawer.addEventListener("click", function (e) { if (e.target.closest("a")) { drawer.hidden = true; toggle.setAttribute("aria-expanded", "false"); } });
    }
    // in-page links scroll the right box and clear the sticky bar
    root.querySelectorAll("a[href^='#']").forEach(function (a) {
      a.addEventListener("click", function (e) {
        var t = document.getElementById(decodeURIComponent(a.getAttribute("href").slice(1)));
        if (!t || !root.contains(t) || !state.scroller) return;
        e.preventDefault();
        try { history.pushState(null, "", a.getAttribute("href")); } catch (err) {}
        var b = root.querySelector(".rs-bar"); var off = (b ? b.offsetHeight : 0) + 12;
        var sc = state.scroller;
        if (sc) sc.scrollTop += t.getBoundingClientRect().top - sc.getBoundingClientRect().top - off;
        else window.scrollTo(0, window.scrollY + t.getBoundingClientRect().top - off);
      });
    });
    pages.push(state);
  }

  function copies(root) {
    root.querySelectorAll("[data-rs-copy]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        var src = document.querySelector(btn.getAttribute("data-rs-copy")); if (!src) return;
        var orig = btn.textContent;
        function done(ok) { btn.textContent = ok ? "Copied" : "Select the text to copy"; setTimeout(function () { btn.textContent = orig; }, 2200); }
        try { navigator.clipboard.writeText(src.textContent.trim()).then(function () { done(true); }, function () { done(false); }); } catch (e) { done(false); }
      });
    });
  }

  function noteMode(root) {
    function apply() {
      var wide = root.clientWidth >= 760;
      root.querySelectorAll(".rs-sn-ref").forEach(function (b) {
        if (wide) { b.setAttribute("tabindex", "-1"); b.setAttribute("aria-expanded", "true"); }
        else { b.removeAttribute("tabindex"); b.setAttribute("aria-expanded", String(b.parentNode.classList.contains("rs-open"))); }
      });
    }
    if (window.ResizeObserver) new ResizeObserver(apply).observe(root); else window.addEventListener("resize", apply);
    apply();
  }

  function init(root) {
    if (root.__rs) return; root.__rs = true;
    sidenotes(root);
    firstParagraphs(root);
    var heads = contents(root);
    bar(root, heads);
    copies(root);
    noteMode(root);
  }

  window.ReadingSystem = {
    init: init,
    refresh: function () { pages.forEach(function (p) { p.attach(); }); }
  };
  function boot() { document.querySelectorAll(".rs").forEach(init); }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot); else boot();
})();
