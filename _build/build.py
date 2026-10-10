#!/usr/bin/env python3
"""Option B – Prestige : générateur statique.
Pages sources : _build/pages/*.html (FR + traductions EN/DE en ligne).
  [[fr || en || de]]                 -> <span data-i18n="k…">fr</span>
  {{alt: fr || en || de}}            -> alt="fr" data-i18n-alt="k…"   (alt, aria-label, title)
  <!--img name|sizes|class|eager/lazy|alt fr || en || de-->     -> <picture> WebP responsive + JPEG
  <!--gal name|caption fr || en || de-->                         -> vignette ouvrant la lightbox
Sorties : *.html à la racine, assets/js/i18n.js (dictionnaires EN/DE), assets/js/site.min.js.
Usage : python3 _build/build.py
"""
import re, json, hashlib, os, subprocess, html
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
import sys; sys.path.insert(0, HERE); import suites; suites.generate()
MAN = json.load(open(os.path.join(HERE, 'manifest.json')))
DICT = {'en': {}, 'de': {}}

def key(fr):
    return 'k' + hashlib.md5(fr.strip().encode()).hexdigest()[:7]

def reg(triple):
    parts = [p.strip() for p in triple.split('||')]
    if len(parts) != 3:
        raise SystemExit('Bad triple: ' + triple[:120])
    fr, en, de = parts
    k = key(fr)
    for lang, val in (('en', en), ('de', de)):
        if k in DICT[lang] and DICT[lang][k] != val:
            raise SystemExit(f'Conflicting translation for {fr!r}')
        DICT[lang][k] = val
    return k, fr

def esc_attr(s):
    return html.escape(html.unescape(s), quote=True)

def picture(name, sizes, cls, loading, alt_triple, extra=''):
    k, fr = reg(alt_triple)
    d = MAN[name]; W, H = d['ratio']; jw = d['jpg']; jh = round(H * jw / W)
    srcset = ', '.join(f'assets/img/{name}-{w}.webp {w}w' for w in d['w'])
    load = 'fetchpriority="high"' if loading == 'eager' else 'loading="lazy" decoding="async"'
    return (f'<picture><source type="image/webp" srcset="{srcset}" sizes="{sizes}">'
            f'<img class="{cls}" src="assets/img/{name}-{jw}.jpg" width="{jw}" height="{jh}" '
            f'alt="{esc_attr(fr)}" data-i18n-alt="{k}" {load}{extra}></picture>')

def gallery_item(name, cap_triple):
    k, fr = reg(cap_triple)
    d = MAN[name]; W, H = d['ratio']; big = max(d['w'])
    srcset = ', '.join(f'assets/img/{name}-{w}.webp {w}w' for w in d['w'])
    return (f'<li><button type="button" class="g-item" data-full="assets/img/{name}-{big}.webp" '
            f'data-srcset="{srcset}" data-w="{W}" data-h="{H}" data-cap="{k}">'
            f'<img src="assets/img/{name}-480.webp" width="480" height="{round(H*480/W)}" alt="{esc_attr(fr)}" '
            f'data-i18n-alt="{k}" loading="lazy" decoding="async">'
            f'<span class="g-cap" data-i18n="{k}">{fr}</span></button></li>')

def process(s):
    s = re.sub(r'<!--img (.*?)-->', lambda m: picture(*m.group(1).split('|', 4)), s, flags=re.S)
    s = re.sub(r'<!--gal (.*?)-->', lambda m: gallery_item(*m.group(1).split('|', 1)), s, flags=re.S)
    def attr(m):
        a, triple = m.group(1), m.group(2)
        k, fr = reg(triple)
        return f'{a}="{esc_attr(fr)}" data-i18n-{a}="{k}"'
    s = re.sub(r'\{\{(alt|aria-label|title): (.*?)\}\}', attr, s, flags=re.S)
    def text(m):
        k, fr = reg(m.group(1))
        return f'<span data-i18n="{k}">{fr}</span>'
    s = re.sub(r'\[\[(.*?)\]\]', text, s, flags=re.S)
    return s

