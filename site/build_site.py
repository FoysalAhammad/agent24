#!/usr/bin/env python3
import os
import markdown

SRC = os.path.expanduser('~/agent24-wiki')
OUT = os.path.expanduser('~/agent24-docs')

PAGES = [
    ('home', 'Home', '🏠', 'Home.md'),
    ('getting-started', 'Getting Started', '🚀', 'Getting-Started.md'),
    ('agents', 'Agents', '🤖', 'Agents.md'),
    ('tools', 'Tools', '🔧', 'Tools.md'),
    ('providers', 'Providers', '🌍', 'Providers.md'),
    ('permissions', 'Permissions', '🔐', 'Permissions.md'),
    ('faq', 'FAQ', '❓', 'FAQ.md'),
]

md = markdown.Markdown(extensions=['tables', 'fenced_code', 'attr_list', 'sane_lists'])
sections = []
for pid, title, icon, fn in PAGES:
    with open(os.path.join(SRC, fn), encoding='utf-8') as f:
        text = f.read()
    md.reset()
    body = md.convert(text)
    sections.append('<section id="%s" class="doc-section">%s</section>' % (pid, body))

nav_items = '\n'.join(
    '<a class="nav-link" href="#{0}" data-target="{0}"><span class="nav-icon">{1}</span>{2}</a>'.format(pid, icon, title)
    for pid, title, icon, fn in PAGES
)

CSS = r'''
:root {
  --bg: #0b0f19; --bg-soft: #111827; --bg-card: #161f31; --border: #263149;
  --text: #e5eaf5; --muted: #94a3b8; --accent: #6d5cff; --accent2: #22d3ee;
  --grad: linear-gradient(135deg, #6d5cff 0%, #22d3ee 100%);
}
* { box-sizing: border-box; }
html { scroll-behavior: smooth; }
body { margin: 0; background: var(--bg); color: var(--text);
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Noto Sans Bengali", sans-serif;
  line-height: 1.65; -webkit-font-smoothing: antialiased; }
a { color: var(--accent2); text-decoration: none; }
a:hover { text-decoration: underline; }
.topbar { position: sticky; top: 0; z-index: 50; display: none; align-items: center;
  justify-content: space-between; padding: .7rem 1rem; background: rgba(11,15,25,.92);
  backdrop-filter: blur(10px); border-bottom: 1px solid var(--border); }
.topbar .brand { font-weight: 800; background: var(--grad); -webkit-background-clip: text;
  background-clip: text; color: transparent; font-size: 1.05rem; }
.hamb { background: var(--bg-card); border: 1px solid var(--border); color: var(--text);
  border-radius: 8px; padding: .35rem .7rem; font-size: 1rem; cursor: pointer; }
.layout { display: flex; min-height: 100vh; }
.sidebar { width: 264px; flex-shrink: 0; position: sticky; top: 0; height: 100vh;
  overflow-y: auto; padding: 1.4rem 1rem; background: var(--bg-soft);
  border-right: 1px solid var(--border); }
.sidebar .logo { font-size: 1.25rem; font-weight: 800; margin-bottom: .2rem;
  background: var(--grad); -webkit-background-clip: text; background-clip: text; color: transparent; }
.sidebar .tagline { font-size: .74rem; color: var(--muted); margin-bottom: 1.3rem; }
.nav-link { display: flex; align-items: center; gap: .55rem; padding: .5rem .7rem;
  margin-bottom: .2rem; border-radius: 8px; color: var(--muted); font-size: .9rem;
  font-weight: 500; transition: .15s; border-left: 2px solid transparent; }
.nav-link:hover { background: var(--bg-card); color: var(--text); text-decoration: none; }
.nav-link.active { background: rgba(109,92,255,.14); color: #fff;
  border-left-color: var(--accent); }
.nav-icon { font-size: .95rem; }
.side-foot { margin-top: 1.4rem; padding-top: 1rem; border-top: 1px solid var(--border);
  font-size: .78rem; color: var(--muted); }
.content { flex: 1; min-width: 0; padding: 2.2rem clamp(1rem, 4vw, 3.4rem) 4rem; max-width: 1060px; }
.doc-section { scroll-margin-top: 70px; }
.doc-section + .doc-section { margin-top: 3.2rem; padding-top: 2.4rem;
  border-top: 1px solid var(--border); }
h1, h2, h3 { line-height: 1.3; }
h1 { font-size: clamp(1.7rem, 4vw, 2.3rem); margin: .4rem 0 1rem; }
h2 { font-size: clamp(1.25rem, 3vw, 1.55rem); margin: 2rem 0 .8rem;
  padding-bottom: .4rem; border-bottom: 1px solid var(--border); }
h3 { font-size: 1.08rem; margin: 1.5rem 0 .6rem; color: #fff; }
blockquote { margin: 1rem 0; padding: .7rem 1rem; border-left: 3px solid var(--accent);
  background: rgba(109,92,255,.08); border-radius: 0 10px 10px 0; color: var(--muted); }
blockquote p { margin: 0; }
.table-wrap, table { border-collapse: collapse; }
.table-wrap { overflow-x: auto; margin: 1rem 0; border: 1px solid var(--border);
  border-radius: 12px; }
table { width: 100%; font-size: .9rem; }
th { background: var(--bg-card); text-align: left; font-weight: 700; color: #fff;
  padding: .65rem .9rem; border-bottom: 2px solid var(--border); }
td { padding: .6rem .9rem; border-bottom: 1px solid var(--border); color: var(--muted); }
tr:last-child td { border-bottom: none; }
tr:hover td { background: rgba(255,255,255,.02); color: var(--text); }
code { background: var(--bg-card); border: 1px solid var(--border); padding: .12rem .4rem;
  border-radius: 6px; font-size: .85em; color: #f0abfc; font-family: ui-monospace, "SF Mono", Menlo, monospace; }
pre { background: #0a0e17; border: 1px solid var(--border); padding: 1rem 1.1rem;
  border-radius: 12px; overflow-x: auto; }
pre code { background: none; border: none; color: #a5f3fc; padding: 0; }
ul, ol { padding-left: 1.4rem; color: var(--muted); }
li { margin: .3rem 0; }
strong { color: #fff; }
details { background: var(--bg-card); border: 1px solid var(--border);
  border-radius: 12px; padding: .6rem 1rem; margin: 1rem 0; }
summary { cursor: pointer; font-weight: 600; color: var(--text); }
img { max-width: 100%; }
p[align="center"], div[align="center"] { text-align: center; }
hr { border: none; border-top: 1px solid var(--border); margin: 1.6rem 0; }
footer.site { margin-top: 3rem; padding-top: 1.4rem; border-top: 1px solid var(--border);
  text-align: center; font-size: .84rem; color: var(--muted); }
@media (max-width: 860px) {
  .topbar { display: flex; }
  .sidebar { position: fixed; left: 0; top: 0; transform: translateX(-100%);
    transition: transform .25s ease; z-index: 60; box-shadow: 0 0 40px rgba(0,0,0,.6); }
  .sidebar.open { transform: translateX(0); }
  .content { padding-top: 1.4rem; }
}
'''

