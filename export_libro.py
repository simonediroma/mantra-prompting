#!/usr/bin/env python3
"""Esporta il libro intero dai capitoli in chapters/.

  python3 export_libro.py

Produce, nella radice del progetto:
  Mantra_Prompting_Capitoli_1-N.pdf   A5 (14,8 x 21 cm), font incorporati, margini a specchio:
                                      interno per la stampa su KDP (copertina morbida).
  Mantra_Prompting_Capitoli_1-N.epub  EPUB 3 per l'eBook Kindle su KDP.

Di ogni capitolo entra solo il testo narrativo (fino a "## Demolition Log").
"""
import re
import sys
import uuid
import zipfile
from datetime import date
from html import escape
from pathlib import Path

import yaml
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A5
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer)
from reportlab.platypus.tableofcontents import TableOfContents

ROOT = Path(__file__).resolve().parent
TITOLO, SOTTOTITOLO, AUTORE = "Mantra Prompting", "Incontrando Emma", "Simone Razzano"
LICENZA = "CC BY-NC-ND 4.0"
LICENZA_URL = "https://creativecommons.org/licenses/by-nc-nd/4.0/deed.it"
CONTATTO = "simone.razzano@gmail.com"
NOTA_LICENZA = (f"Quest'opera è distribuita con licenza Creative Commons Attribuzione - Non commerciale - "
                f"Non opere derivate 4.0 Internazionale ({LICENZA}): {LICENZA_URL}. "
                f"Chi la condivide deve citare autore e titolo originale. "
                f"Per qualsiasi uso commerciale scrivere a {CONTATTO}.")
FONT_DIR = Path("/usr/share/fonts/truetype/liberation")
FONT = {"Serif": "LiberationSerif-Regular", "Serif-Bold": "LiberationSerif-Bold", "Serif-Italic": "LiberationSerif-Italic",
        "Serif-BoldItalic": "LiberationSerif-BoldItalic", "Mono": "LiberationMono-Regular", "Mono-Bold": "LiberationMono-Bold"}


# --- lettura dei capitoli -----------------------------------------------
def capitoli():
    out = []
    for f in sorted((ROOT / "chapters").glob("[0-9][0-9]-*.md")):
        testo = f.read_text(encoding="utf-8")
        _, testa, corpo = testo.split("---", 2)
        corpo = corpo.split("\n## Demolition Log")[0]
        blocchi = [b.strip("\n") for b in re.split(r"\n\s*\n", corpo) if b.strip()]
        out.append({"n": int(f.name[:2]), "titolo": yaml.safe_load(testa)["title"], "blocchi": [tipo(b) for b in blocchi]})
    return out


def tipo(b):
    """Classifica un blocco: modulo (righe di scheda/schermata), citazione, centro (Morse, cartelli), testo."""
    righe = [r.strip() for r in b.split("\n")]
    if all(r.startswith(">") for r in righe):
        return "modulo", [r.lstrip("> ").strip() for r in righe]
    if all(r.startswith("**") for r in righe) and (len(righe) > 1 or righe[0].rstrip("*").count("**") == 1 and righe[0].endswith("**")):
        return "modulo", righe
    if len(righe) == 1:
        r = righe[0]
        nudo = re.sub(r"[*`]", "", r)
        if nudo.startswith('"') and nudo.endswith('"'):
            return "citazione", [r]
        if len(nudo) < 100 and (re.fullmatch(r"[.\-/ ]+", nudo) or (nudo == nudo.upper() and re.search(r"[A-Z]{2}", nudo))):
            return "centro", [r]
    return "testo", [" ".join(righe)]


def inline(s, b="b", i="i", mono='<font name="Mono" size="9">%s</font>'):
    s = escape(s, quote=False)
    s = re.sub(r"\*\*\*(.+?)\*\*\*", rf"<{b}><{i}>\1</{i}></{b}>", s)
    s = re.sub(r"\*\*(.+?)\*\*", rf"<{b}>\1</{b}>", s)
    s = re.sub(r"\*(.+?)\*", rf"<{i}>\1</{i}>", s)
    return re.sub(r"`(.+?)`", lambda m: mono % m.group(1), s)


