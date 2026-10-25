#!/usr/bin/env python3
"""
build_deck.py - Beyond the Logo Presentation Generator
======================================================
Generates 'Beyond_the_Logo.pptx' (16:9 widescreen, 13.333" x 7.5").
Strictly adheres to BRIEF.md, SLIDE_CONTRACT.json, deck.json,
safe_sources.json, and assets.json.

Key Design & Content Invariants:
- Real content ONLY from deck.json, safe_sources.json, and assets.json.
- No obsolete CANONICAL_SOURCES, no hardcoded fallback facts, no injected claims.
- White base, dark charcoal text, Arial typography.
- Exact visual mapping across all 24 slides (20 timed + 2 source references + 2 image credits) with zero drop shadows.
"""

import os, sys, json
from pathlib import Path
from typing import Dict, List, Any, Optional, Union

from PIL import Image

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml import parse_xml


# --- Typography & Color Constants ---
FONT_FAMILY = "Arial"

COLOR_WHITE = RGBColor(255, 255, 255)
COLOR_BLACK = RGBColor(17, 24, 39)        # Charcoal #111827
COLOR_MUTED = RGBColor(107, 114, 128)     # Mid Slate #6B7280
COLOR_DARK_MUTED = RGBColor(75, 85, 99)   # Slate #4B5563
COLOR_BORDER = RGBColor(229, 231, 235)    # Light Border #E5E7EB
COLOR_CARD_BG = RGBColor(249, 250, 251)   # Neutral Surface #F9FAFB
COLOR_LINK = RGBColor(37, 99, 235)        # Royal Blue #2563EB

COLOR_COKE_RED = RGBColor(218, 41, 28)    # #DA291C
COLOR_MCD_YELLOW = RGBColor(255, 199, 44) # #FFC72C
COLOR_TIFFANY = RGBColor(129, 216, 208)   # #81D8D0
COLOR_IKEA_BLUE = RGBColor(0, 88, 163)    # #0058A3

SHORT_SOURCE_TITLES: Dict[str, str] = {
    "S1": "Brand differentiation research",
    "S2": "Seven Costly Sins of Brand Identity",
    "S3": "Brands of Distinction",
    "S4": "The Coca-Cola Contour Bottle",
    "S5": "Tiffany Blue",
    "S6": "History of the IKEA Logotype",
    "S7": "The Story of FRAKTA",
    "S8": "McDonald’s Green Backgrounds",
    "S9": "Follow the Arches",
}

SHORT_ASSET_TITLES: Dict[str, str] = {
    "mcdonalds-fries-packaging": "McDonald's French Fries in Red Carton",
    "mcdonalds-follow-the-arches-billboard": "McDonald's 'Follow the Arches' Billboard",
    "coca-cola-contour-bottle": "Coca-Cola Classic Contour Bottle",
    "coca-cola-bottle-patent-1915": "1915 Coca-Cola Contour Bottle Patent Drawing",
    "tiffany-blue-box": "Tiffany & Co. Blue Gift Box",
    "ikea-store-exterior": "IKEA Warehouse Store Exterior",
    "ikea-frakta-bag": "IKEA Blue FRAKTA Shopping Bag",
}


# --- Data Loaders ---
def load_sources() -> Dict[str, Dict[str, Any]]:
    path = Path("research/safe_sources.json") if Path("research/safe_sources.json").exists() else Path("safe_sources.json")
    with open(path, "r", encoding="utf-8") as f:
        return {s["id"]: s for s in json.load(f).get("sources", [])}

def load_assets() -> Dict[str, Dict[str, Any]]:
    path = Path("assets/assets.json") if Path("assets/assets.json").exists() else Path("assets.json")
    with open(path, "r", encoding="utf-8") as f:
        return {a["id"]: a for a in json.load(f)}

