# Dalecarlia Rebels AFF — Project Brief & Product Requirements Document (PRD)

---

## 1. Executive Summary & Vision

### 1.1 Project Overview
**Dalecarlia Rebels AFF** is the official American football club representing Falun, Borlänge, and the surrounding Dalarna region in Sweden. Rooted in grassroots sports development, community inclusion, and athletic excellence, the club provides opportunities for youth (U15, U19), adult players, rookies, and returning veterans.

This document serves as the formal Project Brief and Product Requirements Document (PRD) for the club's digital presence and web application across Swedish (`dalecarliarebels.se`) and international/English (`dalecarliarebels.com`) domains.

### 1.2 Core Mission & Objectives
- **Drive Player Recruitment:** Lower the threshold for new players, parents, and coaches to join through transparent information, loaner gear access, and an interactive "Position Finder".
- **Establish Regional Identity:** Cement the club's status as Dalarna's premier American football organization, anchored in Falun & Borlänge (Kvarnsvedens IP), free of external or legacy affiliations.
- **Engage Parents & Community:** Provide clear safety guidelines, age-appropriate developmental pathways (non-contact flag football progression to full-contact equipment), and scheduling transparency.
- **Commercial & Sponsor Visibility:** Offer premium exposure for local municipal and commercial partners (e.g., Falu Energi & Vatten) and federation governance (SWE3).
- **Streamline Club Operations:** Enable rapid interest registrations, camp sign-ups, and calendar dissemination.

---

## 2. Brand Identity & Design System Specification

### 2.1 Color Palette
The visual identity directly reflects the official Dalecarlia Rebels logo and apparel styling:

| Token Name | Hex Code | RGB | Role / Usage |
| :--- | :--- | :--- | :--- |
| **Primary Rebels Navy** | `#213567` (alt `#1E3466`) | `rgb(33, 53, 103)` | Dominant brand signature, arrows, typography, primary chrome |
| **Midnight Surface** | `#021134` / `#0B1A3D` | `rgb(2, 17, 52)` | App background, dark mode canvas, structural depth |
| **Crisp White** | `#FFFFFF` | `rgb(255, 255, 255)` | Inline accents, typography on dark backgrounds, badges, logo borders |
| **Athletic Crimson Red** | `#C5222F` | `rgb(197, 34, 47)` | Primary Call-to-Action (CTA), urgency cues, live match badges |
| **Trophy Gold** | `#F59E0B` | `rgb(245, 158, 11)` | Featured highlights (e.g. Dukes Tourney), awards, special announcements |
| **Muted Slate** | `#94A3B8` / `#64748B` | `rgb(148, 163, 184)` | Secondary copy, metadata, timestamps, subtle borders |

### 2.2 Typography Hierarchy
- **Display & Headings:** `Barlow Condensed` / Bold athletic gothic sans (Uppercase, `tracking-wider`, heavy weights 700–900).
- **Body & Functional UI:** Clean modern sans-serif (`Inter` or system athletic grotesque), high legibility, 16px base font size on mobile.
- **Accents & Data:** Monospace or tabular numerals for dates, scores, and practice schedules.

### 2.3 Brand Constraints & Governance
- **Mandatory Exclusions:** Strictly **NO** references to "Uppland-Bro", "Broncos", "Kungsängen", or external joint mergers.
- **Affiliation:** Official member of **SWE3** (*Svenska Förbundet för Amerikansk Fotboll, Flagfotboll och Cheerleading*).
- **Key Personnel:** Head Coach **CJ Rahmings**.
- **Key Venues:** Kvarnsvedens IP, Falun & Borlänge training fields.

---

## 3. Target Audience & User Personas

| Persona | Demographics & Context | Primary Goals & Needs | Key User Journey |
| :--- | :--- | :--- | :--- |
| **1. The Rookie Player ("Nybörjaren")** | Youth/adult (13–30 yrs) in Dalarna; no prior American football experience. | Wants to know if they fit, what gear is needed, and when they can try without cost or pressure. | Uses the "Hitta din position" tool → sees loaner gear is free → fills out the 30-second Prova-På form. |
| **2. The Concerned Parent ("Föräldern")** | Parents of youth players (aged 10–18). | Worried about injury risk, concussion protocols, equipment costs, and coaching credibility. | Reviews youth safety progression → inspects Coach CJ Rahmings' credentials & SWE3 licensing → reads Parent FAQ. |
| **3. The Returning / Active Athlete** | Experienced players transferring or returning to the sport. | Checking game schedules, Dukes Tourney logistics, pre-season camps, and competitive level. | Navigates to Säsongen 2026 / Roadmap → notes camp dates and series format. |
| **4. Sponsors & Municipal Partners** | Local businesses (e.g., Falu Energi & Vatten), kommuner. | Brand alignment with healthy youth development and regional sports culture. | Reviews partner section, contact channels, and community footprint in Falun & Borlänge. |

---

## 4. Information Architecture & Navigation

### 4.1 Global Shell & Navigation
- **Top Utility Banner:**
  - Regional indicator badge: `Amerikansk fotboll i Falun & Borlänge · Nybörjare välkomna`
  - Bilingual switcher: `🇸🇪 dalecarliarebels.se` ↔ `🌐 dalecarliarebels.com`
- **Header:**
  - Left: Dalecarlia Rebels official crest / logo
  - Center/Nav menu: *Hem, Bli en Rebel, Ungdom & Föräldrar, Säsongen 2026, Ledare & Coach, Partners, Kontakt*
  - Right: High-contrast primary CTA button (*"Kom på din första träning"*)