# --- PDF ----------------------------------------------------------------
def pdf(caps, dest):
    for nome, file in FONT.items():
        pdfmetrics.registerFont(TTFont(nome, str(FONT_DIR / f"{file}.ttf")))
    pdfmetrics.registerFontFamily("Serif", normal="Serif", bold="Serif-Bold", italic="Serif-Italic", boldItalic="Serif-BoldItalic")
    pdfmetrics.registerFontFamily("Mono", normal="Mono", bold="Mono-Bold", italic="Mono", boldItalic="Mono-Bold")
    from reportlab import rl_config
    rl_config.canvas_basefontname = "Serif"   # altrimenti ogni pagina dichiara Helvetica non incorporato (KDP lo rifiuta)

    W, H = A5
    interno, esterno, alto, basso = 17 * mm, 17 * mm, 18 * mm, 20 * mm   # KDP: interno >= 9,6 mm, esterno >= 6,4 mm
    base = ParagraphStyle("testo", fontName="Serif", fontSize=10.5, leading=14.6, alignment=TA_JUSTIFY, firstLineIndent=5 * mm)
    S = {
        "testo": base,
        "primo": ParagraphStyle("primo", parent=base, firstLineIndent=0),
        "citazione": ParagraphStyle("cit", parent=base, firstLineIndent=0, leftIndent=6 * mm, rightIndent=6 * mm,
                                    spaceBefore=6, spaceAfter=6, alignment=TA_LEFT),
        "centro": ParagraphStyle("centro", parent=base, firstLineIndent=0, alignment=TA_CENTER, spaceBefore=7, spaceAfter=7),
        "modulo": ParagraphStyle("modulo", fontName="Mono", fontSize=8.2, leading=11.6, leftIndent=5 * mm, rightIndent=3 * mm,
                                 spaceBefore=7, spaceAfter=7, alignment=TA_LEFT),
        "num": ParagraphStyle("num", fontName="Serif", fontSize=11, leading=14, alignment=TA_CENTER, spaceBefore=30 * mm,
                              textColor="#555555"),
        "cap": ParagraphStyle("cap", fontName="Serif", fontSize=19, leading=24, alignment=TA_CENTER, spaceAfter=16 * mm),
        "indice": ParagraphStyle("indice", fontName="Serif", fontSize=10.5, leading=17),
    }

    class Libro(BaseDocTemplate):
        def afterFlowable(self, fl):
            if getattr(fl, "voce", None):
                self.notify("TOCEntry", (0, fl.voce, self.page))

    def numero(c, doc):
        c.setFont("Serif", 9)
        c.drawCentredString(W / 2, 11 * mm, str(doc.page))

    def cornice(dispari):
        sx = interno if dispari else esterno
        return Frame(sx, basso, W - interno - esterno, H - alto - basso, leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)

    doc = Libro(str(dest), pagesize=A5, title=f"{TITOLO}: {SOTTOTITOLO}", author=AUTORE, subject="Romanzo", creator="export_libro.py",
                 initialFontName="Serif", initialFontSize=10.5)
    doc.addPageTemplates([
        PageTemplate("nuda", [cornice(True)]),
        PageTemplate("corpo", [cornice(True)], onPage=numero),
    ])

    st = [Spacer(1, 48 * mm),
          Paragraph(TITOLO.upper(), ParagraphStyle("t", fontName="Serif", fontSize=26, leading=32, alignment=TA_CENTER)),
          Spacer(1, 5 * mm),
          Paragraph(SOTTOTITOLO, ParagraphStyle("s", fontName="Serif-Italic", fontSize=16, leading=20, alignment=TA_CENTER)),
          Spacer(1, 60 * mm),
          Paragraph(AUTORE, ParagraphStyle("a", fontName="Serif", fontSize=12, leading=16, alignment=TA_CENTER)),
          PageBreak(),
          Spacer(1, 120 * mm),
          Paragraph(f"{TITOLO}: {SOTTOTITOLO}<br/>© {date.today().year} {AUTORE}<br/><br/>{NOTA_LICENZA}<br/><br/>"
                    "Questo libro è un'opera di fantasia. Nomi, personaggi, aziende, luoghi ed eventi sono frutto "
                    "dell'immaginazione dell'autore o sono usati in modo fittizio.",
                    ParagraphStyle("c", fontName="Serif", fontSize=8.5, leading=12)),
          PageBreak(),
          Paragraph("Indice", ParagraphStyle("ti", fontName="Serif", fontSize=17, leading=22, alignment=TA_CENTER,
                                             spaceBefore=14 * mm, spaceAfter=10 * mm))]
    toc = TableOfContents()
    toc.levelStyles = [S["indice"]]
    toc.dotsMinLevel = 0
    from reportlab.platypus import TableStyle
    toc.tableStyle = TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                                 ("LEFTPADDING", (0, 0), (-1, -1), 0), ("FONTNAME", (0, 0), (-1, -1), "Serif")])
    st += [toc]
    for c in caps:
        # ogni capitolo comincia su una pagina nuova
        st += [NextPageTemplate("corpo"), PageBreak()]
        st += [Paragraph(str(c["n"]), S["num"])]
        t = Paragraph(escape(c["titolo"]), S["cap"])
        t.voce = f'{c["n"]}. {escape(c["titolo"])}'
        st.append(t)
        primo = True
        for genere, righe in c["blocchi"]:
            if genere == "modulo":
                st.append(KeepTogether([Paragraph("<br/>".join(inline(r, mono="%s") for r in righe), S["modulo"])]))
                primo = True
            elif genere in ("citazione", "centro"):
                st.append(Paragraph(inline(righe[0]), S[genere]))
                primo = True
            else:
                st.append(Paragraph(inline(righe[0]), S["primo" if primo else "testo"]))
                primo = False
    doc.multiBuild(st)


def correggi_specchio(dest):
    """Dopo l'impaginazione verifica che i margini siano a specchio: pagine dispari a destra."""
    from pypdf import PdfReader
    return len(PdfReader(str(dest)).pages)