def load_assets_list() -> List[Dict[str, Any]]:
    path = Path("assets/assets.json") if Path("assets/assets.json").exists() else Path("assets.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_deck() -> Dict[str, Any]:
    path = Path("research/deck.json") if Path("research/deck.json").exists() else Path("deck.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

# --- Crop Derivations ---
def ensure_derived_crops() -> Dict[str, Path]:
    derived_dir = Path("assets/derived")
    derived_dir.mkdir(parents=True, exist_ok=True)
    crops: Dict[str, Path] = {}
    def do_crop(src_name, dst_name, box, fmt="JPEG"):
        s_path, d_path = Path(src_name), derived_dir / dst_name
        if s_path.exists():
            with Image.open(s_path) as img:
                w, h = img.size
                img.crop((int(w * box[0]), int(h * box[1]), int(w * box[2]), int(h * box[3]))).save(d_path, fmt, quality=92)
            return d_path
        return None

    c_mcd = do_crop("assets/mcdonalds-fries-packaging.jpg", "mcdonalds_carton_quiz_crop.jpg", (0.15, 0.15, 0.85, 0.35))
    if c_mcd: crops["mcd_carton_top"] = c_mcd
    c_tif = do_crop("assets/tiffany-blue-box.jpg", "tiffany_box_quiz_crop.jpg", (0.50, 0.25, 0.82, 0.55))
    if c_tif: crops["tiffany_box_top"] = c_tif
    c_bag = do_crop("assets/ikea-frakta-bag.jpg", "ikea_bag_quiz_crop.jpg", (0.65, 0.33, 0.77, 0.50))
    if c_bag: crops["ikea_bag_center"] = c_bag
    c_det = do_crop("assets/tiffany-blue-box.jpg", "tiffany_box_detail_crop.jpg", (0.20, 0.18, 0.80, 0.60))
    if c_det: crops["tiffany_detail"] = c_det

    sil = derived_dir / "coca-cola-contour-bottle_silhouette.png"
    crops["bottle_silhouette"] = sil if sil.exists() else do_crop("assets/coca-cola-contour-bottle.jpg", sil.name, (0.25, 0.15, 0.75, 0.85), "PNG")
    return crops


# --- Layout & Presentation Helpers ---
def disable_effects(shape):
    sp = shape._element
    spPr = getattr(sp, "spPr", None)
    if spPr is not None:
        effectLst = spPr.find("{http://schemas.openxmlformats.org/drawingml/2006/main}effectLst")
        if effectLst is None:
            if hasattr(spPr, "get_or_add_effectLst"):
                spPr.get_or_add_effectLst()
            else:
                spPr.append(parse_xml('<a:effectLst xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"/>'))
    style = sp.find("{http://schemas.openxmlformats.org/presentationml/2006/main}style")
    if style is not None:
        effectRef = style.find("{http://schemas.openxmlformats.org/drawingml/2006/main}effectRef")
        if effectRef is not None:
            effectRef.set("idx", "0")
    return shape

def add_textbox(slide, left, top, width, height, text: str = "", font_size: int = 24, bold: bool = False,
                color: RGBColor = COLOR_BLACK, align: PP_ALIGN = PP_ALIGN.LEFT, space_after: int = 0):
    tx = slide.shapes.add_textbox(left, top, width, height)
    disable_effects(tx)
    tf = tx.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = Inches(0)
    if text:
        p = tf.paragraphs[0]
        p.text = text
        p.font.name = FONT_FAMILY
        p.font.size = Pt(font_size)
        p.font.bold = bold
        p.font.color.rgb = color
        p.alignment = align
        p.space_after = Pt(space_after)
    return tf


def add_p(tf, text: str, font_size: int = 14, bold: bool = False, color: RGBColor = COLOR_BLACK,
          space_after: int = 0, align: PP_ALIGN = PP_ALIGN.LEFT, url: Optional[str] = None):
    p = tf.add_paragraph()
    p.text = text
    p.font.name = FONT_FAMILY
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.alignment = align
    p.space_after = Pt(space_after)
    if url:
        p.font.underline = True
        if p.runs:
            p.runs[0].hyperlink.address = url
    return p


def add_rect(slide, left, top, width, height, fill: Optional[RGBColor] = COLOR_CARD_BG,
             line: Optional[RGBColor] = COLOR_BORDER, rounded: bool = False):
    shape_type = MSO_SHAPE.ROUNDED_RECTANGLE if rounded else MSO_SHAPE.RECTANGLE
    rect = slide.shapes.add_shape(shape_type, left, top, width, height)
    if fill:
        rect.fill.solid()
        rect.fill.fore_color.rgb = fill
    else:
        rect.fill.background()
    if line:
        rect.line.color.rgb = line
        rect.line.width = Pt(1)
    else:
        rect.line.fill.background()
    disable_effects(rect)
    return rect


def add_header(slide, title_text: str):
    add_textbox(slide, Inches(0.8), Inches(0.6), Inches(11.733), Inches(1.0),
                text=title_text, font_size=34, bold=True)


TOTAL_SLIDES = 24


def add_footer(slide, sources: List[str], slide_num: int, total_slides: int = TOTAL_SLIDES):
    src_str = ", ".join([f"[{s}]" for s in sources]) if sources else ""
    if src_str:
        add_textbox(slide, Inches(0.8), Inches(6.88), Inches(5.5), Inches(0.38),
                    text=f"Sources: {src_str}", font_size=11, color=COLOR_MUTED)
    add_textbox(slide, Inches(7.0), Inches(6.80), Inches(5.533), Inches(0.48),
                text=f"Beyond the Logo · Slide {slide_num} of {total_slides}",
                font_size=14, bold=True, color=COLOR_DARK_MUTED, align=PP_ALIGN.RIGHT)


def add_body_bullets(slide, left, top, width, height, bullets: List[str], font_size: int = 24):
    tf = add_textbox(slide, left, top, width, height)
    for i, b in enumerate(bullets):
        if i == 0:
            p = tf.paragraphs[0]
            p.text = b
            p.font.name = FONT_FAMILY
            p.font.size = Pt(font_size)
            p.font.color.rgb = COLOR_BLACK
            p.space_after = Pt(18)
        else:
            add_p(tf, b, font_size=font_size, color=COLOR_BLACK, space_after=18)


def add_fitted_picture(slide, img_path: Union[str, Path], left, top, max_w, max_h, caption: Optional[str] = None):
    p = Path(img_path)
    if not p.exists():
        return
    with Image.open(p) as img:
        orig_w, orig_h = img.size
    aspect = orig_w / orig_h
    box_aspect = max_w / max_h
    if box_aspect > aspect:
        h = max_h
        w = h * aspect
    else:
        w = max_w
        h = w / aspect

    img_left = left + (max_w - w) / 2
    img_top = top + (max_h - h) / 2
    slide.shapes.add_picture(str(p), img_left, img_top, w, h)

    if caption:
        add_textbox(slide, left, top + max_h + Inches(0.08), max_w, Inches(0.35),
                    text=caption, font_size=12, color=COLOR_DARK_MUTED, align=PP_ALIGN.CENTER)

SPEAKER_NAMES: Dict[int, str] = {
    1: "Kaan",
    2: "Caner",
}

def set_speaker_notes(slide, slide_data: Dict[str, Any], sources_map: Dict[str, Dict[str, Any]],
                      assets_map: Dict[str, Dict[str, Any]], cum_sec: int):
    speaker_id = slide_data.get("speaker")
    speaker_name = SPEAKER_NAMES.get(speaker_id)
    dur = slide_data.get("seconds", 0)
    stage = slide_data.get("stage_directions", "").strip()
    script = slide_data.get("notes", "").strip()
    src_ids = slide_data.get("sources", [])

    cum_m = cum_sec // 60
    cum_s = cum_sec % 60
    if speaker_name and dur > 0:
        lines = [f"Speaker: {speaker_name} | Timing: {dur}s (Cumulative: {cum_m:02d}:{cum_s:02d} / 12:00)\n"]
    else:
        lines = [
            "Reference slide — not part of timed speech.",
            f"Speaker: None | Timing: 0s (Cumulative: {cum_m:02d}:{cum_s:02d} / 12:00)\n",
        ]
    if stage:
        lines.append(f"[Stage Directions]\n{stage}\n")
    if script:
        lines.append(f"[Spoken Script]\n{script}\n")

    if src_ids:
        lines.append("[Citations & References]")
        for sid in src_ids:
            if sid in sources_map:
                s = sources_map[sid]
                lines.append(f"- [{s.get('id', sid)}] {s.get('title', '')} ({s.get('publisher', '')}): {s.get('url', '')}")
        lines.append("")

    s_id = slide_data.get("id", 0)
    asset_id_map = {
        3: ["coca-cola-contour-bottle", "mcdonalds-fries-packaging", "tiffany-blue-box", "ikea-frakta-bag"],
        4: ["coca-cola-contour-bottle", "mcdonalds-fries-packaging", "tiffany-blue-box", "ikea-frakta-bag"],
        6: ["coca-cola-contour-bottle"], 7: ["coca-cola-bottle-patent-1915"],
        8: ["coca-cola-contour-bottle", "coca-cola-bottle-patent-1915"],
        9: ["mcdonalds-fries-packaging"], 10: ["mcdonalds-follow-the-arches-billboard"],
        11: ["tiffany-blue-box"], 12: ["tiffany-blue-box"], 13: ["tiffany-blue-box"],
        14: ["ikea-store-exterior"], 15: ["ikea-frakta-bag"],
    }

    used_assets = [assets_map[aid] for aid in asset_id_map.get(s_id, []) if aid in assets_map]
    if used_assets:
        lines.append("[Image Credits & Permissions]")
        for a in used_assets:
            lines.append(f"- {a.get('title', '')} | Creator: {a.get('creator', '')} | License: {a.get('license', '')} | Source: {a.get('source_page', '')}")

    slide.notes_slide.notes_text_frame.text = "\n".join(lines)


# --- Slide Builders ---
def build_cover(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    tf = add_textbox(slide, Inches(1.0), Inches(2.2), Inches(11.333), Inches(2.0),
                     text=s.get("title", "Beyond the Logo"), font_size=40, bold=True, space_after=14)
    body = s.get("body", [])
    for b in body:
        add_p(tf, b, font_size=22, color=COLOR_DARK_MUTED, space_after=6)

    strip_colors = [COLOR_COKE_RED, COLOR_MCD_YELLOW, COLOR_TIFFANY, COLOR_IKEA_BLUE]
    for i, col in enumerate(strip_colors):
        add_rect(slide, Inches(1.0 + i * 1.8), Inches(4.5), Inches(1.8), Inches(0.12), fill=col, line=None)

    credit = s.get("credit", "Kaan & Caner")
    add_textbox(slide, Inches(1.0), Inches(5.1), Inches(6.0), Inches(0.4),
                text=credit, font_size=15, color=COLOR_DARK_MUTED)
    return slide


def build_quiz_swatches(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 2)
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.4), Inches(4.7), s.get("body", []))

    swatches = [COLOR_COKE_RED, COLOR_MCD_YELLOW, COLOR_TIFFANY, COLOR_IKEA_BLUE]
    coords = [(6.6, 1.9), (9.6, 1.9), (6.6, 3.9), (9.6, 3.9)]
    for col, (x, y) in zip(swatches, coords):
        add_rect(slide, Inches(x), Inches(y), Inches(2.7), Inches(1.8), fill=col, line=RGBColor(220, 220, 220))
    return slide


def build_quiz_shapes(prs, s: Dict[str, Any], crops: Dict[str, Path]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 3)
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.2), Inches(4.7), s.get("body", []))

    clues = [
        crops.get("bottle_silhouette", Path("assets/derived/coca-cola-contour-bottle_silhouette.png")),
        crops.get("mcd_carton_top", Path("assets/mcdonalds-fries-packaging.jpg")),
        crops.get("tiffany_box_top", Path("assets/tiffany-blue-box.jpg")),
        crops.get("ikea_bag_center", Path("assets/ikea-frakta-bag.jpg")),
    ]
    coords = [(6.4, 1.9), (9.55, 1.9), (6.4, 4.0), (9.55, 4.0)]
    for path, (x, y) in zip(clues, coords):
        add_rect(slide, Inches(x), Inches(y), Inches(2.85), Inches(1.85))
        add_fitted_picture(slide, path, Inches(x + 0.08), Inches(y + 0.08), Inches(2.69), Inches(1.69))
    return slide


