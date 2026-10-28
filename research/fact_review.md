# Independent Factual Review: Beyond the Logo Presentation Deck

**Target Workspace:** `/Users/kaan/Cloud/omp-sessions/beyond-the-logo`  
**Review Target:** `deck.json` (Presentation Deck Specification & Slide Notes)  
**Baseline Authorities:** `BRIEF.md`, `safe_sources.json`, `research.md`  
**Date of Audit:** October 2026  
**Auditor:** Independent Factual Reviewer  

---

## 1. Executive Summary & Audit Baseline

This independent factual review evaluates the complete 22-slide deck specification (`deck.json`) and accompanying delivery notes (`Speaker_Notes.md`) for the 25-minute two-person B2 presentation *Beyond the Logo*.

### 1.1 Methodological Baseline
All claims, citations, URLs, and legal descriptions were audited against the authoritative `safe_sources.json` registry (Sources S1–S9) and the pedagogical mandates of `BRIEF.md`:
1. **Source Registry Integrity:** Every citation must link directly to an authorized entry in `safe_sources.json`. Unapproved sources, unauthorized remappings, or broken URLs are flagged.
2. **Empirical Marketing Science vs. Corporate Lore:** Academic findings from the Ehrenberg-Bass Institute for Marketing Science (S1, S2, S3) are held to empirical standards and distinguished from corporate archives (S4, S5, S6, S7) and agency press materials (S8, S9).
3. **Classroom Demonstrations vs. Scientific Proof:** Perceptual guessing activities in Slides 2–3 must remain strictly framed as interactive demonstrations of learned associations rather than controlled scientific experiments; no invented statistical percentages or universal color-psychology claims are permitted.
4. **Legal & Intellectual Property Rigor:** Trademark and patent claims must accurately reflect statutory realities (e.g., category-bounded color trademark protection under trademark law vs. universal color monopolies) and avoid speculative or unverified legal narratives.

---

## 2. Known-in-Flight Corrections (Status: Under Active Writer Revision)

The deck writer is currently implementing five targeted corrections across the deck and assets. To prevent duplicate reporting, these items are formally recognized here with their factual justification and verified status:

