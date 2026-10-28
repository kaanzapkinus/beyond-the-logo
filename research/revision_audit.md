# Substantive Revision Audit: Beyond the Logo Presentation Deck

**Target Document:** `/Users/kaan/Cloud/omp-sessions/beyond-the-logo/revision_audit.md`  
**Audit Target Workspace:** `/Users/kaan/Cloud/omp-sessions/beyond-the-logo`  
**Auditor Role:** Substantive Audit Worker (Independent Inspection & Verification)  
**Date of Audit:** October 2026  
**Status:** Complete Forensic Audit (Supersedes prior blanket PASS in `final_content_review.md`)

---

## 1. Executive Summary & Audit Baseline

This substantive audit provides an exhaustive, evidence-backed evaluation of the existing presentation materials for *Beyond the Logo: Can we recognize a brand without its name?*. Inspection was conducted directly against physical and digital artifacts in the repository:
- `Beyond_the_Logo.pptx` (24-slide widescreen presentation generated via `python-pptx`)
- `Beyond_the_Logo.pdf` (24-page compiled PDF document, 2.8 MB, LibreOffice Impress metadata)
- `deck.json` (22-item deck specification and delivery script data)
- `Speaker_Notes.md` (22-slide markdown delivery script reference)
- `safe_sources.json` (canonical 9-source factual registry S1–S9)
- `assets.json` (11 acquired brand visual assets and crop specifications)
- `build_deck.py` (827-line programmatic PPTX layout builder)
- `review/*.png` (existing rendered slide proof images: Slides 1, 3, 5, 8, 17, 18, 20)

### 1.1 Rejection of Prior Blanket PASS (`final_content_review.md`)
The prior audit document (`final_content_review.md`, dated 2026-10-26) issued an uncritical blanket "PASS", asserting zero defects across all dimensions. Forensic inspection of the actual PPTX, PDF, JSON, and python builder reveals that `final_content_review.md` failed to verify critical structural, visual, and script defects:
1. It validated an obsolete 10/10 slide speaker split (Slides 1–10 vs 11–22) that directly violates the project's immutable speaker contract.
2. It failed to inspect the actual quiz crop image on Slide 3 (`tiffany_box_quiz_crop.jpg`), which leaks visible brand typography ("TIFFANY") before the official answer reveal.
3. It overlooked that Slide 8 displays a flat silhouette cutout while the slide title, body, script, and caption claim to display the "real glass bottle photo".
4. It ignored misleading conceptual diagram arrows on Slide 5 that portray debunked myths as the primary step of an empirical workflow.
5. It missed deceptive "License" hyperlinks on Appendix Slide 23 that link a copyrighted commercial billboard to an agency promotional blog.

### 1.2 Shared Immutable Contract Conformance

| Contract Parameter | Immutable Requirement | Current State in `deck.json` & PPTX | Conformance Status | Action Required |
| :--- | :--- | :--- | :---: | :--- |
| **Total Deck Slides** | Exactly 24 slides | 22 in `deck.json` + 2 appended by builder = 24 in PPTX/PDF | **MET** | Maintain 24-slide total structure. |
| **Total Duration** | Exactly 1,500s (25:00) | Sum of slide seconds = 1,500s | **MET** | Maintain exact per-slide timings. |
| **Speaker 1 (Kaan)** | Slides 1–5 (375s) & Slides 15–20 (450s) = **825s** (13:45) | Assigned Slides 1–10 (750s / 12:30) | **CRITICAL FAIL** | Reassign Slides 6–10 to Speaker 2; reassign Slides 15–20 to Speaker 1. |
| **Speaker 2 (Caner)** | Slides 6–14 (9 slides × 75s) = **675s** (11:15) | Assigned Slides 11–22 (750s / 12:30) | **CRITICAL FAIL** | Reassign Slides 6–14 to Speaker 2; reassign Slides 15–20 to Speaker 1. |
| **Presenter Names** | Kaan (Speaker 1) & Caner (Speaker 2) | Omitted entirely; generic "my partner" / "my co-presenter" | **FAIL** | Add names to Slide 1 cover, handovers, and notes. |
| **Handover 1** | Slide 5 $\rightarrow$ Slide 6 (Kaan to Caner) | Missing; Speaker 1 continues through Slide 10 | **CRITICAL FAIL** | Add handover script at Slide 5 end; add takeover at Slide 6 start. |
| **Handover 2** | Slide 14 $\rightarrow$ Slide 15 (Caner to Kaan) | Missing; Speaker 2 continues through Slide 20 | **CRITICAL FAIL** | Add handover script at Slide 14 end; add takeover at Slide 15 start. |
| **Erroneous Handover** | None at Slide 10 $\rightarrow$ 11 | Outdated handover present at Slide 10 $\rightarrow$ 11 | **FAIL** | Remove mid-case handover between McDonald's and Tiffany. |

---

## 2. High-Severity Finding Matrix

The following matrix summarizes all critical and important findings identified during this forensic audit, categorizing each by severity, affected slide IDs, and core defect domain:

| ID | Severity | Category | Affected Slides | Summary of Defect |
| :---: | :---: | :--- | :---: | :--- |
| **F-01** | **CRITICAL** | Speaker Contract | Slides 6–10, 15–20 | Speaker allocation inverted on 11 slides; violates 825s/675s Kaan/Caner contract. |
| **F-02** | **CRITICAL** | Script Architecture | Slides 5, 6, 10, 11, 14, 15 | Handover locations desynchronized; obsolete handover at 10 $\rightarrow$ 11; missing handovers at 5 $\rightarrow$ 6 and 14 $\rightarrow$ 15. |
| **F-03** | **CRITICAL** | Quiz Spoiler | Slide 3 | `tiffany_box_quiz_crop.jpg` leaks black serif letters "TIFFANY" under the ribbon knot. |
| **F-04** | **CRITICAL** | Visual Mismatch | Slide 8 | Slide claims to compare "real bottle photo" with patent; PPTX displays flat silhouette cutout. |
| **F-05** | **HIGH** | Visual Mismatch | Slide 3 | Body/script claims "Same 4 colors... product outlines"; PPTX shows charcoal silhouette, 2 photos, 1 blue plastic patch. |
| **F-06** | **HIGH** | Quiz Integrity | Slide 3 | Clue 4 (`ikea_bag_quiz_crop.jpg`) is a 392×417 texture patch with zero tote bag silhouette, shape, or yellow strap. |
| **F-07** | **HIGH** | Conceptual Diagram | Slide 5 | `build_theory_5` links debunked myth ("Popular Assumptions") via downward arrow as Step 1 of empirical workflow. |
| **F-08** | **HIGH** | Copyright / Legal | Slide 23 | Misleading clickable "License" link points to Cossette agency blog for copyrighted billboard. |
| **F-09** | **MEDIUM** | Legal Overclaim | Slide 13 | Unhedged presenter assertion that other companies can "freely use turquoise in clothing without breaking trademark laws". |
| **F-10** | **MEDIUM** | Factual Scope | Slide 10 | Unqualified assertion that "European restaurants changed red background to deep forest green" overstates S8 rollout scope. |
| **F-11** | **MEDIUM** | Visual Mismatch | Slide 9 | Script claims "Even if we completely hide the yellow arches...", but PPTX displays arches full and uncropped. |
| **F-12** | **MEDIUM** | Visual Redundancy | Slides 11, 12, 13 | Same photograph (`assets/tiffany-blue-box.jpg`) displayed 3 consecutive times with negligible variation. |
| **F-13** | **MEDIUM** | Layout Redundancy | Slide 16 | Right cards verbatim copy left body bullets; promised competitor logo circles omitted. |
| **F-14** | **MEDIUM** | Category Error | Slide 17 | Interaction formula equates stimulus + consumer memory to stimulus: `(Color + Shape) + (Familiarity) = Combined Cues`. |
| **F-15** | **MEDIUM** | Theoretical Accuracy | Slide 19 | Declaring brand cues "unchanged" / immutable contradicts S2 refresh principles and McDonald's green rollout. |
| **F-16** | **MEDIUM** | Visual Omission | Slide 20 | Promised closing visual of 4 minimalist case silhouettes omitted; renders pure text bullets. |
| **F-17** | **LOW** | Attribution Gap | Slides 23, 24 | Builder filters out all 4 acquired SVG brand logos (`format == 'svg'`), leaving them uncredited in Image Credits. |
| **F-18** | **LOW** | Slide Clutter | Slides 7, 8 | Uncropped patent drawing displays illegible patent office headers, filing dates, and signatures. |
| **F-19** | **LOW** | Presentation Identity | Slide 1 | Presenter names "Kaan" and "Caner" omitted from cover slide layout. |