# --- EPUB ---------------------------------------------------------------
CSS = """body{font-family:serif;line-height:1.45}
h1{text-align:center;font-weight:normal;font-size:1.6em;margin:2.5em 0 2em}
h1 span{display:block;font-size:.6em;color:#555;margin-bottom:.6em}
p{margin:0;text-indent:1.3em;text-align:justify}
p.primo{text-indent:0}
p.citazione{text-indent:0;margin:.8em 1.3em;text-align:left}
p.centro{text-indent:0;text-align:center;margin:.9em 0}
p.modulo{text-indent:0;text-align:left;font-family:monospace;font-size:.82em;margin:.9em 0 .9em 1.2em;line-height:1.5}
code{font-family:monospace;font-size:.9em}
.fronte{text-align:center;margin-top:30%}.fronte h1{font-size:2em;margin:0}.fronte p{text-indent:0;text-align:center}
"""
XHTML = ('<?xml version="1.0" encoding="utf-8"?>\n<!DOCTYPE html>\n<html xmlns="http://www.w3.org/1999/xhtml" '
         'xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="it" lang="it"><head><meta charset="utf-8"/><title>%s</title>'
         '<link rel="stylesheet" type="text/css" href="stile.css"/></head><body>%s</body></html>')


def epub(caps, dest):
    uid = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "https://simonediroma.github.io/mantra-prompting"))
    tag = dict(b="strong", i="em", mono="<code>%s</code>")
    file = [("fronte.xhtml", TITOLO, f'<div class="fronte"><h1>{TITOLO}</h1><p><em>{SOTTOTITOLO}</em></p><p>&#160;</p>'
             f'<p>{AUTORE}</p><p>&#160;</p><p>© {date.today().year} {AUTORE}.</p><p>{escape(NOTA_LICENZA)}</p></div>')]
    for c in caps:
        h = [f'<h1><span>{c["n"]}</span>{escape(c["titolo"])}</h1>']
        primo = True
        for genere, righe in c["blocchi"]:
            if genere == "testo":
                h.append(f'<p{" class=%sprimo%s" % (chr(34), chr(34)) if primo else ""}>{inline(righe[0], **tag)}</p>')
                primo = False
            else:
                h.append(f'<p class="{genere}">{"<br/>".join(inline(r, **tag) for r in righe)}</p>')
                primo = True
        file.append((f'cap{c["n"]:02d}.xhtml', f'{c["n"]}. {c["titolo"]}', "".join(h)))
    nav = "".join(f'<li><a href="{f}">{escape(t)}</a></li>' for f, t, _ in file[1:])
    manifest = "".join(f'<item id="f{k}" href="{f}" media-type="application/xhtml+xml"/>' for k, (f, _, _) in enumerate(file))
    spine = "".join(f'<itemref idref="f{k}"/>' for k in range(len(file)))
    opf = (f'<?xml version="1.0" encoding="utf-8"?>\n<package xmlns="http://www.idpf.org/2007/opf" version="3.0" '
           f'unique-identifier="id" xml:lang="it"><metadata xmlns:dc="http://purl.org/dc/elements/1.1/">'
           f'<dc:identifier id="id">{uid}</dc:identifier><dc:title>{TITOLO}: {SOTTOTITOLO}</dc:title>'
           f'<dc:creator>{AUTORE}</dc:creator><dc:language>it</dc:language><dc:rights>{LICENZA} {LICENZA_URL}</dc:rights>'
           f'<meta property="dcterms:modified">{date.today().isoformat()}T00:00:00Z</meta></metadata>'
           f'<manifest><item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>'
           f'<item id="css" href="stile.css" media-type="text/css"/>{manifest}</manifest><spine>{spine}</spine></package>')
    with zipfile.ZipFile(dest, "w") as z:
        z.writestr(zipfile.ZipInfo("mimetype"), "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        d = zipfile.ZIP_DEFLATED
        z.writestr("META-INF/container.xml", '<?xml version="1.0"?><container version="1.0" '
                   'xmlns="urn:oasis:names:tc:opendocument:xmlns:container"><rootfiles><rootfile full-path="OEBPS/libro.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles></container>', d)
        z.writestr("OEBPS/libro.opf", opf, d)
        z.writestr("OEBPS/stile.css", CSS, d)
        z.writestr("OEBPS/nav.xhtml", XHTML % ("Indice", f'<nav epub:type="toc"><h1>Indice</h1><ol>{nav}</ol></nav>'), d)
        for f, t, corpo in file:
            z.writestr("OEBPS/" + f, XHTML % (escape(t), corpo), d)


def main():
    caps = capitoli()
    nome = f"Mantra_Prompting_Capitoli_1-{caps[-1]['n']}"
    pdf(caps, ROOT / f"{nome}.pdf")
    pagine = correggi_specchio(ROOT / f"{nome}.pdf")
    epub(caps, ROOT / f"{nome}.epub")
    parole = sum(len(r.split()) for c in caps for _, righe in c["blocchi"] for r in righe)
    print(f"OK: {nome}.pdf ({pagine} pagine) e {nome}.epub · {len(caps)} capitoli · {parole} parole")


if __name__ == "__main__":
    sys.exit(main())
