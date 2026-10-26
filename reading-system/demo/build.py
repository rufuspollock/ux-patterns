"""Build the Reading System demo from the In Tech We Trust essay.

The body is emitted the way a Markdown pipeline would (GFM footnotes, plain
headings, blockquotes), plus a few Reading System classes, so the demo shows
what reading.css and reading.js do with ordinary content.

    python3 build.py            -> index.html (links ../reading.css)
    python3 build.py --flat OUT -> OUT/index.html with reading.css beside it (for publishing)
"""
import re, html, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.expanduser("~/src/life-itself/publications/tech/essay.md")
L = open(SRC).read().split("\n")

NOTES = {}
for ln in L:
    m = re.match(r"\[\^(\d+)\]:\s*(.*)", ln)
    if m: NOTES[m.group(1)] = m.group(2).strip()
USED = []

def clean(t):
    return t.replace("\\-", "–").replace("\\!", "!").replace("\\.", ".").replace(" -- ", " – ")

def inline(t, notes=True):
    t = html.escape(clean(t), quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2) if m.group(2).startswith("http") else "https://secondrenaissance.net" + m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    if notes:
        def fn(m):
            n = m.group(1)
            if n not in USED: USED.append(n)
            return f'<sup><a href="#fn-{n}" id="fnref-{n}" data-footnote-ref>{n}</a></sup>'
        t = re.sub(r"\[\^(\d+)\]", fn, t)
    return t

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower())[:40].strip("-")

def convert(a, b):
    out, para = [], []
    lines = L[a-1:b]
    i = 0
    def flush():
        if para:
            txt = " ".join(para).strip(); para.clear()
            if not txt: return
            if txt.startswith("**") and txt.endswith("**") and txt.count("**") == 2:
                out.append(f'<p class="rs-inbrief"><span class="rs-inbrief-label">In brief</span> {inline(txt[2:-2])}</p>')
            else:
                out.append(f"<p>{inline(txt)}</p>")
    while i < len(lines):
        ln = lines[i].rstrip()
        h = re.match(r"(#{1,4})\s+(.*?)\s*(\{#.*\})?\s*$", ln)
        if h and h.group(2).strip():
            flush()
            lvl = len(h.group(1)); title = clean(h.group(2).strip()); hid = slug(re.sub(r"^\d+\.\s+", "", title))
            if lvl == 1:
                m = re.match(r"(\d+)\.\s+(.*)", title)
                num, name = (m.group(1), m.group(2)) if m else ("", title)
                out.append(f'<h2 id="{hid}"><span class="rs-num">{num}</span>{html.escape(name)}</h2>')
            elif lvl == 2: out.append(f'<h3 id="{hid}">{html.escape(title)}</h3>')
            elif lvl == 3: out.append(f'<h4 id="{hid}">{html.escape(title)}</h4>')
            else: out.append(f'<h5>{html.escape(title)}</h5>')
            i += 1; continue
        if ln.startswith("*") and not ln.startswith("**"):
            j = i; quote = []
            while j < len(lines) and lines[j].strip() and not lines[j].strip().startswith("- "):
                quote.append(lines[j].strip()); j += 1
            k = j
            while k < len(lines) and not lines[k].strip(): k += 1
            if k < len(lines) and lines[k].strip().startswith("- "):
                flush()
                q = " ".join(x.strip("* ").strip() for x in quote)
                out.append(f'<blockquote><p>{inline(q)}</p><cite>{inline(lines[k].strip()[2:])}</cite></blockquote>')
                i = k + 1; continue
        if not ln.strip(): flush()
        else: para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(out)

SERIES = '''<figure class="rs-margin demo-series"><ol>
  <li>What and Why</li><li>How</li><li>Polycrisis to Metacrisis</li><li>Developmental Spaces</li><li class="here">In Tech We Trust</li><li>Wisdom</li></ol>
  <figcaption><span class="rs-fignum">Margin figure</span> Where this paper sits in the series.</figcaption></figure>'''
