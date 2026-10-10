/* Private redesign proposal, photos © Gîtes de Kerhotten, not for publication without owners' consent. */
/* Option B – Prestige. No network calls except loading i18n.js (same origin) when EN/DE is chosen. Nothing is ever sent. */
(function () {
  'use strict';
  var d = document, root = d.documentElement;
  var FR = /*FR_STRINGS*/{};
  var lang = 'fr', dict = null;

  function t(k, vars) {
    var s = (lang !== 'fr' && dict && dict[lang]['js.' + k]) || FR[k] || k;
    if (vars) Object.keys(vars).forEach(function (v) { s = s.split('{' + v + '}').join(vars[v]); });
    return s;
  }
  var LOCALE = { fr: 'fr-FR', en: 'en-GB', de: 'de-DE' };

  /* ---------------- i18n ---------------- */
  var orig = null;
  function snapshot() {
    if (orig) return;
    orig = { text: [], attr: [] };
    d.querySelectorAll('[data-i18n]').forEach(function (el) { orig.text.push([el, el.innerHTML]); });
    ['alt', 'aria-label', 'title'].forEach(function (a) {
      d.querySelectorAll('[data-i18n-' + a + ']').forEach(function (el) { orig.attr.push([el, a, el.getAttribute(a)]); });
    });
    var ti = d.querySelector('title'), de = d.querySelector('meta[name="description"]');
    orig.title = ti.textContent; orig.desc = de.content;
  }
  function apply(l) {
    snapshot();
    var D = l === 'fr' ? null : dict[l];
    orig.text.forEach(function (p) { var k = p[0].getAttribute('data-i18n'); p[0].innerHTML = D && D[k] != null ? D[k] : p[1]; });
    orig.attr.forEach(function (p) { var k = p[0].getAttribute('data-i18n-' + p[1]); p[0].setAttribute(p[1], D && D[k] != null ? D[k] : p[2]); });
    var ti = d.querySelector('title'), de = d.querySelector('meta[name="description"]');
    ti.textContent = D ? D[ti.getAttribute('data-i18n-doc')] || orig.title : orig.title;
    de.content = D ? D[de.getAttribute('data-i18n-desc')] || orig.desc : orig.desc;
    lang = l; root.lang = l;
    d.querySelectorAll('.lang button').forEach(function (b) { b.setAttribute('aria-pressed', String(b.dataset.lang === l)); });
    try { localStorage.setItem('khb-lang', l); } catch (e) {}
    d.dispatchEvent(new CustomEvent('kh:lang'));
  }
  function setLang(l) {
    if (l === 'fr' || dict) return apply(l);
    var s = d.createElement('script');
    s.src = 'assets/js/i18n.js';
    s.onload = function () { dict = window.KH_I18N; apply(l); };
    d.head.appendChild(s);
  }
  d.querySelectorAll('.lang button').forEach(function (b) { b.addEventListener('click', function () { setLang(b.dataset.lang); }); });

  /* ---------------- header ---------------- */
  var hdr = d.getElementById('hdr'), burger = d.querySelector('.burger'), nav = d.getElementById('nav');
  function closeNav() { burger.setAttribute('aria-expanded', 'false'); nav.classList.remove('open'); }
  burger.addEventListener('click', function () {
    var o = burger.getAttribute('aria-expanded') !== 'true';
    burger.setAttribute('aria-expanded', String(o)); nav.classList.toggle('open', o);
  });
  nav.addEventListener('click', function (e) { if (e.target.closest('a')) closeNav(); });
  d.addEventListener('keydown', function (e) { if (e.key === 'Escape' && nav.classList.contains('open')) { closeNav(); burger.focus(); } });
  var hero = d.querySelector('.hero, .p-hero');
  if (hero && 'IntersectionObserver' in window) {
    new IntersectionObserver(function (en) { hdr.classList.toggle('solid', !en[0].isIntersecting); }, { rootMargin: '-80px 0px 0px 0px' }).observe(hero);
  } else { hdr.classList.add('solid'); }

  /* ---------------- lightbox ---------------- */
  var lb = d.getElementById('lb');
  var items = Array.prototype.slice.call(d.querySelectorAll('[data-gallery] .g-item'));
  if (lb && items.length) {
    var img = d.getElementById('lb-img'), cap = d.getElementById('lb-cap'), cnt = d.getElementById('lb-count');
    var cur = 0, opener = null;
    function show(i) {
      cur = (i + items.length) % items.length;
      var b = items[cur], im = b.querySelector('img');
      img.removeAttribute('src');
      img.width = +b.dataset.w; img.height = +b.dataset.h;
      img.srcset = b.dataset.srcset; img.sizes = '(min-width: 1000px) 80vw, 100vw';
      img.src = b.dataset.full; img.alt = im.alt;
      cap.textContent = b.querySelector('.g-cap').textContent;
      cnt.textContent = t('photo', { i: cur + 1, n: items.length });
    }
    function open(i, from) {
      opener = from; show(i);
      if (lb.showModal) lb.showModal(); else lb.setAttribute('open', '');
      root.classList.add('lb-open');
      d.getElementById('lb-close').focus();
    }
    function close() { if (lb.open) lb.close(); }
    lb.addEventListener('close', function () { root.classList.remove('lb-open'); if (opener) opener.focus(); });
    items.forEach(function (b, i) { b.addEventListener('click', function () { open(i, b); }); });
    d.getElementById('lb-prev').addEventListener('click', function () { show(cur - 1); });
    d.getElementById('lb-next').addEventListener('click', function () { show(cur + 1); });
    d.getElementById('lb-close').addEventListener('click', close);
    lb.addEventListener('click', function (e) { if (e.target === lb) close(); });
    lb.addEventListener('keydown', function (e) {
      if (e.key === 'ArrowLeft') { e.preventDefault(); show(cur - 1); }
      else if (e.key === 'ArrowRight') { e.preventDefault(); show(cur + 1); }
      else if (e.key === 'Escape') { e.preventDefault(); close(); }
      else if (e.key === 'Tab') { /* focus trap across the 3 controls */
        var f = Array.prototype.slice.call(lb.querySelectorAll('button'));
        var i = f.indexOf(d.activeElement);
        e.preventDefault();
        f[(i + (e.shiftKey ? -1 : 1) + f.length) % f.length].focus();
      }
    });
    d.addEventListener('kh:lang', function () { if (lb.open) show(cur); });
  }

  /* ---------------- booking engine (demo) ---------------- */
  var cal = d.getElementById('cal');
  if (cal) {
    var SUITES = ['saule', 'chataigne', 'grange'], OFF = { saule: 0, chataigne: 6, grange: 11 };
    var NAMES = { saule: 'Le Saule', chataigne: 'La Châtaigne', grange: 'La Grange' };
    var today = new Date(); today.setHours(0, 0, 0, 0);
    var view = new Date(today.getFullYear(), today.getMonth(), 1);
    var arr = null, dep = null;
    var ad = 2, ch = 0;
    var radios = Array.prototype.slice.call(d.querySelectorAll('input[name="suite"]'));
    var q = new URLSearchParams(location.search).get('suite');
    radios.forEach(function (r) { if (r.value === q) r.checked = true; });
    function suite() { return radios.filter(function (r) { return r.checked; })[0]; }
    function dayNum(dt) { return Math.floor((dt - new Date(2026, 0, 1)) / 864e5); }
    /* Deterministic FICTITIOUS occupancy, for the demo only */
    function bookedFor(s, dt) { var n = dayNum(dt) + OFF[s]; return ((n % 19) + 19) % 19 < 5; }
    function booked(dt) {
      var s = suite().value;
      return s === 'hameau' ? SUITES.some(function (x) { return bookedFor(x, dt); }) : bookedFor(s, dt);
    }
    function same(a, b) { return a && b && a.getTime() === b.getTime(); }
    function fmt(dt, long) { return dt.toLocaleDateString(LOCALE[lang], long ? { weekday: 'long', day: 'numeric', month: 'long', year: 'numeric' } : { day: 'numeric', month: 'short', year: 'numeric' }); }
    var hint = d.getElementById('cal-hint');
    function setHint(k) { hint.textContent = t(k); hint.dataset.k = k; }

    function render() {
      cal.innerHTML = '';
      for (var m = 0; m < 2; m++) {
        var first = new Date(view.getFullYear(), view.getMonth() + m, 1);
        var box = d.createElement('div'); box.className = 'cal-month';
        var h = d.createElement('h2'); h.textContent = first.toLocaleDateString(LOCALE[lang], { month: 'long', year: 'numeric' });
        box.appendChild(h);
        var tbl = d.createElement('table'); 
        var thead = '<thead><tr>';
        for (var w = 0; w < 7; w++) {
          var wd = new Date(2024, 0, 1 + w); /* Monday-first */
          thead += '<th scope="col" abbr="' + wd.toLocaleDateString(LOCALE[lang], { weekday: 'long' }) + '">' + wd.toLocaleDateString(LOCALE[lang], { weekday: 'narrow' }) + '</th>';
        }
        tbl.innerHTML = thead + '</tr></thead>';
        var tb = d.createElement('tbody'), tr = d.createElement('tr');
        var lead = (first.getDay() + 6) % 7;
        for (var i = 0; i < lead; i++) tr.appendChild(d.createElement('td'));
        var days = new Date(first.getFullYear(), first.getMonth() + 1, 0).getDate();
        for (var day = 1; day <= days; day++) {
          var dt = new Date(first.getFullYear(), first.getMonth(), day);
          var td = d.createElement('td'), b = d.createElement('button');
          b.type = 'button'; b.textContent = day; b.dataset.t = dt.getTime();
          var past = dt < today, bk = !past && booked(dt);
          var inRange = arr && dep && dt > arr && dt < dep, sel = same(dt, arr) || same(dt, dep);
          var state = past ? t('past') : bk ? t('booked') : sel ? t('selected') : t('free');
          b.className = past ? 'past' : bk ? 'booked' : 'free';
          if (sel) b.classList.add('sel'); if (inRange) b.classList.add('range');
          if (past || bk) b.disabled = true;
          b.setAttribute('aria-label', fmt(dt, true) + ', ' + state);
          if (sel) b.setAttribute('aria-pressed', 'true');
          td.appendChild(b); tr.appendChild(td);
          if ((lead + day) % 7 === 0) { tb.appendChild(tr); tr = d.createElement('tr'); }
        }
        if (tr.children.length) tb.appendChild(tr);
        tbl.appendChild(tb); box.appendChild(tbl); cal.appendChild(box);
      }
      d.getElementById('cal-prev').disabled = view <= new Date(today.getFullYear(), today.getMonth(), 1);
    }
    cal.addEventListener('click', function (e) {
      var b = e.target.closest('button'); if (!b || b.disabled) return;
      var dt = new Date(+b.dataset.t);
      msg('');
      if (!arr || dep || dt <= arr) { arr = dt; dep = null; setHint('pickOut'); step(2); }
      else {
        for (var x = new Date(arr); x < dt; x.setDate(x.getDate() + 1)) {
          if (booked(x)) { setHint('overlap'); render(); refocus(b.dataset.t); return; }
        }
        dep = dt; setHint('picked'); step(3);
      }
      render(); summary(); refocus(b.dataset.t);
    });
    function refocus(ts) { var nb = cal.querySelector('button[data-t="' + ts + '"]'); if (nb) nb.focus(); }
    d.getElementById('cal-prev').addEventListener('click', function () { view.setMonth(view.getMonth() - 1); render(); });
    d.getElementById('cal-next').addEventListener('click', function () { view.setMonth(view.getMonth() + 1); render(); });
    radios.forEach(function (r) { r.addEventListener('change', function () {
      if (arr && dep) { for (var x = new Date(arr); x < dep; x.setDate(x.getDate() + 1)) if (booked(x)) { arr = dep = null; setHint('pickIn'); break; } }
      render(); summary();
    }); });
    d.querySelectorAll('[data-step-for]').forEach(function (b) { b.addEventListener('click', function () {
      var dd = +b.dataset.d;
      if (b.dataset.stepFor === 'ad') ad = Math.max(1, Math.min(20, ad + dd)); else ch = Math.max(0, Math.min(19, ch + dd));
      d.getElementById('ad').textContent = ad; d.getElementById('ch').textContent = ch; summary();
    }); });
    function sname() { var s = suite().value; return s === 'hameau' ? t('hameau') : NAMES[s]; }
    function nights() { return arr && dep ? Math.round((dep - arr) / 864e5) : 0; }
    function guests() { return ad + ' ' + t(ad > 1 ? 'adults' : 'adult') + (ch ? ', ' + ch + ' ' + t(ch > 1 ? 'children' : 'child') : ''); }
    function summary() {
      d.getElementById('s-suite').textContent = sname();
      d.getElementById('s-in').textContent = arr ? fmt(arr) : '—';
      d.getElementById('s-out').textContent = dep ? fmt(dep) : '—';
      var n = nights(); d.getElementById('s-n').textContent = n ? n + ' ' + t(n > 1 ? 'nights' : 'night') : '—';
      d.getElementById('s-g').textContent = guests();
      d.getElementById('pay').hidden = true;
    }
    function step(n) { d.querySelectorAll('.steps li').forEach(function (li) { li.classList.toggle('on', +li.dataset.step <= n); }); }
    var msgEl = d.getElementById('b-msg');
    function msg(s) { msgEl.textContent = s; }
    d.getElementById('b-continue').addEventListener('click', function () {
      if (!arr || !dep) { msg(t('needDates')); return; }
      var cap = +suite().dataset.cap;
      if (ad + ch > cap) { msg(t('tooMany', { n: ad + ch, s: sname(), c: cap })); return; }
      msg(''); step(4);
      var n = nights();
      var subject = t('mailSubject', { s: sname(), a: fmt(arr), d: fmt(dep) });
      var body = t('mailBody', { s: sname(), a: fmt(arr, true), d: fmt(dep, true), n: n + ' ' + t(n > 1 ? 'nights' : 'night'), g: guests() });
      d.getElementById('b-mail').href = 'mailto:kerhotten@outlook.fr?subject=' + encodeURIComponent(subject) + '&body=' + encodeURIComponent(body);
      var pay = d.getElementById('pay'); pay.hidden = false; pay.focus();
    });
    d.addEventListener('kh:lang', function () { render(); summary(); setHint(hint.dataset.k || 'pickIn'); });
    render(); summary();
  }

  /* ---------------- init ---------------- */
  var saved = null;
  try { saved = localStorage.getItem('khb-lang'); } catch (e) {}
  var ql = (location.search.match(/[?&]lang=(en|de|fr)\b/) || [])[1];
  if (ql || (saved && saved !== 'fr')) setLang(ql || saved);
})();
