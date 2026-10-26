import re, html, os
SRC = os.path.expanduser("~/src/life-itself/publications/tech/essay.md")
L = open(SRC).read().split("\n")

# footnotes
NOTES = {}
for ln in L:
    m = re.match(r"\[\^(\d+)\]:\s*(.*)", ln)
    if m: NOTES[m.group(1)] = m.group(2).strip()

def clean(t):
    t = t.replace("\\-", "–").replace("\\!", "!").replace("\\.", ".").replace(" -- ", " – ")
    return t

def inline(t, notes=True):
    t = clean(t)
    t = html.escape(t, quote=False)
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: f'<a href="{m.group(2) if m.group(2).startswith("http") else "https://secondrenaissance.net" + m.group(2)}">{m.group(1)}</a>', t)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    if notes:
        def sn(m):
            n = m.group(1)
            body = inline(NOTES.get(n, ""), notes=False)
            return (f'<span class="sn"><button type="button" class="sn-ref" aria-expanded="false" aria-controls="sn{n}" aria-label="Note {n}">{n}</button>'
                    f'<span class="sn-note" id="sn{n}" role="note"><span class="sn-n">{n}</span> {body}</span></span>')
        t = re.sub(r"([^\s<>]*)\[\^(\d+)\]", lambda m: '<span class="nw">' + m.group(1) + sn(type("M", (), {"group": lambda self, k: m.group(2)})()) + "</span>", t)
    return t

def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:40]

TOC = []  # (level, id, label, included)

def convert(a, b, chapter_first=True):
    """lines a..b inclusive (1-based)"""
    out, para = [], []
    lines = L[a-1:b]
    i = 0
    first_p_in_chapter = False
    def flush():
        nonlocal first_p_in_chapter
        if para:
            txt = " ".join(para).strip()
            para.clear()
            if not txt: return
            if txt.startswith("**") and txt.endswith("**") and txt.count("**") == 2:
                out.append(f'<p class="inbrief"><span class="inbrief-label">In brief</span> {inline(txt[2:-2])}</p>')
                return
            cls = ' class="first"' if first_p_in_chapter else ""
            first_p_in_chapter = False
            out.append(f"<p{cls}>{inline(txt)}</p>")
    while i < len(lines):
        ln = lines[i].rstrip()
        h = re.match(r"(#{1,4})\s+(.*?)\s*(\{#.*\})?\s*$", ln)
        if h and h.group(2).strip():
            flush()
            lvl = len(h.group(1)); title = clean(h.group(2).strip())
            hid = slug(title)
            if lvl == 1:
                m = re.match(r"(\d+)\.\s+(.*)", title)
                num, name = (m.group(1), m.group(2)) if m else ("", title)
                TOC.append((1, hid, (num + ". " if num else "") + name, True))
                out.append('<div class="break" aria-hidden="true"></div>' if out or a > 24 else "")
                out.append(f'<h2 id="{hid}" class="chapter"><span class="num">{num}</span><span class="name">{html.escape(name)}</span></h2>')
                first_p_in_chapter = True
            elif lvl == 2:
                TOC.append((2, hid, title, True))
                out.append(f'<h3 id="{hid}">{html.escape(title)}</h3>')
                first_p_in_chapter = False
            elif lvl == 3:
                out.append(f'<h4 id="{hid}">{html.escape(title)}</h4>')
            else:
                out.append(f'<h5>{html.escape(title)}</h5>')
            i += 1; continue
        if ln.startswith("*") and not ln.startswith("**") and i + 1 < len(lines):
            # epigraph block: italic lines until "- Name"
            j = i; quote = []
            while j < len(lines) and lines[j].strip() and not lines[j].strip().startswith("- "):
                quote.append(lines[j].strip()); j += 1
            k = j
            while k < len(lines) and not lines[k].strip(): k += 1
            if k < len(lines) and lines[k].strip().startswith("- "):
                flush()
                q = " ".join(x.strip("* ").strip() for x in quote)
                who = lines[k].strip()[2:]
                out.append(f'<blockquote class="epigraph"><p>{inline(q)}</p><cite>{inline(who)}</cite></blockquote>')
                i = k + 1; continue
        if not ln.strip():
            flush()
        else:
            para.append(ln.strip())
        i += 1
    flush()
    return "\n".join(x for x in out if x)

PULL = '<aside class="pull" aria-hidden="true"><p>“There’s no discernible difference between the internet and an omniscient being – except that the former answers questions with a higher degree of reliability.”</p></aside>'