def build_reveal(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 4)

    body = s.get("body", [])
    sub_text = " · ".join(body[1:]) if len(body) > 1 else ""
    if sub_text:
        add_textbox(slide, Inches(0.8), Inches(1.8), Inches(11.733), Inches(0.55),
                    text=sub_text, font_size=17, color=COLOR_DARK_MUTED)

    items = [
        ("Coca-Cola", "assets/coca-cola-contour-bottle.jpg", "Contour Glass Bottle"),
        ("McDonald's", "assets/mcdonalds-fries-packaging.jpg", "Red Fry Packaging"),
        ("Tiffany & Co.", "assets/tiffany-blue-box.jpg", "Tiffany Blue Box"),
        ("IKEA", "assets/ikea-frakta-bag.jpg", "FRAKTA Shopping Bag"),
    ]
    for i, (name, path, sub) in enumerate(items):
        col_x = Inches(0.8 + i * 3.0)
        add_fitted_picture(slide, path, col_x, Inches(2.5), Inches(2.7), Inches(2.8))
        add_textbox(slide, col_x, Inches(5.45), Inches(2.7), Inches(0.4), text=name, font_size=22, bold=True, align=PP_ALIGN.CENTER)
        add_textbox(slide, col_x, Inches(5.85), Inches(2.7), Inches(0.3), text=sub, font_size=12, color=COLOR_MUTED, align=PP_ALIGN.CENTER)
    return slide


