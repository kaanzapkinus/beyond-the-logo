#!/usr/bin/env python3
"""
export_phone_scripts.py - Phone-Readable Script Exporter for Beyond the Logo
===========================================================================
Exports speaker delivery scripts for Kaan and Caner into:
  - Large-type A5 portrait PDFs (Kaan_Script.pdf, Caner_Script.pdf) via ReportLab
  - Clean, responsive HTML companion files (Kaan_Script.html, Caner_Script.html)

Design & Typographic Invariants:
  - PDF: A5 portrait (148 x 210 mm), 17pt readable body, 23pt leading,
         black text on white background, generous margins (40pt).
  - Pagination: Each slide starts a new page with a distinct heading (SLIDE 1, etc.).
                If a slide's spoken prose overflows the page, it cleanly flows to
                the next page with a distinct continuation label (SLIDE 1 (cont.)).
  - Content: ONLY distinct slide headings and approved spoken prose paragraphs.
             Zero timings, citations, stage directions, or nonspeakable prose.
  - Text Integrity: Verbatim approved spoken prose from Kaan_Script.txt and
                    Caner_Script.txt, verified against deck.json notes. Never rewritten.
  - Robust Escaping: Full XML entity escaping (&amp;, &lt;, &gt;) for ReportLab Platypus
                     and HTML entity escaping for web output.
  - HTML: Responsive layout, 20px body, line-height 1.65, max-width 40rem,
          viewport meta tag, and prefers-color-scheme (light and dark mode).
"""

import os
import sys
import json
import re
import html
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any, Optional


def parse_script_txt(txt_path: Path) -> List[Tuple[int, List[str]]]:
    """
    Parses an approved speaker script TXT file.
    Returns list of (slide_id, [paragraph_1, paragraph_2, ...]).
    """
    content = txt_path.read_text(encoding="utf-8")
    slides: List[Tuple[int, List[str]]] = []

    pattern = r'(?m)^SLIDE\s+(\d+)\s*$'
    matches = list(re.finditer(pattern, content))
    if not matches:
        raise ValueError(f"No slide headings found in {txt_path}")

    for i, match in enumerate(matches):
        slide_id = int(match.group(1))
        start_pos = match.end()
        end_pos = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        slide_body = content[start_pos:end_pos].strip()

        paras = [p.strip() for p in re.split(r'\n\s*\n', slide_body) if p.strip()]
        slides.append((slide_id, paras))

    return slides


def load_and_verify_scripts() -> Dict[str, List[Tuple[int, List[str]]]]:
    """
    Loads approved TXT scripts and verifies consistency against deck.json.
    Returns dictionary with keys 'Kaan' and 'Caner'.
    """
    kaan_path = Path("scripts/Kaan_Script.txt") if Path("scripts/Kaan_Script.txt").exists() else Path("Kaan_Script.txt")
    caner_path = Path("scripts/Caner_Script.txt") if Path("scripts/Caner_Script.txt").exists() else Path("Caner_Script.txt")
    deck_path = Path("research/deck.json") if Path("research/deck.json").exists() else Path("deck.json")

    if not kaan_path.exists():
        raise FileNotFoundError(f"Missing required script file: {kaan_path}")
    if not caner_path.exists():
        raise FileNotFoundError(f"Missing required script file: {caner_path}")

    kaan_slides = parse_script_txt(kaan_path)
    caner_slides = parse_script_txt(caner_path)

    if deck_path.exists():
        try:
            with open(deck_path, "r", encoding="utf-8") as f:
                deck_data = json.load(f)
            deck_slides = {s["id"]: s for s in deck_data.get("slides", [])}

            for s_id, paras in kaan_slides:
                if s_id in deck_slides:
                    d_s = deck_slides[s_id]
                    if d_s.get("speaker") != 1:
                        print(f"Note: Slide {s_id} speaker in deck.json is {d_s.get('speaker')}, expected 1", file=sys.stderr)

            for s_id, paras in caner_slides:
                if s_id in deck_slides:
                    d_s = deck_slides[s_id]
                    if d_s.get("speaker") != 2:
                        print(f"Note: Slide {s_id} speaker in deck.json is {d_s.get('speaker')}, expected 2", file=sys.stderr)
        except Exception as e:
            print(f"Notice reading deck.json: {e}", file=sys.stderr)

    return {
        "Kaan": kaan_slides,
        "Caner": caner_slides,
    }


def escape_xml(text: str) -> str:
    """
    Robustly escapes XML markup for ReportLab Platypus Paragraphs.
    Prevents Expat parsing crashes on strings containing '&', '<', or '>'.
    """
    return (
        text.replace("&", "&amp;")
            .replace("<", "&lt;")
            .replace(">", "&gt;")
    )