JS = r'''
const links = document.querySelectorAll('.nav-link');
const sections = [...document.querySelectorAll('.doc-section')];
function spy() {
  let cur = sections[0].id;
  for (const s of sections) { if (s.getBoundingClientRect().top <= 120) cur = s.id; }
  links.forEach(a => a.classList.toggle('active', a.dataset.target === cur));
}
document.addEventListener('scroll', spy, { passive: true }); spy();
const sb = document.querySelector('.sidebar'), ham = document.querySelector('.hamb');
ham.addEventListener('click', () => sb.classList.toggle('open'));
links.forEach(a => a.addEventListener('click', () => sb.classList.remove('open')));
'''

nav_html = '\n    '.join([
    '<a class="nav-link" href="#{0}" data-target="{0}"><span class="nav-icon">{1}</span>{2}</a>'.format(p[0], p[2], p[1])
    for p in PAGES
])

html_doc = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Agent 24 — Autonomous AI Assistant for Android</title>
<meta name="description" content="Agent 24 is an autonomous AI coding and technical assistant for Android: 18 built-in tools, permission model, 13+ providers.">
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🤖</text></svg>">
<style>''' + CSS + '''</style>
</head>
<body>
<div class="topbar">
  <span class="brand">🤖 Agent 24</span>
  <button class="hamb" aria-label="Menu">☰</button>
</div>
<div class="layout">
  <aside class="sidebar">
    <div class="logo">🤖 Agent 24</div>
    <div class="tagline">Autonomous AI assistant for Android</div>
    <nav>
    ''' + nav_html + '''
    </nav>
    <div class="side-foot">
      Built by <a href="https://github.com/FoysalAhammad">Foysal Ahammad</a><br>
      <a href="https://github.com/FoysalAhammad/agent24">📦 Repository</a>
    </div>
  </aside>
  <main class="content">
''' + ''.join(sections) + '''
<footer class="site">
  🤖 <strong>Agent 24</strong> · Built by <a href="https://github.com/FoysalAhammad">Foysal Ahammad</a>
  · <a href="https://github.com/FoysalAhammad/agent24">Repository</a>
</footer>
  </main>
</div>
<script>''' + JS + '''</script>
</body>
</html>'''

with open(os.path.join(OUT, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(html_doc)
print('index.html written:', os.path.getsize(os.path.join(OUT, 'index.html')), 'bytes')
