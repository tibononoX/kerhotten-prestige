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

  /* ---------------- group request (DEMO: no network call) ---------------- */
  var gf = d.getElementById('group-form');
  if (gf) {
    var gErr = d.getElementById('g-error'), gOk = d.getElementById('g-ok');
    var gIds = ['g-nom', 'g-email', 'g-type', 'g-arrivee', 'g-depart', 'g-nb'];
    var gFail = function (k, f) { gErr.textContent = t(k); gOk.hidden = true; f.setAttribute('aria-invalid', 'true'); f.focus(); return false; };
    gf.addEventListener('submit', function (e) {
      e.preventDefault(); gErr.textContent = '';
      var f = gIds.map(function (id) { var el = d.getElementById(id); el.removeAttribute('aria-invalid'); return el; });
      for (var i = 0; i < f.length; i++) if (!f[i].value.trim()) return gFail('gReq', f[i]);
      if (!f[1].checkValidity()) return gFail('gEmail', f[1]);
      if (f[4].value <= f[3].value) return gFail('gOrder', f[4]);
      var n = parseInt(f[5].value, 10);
      if (!(n >= 1 && n <= 20)) return gFail('gNb', f[5]);
      gOk.textContent = t('gOk'); gOk.hidden = false; gOk.focus();
    });
    d.addEventListener('kh:lang', function () { if (!gOk.hidden) gOk.textContent = t('gOk'); });
  }

  /* ---------------- init ---------------- */
  var saved = null;
  try { saved = localStorage.getItem('khb-lang'); } catch (e) {}
  var ql = (location.search.match(/[?&]lang=(en|de|fr)\b/) || [])[1];
  if (ql || (saved && saved !== 'fr')) setLang(ql || saved);
})();