---

## 3. Structural & Contractual Audit: Speaker Split & Handovers

### 3.1 Immutable Speaker Allocation Verification
The project brief establishes a non-negotiable contract:
- **Total Duration:** 1,500 seconds (25 minutes 00 seconds).
- **Speaker 1 (Kaan):** Slides 1–5 (375s, 06:15) and Slides 15–20 (450s, 07:30). Total: **825 seconds (13:45)**.
- **Speaker 2 (Caner):** Slides 6–14 (9 slides × 75s). Total: **675 seconds (11:15)**.
- **Reference & Appendix Slides (Slides 21–24):** 0 spoken seconds (displayed during audience Q&A).

#### Observed Defect in Existing Files
In `deck.json`, `Speaker_Notes.md`, and `Beyond_the_Logo.pptx`:
- Slides 1–10 are marked `"speaker": 1` (750s / 12:30).
- Slides 11–22 are marked `"speaker": 2` (750s / 12:30).
- PPTX notes text frames on Slides 6–10 explicitly print `"Speaker: Speaker 1"`.
- PPTX notes text frames on Slides 15–20 explicitly print `"Speaker: Speaker 2"`.
- This represents an erroneous 50/50 temporal split that misassigns **5 content slides to Speaker 1 (Slides 6–10)** and **6 content slides to Speaker 2 (Slides 15–20)**.

### 3.2 Handover Architecture Audit
Because the speaker split was incorrectly modeled as Slides 1–10 and 11–20, the oral scripts contain severe structural transition defects:

1. **Missing Handover 1 (Slide 5 $\rightarrow$ Slide 6):**
   - *Slide 5 End:* Kaan finishes explaining the Ehrenberg-Bass color consistency model. The script currently terminates abruptly: *"Rather, if a brand consistently uses blue in its packaging and communications, and is the only brand that uses blue, consumers will come to quickly and easily identify that the color blue represents the brand."*
   - *Defect:* There is zero verbal handover to Caner.
   - *Actionable Fix:* Kaan must conclude Slide 5 with: *"To see how these principles operate in commercial reality, I will now hand over to Caner to examine our four case studies, beginning with Coca-Cola."*
   - *Slide 6 Start:* Caner currently opens with: *"Our first case study looks at Coca-Cola..."* Caner must acknowledge Kaan: *"Thank you, Kaan! Our first case study looks at Coca-Cola..."*