SHIFTS = '''<figure class="fig wide shifts" id="fig-shifts">
  <div class="shift"><div class="from"><span class="lab">From</span>Out-of-control tech, arising from collective action problems <span class="root">rooted in modern individualism and reductivism</span></div><div class="arrow" aria-hidden="true">→</div><div class="to"><span class="lab">To</span>Collective restraint, supported by a worldview of <b>interbeing</b></div></div>
  <div class="shift"><div class="from"><span class="lab">From</span>A tyranny of technology, arising from a rationalist illusion of human agency and freedom</div><div class="arrow" aria-hidden="true">→</div><div class="to"><span class="lab">To</span>Wiser choice, founded on a holistic understanding of human nature and attunement to an <b>inner compass</b></div></div>
  <figcaption><span class="fignum">Figure 1</span> The two shifts the essay proposes. Chapter 3 takes each in turn.</figcaption>
</figure>'''

intro = convert(24, 66)  # up to "Shifting our relationship" para
SERIES = '''<figure class="fig margin series-fig"><ol>
  <li>What and Why</li><li>How</li><li>Polycrisis to Metacrisis</li><li>Developmental Spaces</li><li class="here">In Tech We Trust</li><li>Wisdom</li></ol>
  <figcaption><span class="fignum">Figure 0</span> Where this paper sits in the series.</figcaption></figure>'''
FEATURES = '''<figure class="fig column features"><ul>
  <li>Material reality as paramount</li><li>The myth of progress</li><li>Technology as cosmological metaphor</li><li>Individualism</li><li>Rationalism and freedom</li><li>Homo economicus</li></ul>
  <figcaption><span class="fignum">Figure 2</span> Six features of the modern cultural paradigm that shape, and are shaped by, our relationship with technology.</figcaption></figure>'''
intro = intro.replace("<p class=\"first\">", SERIES + "\n<p class=\"first\">", 1)
intro = intro.replace("<h5>Material reality as paramount</h5>", FEATURES + "\n<h5>Material reality as paramount</h5>", 1)
intro += "\n" + SHIFTS
ch1 = convert(76, 84)
ch2 = convert(86, 115)
ch2 = ch2.replace("<h4 id=\"in-tech-we-trust\">", PULL + "\n<h4 id=\"in-tech-we-trust\">", 1)
ch22 = convert(116, 133)
OMIT = [(2, "utility", "2.2 (continued) Utility and the rational fallacy; Tech as creator", False),
        (2, "ai", "2.3 AI: the logical conclusion of modern attitudes to tech?", False),
        (1, "future", "3. Tech in a future society: a wiser relationship?", False),
        (2, "agency", "3.1 Restoring agency: beyond collective action problems", False),
        (2, "tyranny", "3.2 Escaping the tyranny of tech", False)]
gap = '''<div class="omitted" role="note"><span class="lab">Not in this mockup</span><p>The rest of 2.2, section 2.3 and chapter 3 (about 6,000 words) are left out to keep the mockup light. The full text is in <code>2rbook/tech/essay.md</code>.</p></div>'''
TOC.extend(OMIT)
concl = convert(299, 305)

# bibliography: first 8 entries
bib = []
cont = False
for ln in L[308:]:
    s = ln.strip()
    if s.startswith("[^"): break
    if s and not s.startswith("#"):
        if cont and bib: bib[-1] += " " + s
        else: bib.append(s)
    cont = ln.endswith("  ") and bool(s)
bibhtml = "\n".join(f"<li>{inline(x, notes=False)}</li>" for x in bib[:8])

body = intro + "\n" + ch1 + "\n" + ch2 + "\n" + ch22 + "\n" + gap + "\n" + concl

# reorder TOC: insert omitted after 2.2
toc_items = [t for t in TOC if t[3]]
conc = [t for t in toc_items if t[1] == "conclusion"]
main = [t for t in toc_items if t[1] != "conclusion"]
toc_all = main + OMIT + conc
def tochtml():
    out = []
    for lvl, hid, label, inc in toc_all:
        cls = f"l{lvl}" + ("" if inc else " off")
        out.append(f'<li class="{cls}">' + (f'<a href="#{hid}">{html.escape(label)}</a>' if inc else f'<span>{html.escape(label)}</span>') + "</li>")
    return "\n".join(out)

used = sorted({int(n) for n in re.findall(r'id="sn(\d+)"', body)})
notes_list = "\n".join(f'<li value="{n}">{inline(NOTES[str(n)], notes=False)}</li>' for n in used)

words = len(re.sub("<[^>]+>", " ", body).split())
tpl = open("template.html").read()
page = (tpl.replace("{{BODY}}", body).replace("{{TOC}}", tochtml())
           .replace("{{NOTES}}", notes_list).replace("{{BIB}}", bibhtml))
open("index.html", "w").write(page)
print("ok words in mockup", words, "notes", len(used))