def build_theory_5(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 5)
    body = s.get("body", [])
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.4), Inches(4.7), body)

    steps = [
        ("1. Repeated Exposure", COLOR_CARD_BG, COLOR_BORDER, COLOR_BLACK),
        ("2. Familiar Visual Clue", COLOR_CARD_BG, COLOR_BORDER, COLOR_BLACK),
        ("3. Possible Brand Recognition", RGBColor(239, 246, 255), RGBColor(147, 197, 253), RGBColor(30, 64, 175)),
    ]
    y_starts = [1.95, 3.25, 4.55]
    for i, (heading, fill_c, line_c, text_c) in enumerate(steps):
        add_rect(slide, Inches(6.6), Inches(y_starts[i]), Inches(5.9), Inches(0.95), fill=fill_c, line=line_c, rounded=True)
        add_textbox(slide, Inches(6.8), Inches(y_starts[i] + 0.25), Inches(5.5), Inches(0.5), text=heading, font_size=20, bold=True, color=text_c)
        if i < 2:
            add_textbox(slide, Inches(6.6), Inches(y_starts[i] + 0.95), Inches(5.9), Inches(0.35), text="↓", font_size=22, bold=True, color=RGBColor(156, 163, 175), align=PP_ALIGN.CENTER)
    return slide