2. **Obsolete Mid-Case Handover on Slide 10 (Removal Required):**
   - *Slide 10 End:* Speaker 1 currently states: *"That brings me to the end of our first section. I will now hand over to my co-presenter to explore our next cases."*
   - *Defect:* Under the contract, Caner is already speaking from Slide 6 through Slide 14. Caner is in the middle of his case study run (having delivered Coca-Cola and McDonald's, and continuing to Tiffany and IKEA). Having a handover here splits McDonald's from Tiffany and makes Caner hand over to himself.
   - *Actionable Fix:* Delete the handover sentence entirely from Slide 10 script and stage directions. Caner transitions smoothly within his own block: *"These adaptations prove that strong visual assets can evolve while maintaining their core identity."*

3. **Obsolete Greeting on Slide 11 (Removal Required):**
   - *Slide 11 Start:* Speaker 2 currently opens with: *"Thank you! Let us now step into the world of luxury with our third case study: Tiffany & Co."*
   - *Defect:* Caner is already presenting; thanking an imaginary co-presenter mid-stride disrupts presentation flow.
   - *Actionable Fix:* Replace with internal transition: *"Moving from fast food to luxury packaging, our third case study brings us to Tiffany & Co."*

4. **Missing Handover 2 (Slide 14 $\rightarrow$ Slide 15):**
   - *Slide 14 End:* Caner completes the IKEA store exterior case study. The script terminates: *"Consistency took deliberate time and patience."*
   - *Defect:* Caner does not hand back to Kaan.
   - *Actionable Fix:* Caner concludes Slide 14: *"To explore IKEA's everyday retail packaging and see what these cases teach us about brand design principles, I will now hand back to Kaan."*
   - *Slide 15 Start:* Kaan currently opens: *"Alongside its blue warehouse buildings, IKEA's most familiar object is the blue FRAKTA shopping bag."* Kaan must acknowledge Caner: *"Thank you, Caner! Alongside its blue warehouse buildings..."*

5. **Presenter Naming Defect:**
   - Neither Kaan nor Caner is named on Slide 1 (Cover), in `deck.json`, or in `Speaker_Notes.md`. Both presenters must be explicitly credited on the title slide and referenced by name in handover cues.

### 3.3 Word Count & Pacing Verification Under Contract Split

| Speaker | Assigned Slides | Total Seconds | Spoken Words | Delivery Pace | Target Pace (B2 Oral) | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Kaan (Speaker 1)** | Slides 1–5, 15–20 | 825s (13:45) | 1,404 words | 102.1 wpm | 100–120 wpm | **OPTIMAL** |
| **Caner (Speaker 2)** | Slides 6–14 | 675s (11:15) | 1,158 words | 102.9 wpm | 100–120 wpm | **OPTIMAL** |
| **Total Deck** | Slides 1–20 (Timed) | 1,500s (25:00) | 2,562 words | 102.5 wpm | 100–120 wpm | **OPTIMAL** |

*Note: Total word count (2,562 words) falls perfectly within the brief's mandated 2,400–2,700 word window.*

---

## 4. Residual Concerns on Sibling Writer Known Issues

A sibling writer is actively implementing fixes for seven known defects. This section documents the exact artifact observations, verified baseline evidence, and residual concerns to ensure these items are completely resolved without regressing:

### 4.1 Fabricated Audience Responses (Slides 2, 3, 9)
- **Artifact Observation:**
  - *Slide 2 Script:* *"As you can hear around the room, people are shouting very different names, especially for the red and yellow squares. Some people guess fast-food restaurants, while others think of soft drinks, retail stores, or delivery companies."*
  - *Slide 3 Script:* *"Many people in the room now guess Coca-Cola for the bottle, McDonald's for the paper carton, Tiffany for the gift box, and IKEA for the shopping tote."*
  - *Slide 9 Script:* *"...almost everyone in this room immediately recognizes what brand this is."*
- **Baseline Evidence:** `BRIEF.md` mandates: *"Classroom guessing is demonstration, not scientific experiment... No invented student names [or scripted responses]."*
- **Residual Concern:** A pre-scripted presentation cannot narrate live audience behavior as an established historical fact. If the live audience remains silent or guesses a different brand (e.g., Lego or DHL), the presenter's script becomes jarringly detached from reality.
- **Actionable Fix:** Convert declarative assertions into conditional speaker staging:
  - *Slide 2:* *"Take a look at each color and call out your guesses... In classroom trials, colors like red and yellow produce widespread disagreement, because dozens of brands share those exact wavelengths."*
  - *Slide 3:* *"Notice how your focus shifts when shape appears. The silhouette narrows the possibilities immediately, making brands like Coca-Cola or Tiffany come to mind much faster."*
  - *Slide 9:* *"Even without seeing the golden arches logo, the packaging form and colorway provide powerful clues that make identification far easier."*

### 4.2 "Same 4 Colors / Outlines" Visual Mismatch (Slide 3)
- **Artifact Observation:**
  - *Slide 3 Body Bullet 1:* *"Classroom illustration: Four colors paired with unbranded shapes"*
  - *Slide 3 Script:* *"We kept the exact same four colors, but this time we added simple unbranded product outlines..."*
  - *PPTX Visual Inspection:*
    1. Bottle Clue (`Picture 6`): Uses `assets/derived/coca-cola-contour-bottle_silhouette.png`, rendered as a flat charcoal/black (`#111827`) silhouette cutout. It does NOT contain red!
    2. McDonald's Clue (`Picture 8`): Uses `mcdonalds_carton_quiz_crop.jpg`, a photographic crop showing yellow fries protruding from a red rim.
    3. Tiffany Clue (`Picture 10`): Uses `tiffany_box_quiz_crop.jpg`, a photographic crop showing turquoise boxes tied with white satin ribbon.
    4. IKEA Clue (`Picture 12`): Uses `ikea_bag_quiz_crop.jpg`, a photographic crop of blue crinkled plastic with no yellow and no bag shape.
- **Residual Concern:** The visual contradicts the slide text in three distinct ways: (a) Clue 1 is charcoal/black, completely missing the red swatch from Slide 2; (b) Clues 2–4 are photographic crops, not "outlines" or "silhouettes"; (c) Clue 4 is a featureless texture swatch, not a tote bag shape.
- **Actionable Fix:** Either standardize all 4 clues as unbranded geometric line drawings/silhouettes filled with the exact swatches from Slide 2 (Red bottle, Yellow carton, Turquoise box, Blue bag), OR rewrite the body and script to state: *"Classroom illustration: Adding packaging shapes and physical textures to our four brand colors."*

### 4.3 Photo-vs-Silhouette Contradiction (Slide 8)
- **Artifact Observation:**
  - *Slide 8 Title:* *"Shape Still Matters Without Color"*
  - *Slide 8 Body Bullet 1:* *"Comparing the real glass bottle with the patent drawing"*
  - *Slide 8 Script:* *"Here on the screen, we place the real glass bottle photo right next to the original 1915 patent drawing."*
  - *Slide 8 Caption:* *"Visual comparison: Bottle photograph and patent drawing showing shape recognition without color."*
  - *PPTX Visual Inspection:* Slide 8 (`build_comparison_8`) renders `Picture 5` using `crops.get("bottle_silhouette")` (`coca-cola-contour-bottle_silhouette.png`), labeled *"Photo-derived silhouette"*. It does NOT display the real glass bottle photograph!
- **Residual Concern:** The body, script, and caption all describe a real bottle photograph, but the slide displays an artificial vector-like silhouette cutout. The audience sees a black graphic and a line drawing, contradicting the presenter's spoken words.
- **Actionable Fix:** Align visual and script: Place the actual studio photograph (`assets/coca-cola-contour-bottle.jpg`, cropped or desaturated to grayscale) in the left container, OR update the slide text, caption, and script to say: *"Comparing the bottle's physical silhouette with the original 1915 patent drawing."*

### 4.4 Universal Recognition & Absolute Certainty Overclaims (Slides 9, 17, 20)
- **Artifact Observation:**
  - *Slide 9 Script:* *"...almost everyone in this room immediately recognizes what brand this is."*
  - *Slide 17 Script:* *"...when you pair a specific color with a distinctive physical shape... confusion disappears."*
  - *Slide 20 Script:* *"...brands become memorable without needing to display a logo."*
- **Baseline Evidence:** Empirical marketing science (S1, S3) establishes that brand retrieval is probabilistic and heavily contingent on category buyer status, market penetration, and geographic familiarity. `BRIEF.md` explicitly warns: *"Classroom guessing is demonstration, not scientific experiment... No unsupported recognition percentages."*
- **Residual Concern:** Asserting that "confusion disappears" or that recognition is "immediate for almost everyone" makes an unhedged claim of universal cognitive recognition.
- **Actionable Fix:** Introduce proper scientific hedging:
  - *Slide 17:* Replace *"confusion disappears"* with *"identification ambiguity drops significantly for regular category buyers."*
  - *Slide 9:* Replace *"almost everyone in this room immediately recognizes"* with *"consumers familiar with the brand can identify it rapidly."*

### 4.5 Legal Overclaims & Category Boundary Editorializing (Slide 13)
- **Artifact Observation:**
  - *Slide 13 Body Bullet 3:* *"Protection covers luxury jewelry boxes, not all turquoise products"*
  - *Slide 13 Script:* *"However, designers should understand an important legal limit: Tiffany does not own every shade of turquoise in the world. Trademark protection only applies to jewelry boxes, retail shopping bags, and related luxury goods where a competitor's color might confuse buyers. Other companies can freely use turquoise in different business categories, such as clothing or home appliances, without breaking trademark laws."*
- **Baseline Evidence:** Canonical source **S5** (*Tiffany Blue*, Tiffany & Co. Press Archives) documents that Tiffany registered Tiffany Blue as a color trademark in 1998 and standardized Pantone 1837 in 2001. S5 contains zero statements regarding clothing, home appliances, or third-party safe harbors.
- **Residual Concern:** Asserting that third parties can "freely use turquoise in clothing... without breaking trademark laws" represents unhedged presenter legal analysis. In trademark law, luxury apparel and accessories are closely related to jewelry; using Tiffany Blue on luxury fashion could trigger trademark infringement or dilution claims under Lanham Act principles.
- **Actionable Fix:** Ground the distinction strictly between S5 source facts and general trademark principles:
  - *Source Fact:* Tiffany registered its robin's-egg blue hue as a trademark for its signature jewelry boxes and retail packaging.
  - *Presenter Analysis:* *"Under trademark law, color protection is not a universal monopoly over a wavelength; it protects against consumer confusion within specific product classes. While Tiffany protects its hue in jewelry and luxury packaging, other industries remain free to use turquoise where no consumer confusion exists."* (Drop specific claims about clothing).

### 4.6 Scope Overreach on European Green Rollout (Slide 10)
- **Artifact Observation:**
  - *Slide 10 Body Bullet 1:* *"European restaurants changed red background to deep forest green"*
  - *Slide 10 Script:* *"In late 2009, European McDonald's restaurants replaced their traditional red background with deep forest green to highlight environmental efforts."*
- **Baseline Evidence:** Canonical source **S8** (*McDonald's rolling out green logo in Europe*, NBC News / AP) specifies: *"About 100 German McDonald's restaurants will make the change by the end of 2009... Some franchises in Great Britain and France have already started using the new color scheme behind their Golden Arches."*
- **Residual Concern:** Stating that "European restaurants replaced their traditional red background" implies a blanket, instantaneous continent-wide replacement across all European outlets.
- **Actionable Fix:** Accurately scope the claim per S8: *"In late 2009, McDonald's began replacing its traditional red background with deep forest green across European outlets, starting with approximately 100 pilot locations in Germany, France, and Great Britain."*

### 4.7 "Immutable Cues" Rule Contradiction (Slide 19)
- **Artifact Observation:**
  - *Slide 19 Script:* *"Companies can refresh secondary graphic styles to look modern, but they must keep their core shapes and colors unchanged."*
- **Baseline Evidence:** Ehrenberg-Bass research (S2: *Seven Costly Sins of Brand Identity*) does not mandate that brand assets must remain eternally static: *"If you design with the long-term future in mind, you should not need to update very often. If you do update, quantify the short term branding loss and compensate with stronger direct branding as you build up the refreshed asset."* Furthermore, McDonald's transition from red to green in Europe (Slide 10) demonstrates that core cues can strategically adapt.
- **Residual Concern:** Demanding that core assets remain "unchanged" contradicts empirical marketing science and the deck's own case studies.
- **Actionable Fix:** Reframe Rule 3 around disciplined asset preservation rather than absolute immutability: *"Rule 3: Protect core visual clues over time. Marketing research warns against frequent refreshes that destroy learned memory shortcuts. When visual updates are necessary, brands must preserve their primary distinctive shapes and compensate with strong direct branding."*

---

## 5. Additional Critical & Important Findings (Forensic Inspections)

The following 11 substantive defects were uncovered during deep inspection of the PPTX structure, source code, and image artifacts. None of these were identified by prior reviews:

### 5.1 Quiz Logo Typography Spoiler on Slide 3 (`tiffany_box_quiz_crop.jpg`)
- **Artifact Observation:** In `assets/derived/tiffany_box_quiz_crop.jpg`, the image is cropped from `assets/tiffany-blue-box.jpg` using normalized coordinates `(0.20, 0.22, 0.80, 0.55)` (`build_deck.py` line 102). Visual inspection of the resulting 1959×808 pixel JPEG reveals that the top surface of the left gift box contains black embossed serif lettering: the letters **"TI..." / "...FFANY"** are clearly visible immediately adjacent to the ribbon knot.
- **Breach of Specification:** `BRIEF.md` strictly dictates: *"Quiz must precede answers; no early logo spoilers on quiz slides."* `assets.json` specifically warns: *"Focuses strictly on the top surface of the turquoise box and ribbon knot safely above the lid edge where the black wordmark appears, allowing students to evaluate color and packaging presentation without brand typography spoilers."*
- **Root Cause in Code:** `build_deck.py` cropped too far down the box lid ($y_2 = 0.55$), capturing the printed firm name.
- **Surgical Correction:** Re-crop `assets/tiffany-blue-box.jpg` using normalized bounds `(0.25, 0.22, 0.75, 0.42)` to isolate strictly the ribbon knot and satin bow, or digitally clone the turquoise paperboard texture over the letters.

### 5.2 Clue 4 on Slide 3 Completely Lacks Bag Shape (`ikea_bag_quiz_crop.jpg`)
- **Artifact Observation:** In `assets/derived/ikea_bag_quiz_crop.jpg`, `build_deck.py` line 104 executed:
  `do_crop("assets/ikea-frakta-bag.jpg", "ikea_bag_quiz_crop.jpg", (0.65, 0.33, 0.77, 0.50))`.
  The resulting image is a tiny 392×417 pixel swatch showing only a close-up of crinkled blue polypropylene fabric. It contains NO handles, NO webbing straps, NO yellow accent, and NO tote bag silhouette.
- **Mismatch with Text:** Slide 3 body promises *"A fluted bottle, paper carton, gift box, and bag"*, and the script promises *"a large utility shopping bag"*. Students viewing Clue 4 see an abstract blue crumpled texture that resembles a plastic tarp rather than a shopping bag.
- **Surgical Correction:** Crop the upper rim of the bag showing the flared opening and the attachment points of the handles (`assets.json` suggested bounds `(0.15, 0.20, 0.85, 0.65)`), ensuring the yellow text on the handles is masked while preserving the unmistakable shopping tote geometry.

### 5.3 Misleading Sequential Flow Diagram on Slide 5 (`build_theory_5`)
- **Artifact Observation:** On Slide 5, `build_theory_5` (lines 371–382) renders three rounded rectangle cards with downward arrows:
  `[1. Popular Assumptions]` $\rightarrow$ `↓` $\rightarrow$ `[2. Consistent Use]` $\rightarrow$ `↓` $\rightarrow$ `[3. Learned Familiarity]`.
- **Conceptual Flaw:** In design pedagogy and marketing science, "Popular Assumptions" represents the **debunked myth** (the false belief that colors possess innate biological meanings). "Consistent Use" and "Learned Familiarity" represent the **empirical reality** (Ehrenberg-Bass S1). Connecting Step 1 to Step 2 with a downward arrow implies that popular assumptions cause, produce, or lead to consistent use!
- **Surgical Correction:** Restructure the graphic into a two-part comparative layout:
  - *Top Card (Negative/Red outline):* *"Debunked Assumption: Innate Color Meanings (Colors do not carry universal biological triggers)."*
  - *Downward Arrow / Contrast Marker:* *"Marketing Science Reality ↓"*
  - *Bottom Process Card (Blue outline):* *"Consistent Brand Exposure $\longrightarrow$ Learned Mental Shortcuts (Retail Context)."*

### 5.4 Repetitive Image Recycling Across Tiffany Slides (Slides 11, 12, 13)
- **Artifact Observation:** The identical photograph (`assets/tiffany-blue-box.jpg`) is placed across three consecutive slides:
  1. *Slide 11:* Displayed full width in `build_case_standard`.
  2. *Slide 12:* Displayed in `build_case_12` using `tiffany_box_detail_crop.jpg`, which is cropped so minimally `(0.20, 0.18, 0.80, 0.60)` that it appears virtually identical to Slide 11.
  3. *Slide 13:* In `build_case_13` (line 434), the full photograph is pasted *again* inside a turquoise card.
- **Impact:** Presenting the same photograph three times diminishes editorial quality and bores the audience. Slide 12 claims to show "Packaging craftsmanship", but reveals no new macro-details (such as custom paperboard scoring or embossed textures). Slide 13 claims to be a "Graphic card representing custom color standard Pantone 1837", but clutters the card with the recycled photo.
- **Surgical Correction:**
  - *Slide 12:* Crop tightly into an ultra-close macro detail of the white satin ribbon weave and paperboard edge.
  - *Slide 13:* Remove the photograph entirely. Replace with a clean, high-impact typographic Pantone swatch card: a solid 1837 Blue block above a white card base displaying *"PANTONE® 1837 Blue / Standardized 2001 / Registered Trademark 1998"*.

### 5.5 Visual / Script Mismatch on Slide 9 (Golden Arches Uncropped)
- **Artifact Observation:** On Slide 9 (`build_case_standard`), the image used is `assets/mcdonalds-fries-packaging.jpg` displayed uncropped. The Golden Arches logo is prominently visible in bright yellow on the front of the red fry carton.
- **Script Contradiction:** The spoken script states: *"Even if we completely hide the yellow arches printed on the front, almost everyone in this room immediately recognizes what brand this is."*
- **Defect:** The speaker claims the arches are hidden, but the audience sees them in plain sight.
- **Surgical Correction:** Either digitally mask the golden arches on the slide image to match the spoken premise, or adjust the script to state: *"Here you see the familiar red carton and golden arches. But even if you cover the logo with your thumb, the combination of red paperboard and hot yellow fries immediately signals McDonald's."*

### 5.6 Redundant Content Duplication on Slide 16 (`build_comparison_16`)
- **Artifact Observation:** On Slide 16, the left body bullets state:
  - Bullet 2: *"Red is shared by Coca-Cola, Target, and McDonald's"*
  - Bullet 3: *"Yellow is shared by IKEA, Shell, and DHL"*
  On the right side of the slide, `build_comparison_16` (lines 450–459) creates two cards titled "Shared Red" and "Shared Yellow", whose body text literally copies and pastes those exact two sentences word for word.
- **Defect:** The right half of the slide provides zero new visual insight, zero diagrams, and zero competitor logos (violating the asset hint in `deck.json`: *"Comparative chart displaying multiple well-known brand logos grouped inside identical red circles and yellow circles"*).
- **Surgical Correction:** Replace the redundant text inside the cards with clean visual competitor pills or badges displaying competitor names (Red card: Target, Netflix, Lego, Coca-Cola; Yellow card: Shell, DHL, Nikon, IKEA) to visually demonstrate category crowding.

### 5.7 Category Error in Slide 17 Interaction Formula (`build_theory_17`)
- **Artifact Observation:** `build_theory_17` (lines 473–486) builds the visual equation:
  `[Color and Shape]` + `[Familiarity and Habits]` = `[= Combined Visual Clues]`.
- **Defect:** This equation contains a basic category error. "Color and Shape" are external visual stimuli. "Familiarity and Habits" are internal consumer cognitive memories. Adding consumer memory to visual stimuli does NOT produce "Combined Visual Clues"—it produces **Brand Recognition** or **Mental Retrieval**.
- **Surgical Correction:** Re-label the third box:
  `[Distinctive Cues: Color + Shape]` + `[Consumer Context: Familiarity + Habit]` = `[= Rapid Brand Recognition]`.

### 5.8 Complete Omission of Promised Silhouettes on Slide 20 (`build_conclusion_20`)
- **Artifact Observation:** `deck.json` specifies for Slide 20:
  `"visual": {"brand": "none", "kind": "comparison", "asset_hint": "Closing visual bringing together minimalist silhouettes of the four case study packaging and building shapes on a clean white background.", "caption": "Beyond the Logo: Building brand recognition through familiar shapes and colors."}`.
- **Defect:** In `build_deck.py` (lines 529–547), `build_conclusion_20` completely omitted the visual component. It rendered a text-only slide consisting of a blue banner and three bullet points spanning the full 11.33-inch slide width.
- **Surgical Correction:** Render the four case silhouettes (contour bottle, fry carton rim, gift box with ribbon, warehouse exterior) in a clean horizontal row across the bottom of Slide 20, or update `deck.json` to reflect a text-only summary layout.

### 5.9 Copyright Attribution & Misleading "License" Hyperlinks on Slides 23 & 24
- **Artifact Observation:**
  1. *Deceptive License Link (Slide 23):* For `mcdonalds-follow-the-arches-billboard`, the license field in `assets.json` states: `"Copyrighted; no reuse license stated; included for classroom commentary"`. In `build_deck.py` line 640:
     `license_url = a.get("license_url") or a.get("source_page", "")`.
     Because `assets.json` set `license_url` to the Cossette agency blog URL, Slide 23 renders a blue clickable hyperlink labeled **"License"** that takes users to the agency's commercial promotional article! Presenting an agency case study URL as a "License" link for a copyrighted asset without an open license is legally misleading.
  2. *Duplicate Links for Public Domain Assets (Slide 23):* For the Coca-Cola bottle photograph and the 1915 patent drawing, `license_url` is `null` in `assets.json`. The fallback in line 640 causes the "License" link to point to the Wikimedia Commons source page, creating two identical links side by side ("Source · License") that both lead to the same URL.
  3. *Omission of SVG Logo Assets (Slides 23 & 24):* In `build_deck.py` line 748, the builder executes:
     `raster_assets = [a for a in load_assets_list() if a.get("format") != "svg"]`.
     This systematically excluded all 4 official vector brand logos (`mcdonalds-golden-arches-logo.svg`, `coca-cola-script-logo.svg`, `tiffany-wordmark-logo.svg`, `ikea-logo.svg`) from the Image Credits slides, leaving them uncredited.
- **Surgical Correction:**
  - For Public Domain assets, point the "License" hyperlink to the Creative Commons Public Domain deed (`https://creativecommons.org/publicdomain/mark/1.0/`) or display unlinked text: *"Public Domain"*.
  - For copyrighted assets included under fair use / classroom commentary, omit the "License" hyperlink and print: *"Classroom commentary / Fair use (No open license)"*.
  - Include SVG logo entries in the Image Credits appendix.

### 5.10 Missing Presenter Names on Cover Slide 1
- **Artifact Observation:** Slide 1 in `Beyond_the_Logo.pptx` contains only the presentation title, subtitle, and four decorative color stripes. Presenter names "Kaan" and "Caner" are completely missing from the cover layout.
- **Surgical Correction:** Add a clean subtitle text frame at `top = 5.2 in`: *"Presented by Kaan & Caner | 25-Minute Presentation | B2 English"*.

### 5.11 Uncropped Patent Drawing Clutter on Slides 7 and 8
- **Artifact Observation:** On Slide 7 (`build_case_standard`) and Slide 8 (`build_comparison_8`), the image file `assets/coca-cola-bottle-patent-1915.png` is placed full and uncropped. More than 50% of the graphic is occupied by patent office boilerplate: *"DESIGN. A. SAMUELSON. BOTTLE OR SIMILAR ARTICLE. APPLICATION FILED AUG. 18, 1915. 48,160. Patented Nov. 16, 1915."*, cross-section Figure 2, and attorney signatures. Shrunk to fit a 3.7-inch card, the central bottle elevation is tiny and illegible.
- **Surgical Correction:** Crop the patent drawing using normalized coordinates `(0.22, 0.16, 0.78, 0.65)` per `assets.json` to isolate strictly Figure 1 (the fluted bottle elevation).

---

## 6. Factual Grounding: Safe Sources vs. Presenter Analysis Matrix

To satisfy the brief's requirement for strict factual boundaries, all claims across Slides 1–20 were cross-checked against `safe_sources.json` (Sources S1–S9). The table below demarcates verified empirical/archival facts from presenter analysis and flags ungrounded overclaims:

| Slide ID | Slide Topic | Safe Source ID | Verified Source Facts (Ground Truth) | Presenter Analysis & Classroom Demonstrations | Ungrounded Overclaims / Risks |
| :---: | :--- | :---: | :--- | :--- | :--- |
| **1** | Title & Overview | S1 | Branding originated to identify product sources; distinctive brand assets substitute for brand names. | Structuring talk into 4 cases, theory, and design rules. | None. |
| **2** | Color Quiz | S1 | Single colors without exclusivity fail to uniquely signal a brand; wavelength sharing across competitors. | Classroom 4-swatch guessing activity to illustrate ambiguity. | Scripting audience shouts as pre-determined facts. |
| **3** | Shape Quiz | S1, S2 | Distinctive assets act as retrieval cues; compounding stimuli narrows brand search. | Classroom packaging shape guessing demonstration. | Clue 1 black silhouette; Clue 4 texture swatch; Tiffany logo leak. |
| **4** | The Reveal | S1, S2 | Brand recognition is learned through cumulative market exposure, not innate differentiation. | Synthesis of 4 case examples as learned memory shortcuts. | Visual asset hint promises logos; renders photos. |
| **5** | Memory & Myths | S1 | Ehrenberg-Bass: value of color is consistent exclusive use, not emotional preference (blue vs yellow). | Debunking universal color psychology formulas. | Diagram arrows imply myth causes consistent use. |
| **6** | Coca-Cola Brief | S4 | 1915 Bottling Association $500 challenge: recognize bottle by feel in dark or broken on ground. | Explaining competitive market of straight-sided bottles. | None. |
| **7** | 1915 Bottle Patent | S4 | Root Glass Co., cocoa bean inspiration, Alexander Samuelson patent D48,160 granted Nov 16, 1915. | Pointing out absence of red color and script lettering in patent. | Displaying full uncropped patent document clutter. |
| **8** | Shape Without Color | S4 | Bottle geometry (vertical fluting, curved waist) designed for recognition by touch. | Comparing bottle outline with patent drawing in black & white. | Claiming to compare "real bottle photo" while showing silhouette. |
| **9** | McDonald's Packaging | S1, S3 | Distinctive Asset Grid: packaging shapes and color combinations serve as brand retrieval cues. | Analyzing red fry carton + yellow fries as an everyday retail asset. | Claiming arches are hidden while showing them uncropped. |
| **10** | McDonald's Evolution | S8, S9 | S8: Late 2009 green rollout in Germany (~100 stores), France, UK. S9: 2018 Cossette Canada cropped arches billboards. | Differentiating logo fragment campaigns from color-alone recognition. | Stating all European restaurants replaced red background. |
| **11** | Tiffany Blue Box | S5 | 19th c. origin under Charles Lewis Tiffany for annual Blue Book; Tiffany Blue Box with white ribbon. | Framing luxury packaging as a long-term brand clue. | Using vague "pale ribbon" instead of white satin ribbon. |
| **12** | Tiffany Store Rules | S5 | 1906 NY Sun report: box unpurchasable alone, strictly accompanied by sold store item. | Explaining exclusivity as protection against brand dilution. | Recycled identical photograph from Slide 11. |
| **13** | Trademark Scope | S5 | 1998 color trademark registration; 2001 custom private Pantone standard "1837 Blue". | Distinguishing trademark category scope from universal color monopoly. | Asserting clothing/appliances are legally risk-free safe harbors. |
| **14** | IKEA Standardization | S6 | 1984 first visual profile manual; red/white in Scandinavia; 1991 standard blue warehouse stores with yellow wordmarks. | Analyzing large-scale architectural color blocking. | None. |
| **15** | IKEA FRAKTA Bag | S7 | 1986 shopping abandonment; 1989 Hamburg yellow test; blue FRAKTA sold at checkout, yellow for in-store loaners. | Framing utilitarian retail items as everyday distinctive brand assets. | Marked as Speaker 2 in PPTX; missing takeover cue. |
| **16** | Limits of Color | S1, S3 | S3 *Avoid* quadrant: elements high in fame but low in uniqueness (shared category cues). | Grouping competing brands into red and yellow categories. | Right cards duplicate left body text verbatim. |
| **17** | Compounding Clues | S1, S2, S3 | S1/S2 multi-stimulus processing; S3 compounding assets moves brands into *Use or Lose* quadrant. | Conceptual framework for interaction of color, shape, and context. | Claiming "confusion disappears"; category error in formula. |
| **18** | Redesign Risks | S2 | S2 Seven Costly Sins: brand assets are long-term investments like a classic suit; test before refreshing. | Warning against impulsive redesigns by new management teams. | Visual consists of two giant cards with no subpoints. |
| **19** | Design Guidelines | S1, S2, S3 | S1 consistency; S2 long-term investment; S3 distinctive shapes without logo reliance. | Three practical design rules for graphic designers. | Claiming core cues must remain "unchanged" (immutability). |
| **20** | Conclusion & Q&A | S1 | Logos confirm identity; distinctive visual cues guide discovery in crowded environments. | Recapitulation of thesis; transition to audience discussion. | Omitted 4 promised minimalist case silhouettes. |

---

## 7. Slide-by-Slide Audit & Actionable Remediation Ledger (Slides 1–24)

The following ledger details the verified facts, observed artifact defects, and exact surgical corrections required for each of the 24 presentation slides:

```
====================================================================================================
SLIDE 01 | COVER: BEYOND THE LOGO
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 60s (00:00 - 01:00) | Spoken Words: 127 (127 wpm)
* Current PPTX Status:     Speaker: 1 | 60s | Sources: [S1] (Header/Footer omitted on cover)
* Visual Elements:         Title (40pt), 2 subtitle paragraphs (22pt), 4 thin color stripes (0.12in).
* Factual Classification:  Source Fact (S1 branding purpose) + Presenter Overview.
* Observed Defects:
  1. Presenter identities "Kaan" and "Caner" are completely absent from the title slide.
  2. Slide visual asset hint in deck.json promised abstract packaging outlines; PPTX shows only 4 thin bars.
* Surgical Actionable Corrections:
  1. Add presenter credits below subtitle: "Presented by Kaan & Caner | 25-Minute Presentation | B2 English".
  2. In script, specify both presenters: "Today, Caner and I will explore how brands become recognizable..."

====================================================================================================
SLIDE 02 | VISUAL QUIZ: CAN COLOR ALONE IDENTIFY A BRAND?
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 85s (01:00 - 02:25) | Spoken Words: 136 (96 wpm net)
* Current PPTX Status:     Speaker: 1 | 85s | Sources: [S1] | Footer: Slide 2 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 4 colored rectangles (2.7x1.8in; Red,
                           Yellow, Turquoise, Blue) + Caption (11pt).
* Factual Classification:  Source Fact (S1 color ambiguity) + Classroom Demonstration.
* Observed Defects:
  1. Script pre-records audience reactions: "As you can hear around the room, people are shouting..."
* Surgical Actionable Corrections:
  1. Replace script lines with conditional oral staging: "Take a look at each color and shout out your
     guesses... In live classrooms, answers vary widely because primary colors belong to entire categories."

====================================================================================================
SLIDE 03 | VISUAL QUIZ: ADDING PRODUCT SHAPES TO COLORS
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 85s (02:25 - 03:50) | Spoken Words: 132 (93 wpm net)
* Current PPTX Status:     Speaker: 1 | 85s | Sources: [S1], [S2] | Footer: Slide 3 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 4 cards with clues + Caption (11pt).
* Factual Classification:  Source Fact (S1, S2 retrieval cues) + Classroom Demonstration.
* Observed Defects:
  1. [CRITICAL QUIZ SPOILER] `tiffany_box_quiz_crop.jpg` leaks black serif letters "TIFFANY" under ribbon bow.
  2. [VISUAL MISMATCH] Clue 1 is charcoal/black (`#111827`), NOT Coca-Cola red.
  3. [VISUAL DEFECT] Clue 4 (`ikea_bag_quiz_crop.jpg`) is a 392x417 texture swatch; has no bag silhouette.
  4. Body and script claim "Same 4 colors... product outlines", but clues are 1 cutout and 3 photo crops.
  5. Script fabricates audience guesses: "Many people in the room now guess Coca-Cola..."
* Surgical Actionable Corrections:
  1. Re-crop Tiffany box tightly around ribbon knot `(0.25, 0.22, 0.75, 0.42)` to completely eliminate typography.
  2. Standardize Clues 1–4 as unbranded vector silhouettes in the exact 4 colors (Red bottle, Yellow carton,
     Turquoise box, Blue tote), OR adjust text to say: "Packaging shapes and textures paired with colors".
  3. Re-crop IKEA bag to show tote bag rim and strap handles, masking yellow brand text.

====================================================================================================
SLIDE 04 | THE REVEAL: LEARNED BRAND CONNECTIONS IN DAILY LIFE
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 70s (03:50 - 05:00) | Spoken Words: 122 (105 wpm)
* Current PPTX Status:     Speaker: 1 | 70s | Sources: [S1], [S2] | Footer: Slide 4 of 24
* Visual Elements:         4 columns: Photo + Brand Name (22pt bold) + Subtitle (12pt).
* Factual Classification:  Source Fact (S1, S2 learned associations) + Case Study Reveal.
* Observed Defects:
  1. deck.json asset hint promised "revealing the official logos"; PPTX displays packaging photos.
  2. SVG logo assets in assets.json remain completely unused.
* Surgical Actionable Corrections:
  1. Update deck.json visual asset hint to reflect actual photographic packaging reveal layout.
  2. Maintain current clean photographic grid with bold brand typography labels.

====================================================================================================
SLIDE 05 | HOW BRAND MEMORY WORKS: CONTEXT BEATS COLOR MYTHS
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (05:00 - 06:15) | Spoken Words: 133 (106 wpm)
* Current PPTX Status:     Speaker: 1 | 75s | Sources: [S1] | Footer: Slide 5 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 3 rounded cards connected by "↓" arrows.
* Factual Classification:  Empirical Marketing Science (S1 Ehrenberg-Bass brand differentiation).
* Observed Defects:
  1. [CONCEPTUAL DIAGRAM ERROR] Downward arrows link "1. Popular Assumptions" -> "2. Consistent Use",
     implying the debunked myth causes or leads to consistent market use.
  2. [CRITICAL HANDOVER DEFECT] Missing Handover 1 to Caner at the conclusion of Slide 5.
* Surgical Actionable Corrections:
  1. Restructure diagram: Label Card 1 "Debunked Myth: Inherent Color Meaning", contrast with Card 2/3
     flow: "Empirical Mechanism: Consistent Brand Exposure -> Learned Mental Retrieval".
  2. Add Handover 1 in script: "To see how these principles operate in real commercial history, I will now
     hand over to Caner to walk through our four case studies, starting with Coca-Cola."

====================================================================================================
SLIDE 06 | CASE 1: COCA-COLA AND THE 1915 BOTTLE CHALLENGE
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (06:15 - 07:30) | Spoken Words: 136 (109 wpm)
* Current PPTX Status:     Speaker: 1 (WRONG) | 75s | Sources: [S4] | Footer: Slide 6 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Contour bottle photo (2.43x4.30in) + Caption.
* Factual Classification:  Corporate Archive Fact (S4 Coca-Cola Bottling Association 1915 challenge).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 1 in deck.json and PPTX notes; must be Speaker 2 (Caner).
  2. Missing takeover greeting acknowledging Kaan.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 2 (Caner) in deck.json and PPTX notes.
  2. Update opening script line: "Thank you, Kaan! Our first case study looks at Coca-Cola..."

====================================================================================================
SLIDE 07 | COCA-COLA: THE 1915 FLUTED BOTTLE DESIGN
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (07:30 - 08:45) | Spoken Words: 122 (98 wpm)
* Current PPTX Status:     Speaker: 1 (WRONG) | 75s | Sources: [S4] | Footer: Slide 7 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Patent drawing (2.61x4.30in) + Caption.
* Factual Classification:  Corporate Archive Fact (S4 Samuelson patent granted Nov 16, 1915).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 1; must be Speaker 2 (Caner).
  2. Patent drawing is uncropped; small patent office text, Fig 2, and signatures clutter the graphic.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 2 (Caner).
  2. Apply suggested crop `(0.22, 0.16, 0.78, 0.65)` to isolate Figure 1 fluted bottle profile.

====================================================================================================
SLIDE 08 | SHAPE STILL MATTERS WITHOUT COLOR
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (08:45 - 10:00) | Spoken Words: 126 (101 wpm)
* Current PPTX Status:     Speaker: 1 (WRONG) | 75s | Sources: [S4] | Footer: Slide 8 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 2 images (Silhouette + Patent) + 2 labels.
* Factual Classification:  Corporate Archive Fact (S4) + Presenter Visual Analysis.
* Observed Defects:
  1. [CRITICAL VISUAL MISMATCH] Script, body, and caption state: "Comparing the real glass bottle photo
     with the patent drawing", but PPTX renders a flat silhouette cutout (`coca-cola-contour-bottle_silhouette.png`).
  2. [SPEAKER CONTRACT DEFECT] Marked as Speaker 1; must be Speaker 2 (Caner).
* Surgical Actionable Corrections:
  1. Place actual studio bottle photo (`assets/coca-cola-contour-bottle.jpg`, cropped or desaturated)
     in left card, OR update body, script, and caption to explicitly state "Photo-derived silhouette".
  2. Reassign speaker to Speaker 2 (Caner).

====================================================================================================
SLIDE 09 | MCDONALD’S: MORE THAN RED AND YELLOW
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (10:00 - 11:15) | Spoken Words: 139 (111 wpm)
* Current PPTX Status:     Speaker: 1 (WRONG) | 75s | Sources: [S1], [S3] | Footer: Slide 9 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Red fry carton photo (2.78x4.30in) + Caption.
* Factual Classification:  Empirical Theory (S1, S3 retrieval cues) + Presenter Packaging Analysis.
* Observed Defects:
  1. [VISUAL / SCRIPT CONTRADICTION] Script says "Even if we completely hide the yellow arches...", but
     PPTX displays uncropped photo with giant yellow arches on the carton face.
  2. Universal recognition claim: "...almost everyone in this room immediately recognizes..."
  3. [SPEAKER CONTRACT DEFECT] Marked as Speaker 1; must be Speaker 2 (Caner).
* Surgical Actionable Corrections:
  1. Realign script: "Even if you cover the yellow arches, the packaging form and colorway remain unmistakable."
  2. Reassign speaker to Speaker 2 (Caner).

====================================================================================================
SLIDE 10 | MCDONALD’S: EUROPEAN GREEN AND CROPPED ARCHES
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (11:15 - 12:30) | Spoken Words: 130 (104 wpm)
* Current PPTX Status:     Speaker: 1 (WRONG) | 75s | Sources: [S8], [S9] | Footer: Slide 10 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Billboard photo (5.70x4.04in) + Caption.
* Factual Classification:  News Reporting Fact (S8 NBC green rollout) + Agency Case Fact (S9 Cossette 2018).
* Observed Defects:
  1. [CRITICAL HANDOVER DEFECT] Script terminates with obsolete handover to Speaker 2: "That brings me to
     the end of our first section. I will now hand over to my co-presenter to explore our next cases."
  2. Overstated European green scope: S8 specifies rollout starting in Germany (~100 stores), France, UK.
  3. Visual shows Canadian red billboard; contains zero visual evidence of European green background.
  4. [SPEAKER CONTRACT DEFECT] Marked as Speaker 1; must be Speaker 2 (Caner).
* Surgical Actionable Corrections:
  1. Delete obsolete handover sentence from script and stage directions.
  2. Accurately scope green rollout in bullet 1 and script: "...rolled out across European outlets, starting
     with pilot locations in Germany, France, and Great Britain."
  3. Reassign speaker to Speaker 2 (Caner).

====================================================================================================
SLIDE 11 | CASE 3: TIFFANY BLUE AND LUXURY PACKAGING
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (12:30 - 13:45) | Spoken Words: 127 (102 wpm)
* Current PPTX Status:     Speaker: 2 | 75s | Sources: [S5] | Footer: Slide 11 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Blue gift box photo (5.70x4.28in) + Caption.
* Factual Classification:  Corporate Archive Fact (S5 Charles Lewis Tiffany, 19th c. Blue Book).
* Observed Defects:
  1. Script opens with obsolete handover greeting: "Thank you! Let us now step into the world of luxury..."
  2. Script and body use vague "pale ribbon" instead of authentic S5 "white satin ribbon".
* Surgical Actionable Corrections:
  1. Update opening script line for internal continuity: "Moving from fast food to luxury packaging, our
     third case study brings us to Tiffany & Co."
  2. Replace "pale ribbon" with "white satin ribbon" in body bullet 2, script, and caption.

====================================================================================================
SLIDE 12 | TIFFANY: STORE RULES AND PRESENTATION
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (13:45 - 15:00) | Spoken Words: 128 (102 wpm)
* Current PPTX Status:     Speaker: 2 | 75s | Sources: [S5] | Footer: Slide 12 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Blue box detail photo (5.70x2.99in) + Caption.
* Factual Classification:  Corporate Archive Fact (S5 1906 New York Sun unpurchasable box report).
* Observed Defects:
  1. [VISUAL REDUNDANCY] `tiffany_box_detail_crop.jpg` is virtually identical to Slide 11 photo.
  2. Caption claims "Packaging craftsmanship", but photo reveals no macro craftsmanship details.
* Surgical Actionable Corrections:
  1. Crop tightly into an authentic macro detail of the white satin ribbon knot and paperboard texture.
  2. Replace "pale ribbon" in script with "white satin ribbon".

====================================================================================================
SLIDE 13 | TIFFANY: STANDARD COLOR AND TRADEMARK SCOPE
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (15:00 - 16:15) | Spoken Words: 122 (98 wpm)
* Current PPTX Status:     Speaker: 2 | 75s | Sources: [S5] | Footer: Slide 13 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: Turquoise rect + disclaimer + photo + Caption.
* Factual Classification:  Corporate Archive Fact (S5 1998 trademark, 2001 Pantone 1837) + Legal Analysis.
* Observed Defects:
  1. [VISUAL REDUNDANCY] Pastes `assets/tiffany-blue-box.jpg` for the third consecutive slide.
  2. Awkward banner: "Approximate screen color — not the official Pantone standard. No exact color guarantee."
  3. [LEGAL OVERCLAIM] Script asserts other companies can "freely use turquoise in clothing without breaking laws".
* Surgical Actionable Corrections:
  1. Remove recycled box photo. Replace with a clean graphic card showing Pantone 1837 color block and
     registration facts: "PANTONE® 1837 Blue / Standardized 2001 / Registered Trademark 1998".
  2. Reframe legal distinction: trademark protects against consumer confusion within retail jewelry classes,
     rather than providing a universal monopoly; avoid speculative clothing claims.

====================================================================================================
SLIDE 14 | CASE 4: IKEA AND STORE COLOR STANDARDIZATION
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 2 (Caner) | 75s (16:15 - 17:30) | Spoken Words: 128 (102 wpm)
* Current PPTX Status:     Speaker: 2 | 75s | Sources: [S6] | Footer: Slide 14 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: IKEA Halifax store photo (5.70x3.77in) + Caption.
* Factual Classification:  Museum Archive Fact (S6 1984 visual manual, Scandinavian red/white, 1991 blue stores).
* Observed Defects:
  1. [CRITICAL HANDOVER DEFECT] Missing Handover 2 at Slide 14 end (Caner handing back to Kaan).
* Surgical Actionable Corrections:
  1. Add Handover 2 at Slide 14 end: "To explore IKEA's everyday retail packaging and see what these cases
     teach us about distinctive design principles, I will now hand back to Kaan."

====================================================================================================
SLIDE 15 | IKEA: THE BLUE FRAKTA SHOPPING BAG
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (17:30 - 18:45) | Spoken Words: 130 (104 wpm)
* Current PPTX Status:     Speaker: 2 (WRONG) | 75s | Sources: [S7] | Footer: Slide 15 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: FRAKTA bag photo (5.70x4.28in) + Caption.
* Factual Classification:  Museum Archive Fact (S7 1986 Lundén observation, 1989 Hamburg yellow test, blue FRAKTA).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 2 in deck.json and PPTX notes; must be Speaker 1 (Kaan).
  2. Missing takeover greeting acknowledging Caner.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 1 (Kaan) in deck.json and PPTX notes.
  2. Add takeover greeting in opening script line: "Thank you, Caner! Alongside its blue warehouse buildings..."

====================================================================================================
SLIDE 16 | LIMITS OF SINGLE COLORS: SHARED BRAND CLUES
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (18:45 - 20:00) | Spoken Words: 126 (101 wpm)
* Current PPTX Status:     Speaker: 2 (WRONG) | 75s | Sources: [S1], [S3] | Footer: Slide 16 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 2 cards with swatches and duplicated text.
* Factual Classification:  Empirical Marketing Science (S1, S3 Ehrenberg-Bass Distinctive Asset Grid: Avoid).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 2; must be Speaker 1 (Kaan).
  2. [CONTENT DUPLICATION] Right cards verbatim copy left body bullets 2 and 3.
  3. Omitted promised competitor logo circles from asset hint.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 1 (Kaan).
  2. Replace duplicated text inside cards with clean competitor badges (Red: Target, Netflix, Lego, Coca-Cola;
     Yellow: Shell, DHL, Nikon, IKEA) to visually illustrate category crowding.

====================================================================================================
SLIDE 17 | COMBINING VISUAL CLUES: COLOR, SHAPE, AND CONTEXT
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (20:00 - 21:15) | Spoken Words: 126 (101 wpm)
* Current PPTX Status:     Speaker: 2 (WRONG) | 75s | Sources: [S1], [S2], [S3] | Footer: Slide 17 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 3 stacked cards with "+" and "=" operators.
* Factual Classification:  Empirical Marketing Science (S1, S2, S3 multi-stimulus compounding).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 2; must be Speaker 1 (Kaan).
  2. [CATEGORY ERROR IN FORMULA] Diagram equates `[Color + Shape] + [Familiarity] = [= Combined Visual Clues]`.
  3. Absolute certainty overclaim: "...confusion disappears."
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 1 (Kaan).
  2. Fix equation label: Card 3 should read `[= Rapid Brand Recognition]`.
  3. Replace "confusion disappears" with "identification ambiguity drops significantly".

====================================================================================================
SLIDE 18 | REDESIGN RISKS: PROTECTING FAMILIAR VISUAL CLUES
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (21:15 - 22:30) | Spoken Words: 123 (98 wpm)
* Current PPTX Status:     Speaker: 2 (WRONG) | 75s | Sources: [S2] | Footer: Slide 18 of 24
* Visual Elements:         Left: 3 body bullets (24pt). Right: 2 giant colored cards (green/red) with 4/3 words.
* Factual Classification:  Empirical Marketing Science (S2 Seven Costly Sins: long-term investment vs fashion).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 2; must be Speaker 1 (Kaan).
  2. Right visual cards are barren; contain only titles with zero explanatory subpoints.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 1 (Kaan).
  2. Add concise sub-bullets to cards: Green card: "Treat as capital investment / Protect learned shopper habits";
     Red card: "Unnecessary visual refreshes / Shelf navigation disruption".

====================================================================================================
SLIDE 19 | PRACTICAL GUIDELINES FOR DISTINCTIVE DESIGN
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (22:30 - 23:45) | Spoken Words: 119 (95 wpm)
* Current PPTX Status:     Speaker: 2 (WRONG) | 75s | Sources: [S1], [S2], [S3] | Footer: Slide 19 of 24
* Visual Elements:         3 numbered horizontal banner cards (01, 02, 03).
* Factual Classification:  Empirical Design Principles (S1 consistency, S2 investments, S3 distinctive assets).
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 2; must be Speaker 1 (Kaan).
  2. [IMMUTABLE CUES OVERCLAIM] Script demands core assets remain "unchanged", contradicting S2 refresh rules.
  3. Visual caption from deck.json is omitted in `build_guidelines_19`.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 1 (Kaan).
  2. Reframe Rule 3 script: "Protect core visual clues over time... If updates are necessary, quantify branding
     loss and compensate with strong direct branding."
  3. Add caption textbox below the cards.

====================================================================================================
SLIDE 20 | CONCLUSION: DISTINCTIVE CLUES IN DAILY LIFE
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Speaker 1 (Kaan) | 75s (23:45 - 25:00) | Spoken Words: 130 (104 wpm)
* Current PPTX Status:     Speaker: 2 (WRONG) | 75s | Sources: [S1] | Footer: Slide 20 of 24
* Visual Elements:         Blue takeaway header + 3 bullet points spanning the entire slide width.
* Factual Classification:  Presentation Synthesis & Thesis Recapitulation.
* Observed Defects:
  1. [SPEAKER CONTRACT DEFECT] Marked as Speaker 2; must be Speaker 1 (Kaan).
  2. [VISUAL OMISSION] Promised closing visual of 4 minimalist case silhouettes completely omitted.
* Surgical Actionable Corrections:
  1. Reassign speaker to Speaker 1 (Kaan).
  2. Render the 4 minimalist case silhouettes across the bottom of the slide, or update deck.json.

====================================================================================================
SLIDE 21 | REFERENCES: RESEARCH STUDIES AND CORPORATE ARCHIVES
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Displayed during Q&A | 0s | Spoken Words: 0 | Sources: S1, S2, S3, S4, S5
* Current PPTX Status:     Speaker: 2 | 0s | Footer: Slide 21 of 24
* Visual Elements:         Two-column layout: Left (S1, S2, S3), Right (S4, S5).
* Factual Classification:  Academic Marketing Science (S1, S2, S3) + Corporate Archives (S4, S5).
* Verification:            All 5 URLs verified against safe_sources.json. Hyperlinks active on titles.
* Observed Defects:
  1. Text box height (4.8in) is tight for 3 entries at 18pt font.
* Surgical Actionable Corrections:
  1. Reduce publisher font size to 15pt or tighten spacing after paragraphs to prevent vertical crowding.

====================================================================================================
SLIDE 22 | REFERENCES: MUSEUM ARCHIVES, NEWS AND AGENCY RECORDS
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Displayed during Q&A | 0s | Spoken Words: 0 | Sources: S6, S7, S8, S9
* Current PPTX Status:     Speaker: 2 | 0s | Footer: Slide 22 of 24
* Visual Elements:         Two-column layout: Left (S6, S7), Right (S8, S9).
* Factual Classification:  Corporate Museum Archives (S6, S7) + News (S8) + Agency Case Study (S9).
* Verification:            All 4 URLs verified against safe_sources.json. Hyperlinks active on titles.
* Observed Defects:        None. Clean 2-item per column layout.
* Surgical Actionable Corrections: None.

====================================================================================================
SLIDE 23 | APPENDIX: IMAGE CREDITS AND ATTRIBUTIONS (PART 1)
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Reference Appendix | 0s | Spoken Words: 0
* Current PPTX Status:     Speaker: 2 | 0s | Footer: Slide 23 of 24 | Notes: Reference appendix
* Visual Elements:         Two-column layout: Left (Fries, Billboard), Right (Contour Bottle, Patent Drawing).
* Observed Defects:
  1. [LEGAL / HYPERLINK DEFECT] Billboard entry renders clickable "License" link pointing to Cossette blog.
  2. [DUPLICATE HYPERLINKS] Contour bottle and Patent drawing link "License" to Wikimedia source page.
  3. Long license string (81 chars) wraps awkwardly at 18pt font.
* Surgical Actionable Corrections:
  1. For billboard, remove "License" hyperlink; display: "Fair use / Classroom commentary (No license stated)".
  2. For Public Domain assets, link "License" to `https://creativecommons.org/publicdomain/mark/1.0/`.
  3. Reduce license description font size to 14pt.

====================================================================================================
SLIDE 24 | APPENDIX: IMAGE CREDITS AND ATTRIBUTIONS (PART 2)
----------------------------------------------------------------------------------------------------
* Contract Speaker & Time: Reference Appendix | 0s | Spoken Words: 0
* Current PPTX Status:     Speaker: 2 | 0s | Footer: Slide 24 of 24 | Notes: Reference appendix
* Visual Elements:         Two-column layout: Left (Tiffany Box, IKEA Store), Right (IKEA FRAKTA Bag).
* Observed Defects:
  1. All 4 vector brand logos (`assets.json` SVGs) are filtered out and uncredited across Slides 23–24.
* Surgical Actionable Corrections:
  1. Add attribution for the 4 acquired SVG brand symbols in the empty right column space on Slide 24.
====================================================================================================
```

---

## 8. Summary of Actionable Remediation for Sibling Writer & PPTX Builder

To bring the presentation deck specification (`deck.json`), delivery script (`Speaker_Notes.md`), and programmatic slide generator (`build_deck.py`) into 100% compliance with all project mandates, the following concrete actions must be executed:

### Phase 1: Structural & Speaker Contract Re-synchronization
1. **Reassign Slide Speakers in `deck.json`:**
   - Change `"speaker": 1` to `"speaker": 2` for **Slides 6, 7, 8, 9, 10**.
   - Change `"speaker": 2` to `"speaker": 1` for **Slides 15, 16, 17, 18, 19, 20**.
   - Maintain Slides 1–5 as Speaker 1 (Kaan) and Slides 21–22 as Q&A references.
2. **Re-architect Handovers:**
   - **Slide 5 End:** Add verbal handover from Kaan to Caner.
   - **Slide 6 Start:** Add verbal takeover greeting from Caner acknowledging Kaan.
   - **Slide 10 End:** Delete obsolete midpoint handover sentence.
   - **Slide 11 Start:** Delete obsolete takeover greeting; replace with case transition.
   - **Slide 14 End:** Add verbal handover from Caner back to Kaan.
   - **Slide 15 Start:** Add verbal takeover greeting from Kaan acknowledging Caner.
3. **Presenter Names:**
   - Add "Presented by Kaan & Caner" to Slide 1 layout, notes, and scripts.

### Phase 2: Visual Artifact & Quiz Spoiler Corrections
1. **Slide 3 Tiffany Crop:** Re-crop `assets/tiffany-blue-box.jpg` to `(0.25, 0.22, 0.75, 0.42)` to completely remove visible "TIFFANY" wordmark letters.
2. **Slide 3 IKEA Bag Crop:** Re-crop `assets/ikea-frakta-bag.jpg` to include the tote rim and handle attachments while masking yellow strap typography.
3. **Slide 3 Colorway Alignment:** Ensure Clue 1 includes red color (or convert all 4 clues into consistent vector silhouettes matching the 4 colors from Slide 2).
4. **Slide 8 Photo vs. Silhouette:** Replace the flat silhouette cutout on Slide 8 with the actual glass contour bottle photograph (`assets/coca-cola-contour-bottle.jpg`, cropped or desaturated), matching the script and caption.
5. **Slide 13 Pantone Card:** Remove the recycled box photo; render a clean, high-impact Pantone 1837 Blue swatch card with legal trademark metadata.
6. **Slides 7 & 8 Patent Crop:** Apply normalized crop `(0.22, 0.16, 0.78, 0.65)` to eliminate patent boilerplate clutter.

### Phase 3: Script & Layout Refinements
1. **Fabricated Audience Responses:** Replace pre-scripted audience shouts on Slides 2, 3, and 9 with conditional speaker delivery prompts.
2. **Slide 5 Diagram:** Replace causal downward arrows from debunked assumptions with a two-part contrast layout (Debunked Myth vs. Empirical Reality).
3. **Slide 9 Arches Script:** Realign script to state: "Even if you were to cover the yellow arches, the packaging form and colorway remain unmistakable."
4. **Slide 10 Green Scope:** Scope European green background rollout accurately per S8 (~100 German restaurants, plus UK and France).
5. **Slide 16 Content Duplication:** Replace duplicated body text inside right cards with competitor brand badges.
6. **Slide 17 Category Error:** Fix diagram equation to `= Rapid Brand Recognition`.
7. **Slide 19 Immutability:** Reframe Rule 3 around disciplined asset preservation rather than absolute immutability.
8. **Slide 23 & 24 Credits & Links:** Fix deceptive "License" link on billboard; link Public Domain assets to CC0/PD deed; credit SVG logos.

---
*End of Substantive Revision Audit.*