| # | Item / Topic | Affected Slides / Assets | Writer Action in Progress | Factual Basis & Evidence Status |
| :--- | :--- | :--- | :--- | :--- |
| **KF-1** | **B2 English Simplification** | Whole deck (Slides 1–20 notes & body) | Rewriting complex academic jargon into clear, natural B2 oral delivery prose suitable for non-native listeners. | **In Progress.** Mandated by `BRIEF.md` (B2 vocabulary, 2400–2700 spoken words). Current word count is 2,523 words. |
| **KF-2** | **Slide 8 Trademark Tangent Removal** | Slide 8 (`From Design Patent to Registered Trademark`) | Removing extended legal discussions regarding 14-year design patent expiration, public domain transition, Lanham Act secondary meaning, and federal trademark registration dates. | **In Progress.** `safe_sources.json` Source S4 verifies only the November 16, 1915 design patent grant date. Acquired distinctiveness and Lanham Act history are unsupported by S4 and represent an unnecessary legal tangent. |
| **KF-3** | **McDonald's Architectural History Removal** | Slide 9 (`Case 2: McDonald's Arches as Roadside Architecture`) | Removing historical claims about drive-in restaurant exterior rooflines and architect Stanley Meston; refocusing on packaging geometry and colorway. | **In Progress.** Slide 9 erroneously cited `S1` (Romaniuk, Sharp, & Ehrenberg 2007) for architectural history. `S1` is an empirical paper on brand differentiation that contains zero facts about McDonald's building history. No architectural source exists in `safe_sources.json`. |
| **KF-4** | **IKEA FRAKTA Handle Details** | Slide 15 (`IKEA: The Utilitarian Blue FRAKTA Bag`) | Correcting text describing "woven yellow handles" to reflect the authentic blue polypropylene webbing straps with yellow woven lettering, and clarifying the yellow in-store loaner bag distinction. | **In Progress.** As documented in `safe_sources.json` (S7), yellow bags were tested in Hamburg (1989) and retained for in-store loaners; production blue FRAKTA bags feature blue webbing straps with yellow IKEA lettering. |
| **KF-5** | **Tiffany Ribbon Color Alignment** | Slide 11 & `assets.json` metadata | Ensuring all references to the Tiffany gift box ribbon specify the signature white satin ribbon rather than the "silver-toned ribbon bow" noted in photographic artifact descriptions. | **In Progress.** `safe_sources.json` Source S5 explicitly documents the signature white satin ribbon as part of the core packaging ritual. The photographic artifact (`assets/tiffany-blue-box.jpg`) exhibits ambient lighting sheen, but the deck prose correctly standardizes on white satin ribbon. |

---

## 3. Critical Citation & Source Alignment Findings (Remaining Concrete Corrections)

The following actionable defects exist in the latest available `deck.json` and require immediate remediation:

### Finding 1: S3 Citation Remapping & Missing Empirical Marketing Science Source
* **Severity:** CRITICAL
* **Affected Locations:** `deck.json` root `sources` table, Slide 7, Slide 21 (References Slide 1).
* **The Defect:**
  In `safe_sources.json`, `S3` is defined as:
  > **Title:** *Brands of Distinction*  
  > **Author:** Jenni Romaniuk (2013)  
  > **Publisher:** Ehrenberg-Bass Institute for Marketing Science / UniSA Business Magazine  
  > **URL:** `https://marketingscience.info/news-and-insights/brands-of-distinction`  
  > **Verified Claims:** Definition of distinctive brand assets as non-brand-name elements; the two core dimensions (Uniqueness and Fame, with Uniqueness being more critical); and the 4-quadrant Distinctive Asset Grid (*Use or Lose*, *Invest*, *Avoid*, *Test or ignore*).

  However, in `deck.json`, `S3` was overwritten/remapped to:
  > `"id": "S3"`, `"title": "Design for a Bottle or Similar Article (U.S. Design Patent D48,160)"`, `"publisher": "United States Patent and Trademark Office / Google Patents"`, `"url": "https://patents.google.com/patent/USD48160S/en"`.

* **Factual & Structural Breakage:**
  1. **Source Registry Breach:** Google Patents is not an approved source in `safe_sources.json`.
  2. **Wrong Citation on Slide 7:** Slide 7 cites `["S3"]` for the fact that U.S. Design Patent D48,160 was granted on November 16, 1915 to the Root Glass Company. But in `safe_sources.json`, this historical milestone is already fully verified under **S4** (*The History of the Coca-Cola Contour Bottle*, The Coca-Cola Company: *"The Root Glass Company put forth a patent registration under Samuelsson’s name which was granted on November 16th, 1915. That date was later incorporated into the lettering on the final design of the bottle."*).
  3. **Loss of Distinctive Asset Grid:** By overwriting `S3`, the presentation loses its citation anchor for the Ehrenberg-Bass Distinctive Asset Grid framework, which is a foundational theoretical requirement in `BRIEF.md` and `research.md`.
  4. **Corrupted References Slide:** Slide 21 displays the Google Patents entry as S3 instead of Romaniuk (2013).

* **Exact Replacement Recommendation:**
  1. **In `deck.json` (Slide 7):**
     ```json
     "sources": [
       "S4"
     ]
     ```
  2. **In `deck.json` (Root `sources` array):** Restore S3 to match `safe_sources.json`:
     ```json
     {
       "id": "S3",
       "title": "Brands of Distinction",
       "publisher": "Ehrenberg-Bass Institute for Marketing Science / UniSA Business Magazine",
       "url": "https://marketingscience.info/news-and-insights/brands-of-distinction"
     }
     ```
  3. **In `deck.json` (Slide 21 body text):** Replace the third bullet with:
     ```text
     "S3: Romaniuk, J. (2013). Brands of Distinction. UniSA Business Magazine / Ehrenberg-Bass Institute for Marketing Science. https://marketingscience.info/news-and-insights/brands-of-distinction"
     ```

---