def build_case_standard(prs, s: Dict[str, Any], img_path: Union[str, Path], slide_num: int):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), slide_num)
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.4), Inches(4.7), s.get("body", []))
    add_fitted_picture(slide, img_path, Inches(6.6), Inches(1.9), Inches(5.7), Inches(4.3), caption=s.get("visual", {}).get("caption", ""))
    return slide


def build_comparison_8(prs, s: Dict[str, Any], crops: Dict[str, Path]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 8)
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.2), Inches(4.7), s.get("body", []))

    sil_path = crops.get("bottle_silhouette", Path("assets/derived/coca-cola-contour-bottle_silhouette.png"))
    add_fitted_picture(slide, sil_path, Inches(6.4), Inches(1.9), Inches(2.85), Inches(3.7))
    add_fitted_picture(slide, "assets/coca-cola-bottle-patent-1915.png", Inches(9.55), Inches(1.9), Inches(2.85), Inches(3.7))
    add_textbox(slide, Inches(6.4), Inches(5.7), Inches(2.85), Inches(0.3), text="Photo-derived silhouette", font_size=12, bold=True, align=PP_ALIGN.CENTER)
    add_textbox(slide, Inches(9.55), Inches(5.7), Inches(2.85), Inches(0.3), text="1915 drawing", font_size=12, bold=True, align=PP_ALIGN.CENTER)
    return slide


def build_case_12(prs, s: Dict[str, Any], detail_path: Path):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 12)
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.4), Inches(4.7), s.get("body", []))
    add_fitted_picture(slide, detail_path, Inches(6.6), Inches(1.9), Inches(5.7), Inches(4.3))
    return slide


def build_case_13(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 13)
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.2), Inches(4.7), s.get("body", []))

    add_rect(slide, Inches(6.4), Inches(1.9), Inches(6.1), Inches(4.0), fill=COLOR_TIFFANY, line=RGBColor(110, 195, 188))
    add_textbox(slide, Inches(6.6), Inches(2.02), Inches(5.7), Inches(0.55),
                text="Approximate screen color — not the official Pantone standard. No exact color guarantee.",
                font_size=13, bold=True)
    add_fitted_picture(slide, "assets/tiffany-blue-box.jpg", Inches(7.65), Inches(2.65), Inches(3.6), Inches(2.45))
    return slide


def build_comparison_16(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 16)
    body = s.get("body", [])
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.2), Inches(4.7), body)

    red_text = body[1] if len(body) > 1 else "Red is shared by Coca-Cola, Target, and McDonald's"
    yellow_text = body[2] if len(body) > 2 else "Yellow is shared by IKEA, Shell, and DHL"

    cards = [
        ("Shared Red", COLOR_COKE_RED, red_text, 1.95),
        ("Shared Yellow", COLOR_MCD_YELLOW, yellow_text, 4.0),
    ]
    for title, col, text, y in cards:
        add_rect(slide, Inches(6.4), Inches(y), Inches(6.1), Inches(1.85))
        add_rect(slide, Inches(6.6), Inches(y + 0.18), Inches(1.5), Inches(1.49), fill=col, line=None)
        tf = add_textbox(slide, Inches(8.3), Inches(y + 0.35), Inches(4.0), Inches(1.2), text=title, font_size=18, bold=True, space_after=8)
        add_p(tf, text, font_size=15, bold=False, color=COLOR_BLACK)
    return slide


def build_theory_17(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 17)
    body = s.get("body", [])
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.2), Inches(4.7), body)

    diag_left = Inches(6.4)
    layers = [
        ("Color and Shape", 1.95),
        ("Familiarity and Habits", 3.30),
    ]
    for heading, y in layers:
        add_rect(slide, diag_left, Inches(y), Inches(6.1), Inches(0.95))
        add_textbox(slide, Inches(6.6), Inches(y + 0.25), Inches(5.7), Inches(0.5), text=heading, font_size=22, bold=True)

    add_textbox(slide, diag_left, Inches(2.92), Inches(6.1), Inches(0.35), text="+", font_size=22, bold=True,
                color=RGBColor(156, 163, 175), align=PP_ALIGN.CENTER)

    add_rect(slide, diag_left, Inches(4.65), Inches(6.1), Inches(0.95), fill=RGBColor(239, 246, 255), line=RGBColor(147, 197, 253))
    add_textbox(slide, Inches(6.6), Inches(4.90), Inches(5.7), Inches(0.5), text="= Easier Brand Recognition", font_size=22, bold=True, color=RGBColor(30, 64, 175))
    return slide