FEATURES = '''<figure class="rs-column demo-features"><ul>
  <li>Material reality as paramount</li><li>The myth of progress</li><li>Technology as cosmological metaphor</li><li>Individualism</li><li>Rationalism and freedom</li><li>Homo economicus</li></ul>
  <figcaption><span class="rs-fignum">Figure 1</span> Six features of the modern cultural paradigm that shape, and are shaped by, our relationship with technology.</figcaption></figure>'''
SHIFTS = '''<figure class="rs-wide demo-shifts">
  <div class="shift"><div class="from"><span class="rs-label">From</span>Out-of-control tech, arising from collective action problems <span class="root">rooted in modern individualism and reductivism</span></div><div class="arrow" aria-hidden="true">→</div><div class="to"><span class="rs-label">To</span>Collective restraint, supported by a worldview of <b>interbeing</b></div></div>
  <div class="shift"><div class="from"><span class="rs-label">From</span>A tyranny of technology, arising from a rationalist illusion of human agency and freedom</div><div class="arrow" aria-hidden="true">→</div><div class="to"><span class="rs-label">To</span>Wiser choice, founded on a holistic understanding of human nature and attunement to an <b>inner compass</b></div></div>
  <figcaption><span class="rs-fignum">Figure 2</span> The two shifts the essay proposes. Chapter 3 takes each in turn.</figcaption>
</figure>'''
PULL = '<aside class="rs-pull" aria-hidden="true"><p>“There’s no discernible difference between the internet and an omniscient being – except that the former answers questions with a higher degree of reliability.”</p></aside>'
GAP = '<div class="demo-omitted" role="note"><span class="rs-label">Not in this demo</span><p>The rest of 2.2, section 2.3 and chapter 3 (about 6,000 words) are left out to keep the demo light.</p></div>'

intro = convert(24, 66)
intro = intro.replace("<p>", SERIES + "\n<p>", 1)
intro = intro.replace("<h5>Material reality as paramount</h5>", FEATURES + "\n<h5>Material reality as paramount</h5>", 1)
intro += "\n" + SHIFTS
ch2 = convert(86, 115).replace('<h4 id="in-tech-we-trust">', PULL + '\n<h4 id="in-tech-we-trust">', 1)
body = "\n".join([intro, convert(76, 84), ch2, convert(116, 133), GAP, convert(299, 305)])

footnotes = '<section class="footnotes" data-footnotes><ol>\n' + "\n".join(
    f'<li id="fn-{n}" value="{n}"><p>{inline(NOTES[n], notes=False)} <a href="#fnref-{n}" data-footnote-backref>↩</a></p></li>' for n in USED) + "\n</ol></section>"

bib, cont = [], False
for ln in L[308:]:
    s = ln.strip()
    if s.startswith("[^"): break
    if s and not s.startswith("#"):
        if cont and bib: bib[-1] += " " + s
        else: bib.append(s)
    cont = ln.endswith("  ") and bool(s)
bibhtml = "\n".join(f"<li>{inline(x, notes=False)}</li>" for x in bib[:8])

TOC = [(2, "introduction", "Introduction"), (2, "co-evolving-with-our-tools", "1. Co-evolving with our tools"),
       (2, "aspects-of-the-late-modern-relationship", "2. Aspects of the late-modern relationship with technology"),
       (3, "2-1-technology-as-god", "2.1 Technology as God"), (3, "2-2-from-servant-to-master", "2.2 From servant to master"),
       (3, None, "2.3 AI: the logical conclusion?"), (2, None, "3. Tech in a future society"), (2, "conclusion", "Conclusion")]
toc = "\n".join(f'<li class="rs-l{l}">' + (f'<a href="#{i}">{html.escape(t)}</a>' if i else f'<span class="rs-off">{html.escape(t)}</span>') + "</li>" for l, i, t in TOC)

flat = "--flat" in sys.argv
prefix = "" if flat else "../"
page = open(os.path.join(HERE, "template.html")).read()
page = (page.replace("{{BODY}}", body + "\n" + footnotes).replace("{{TOC}}", toc).replace("{{BIB}}", bibhtml).replace("{{PREFIX}}", prefix))
out = sys.argv[sys.argv.index("--flat") + 1] if flat else HERE
open(os.path.join(out, "index.html"), "w").write(page)
print("ok", out, "notes", len(USED))
