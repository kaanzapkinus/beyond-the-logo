# Beyond the Logo: Can We Recognize a Brand Without Its Name?

A practical graphic design and visual identity presentation by **Kaan Yazıcıoğlu** and **Caner Akcasu**.

This presentation investigates how brands achieve instant recognition through shape, packaging geometry, color combinations, and context—even when their official names and logos are completely absent.

---

## ⏱️ Structure & 25-Minute Session Breakdown

The presentation is designed and structured for a **25-minute total course presentation session**, balancing spoken content with audience demonstration and discussion:

| Speaker | Assigned Slides | Role & Topics | Target Time |
| :--- | :--- | :--- | :---: |
| **Kaan** | Slides 1–5 & 15–20 | Opening, live color/shape quiz moderation, memory science, design guidelines & conclusion | **~13–14 min** |
| **Caner** | Slides 6–14 | Core brand case studies: Coca-Cola, McDonald's, Tiffany & Co., and IKEA | **~11–12 min** |
| **Combined** | Slides 1–25 | 20 content slides + 1 closing slide + 2 references + 2 image credits + audience Q&A | **25:00 min** |

---

## 📁 Repository Directory Structure

```text
beyond-the-logo/
├── presentation/          # Slide decks in all presentation formats
│   ├── Beyond_the_Logo.pptx   # 16:9 widescreen PowerPoint deck with embedded notes
│   ├── Beyond_the_Logo.pdf    # Full 25-slide high-res PDF export
│   └── Beyond_the_Logo.docx   # Document with slide renders, key bullets & notes
│
├── scripts/               # Speaker reading files for phone & desktop
│   ├── Kaan_Caner_Full_Script.pdf    # Full sequential script with KAAN/CANER header
│   ├── Kaan_Caner_Full_Script.docx   # Full sequential script in Word format
│   ├── Kaan_Script.pdf / .docx / .html / .txt   # Kaan's individual phone script
│   └── Caner_Script.pdf / .docx / .html / .txt  # Caner's individual phone script
│
├── research/              # Academic research, factual dossier & slide contract
│   ├── safe_sources.json      # 9 verified empirical citations with source quotes
│   ├── research.md            # Empirical research dossier (Ehrenberg-Bass model)
│   ├── deck.json              # Slide content, metadata, and synchronized scripts
│   ├── Speaker_Notes.md       # Complete presentation notes & delivery guidelines
│   ├── BRIEF.md               # Presentation design brief and requirements
│   ├── SLIDE_CONTRACT.json    # JSON schema for deck validation
│   └── revision_audit.md      # Independent factual and visual audit report
│
├── assets/                # Authentic brand imagery & historical records
│   ├── assets.json            # Verified image catalog, creators, and license metadata
│   ├── derived/               # High-res silhouette and cropped quiz clues
│   └── *.jpg / *.png / *.svg  # Authentic brand photographs and patent drawings
│
└── src/                   # Automation tooling
    ├── build_deck.py          # Programmatic PowerPoint builder (python-pptx)
    └── export_phone_scripts.py # Script exporter for PDF, HTML, and DOCX formats
```

---

## 🖥️ Presentation Files

- **[PowerPoint Presentation (PPTX)](./presentation/Beyond_the_Logo.pptx)** — Complete 25-slide widescreen presentation (16:9) with embedded presenter notes and timing metadata.
- **[Presentation PDF](./presentation/Beyond_the_Logo.pdf)** — High-resolution slide export (25 slides: 20 content slides, 1 closing slide, 2 references, 2 image credits).
- **[Presentation DOCX](./presentation/Beyond_the_Logo.docx)** — Complete document containing slide renders, key takeaways, and delivery notes.

---

## 📱 Speaker Scripts (Directly Readable on Phone & Desktop)

| Speaker | Assigned Slides | Planned Timing | Files |
| :--- | :--- | :--- | :--- |
| **All Presenters (Full Sequence)** | Slides 1–20 | 25-minute session | [📄 PDF](./scripts/Kaan_Caner_Full_Script.pdf) · [📝 DOCX](./scripts/Kaan_Caner_Full_Script.docx) |
| **Kaan** (Opening, Theory & Conclusion) | Slides 1–5 & 15–20 | ~13–14 min | [📄 PDF](./scripts/Kaan_Script.pdf) · [📝 DOCX](./scripts/Kaan_Script.docx) · [🌐 HTML](./scripts/Kaan_Script.html) · [📜 TXT](./scripts/Kaan_Script.txt) |
| **Caner** (Brand Case Studies) | Slides 6–14 | ~11–12 min | [📄 PDF](./scripts/Caner_Script.pdf) · [📝 DOCX](./scripts/Caner_Script.docx) · [🌐 HTML](./scripts/Caner_Script.html) · [📜 TXT](./scripts/Caner_Script.txt) |

> Every page of the full script clearly indicates **KAAN** or **CANER** in the top-left corner, followed by the corresponding slide number.

---

## 🔍 Case Studies Covered

1. **Coca-Cola** (1915 Contour Bottle Design Patent)
   - Alexander Samuelson & Root Glass Company fluted bottle geometry.
   - Designed to be identified by feel in the dark or lying broken on the ground.
   - Proof that shape functions as an independent identifier without color.

2. **McDonald's** (Fast-Food Packaging & European Adaptation)
   - Red carton geometry paired with golden french fries as a combined visual clue.
   - European transition to deep hunter green backgrounds (2009) while preserving the golden arches.
   - Cossette's *Follow the Arches* campaign (2018): Cropped logo fragments as directional arrows.

3. **Tiffany & Co.** (Packaging Ritual & Custom Color Standard)
   - The iconic Tiffany Blue Box tied with a ribbon bow.
   - Strict store presentation rule: boxes are never sold empty.
   - Custom color standard **Pantone 1837 Blue** (2001) and color trademark registration (1998).

4. **IKEA** (Retail Architecture & Everyday Utilities)
   - Decades of regional branding variation unified from 1984.
   - Blue warehouse architecture with giant yellow wordmarks (from 1991).
   - The blue **FRAKTA** shopping bag (1989): turning an everyday utility item into a brand clue.

---

## 📚 Core Principles & Design Guidelines

- **Context Beats Color Myths:** Rejecting universal color psychology in favor of empirical market learning (Ehrenberg-Bass Institute).
- **Compounding Clues:** Color alone is rarely unique (shared by competitors); pairing color with physical shape creates distinctiveness.
- **Redesign Risks:** Protecting familiar visual shortcuts that shoppers rely on during habitual browsing.
- **Three Practical Rules:**
  1. Build clear shapes that work in black and white.
  2. Pair colors with distinctive packaging silhouettes.
  3. Keep core cues consistent over long periods of time.