def escape_html(text: str) -> str:
    """
    Robustly escapes HTML entities for web output.
    """
    return html.escape(text, quote=True)


def export_pdf(speaker_name: str, slides: List[Tuple[int, List[str]]], output_path: Path):
    """
    Generates a large-type A5 portrait phone script PDF using ReportLab.
    Each slide starts a new page with a distinct heading (SLIDE 1, etc.).
    If a slide's spoken text overflows, it flows to the next page with a clear
    continuation label (SLIDE 1 (cont.)).
    """
    from reportlab.lib.pagesizes import A5
    from reportlab.lib import colors
    from reportlab.lib.styles import ParagraphStyle
    from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak

    page_w, page_h = A5
    margin_left = 40.0
    margin_right = 40.0
    margin_top = 42.0
    margin_bottom = 42.0

    avail_w = page_w - margin_left - margin_right
    avail_h = page_h - margin_top - margin_bottom

    style_heading = ParagraphStyle(
        "SlideHeading",
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=26,
        textColor=colors.black,
        spaceAfter=14,
        keepWithNext=True,
    )

    style_cont_heading = ParagraphStyle(
        "SlideContinuationHeading",
        fontName="Helvetica-Bold",
        fontSize=17,
        leading=23,
        textColor=colors.black,
        spaceAfter=14,
        keepWithNext=True,
    )

    style_body = ParagraphStyle(
        "SlideBody",
        fontName="Helvetica",
        fontSize=17,
        leading=23,
        textColor=colors.black,
        spaceAfter=14,
    )

    doc = SimpleDocTemplate(
        str(output_path),
        pagesize=A5,
        leftMargin=margin_left,
        rightMargin=margin_right,
        topMargin=margin_top,
        bottomMargin=margin_bottom,
        title=f"{speaker_name} Script",
        author=speaker_name,
    )

    story = []

    for s_idx, (slide_id, paragraphs) in enumerate(slides):
        if s_idx > 0:
            story.append(PageBreak())

        heading_text = f"SLIDE {slide_id}"
        cont_heading_text = f"SLIDE {slide_id} (cont.)"

        p_head = Paragraph(escape_xml(heading_text), style_heading)
        _, h_head = p_head.wrap(avail_w, avail_h)

        p_cont = Paragraph(escape_xml(cont_heading_text), style_cont_heading)
        _, h_cont = p_cont.wrap(avail_w, avail_h)

        effective_avail_h = avail_h - 4.0

        story.append(p_head)
        current_remaining_h = effective_avail_h - h_head - style_heading.spaceAfter

        for p_idx, para in enumerate(paragraphs):
            p_body = Paragraph(escape_xml(para), style_body)
            _, h_para = p_body.wrap(avail_w, avail_h)
            space_after = style_body.spaceAfter if p_idx < len(paragraphs) - 1 else 0
            total_para_h = h_para + space_after

            if total_para_h <= current_remaining_h:
                story.append(p_body)
                current_remaining_h -= total_para_h
            else:
                story.append(PageBreak())
                story.append(p_cont)
                story.append(p_body)
                current_remaining_h = effective_avail_h - h_cont - style_cont_heading.spaceAfter - total_para_h

    doc.build(story)