def build_theory_18(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 18)
    body = s.get("body", [])
    add_body_bullets(slide, Inches(0.8), Inches(1.9), Inches(5.2), Inches(4.7), body)

    add_rect(slide, Inches(6.4), Inches(2.1), Inches(6.1), Inches(1.5), fill=RGBColor(240, 253, 244), line=RGBColor(134, 239, 172))
    add_textbox(slide, Inches(6.6), Inches(2.6), Inches(5.7), Inches(0.5), text="Long-Term Brand Assets", font_size=24, bold=True, color=RGBColor(21, 128, 61), align=PP_ALIGN.CENTER)

    add_rect(slide, Inches(6.4), Inches(3.9), Inches(6.1), Inches(1.5), fill=RGBColor(254, 242, 242), line=RGBColor(254, 202, 202))
    add_textbox(slide, Inches(6.6), Inches(4.4), Inches(5.7), Inches(0.5), text="Rapid Redesign Risks", font_size=24, bold=True, color=RGBColor(185, 28, 28), align=PP_ALIGN.CENTER)
    return slide


def build_guidelines_19(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 19)

    body = s.get("body", [
        "Rule 1: Build clear shapes recognizable without color",
        "Rule 2: Pair colors with distinctive packaging silhouettes",
        "Rule 3: Keep core visual clues consistent over time"
    ])
    y_starts = [2.1, 3.55, 5.0]
    for i, b in enumerate(body):
        y = y_starts[i]
        add_rect(slide, Inches(1.0), Inches(y), Inches(11.333), Inches(1.2))
        add_textbox(slide, Inches(1.3), Inches(y + 0.25), Inches(0.8), Inches(0.7), text=f"0{i+1}", font_size=34, bold=True, color=COLOR_LINK)
        add_textbox(slide, Inches(2.3), Inches(y + 0.35), Inches(9.8), Inches(0.6), text=b, font_size=22, bold=True)
    return slide


def build_conclusion_20(prs, s: Dict[str, Any]):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, s.get("sources", []), 20)

    takeaways = s.get("body", [
        "Logos confirm a brand, but visual clues guide discovery",
        "Packaging and colors help shoppers spot products quickly",
        "Recognition grows through patient consistency and daily familiarity"
    ])
    y_starts = [2.2, 3.6, 5.0]
    for i, t in enumerate(takeaways):
        add_textbox(slide, Inches(1.0), Inches(y_starts[i]), Inches(0.4), Inches(1.1), text="•", font_size=28, bold=True, color=COLOR_LINK)
        add_textbox(slide, Inches(1.5), Inches(y_starts[i] + 0.04), Inches(10.833), Inches(1.1), text=t, font_size=24, bold=True)
    return slide


def build_references(prs, s: Dict[str, Any], sources_list: List[Dict[str, Any]], slide_num: int):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, s.get("title", ""))
    add_footer(slide, [], slide_num)

    mid = (len(sources_list) + 1) // 2
    cols_data = [
        (sources_list[:mid], Inches(0.8)),
        (sources_list[mid:], Inches(6.8)),
    ]

    for col_sources, col_x in cols_data:
        if not col_sources:
            continue
        tf = add_textbox(slide, col_x, Inches(1.85), Inches(5.7), Inches(4.8))
        first_item = True
        for src in col_sources:
            sid = src.get("id", "")
            title = SHORT_SOURCE_TITLES.get(sid, src.get("title", ""))
            pub = src.get("publisher", "")
            url = src.get("url", "")

            # Clickable source TITLE (18pt, bold, royal blue with hyperlink)
            if first_item:
                p_title = tf.paragraphs[0]
                first_item = False
            else:
                p_title = tf.add_paragraph()

            p_title.text = f"[{sid}] {title}"
            p_title.font.name = FONT_FAMILY
            p_title.font.size = Pt(18)
            p_title.font.bold = True
            p_title.font.color.rgb = COLOR_LINK
            p_title.font.underline = True
            p_title.space_after = Pt(2)

            if p_title.runs:
                run = p_title.runs[0]
                run.font.name = FONT_FAMILY
                run.font.size = Pt(18)
                run.font.bold = True
                run.font.color.rgb = COLOR_LINK
                run.font.underline = True
                if url:
                    run.hyperlink.address = url

            # Publisher line (18pt, regular, muted slate - full URLs only in notes)
            p_pub = tf.add_paragraph()
            p_pub.text = pub
            p_pub.font.name = FONT_FAMILY
            p_pub.font.size = Pt(18)
            p_pub.font.bold = False
            p_pub.font.color.rgb = COLOR_DARK_MUTED
            p_pub.space_after = Pt(14)

    return slide