- **Mobile Bottom Navigation Bar (Persistent):**
  - Hem (Home)
  - Träna (Practice / Try-out)
  - Ungdom (Youth & Safety)
  - Säsong (2026 Roadmap)
  - Mer (Full Menu)

---

## 5. Functional Scope & Feature Specifications

### 5.1 Hero Section
- **Headline:** *"VARJE STYRKA HAR EN POSITION."*
- **Subheadline:** Clear articulation that all body types, fitness levels, and experience backgrounds have a dedicated role on the gridiron.
- **Credentials Strip:** 4 distinct trust indicators:
  1. *Anslutna till SWE3*
  2. *Falun & Borlänge hemmaplan*
  3. *Låneutrustning finns (Gratis)*
  4. *Alla åldrar & nivåer*
- **Call-to-Action:** Direct lead to practice intake and role exploration.

### 5.2 Interactive "Hitta din position" (Position Finder Widget)
- **Functional Description:** Interactive attribute selector allowing prospective players to self-identify their athletic strengths.
- **Selectable Traits:**
  - *Snabb & rörlig* (Speed & Agility) → Wide Receiver, Cornerback, Returner
  - *Stark & pålitlig* (Strength & Power) → Offensive Line, Defensive Line
  - *Strategisk & lugn* (Leadership & Vision) → Quarterback, Safety
  - *Träffsäker & explosiv* (Tackling & Explosiveness) → Linebacker, Running Back
- **Output Card:** Explains role in everyday terms, reassures that zero previous experience is needed, and highlights that helmets/pads are loaned free by the club.

### 5.3 2026 Calendar & Roadmap ("Rebels Just Nu")
- **Card 1: Rebels Summer Camp (24–26 Juli)** — Regional intensive training camp focusing on fundamentals, position drills, and camaraderie.
- **Card 2 (Featured): Dukes Tourney 2026 (31 Juli – 2 Augusti)** — Participation in Sweden's largest youth American football tournament at Lillegårdens IP in Skövde. Highlighted with Trophy Gold visual hierarchy.
- **Card 3: Höst 2026 SWE3 Seriespel** — Competitive fixtures, regional match-ups, and game day schedules.

### 5.4 Ungdomssatsning & Föräldraguide (Youth Pathway & Safety)
- **Safety Protocol Breakdown:**
  - Progressive contact model (non-contact flag football / footwork → tackling dummy drills → controlled padded drills → live scrimmage).
  - Certified coaches trained under SWE3 safety standards.
- **Interactive Parent FAQ Accordion:**
  - *Vad krävs för att prova på?* (Träningskläder, fotbollsskor/gympaskor, vattenflaska; resten lånas ut).
  - *Hur fungerar säkerheten och kontakten?* (Stegvis kontakt, fokus på form och teknik).
  - *Vilka åldersgrupper finns i Dalarna?* (U15, U19 och seniorer/motion).
  - *Kostnader och medlemskap?* (Fri prova-på period; förmånliga medlemsavgifter med försäkring via SWE3).

### 5.5 Coaching & Leadership Spotlight
- Dedicated bio card for Head Coach **CJ Rahmings** highlighting player development philosophy, sportsmanship, and Swedish/American football experience.

### 5.6 Klubbnyheter & Sponsor Showcase
- High-visibility press releases (e.g., Falu Energi & Vatten partnership extension, Rookie Day turnout at Kvarnsvedens IP).
- Partner badge strip demonstrating institutional support.

### 5.7 Rapid Lead Intake Form ("Prova-På Anmälan")
- **Form Fields:**
  1. Namn (Full Name)
  2. E-post eller Telefon (Email or Phone number)
  3. Kommun (Falun, Borlänge, or other Dalarna municipality)
  4. Kategori (Ungdom U15/U19, Senior, Dam, Nybörjare, Partner)
  5. Meddelande (Valfritt)
- **Actions:** Instant mail client launch (`mailto:dalecarliarebelsaff@gmail.com`) with pre-filled structured subject and body, plus "Kopiera meddelande" fallback.

---

## 6. Technical & Content Requirements

1. **Responsive Design:** Mobile-first architecture with fluid scaling to tablet and desktop viewports.
2. **Performance Budget:** High contrast ratios (WCAG AAA for text copy), optimized WebP/SVG assets, lightweight DOM.
3. **Bilingual Architecture:** Dynamic language switching framework prepared for direct 1-to-1 parity between Swedish (`.se`) and English (`.com`).
4. **SEO & Metadata:**
   - Primary Keywords: *Amerikansk fotboll Dalarna, Amerikansk fotboll Falun Borlänge, Dalecarlia Rebels AFF, Bli amerikansk fotbollsspelare, SWE3 Dalarna, Prova amerikansk fotboll.*
   - OpenGraph cards utilizing official team crest and apparel mockups.

---

## 7. Release Milestones & Next Steps

- **Milestone 1 (Complete):** Core Design System (`Dalecarlia Midnight Varsity`), official branding integration (`#213567`), and high-fidelity mobile landing screen.
- **Milestone 2 (Current):** Formalized PRD and Project Brief specification approved.
- **Milestone 3 (Upcoming):**
  - Dedicated Desktop viewport optimization for the homepage.
  - Dedicated "Ungdom & Föräldrar" sub-page with downloadable guide.
  - "Säsongen 2026" full schedule & tournament logistics screen.
  - English language localization screen (`dalecarliarebels.com`).