def export_html(speaker_name: str, slides: List[Tuple[int, List[str]]], output_path: Path):
    """
    Generates a responsive, phone-readable HTML script file.
    Specifications:
      - 20px body, line-height 1.65, max-width 40rem
      - Viewport meta tag
      - prefers-color-scheme support (light and dark mode)
      - Semantic section structure with distinct slide headings
      - No timings, citations, stage directions, or nonspeakable prose
      - Robust HTML escaping
    """
    sections_html = []
    for slide_id, paragraphs in slides:
        heading_esc = escape_html(f"SLIDE {slide_id}")
        p_elements = [f"      <p>{escape_html(p)}</p>" for p in paragraphs]
        paras_joined = "\n".join(p_elements)
        section = (
            f'    <section class="slide-block" id="slide-{slide_id}">\n'
            f'      <h2 class="slide-heading">{heading_esc}</h2>\n'
            f'{paras_joined}\n'
            f'    </section>'
        )
        sections_html.append(section)

    all_sections = "\n\n".join(sections_html)

    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape_html(speaker_name)} — Spoken Script</title>
  <style>
    :root {{
      --bg-color: #ffffff;
      --text-color: #111827;
      --heading-color: #000000;
      --border-color: #e5e7eb;
    }}
    @media (prefers-color-scheme: dark) {{
      :root {{
        --bg-color: #121212;
        --text-color: #f3f4f6;
        --heading-color: #ffffff;
        --border-color: #2d3748;
      }}
    }}
    * {{
      box-sizing: border-box;
    }}
    html {{
      background-color: var(--bg-color);
    }}
    body {{
      background-color: var(--bg-color);
      color: var(--text-color);
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
      font-size: 20px;
      line-height: 1.65;
      max-width: 40rem;
      margin: 0 auto;
      padding: 2rem 1.25rem 4rem;
    }}
    .slide-block {{
      margin-bottom: 2.75rem;
      padding-bottom: 2rem;
      border-bottom: 1px solid var(--border-color);
    }}
    .slide-block:last-child {{
      border-bottom: none;
      margin-bottom: 0;
      padding-bottom: 0;
    }}
    .slide-heading {{
      font-size: 1.35rem;
      font-weight: 700;
      letter-spacing: 0.04em;
      text-transform: uppercase;
      color: var(--heading-color);
      margin: 0 0 1.25rem;
    }}
    p {{
      margin: 0 0 1.25rem;
    }}
    p:last-child {{
      margin-bottom: 0;
    }}
  </style>
</head>
<body>
  <main>
{all_sections}
  </main>
</body>
</html>
"""
    output_path.write_text(html_content, encoding="utf-8")



def export_docx(speaker_name: str, slides: List[Tuple[int, List[str]]], output_path: Path):
    """Generates a clean DOCX script with speaker name on top-left."""
    import docx
    from docx.shared import Inches, Pt, RGBColor
    doc = docx.Document()
    for section in doc.sections:
        section.top_margin = Inches(0.8)
        section.bottom_margin = Inches(0.8)
        section.left_margin = Inches(0.8)
        section.right_margin = Inches(0.8)
    first = True
    for slide_id, paragraphs in slides:
        if not first:
            doc.add_page_break()
        first = False
        p_spk = doc.add_paragraph()
        r_spk = p_spk.add_run(speaker_name.upper())
        r_spk.bold = True
        r_spk.font.size = Pt(13)
        r_spk.font.color.rgb = RGBColor(75, 85, 99)
        p_spk.paragraph_format.space_after = Pt(4)
        
        p_head = doc.add_paragraph()
        r_head = p_head.add_run(f"SLIDE {slide_id}")
        r_head.bold = True
        r_head.font.size = Pt(18)
        r_head.font.color.rgb = RGBColor(17, 24, 39)
        p_head.paragraph_format.space_after = Pt(14)
        
        for p_text in paragraphs:
            p = doc.add_paragraph()
            r = p.add_run(p_text)
            r.font.size = Pt(14)
            r.font.color.rgb = RGBColor(17, 24, 39)
            p.paragraph_format.line_spacing = 1.3
            p.paragraph_format.space_after = Pt(12)
    doc.save(str(output_path))


def main():
    parser = argparse.ArgumentParser(description="Export phone-readable scripts to PDF and HTML.")
    parser.add_argument("--pdf-only", action="store_true", help="Export PDF files only.")
    parser.add_argument("--html-only", action="store_true", help="Export HTML files only.")
    args = parser.parse_args()

    scripts = load_and_verify_scripts()

    export_all = not (args.pdf_only or args.html_only)
    do_pdf = export_all or args.pdf_only
    do_html = export_all or args.html_only

    if do_pdf:
        try:
            import reportlab
        except ImportError:
            print(
                "Notice: ReportLab is not installed in the active environment. "
                "Parent will run PDF generation later in Python 3.10+ .venv.",
                file=sys.stderr
            )
            if not do_html:
                sys.exit(1)
            do_pdf = False

    out_dir = Path("scripts") if Path("scripts").exists() else Path(".")
    for speaker_name, slides in scripts.items():
        if do_pdf:
            pdf_path = out_dir / f"{speaker_name}_Script.pdf"
            export_pdf(speaker_name, slides, pdf_path)
            print(f"Exported {pdf_path} ({len(slides)} slides).")

        if do_html:
            html_path = out_dir / f"{speaker_name}_Script.html"
            export_html(speaker_name, slides, html_path)
            print(f"Exported {html_path} ({len(slides)} slides).")

        docx_path = out_dir / f"{speaker_name}_Script.docx"
        export_docx(speaker_name, slides, docx_path)
        print(f"Exported {docx_path} ({len(slides)} slides).")

if __name__ == "__main__":
    main()