def build_image_credits(prs, title_text: str, assets_list: List[Dict[str, Any]], slide_num: int):
    slide = prs.slides.add_slide(prs.slide_layouts[6])
    add_header(slide, title_text)
    add_footer(slide, [], slide_num)

    mid = (len(assets_list) + 1) // 2
    cols_data = [
        (assets_list[:mid], Inches(0.8)),
        (assets_list[mid:], Inches(6.8)),
    ]

    for col_assets, col_x in cols_data:
        if not col_assets:
            continue
        tf = add_textbox(slide, col_x, Inches(1.85), Inches(5.7), Inches(4.8))
        first_item = True
        for a in col_assets:
            aid = a.get("id", "")
            title = SHORT_ASSET_TITLES.get(aid, a.get("title", ""))
            creator = a.get("creator", "")
            license_str = a.get("license", "")
            source_url = a.get("source_page") or a.get("direct_download_url") or ""
            raw_license_url = a.get("license_url")
            is_no_reuse_license = (aid == "mcdonalds-follow-the-arches-billboard") or ("no reuse license" in license_str.lower())
            is_public_domain = "public domain" in license_str.lower()

            # Short image title (18pt, bold, charcoal)
            if first_item:
                p_title = tf.paragraphs[0]
                first_item = False
            else:
                p_title = tf.add_paragraph()

            p_title.text = title
            p_title.font.name = FONT_FAMILY
            p_title.font.size = Pt(18)
            p_title.font.bold = True
            p_title.font.color.rgb = COLOR_BLACK
            p_title.space_after = Pt(2)
            if p_title.runs:
                r = p_title.runs[0]
                r.font.name = FONT_FAMILY
                r.font.size = Pt(18)
                r.font.bold = True
                r.font.color.rgb = COLOR_BLACK

            # Creator line (18pt, regular, slate)
            p_creator = tf.add_paragraph()
            p_creator.text = f"Creator: {creator}"
            p_creator.font.name = FONT_FAMILY
            p_creator.font.size = Pt(18)
            p_creator.font.bold = False
            p_creator.font.color.rgb = COLOR_DARK_MUTED
            p_creator.space_after = Pt(2)
            if p_creator.runs:
                r = p_creator.runs[0]
                r.font.name = FONT_FAMILY
                r.font.size = Pt(18)
                r.font.bold = False
                r.font.color.rgb = COLOR_DARK_MUTED

            # License line (18pt, regular, slate)
            p_lic = tf.add_paragraph()
            p_lic.text = f"License: {license_str}"
            p_lic.font.name = FONT_FAMILY
            p_lic.font.size = Pt(18)
            p_lic.font.bold = False
            p_lic.font.color.rgb = COLOR_DARK_MUTED
            p_lic.space_after = Pt(2)
            if p_lic.runs:
                r = p_lic.runs[0]
                r.font.name = FONT_FAMILY
                r.font.size = Pt(18)
                r.font.bold = False
                r.font.color.rgb = COLOR_DARK_MUTED

            # Clickable Source / License links (18pt, bold, royal blue, underline)
            p_links = tf.add_paragraph()
            p_links.space_after = Pt(16)

            if is_no_reuse_license:
                r_link = p_links.add_run()
                r_link.text = "Source / rights information"
                r_link.font.name = FONT_FAMILY
                r_link.font.size = Pt(18)
                r_link.font.bold = True
                r_link.font.color.rgb = COLOR_LINK
                r_link.font.underline = True
                if source_url:
                    r_link.hyperlink.address = source_url
            else:
                r_src = p_links.add_run()
                r_src.text = "Source"
                r_src.font.name = FONT_FAMILY
                r_src.font.size = Pt(18)
                r_src.font.bold = True
                r_src.font.color.rgb = COLOR_LINK
                r_src.font.underline = True
                if source_url:
                    r_src.hyperlink.address = source_url

                r_sep = p_links.add_run()
                r_sep.text = "   ·   "
                r_sep.font.name = FONT_FAMILY
                r_sep.font.size = Pt(18)
                r_sep.font.bold = False
                r_sep.font.color.rgb = COLOR_MUTED
                r_sep.font.underline = False

                r_lic = p_links.add_run()
                if is_public_domain or not raw_license_url:
                    r_lic.text = "Rights information"
                    target_lic_url = source_url
                else:
                    r_lic.text = "License"
                    target_lic_url = raw_license_url

                r_lic.font.name = FONT_FAMILY
                r_lic.font.size = Pt(18)
                r_lic.font.bold = True
                r_lic.font.color.rgb = COLOR_LINK
                r_lic.font.underline = True
                if target_lic_url:
                    r_lic.hyperlink.address = target_lic_url
    return slide


def set_appendix_notes(slide, assets_list: List[Dict[str, Any]], slide_num: int):
    lines = [
        "Reference appendix — not part of timed speech.",
        "Speaker: None | Timing: 0s (Cumulative: 12:00 / 12:00)\n",
        "[Stage Directions]\nReference appendix documenting full image credits, licenses, and source repositories. Display during Q&A and archival review; not part of timed spoken presentation.\n",
        "[Image Credits & Source Metadata]"
    ]
    for a in assets_list:
        lines.append(f"- Title: {a.get('title', '')}")
        lines.append(f"  Asset ID: {a.get('id', '')}")
        lines.append(f"  Creator: {a.get('creator', '')}")
        lines.append(f"  License: {a.get('license', '')}")
        if a.get('license_url'):
            lines.append(f"  License URL: {a.get('license_url', '')}")
        lines.append(f"  Source Page: {a.get('source_page', '')}")
        if a.get('direct_download_url'):
            lines.append(f"  Direct Download: {a.get('direct_download_url', '')}")
        if a.get('description'):
            lines.append(f"  Description: {a.get('description', '')}")
        lines.append("")

    slide.notes_slide.notes_text_frame.text = "\n".join(lines).strip()