def run(cmd, fallback):
    try:
        return subprocess.check_output(cmd, cwd=ROOT, text=True, stderr=subprocess.DEVNULL)
    except Exception:
        return fallback

css_path = os.path.join(ROOT, 'assets/css/site.css')
CSS = run(['npx', '--prefix', '/tmp/tools', 'csso', css_path], open(css_path).read()).strip()
JSFR = {k: v['fr'] for k, v in json.load(open(os.path.join(HERE, 'js-strings.json'))).items()}
js_src = open(os.path.join(ROOT, 'assets/js/site.js')).read().replace('/*FR_STRINGS*/{}', json.dumps(JSFR, ensure_ascii=False))
tmp_js = os.path.join(HERE, '.site.tmp.js'); open(tmp_js, 'w').write(js_src)
open(os.path.join(ROOT, 'assets/js/site.min.js'), 'w').write(
    run(['npx', '--prefix', '/tmp/tools', 'terser', tmp_js, '-c', '-m', '--comments', '/Private redesign/'], js_src))
os.remove(tmp_js)

LAYOUT = open(os.path.join(HERE, 'layout.html')).read()
NAV = [('index.html#histoire', 'Histoire || Story || Geschichte'),
       ('index.html#suites', 'Les suites || The suites || Die Suiten'),
       ('index.html#domaine', 'Le domaine || The estate || Das Anwesen'),
       ('index.html#experiences', 'Expériences || Experiences || Erlebnisse'),
       ('privatisation.html', 'Privatisation || Private hire || Exklusivmiete')]

pages = sorted(f for f in os.listdir(os.path.join(HERE, 'pages')) if f.endswith('.html'))
meta_all = {}
for fname in pages:
    src = open(os.path.join(HERE, 'pages', fname)).read()
    meta = dict(re.findall(r'^@(\w+) (.*)$', src, flags=re.M))
    body = re.sub(r'^@\w+ .*\n', '', src, flags=re.M)
    tk, tfr = reg(meta['title']); dk, dfr = reg(meta['desc'])
    meta_all[fname] = (tk, dk)
    nav = '\n'.join(
        f'<li><a href="{href}"' + (' aria-current="page"' if href == fname else '') + f'>[[{lab}]]</a></li>'
        for href, lab in NAV)
    out = (LAYOUT.replace('%%CSS%%', CSS).replace('%%BODY%%', body).replace('%%NAV%%', nav)
           .replace('%%TITLE%%', esc_attr(tfr)).replace('%%DESC%%', esc_attr(dfr))
           .replace('%%TK%%', tk).replace('%%DK%%', dk)
           .replace('%%PRELOAD%%', meta.get('preload', ''))
           .replace('%%BODYCLASS%%', meta.get('bodyclass', ''))
           .replace('%%CANON%%', 'https://www.gitesdekerhotten.fr/' + ('' if fname == 'index.html' else fname)))
    out = process(out)
    left = re.findall(r'\[\[|\]\]|\{\{|%%', out)
    if left:
        raise SystemExit(f'{fname}: unprocessed markers {left[:5]}')
    open(os.path.join(ROOT, fname), 'w').write(out)
    print(f'{fname}: {len(out)} bytes')

# JS-only strings (booking engine, lightbox) – FR defaults live in site.js
JSSTR = json.load(open(os.path.join(HERE, 'js-strings.json')))
for k, v in JSSTR.items():
    DICT['en']['js.' + k] = v['en']; DICT['de']['js.' + k] = v['de']
with open(os.path.join(ROOT, 'assets/js/i18n.js'), 'w') as f:
    f.write('/* Private redesign proposal, photos © Gîtes de Kerhotten, not for publication without owners\' consent. */\n')
    f.write('window.KH_I18N=' + json.dumps(DICT, ensure_ascii=False, separators=(',', ':')) + ';\n')
print('i18n keys:', len(DICT['en']))