### Finding 2: Unauthorized Secondary Source S10 (Adweek 2018)
* **Severity:** HIGH
* **Affected Locations:** `deck.json` root `sources` table, Slide 10, Slide 22 (References Slide 2).
* **The Defect:**
  In `deck.json`, a tenth source was created:
  > `"id": "S10"`, `"title": "McDonald's Ads Win Cannes Outdoor Grand Prix by Turning Golden Arches Into Arrows"`, `"publisher": "Adweek"`, `"url": "https://www.adweek.com/creativity/mcdonalds-ads-win-cannes-outdoor-grand-prix-by-turning-golden-arches-into-arrows/"`.  
  Slide 10 lists `"sources": ["S8", "S9", "S10"]`, and Slide 22 lists S10 as its fifth reference bullet.

* **Factual & Structural Breakage:**
  1. **Source Registry Breach:** `safe_sources.json` strictly bounds approved sources to S1 through S9. S10 is an unauthorized secondary trade-press addition.
  2. **Redundant Citation:** All claims made on Slide 10 regarding the 2018 Canadian "Follow the Arches" campaign (cropping arches into directional signs, "on your right" copy, and relying on partial logo recognition rather than color-only or logo-free cues) are completely verified by primary source **S9** (*Cossette*, February 13, 2018).
  3. S10 adds no verified facts not already covered by S9 and clutters the reference registry.

* **Exact Replacement Recommendation:**
  1. **In `deck.json` (Slide 10):**
     ```json
     "sources": [
       "S8",
       "S9"
     ]
     ```
  2. **In `deck.json` (Slide 22):** Remove the S10 bullet from `body` and update `sources`:
     ```json
     "sources": [
       "S6",
       "S7",
       "S8",
       "S9"
     ]
     ```
     Remove bullet: `"S10: Adweek (2018). McDonald's Ads Win Cannes Outdoor Grand Prix..."`.
  3. **In `deck.json` (Root `sources` array):** Delete the entire S10 object.

---

### Finding 3: Missing Co-Citations to Restored S3 on Strategy & Framework Slides
* **Severity:** MEDIUM
* **Affected Locations:** Slide 16, Slide 17, Slide 19.
* **The Defect:**
  - **Slide 16** (*The Limits of Isolated Color: Shared Category Cues*): Cites only `["S1"]`. While S1 discusses the necessity of exclusive and consistent use, the specific theoretical concept of category cues that are high in fame but low in uniqueness (the *Avoid* quadrant of the Distinctive Asset Grid) originates in **S3** (*Brands of Distinction*).
  - **Slide 17** (*Compounding Visual Assets: Color, Form, and Context*): Cites `["S1", "S2"]`. The principle of evaluating uniqueness over fame and compounding assets to move out of the ambiguity zone is defined in **S3**.
  - **Slide 19** (*Four Practical Guidelines for Distinctive Design*): Cites `["S1", "S2"]`. Guideline 2 ("Compound color with form to avoid category ambiguity") and Guideline 4 directly reflect the Distinctive Asset Grid principles in **S3**.

* **Exact Replacement Recommendation:**
  - **Slide 16:** Change `"sources": ["S1"]` to `"sources": ["S1", "S3"]`.
  - **Slide 17:** Change `"sources": ["S1", "S2"]` to `"sources": ["S1", "S2", "S3"]`.
  - **Slide 19:** Change `"sources": ["S1", "S2"]` to `"sources": ["S1", "S2", "S3"]`.

---

## 4. Empirical Claims & Methodological Rigor Audit

### 4.1 Precision Refinement: Physiological / Biological vs. Learned Market Repetition (Slide 5)
* **Slide ID:** Slide 5 (*How Visual Memory Works: Context Over Color Psychology*)
* **Current Spoken Notes:**
  > *"However, empirical marketing research from the Ehrenberg-Bass Institute shows that brand color associations do not depend on universal biological reactions. Instead, consumers evaluate brand colors based on category conventions and learned market experience. Red does not make people crave food by nature; rather, decades of seeing red on fast-food packaging taught consumers to associate the color with the category."*