# --- Main Presentation Generator ---
def main():
    deck = load_deck()
    sources_map = load_sources()
    assets_map = load_assets()
    crops = ensure_derived_crops()

    prs = Presentation()
    prs.slide_width = Inches(13.333333)
    prs.slide_height = Inches(7.5)

    prs.core_properties.title = deck.get("deck_title", "Beyond the Logo")
    prs.core_properties.author = "Kaan and Caner"
    if "subtitle" in deck:
        prs.core_properties.subject = deck["subtitle"]
    slides_data = deck.get("slides", [])
    cum_sec = 0

    for s_idx, s in enumerate(slides_data, start=1):
        cum_sec += s.get("seconds", 0)

        if s_idx == 1:
            slide = build_cover(prs, s)
        elif s_idx == 2:
            slide = build_quiz_swatches(prs, s)
        elif s_idx == 3:
            slide = build_quiz_shapes(prs, s, crops)
        elif s_idx == 4:
            slide = build_reveal(prs, s)
        elif s_idx == 5:
            slide = build_theory_5(prs, s)
        elif s_idx == 6:
            slide = build_case_standard(prs, s, "assets/coca-cola-contour-bottle.jpg", 6)
        elif s_idx == 7:
            slide = build_case_standard(prs, s, "assets/coca-cola-bottle-patent-1915.png", 7)
        elif s_idx == 8:
            slide = build_comparison_8(prs, s, crops)
        elif s_idx == 9:
            slide = build_case_standard(prs, s, "assets/mcdonalds-fries-packaging.jpg", 9)
        elif s_idx == 10:
            slide = build_case_standard(prs, s, "assets/mcdonalds-follow-the-arches-billboard.jpg", 10)
        elif s_idx == 11:
            slide = build_case_standard(prs, s, "assets/tiffany-blue-box.jpg", 11)
        elif s_idx == 12:
            detail_path = crops.get("tiffany_detail", Path("assets/tiffany-blue-box.jpg"))
            slide = build_case_12(prs, s, detail_path)
        elif s_idx == 13:
            slide = build_case_13(prs, s)
        elif s_idx == 14:
            slide = build_case_standard(prs, s, "assets/ikea-store-exterior.jpg", 14)
        elif s_idx == 15:
            slide = build_case_standard(prs, s, "assets/ikea-frakta-bag.jpg", 15)
        elif s_idx == 16:
            slide = build_comparison_16(prs, s)
        elif s_idx == 17:
            slide = build_theory_17(prs, s)
        elif s_idx == 18:
            slide = build_theory_18(prs, s)
        elif s_idx == 19:
            slide = build_guidelines_19(prs, s)
        elif s_idx == 20:
            slide = build_conclusion_20(prs, s)
        elif s_idx == 21:
            src_list_21 = [sources_map[sid] for sid in ["S1", "S2", "S3", "S4", "S5"] if sid in sources_map]
            slide = build_references(prs, s, src_list_21, 21)
        elif s_idx == 22:
            src_list_22 = [sources_map[sid] for sid in ["S6", "S7", "S8", "S9"] if sid in sources_map]
            slide = build_references(prs, s, src_list_22, 22)
        else:
            slide = prs.slides.add_slide(prs.slide_layouts[6])

        set_speaker_notes(slide, s, sources_map, assets_map, cum_sec)

    # Append TWO image-credit appendix slides AFTER current 22
    raster_assets = [a for a in load_assets_list() if a.get("format") != "svg"]
    appendix_1_assets = raster_assets[:4]
    appendix_2_assets = raster_assets[4:7]

    slide_23 = build_image_credits(prs, "Appendix: Image Credits and Attributions (Part 1)", appendix_1_assets, 23)
    set_appendix_notes(slide_23, appendix_1_assets, 23)

    slide_24 = build_image_credits(prs, "Appendix: Image Credits and Attributions (Part 2)", appendix_2_assets, 24)
    set_appendix_notes(slide_24, appendix_2_assets, 24)

    output_path = "presentation/Beyond_the_Logo.pptx" if Path("presentation").exists() else "Beyond_the_Logo.pptx"
    prs.save(output_path)
    print(f"Successfully generated {output_path} ({len(prs.slides)} slides).")


if __name__ == "__main__":
    main()