* **Empirical Reality & Nuance:**
  Ehrenberg-Bass empirical research (S1: Romaniuk, Sharp, & Ehrenberg 2007) analyzed consumer survey responses across 17 consumer packaged goods categories to measure perceived brand differentiation in commercial buying situations. They did not conduct neurobiological, physiological, or biological reflex testing on appetite stimulation.
  S1's actual finding and quote is:
  > *"We argue that the real value of building up strong links to an element (such as a particular colour) is not that people may like, for example blue more than yellow, so a brand should choose blue over yellow. Rather, if a brand consistently uses blue in its packaging and communications, and is the only brand that uses blue, consumers will come to quickly and easily identify that the colour blue represents the brand."*
* **Correction Recommendation:**
  Do not claim that Ehrenberg-Bass conducted biological laboratory experiments disproving neurology. Frame the critique within marketing science:
  > *"However, marketing science from the Ehrenberg-Bass Institute shows that brand identification relies on market consistency and category conventions rather than inherent emotional meanings in colors. As researchers point out, the real commercial value of a color is not whether consumers naturally prefer blue over yellow, but whether a brand consistently and exclusively uses that color over time to establish a reliable mental shortcut."*

### 4.2 Audit of Classroom Inferences vs. Source-Supported Facts
A rigorous line must be maintained between empirical findings and classroom demonstrations:

| Slide ID | Slide Concept | Classroom Demonstration / Inference Component | Source-Supported Empirical Fact | Audit Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Slide 2** | Quiz Part 1: Color Alone | Displaying 4 unbranded swatches to solicit audience guesses. Ambiguity demonstrated interactively. | S1 verified claim: Isolated colors without consistency and exclusivity fail to uniquely signal a brand because primary hues are shared across category competitors. | **PASS.** Notes and captions explicitly declare: *"Classroom demonstration: Four isolated color swatches tested without shapes or words."* No false statistical claims (e.g., no invented "only 12% guessed correctly"). |
| **Slide 3** | Quiz Part 2: Structural Outlines | Displaying packaging silhouettes alongside swatches. Audience guesses become more specific. | S1 & S2: Distinctive qualities serve as retrieval cues; compounding visual stimuli significantly reduces identification ambiguity. | **PASS.** Notes explicitly state: *"While recognition is never guaranteed for every single person in an audience, combining a familiar brand color with a distinctive structural packaging shape makes identification significantly easier..."* Avoids claiming universal or 100% recognition. |
| **Slide 4** | The Reveal | Transition from quiz guessing to brand identification. | S1 & S2: Brand assets function as mental shortcuts built through cumulative exposure, not innate biological knowledge. | **PASS.** Clearly explains that recognition is an acquired, learned mental link developed through shopping exposure. |
| **Slide 16** | Shared Category Cues | Grouping brands (Coca-Cola, Target, Netflix, McDonald's; IKEA, Shell, DHL) in shared color swatches. | S1 & S3: Competitive color crowding creates cognitive interference; elements high in fame but low in uniqueness fall in the *Avoid* quadrant. | **PASS.** Legitimate pedagogical grouping illustrating competitive crowding; no unverified market share numbers asserted. |
| **Slide 17** | Compounding Cues | Diagram of Color + Shape + Context interaction. | S1 & S2: Multi-stimulus processing; testing component parts reveals whether cues function independently. | **PASS.** Accurately notes that recognition varies across regional audiences and category buying habits. |

---

## 5. Legal & Intellectual Property Claims Audit

### 5.1 Tiffany & Co. Color Trademark Scope (Slide 13)
* **Slide ID:** Slide 13 (*Tiffany: Standardizing Pantone 1837 and Trademark Scope*)
* **Audit Statement:**
  Slide 13 notes:
  > *"According to company records, Tiffany registered Tiffany Blue as a formal color trademark in 1998. Then in 2001, the company partnered with the Pantone Color Institute to create '1837 Blue,' a proprietary custom standard named after Tiffany's founding year that is not available in public swatch books... However, designers must understand a critical legal boundary: Tiffany does not own every shade of turquoise. Trademark protection applies specifically to luxury jewelry boxes, retail packaging, and related goods where color confusion might mislead buyers. Other companies in unrelated industries remain entirely free to use turquoise in their own branding."*
* **Legal Analysis & Evidence:**
  1. **Trademark vs. Universal Monopoly:** Color trademarks registered under the Lanham Act (and international equivalents following *Qualitex Co. v. Jacobson Products Co.*) protect single colors only upon demonstrating secondary meaning within specific international classes of goods and services (e.g., jewelry packaging, retail jewelry services). They do not grant a general property copyright or patent over the color itself. Slide 13 correctly articulates this fundamental distinction.
  2. **Primary Source Grounding:** The 1998 trademark registration and 2001 Pantone standardization are drawn directly from S5 (*Tiffany Blue: A Color So Famous, It's Trademarked*, Tiffany Press Archives). Slide 13 appropriately hedges corporate claims by citing *"According to company records..."* in compliance with `BRIEF.md`.
* **Verdict:** **PASS.** Legally accurate, well-hedged, and free of legal misinformation.

### 5.2 Coca-Cola Design Patent Milestones (Slide 7 & Slide 8)
* **Slide 7:** Accurately states that U.S. Design Patent D48,160 was granted on November 16, 1915 to Alexander Samuelson of the Root Glass Company for an ornamental bottle design. This is documented in S4.
* **Slide 8:** As noted under KF-2, the extended legal narrative regarding 14-year design patent expiration, public domain transitions, and Lanham Act trademark registration disputes is unsupported by `safe_sources.json` S4. The writer's in-flight removal of this tangent resolves the legal scope overreach.

---

## 6. Master Source Verification & URL Alignment Matrix

Every source referenced in `safe_sources.json`, `research.md`, and `deck.json` was cross-checked for title, publisher, canonical URL, and verified claims:

| ID | Verified Title in `safe_sources.json` | Verified Publisher | Canonical URL (`safe_sources.json`) | Status in `deck.json` | Observed URL in `deck.json` | Audit Finding & Action |
| :---: | :--- | :--- | :--- | :---: | :--- | :--- |
| **S1** | *Evidence concerning the importance of perceived brand differentiation* | Australasian Marketing Journal / Ehrenberg-Bass Institute | `https://assets.marketingscience.info/different.pdf` | **MATCH** | `https://assets.marketingscience.info/different.pdf` | **PASS.** Correctly cited in Slides 1, 2, 3, 4, 5, 9, 16, 17, 19, 20, 21. |
| **S2** | *Q&A: Seven Costly Sins of Brand Identity* | Ehrenberg-Bass Institute for Marketing Science | `https://assets.marketingscience.info/Brand-Identity-QA.pdf` | **MATCH** | `https://assets.marketingscience.info/Brand-Identity-QA.pdf` | **PASS.** Correctly cited in Slides 3, 4, 17, 18, 19, 21. |
| **S3** | *Brands of Distinction* | Ehrenberg-Bass Institute / UniSA Business Magazine | `https://marketingscience.info/news-and-insights/brands-of-distinction` | **CORRUPTED / REMAPPED** | `https://patents.google.com/patent/USD48160S/en` | **FAIL.** Hijacked by Google Patents entry. Must be restored to Romaniuk (2013) and cited on Slides 16, 17, 19, 21. |
| **S4** | *The History of the Coca-Cola Contour Bottle* | The Coca-Cola Company | `https://www.coca-colacompany.com/about-us/history/the-history-of-the-coca-cola-contour-bottle` | **MATCH** | `https://www.coca-colacompany.com/about-us/history/the-history-of-the-coca-cola-contour-bottle` | **PASS.** Correct URL in deck and Slide 21. Must replace S3 on Slide 7. |
| **S5** | *Tiffany Blue: A Color So Famous, It's Trademarked* | Tiffany & Co. Press Archives | `https://press.tiffany.com/our-story/tiffany-blue/` | **MATCH** | `https://press.tiffany.com/our-story/tiffany-blue/` | **PASS.** Correctly cited in Slides 11, 12, 13, 21. |
| **S6** | *History of the logotype: The small steps of evolution* | IKEA Museum / Inter IKEA Systems B.V. | `https://ikeamuseum.com/en/explore/the-story-of-ikea/history-of-the-logotype/` | **MATCH** | `https://ikeamuseum.com/en/explore/the-story-of-ikea/history-of-the-logotype/` | **PASS.** Correctly cited in Slides 14, 22. |
| **S7** | *Beloved bag: The story of FRAKTA* | IKEA Museum / Inter IKEA Systems B.V. | `https://ikeamuseum.com/en/explore/the-story-of-ikea/beloved-bag/` | **MATCH** | `https://ikeamuseum.com/en/explore/the-story-of-ikea/beloved-bag/` | **PASS.** Correctly cited in Slides 15, 22. |
| **S8** | *McDonald’s rolling out green logo in Europe* | NBC News / The Associated Press | `https://www.nbcnews.com/id/wbna34111784` | **MATCH** | `https://www.nbcnews.com/id/wbna34111784` | **PASS.** Correctly cited in Slides 10, 22. |
| **S9** | *Cossette and McDonald's deconstruct the iconic Golden Arches...* | Cossette (February 13, 2018) | `https://www.cossette.com/en/blog/__temp_icoufkdgyfmhfyeayjfwwthtvmmmmbyghnhu` | **MATCH** | `https://www.cossette.com/en/blog/__temp_icoufkdgyfmhfyeayjfwwthtvmmmmbyghnhu` | **PASS.** Correctly cited in Slides 10, 22. |
| **S10** | *McDonald's Ads Win Cannes Outdoor Grand Prix...* | Adweek (2018) | *(None - unapproved source)* | **UNAUTHORIZED** | `https://www.adweek.com/creativity/mcdonalds-ads-win-cannes-outdoor-grand-prix-by-turning-golden-arches-into-arrows/` | **FAIL.** Not in `safe_sources.json`. Must be removed from Slide 10, Slide 22, and root `sources`. |

---

## 7. Slide-by-Slide Audit & Verification Matrix (Slides 1–22)

| Slide ID | Title | Speaker & Time | Listed Sources in `deck.json` | Factual & Methodological Status | Concrete Remediation Required |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | Beyond the Logo | Spk 1 (60s) | S1 | **VERIFIED.** Factual overview; sets two-speaker structure. | None. |
| **2** | Visual Quiz Part 1: Color | Spk 1 (85s) | S1 | **VERIFIED.** Labeled classroom demonstration; no false stats. | None. |
| **3** | Visual Quiz Part 2: Shapes | Spk 1 (85s) | S1, S2 | **VERIFIED.** Labeled classroom demonstration; unbranded silhouettes. | None. |
| **4** | The Reveal: Learned Associations | Spk 1 (70s) | S1, S2 | **VERIFIED.** Clear distinction: learned cues vs biological reflexes. | None. |
| **5** | How Visual Memory Works | Spk 1 (75s) | S1 | **NUANCE REQUIRED.** Refine biological claim to marketing science. | Adjust notes prose per Section 4.1. |
| **6** | Case 1: Coca-Cola Tactile Challenge | Spk 1 (75s) | S4 | **VERIFIED.** 1915 brief ("in dark / broken on ground") matches S4. | None. |
| **7** | The 1915 Contour Patent | Spk 1 (75s) | S3 *(wrong)* | **CITATION DEFECT.** Patent grant date is supported by S4, not S3. | Change `sources` to `["S4"]`. |
| **8** | Design Patent to Trademark | Spk 1 (75s) | S4 | **KNOWN IN-FLIGHT (KF-2).** Writer removing trademark tangent. | Note in-flight removal of trademark tangent. |
| **9** | McDonald's Roadside Architecture | Spk 1 (75s) | S1 *(wrong)* | **KNOWN IN-FLIGHT (KF-3).** Architecture history being removed. | Note in-flight removal; S1 has no architecture facts. |
| **10** | McDonald's Palette & Arches | Spk 1 (75s) | S8, S9, S10 *(extra)* | **UNAUTHORIZED SOURCE.** S10 is unauthorized secondary trade press. | Remove S10; update sources to `["S8", "S9"]`. |
| **11** | Case 3: Tiffany Blue | Spk 2 (75s) | S5 | **KNOWN IN-FLIGHT (KF-5).** Standardizing white satin ribbon. | Verify white satin ribbon description. |
| **12** | Tiffany: Packaging Ritual | Spk 2 (75s) | S5 | **VERIFIED.** 1906 NY Sun unpurchasable box rule matches S5. | None. |
| **13** | Tiffany: Pantone 1837 & Trademark | Spk 2 (75s) | S5 | **VERIFIED.** 1998 trademark, 2001 Pantone standard; scope accurate. | None. |
| **14** | Case 4: IKEA Standardization | Spk 2 (75s) | S6 | **VERIFIED.** 1984 profile, Scandinavian red-white, 1991 blue stores. | None. |
| **15** | IKEA: Blue FRAKTA Bag | Spk 2 (75s) | S7 | **KNOWN IN-FLIGHT (KF-4).** Correcting handle details. | Align handle details (blue straps, yellow text). |
| **16** | Limits of Isolated Color | Spk 2 (75s) | S1 | **CITATION GAP.** Missing co-citation to Distinctive Asset Grid. | Add S3 to `sources` (`["S1", "S3"]`). |
| **17** | Compounding Visual Assets | Spk 2 (75s) | S1, S2 | **CITATION GAP.** Distinctive Asset framework defined in S3. | Add S3 to `sources` (`["S1", "S2", "S3"]`). |
| **18** | Risks of Identity Redesign | Spk 2 (75s) | S2 | **VERIFIED.** Classic suit metaphor and component testing match S2. | None. |
| **19** | Practical Guidelines | Spk 2 (75s) | S1, S2 | **CITATION GAP.** Distinctive design principles draw on S3. | Add S3 to `sources` (`["S1", "S2", "S3"]`). |
| **20** | Conclusion & Q&A | Spk 2 (75s) | S1 | **VERIFIED.** Strong thesis synthesis; no overclaims. | None. |
| **21** | References 1 | Spk 2 (0s) | S1, S2, S3, S4, S5 | **CORRUPTED S3.** Displays Google Patents entry as S3. | Restore S3 to Romaniuk (2013) *Brands of Distinction*. |
| **22** | References 2 | Spk 2 (0s) | S6, S7, S8, S9, S10 | **UNAUTHORIZED S10.** Displays S10 Adweek bullet. | Remove S10 bullet and citation. |

---

## 8. Actionable Remediation Checklist for Deck Writer

To bring `deck.json` and `Speaker_Notes.md` into 100% compliance with `safe_sources.json` and `BRIEF.md`, execute the following precise edits:

1. [ ] **Restore S3 in Root Sources:** In `deck.json` `sources`, replace the Google Patents entry with:
   ```json
   {
     "id": "S3",
     "title": "Brands of Distinction",
     "publisher": "Ehrenberg-Bass Institute for Marketing Science / UniSA Business Magazine",
     "url": "https://marketingscience.info/news-and-insights/brands-of-distinction"
   }
   ```
2. [ ] **Realign Slide 7 Citation:** In `deck.json` Slide 7, change `"sources": ["S3"]` to `"sources": ["S4"]`.
3. [ ] **Remove S10 from Slide 10:** In `deck.json` Slide 10, change `"sources": ["S8", "S9", "S10"]` to `"sources": ["S8", "S9"]`.
4. [ ] **Add S3 Co-Citations to Framework Slides:**
   - Slide 16: `"sources": ["S1", "S3"]`
   - Slide 17: `"sources": ["S1", "S2", "S3"]`
   - Slide 19: `"sources": ["S1", "S2", "S3"]`
5. [ ] **Clean Reference Slides (Slides 21 & 22):**
   - Slide 21: Replace the S3 bullet text with:
     `"S3: Romaniuk, J. (2013). Brands of Distinction. UniSA Business Magazine / Ehrenberg-Bass Institute for Marketing Science. https://marketingscience.info/news-and-insights/brands-of-distinction"`
   - Slide 22: Delete the S10 bullet text and remove `"S10"` from Slide 22 `"sources"`.
   - Root Sources: Delete the `S10` object.
6. [ ] **Refine Slide 5 Spoken Notes:** Replace the biological reflex claim with marketing science category learning per Section 4.1.
7. [ ] **Synchronize Known-in-Flight Edits:** Finalize the removal of Slide 8 trademark tangent and Slide 9 architectural history, verify FRAKTA handle text (Slide 15), and ensure white satin ribbon consistency across Slide 11 and visual assets.

---
*End of Independent Factual Review.*
