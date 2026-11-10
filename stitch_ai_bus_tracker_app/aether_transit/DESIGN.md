---
name: Aether Transit
colors:
  surface: '#f8f9ff'
  surface-dim: '#cbdbf5'
  surface-bright: '#f8f9ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#eff4ff'
  surface-container: '#e5eeff'
  surface-container-high: '#dce9ff'
  surface-container-highest: '#d3e4fe'
  on-surface: '#0b1c30'
  on-surface-variant: '#434655'
  inverse-surface: '#213145'
  inverse-on-surface: '#eaf1ff'
  outline: '#737686'
  outline-variant: '#c3c6d7'
  surface-tint: '#0053db'
  primary: '#004ac6'
  on-primary: '#ffffff'
  primary-container: '#2563eb'
  on-primary-container: '#eeefff'
  inverse-primary: '#b4c5ff'
  secondary: '#565e71'
  on-secondary: '#ffffff'
  secondary-container: '#dbe2f9'
  on-secondary-container: '#5c6477'
  tertiary: '#005e6e'
  on-tertiary: '#ffffff'
  tertiary-container: '#00788c'
  on-tertiary-container: '#d7f6ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dbe1ff'
  primary-fixed-dim: '#b4c5ff'
  on-primary-fixed: '#00174b'
  on-primary-fixed-variant: '#003ea8'
  secondary-fixed: '#dbe2f9'
  secondary-fixed-dim: '#bfc6dc'
  on-secondary-fixed: '#141b2c'
  on-secondary-fixed-variant: '#3f4759'
  tertiary-fixed: '#acedff'
  tertiary-fixed-dim: '#4cd7f6'
  on-tertiary-fixed: '#001f26'
  on-tertiary-fixed-variant: '#004e5c'
  background: '#f8f9ff'
  on-background: '#0b1c30'
  surface-variant: '#d3e4fe'
typography:
  headline-xl:
    fontFamily: Inter
    fontSize: 36px
    fontWeight: '700'
    lineHeight: 44px
    letterSpacing: -0.02em
  headline-xl-mobile:
    fontFamily: Inter
    fontSize: 28px
    fontWeight: '700'
    lineHeight: 36px
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.015em
  headline-md:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '600'
    lineHeight: 24px
    letterSpacing: '0'
  body-lg:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
    letterSpacing: '0'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
    letterSpacing: '0'
  body-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '400'
    lineHeight: 16px
    letterSpacing: 0.01em
  label-lg:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '600'
    lineHeight: 20px
    letterSpacing: 0.01em
  label-md:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
    letterSpacing: 0.02em
  label-sm:
    fontFamily: Inter
    fontSize: 10px
    fontWeight: '700'
    lineHeight: 14px
    letterSpacing: 0.04em
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  gutter: 1rem
  gutter-tablet: 1.5rem
  gutter-desktop: 2rem
  margin: 1rem
  margin-tablet: 2rem
  margin-desktop: 3rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style
The design system delivers an intelligent, frictionless transit experience engineered for urban commuters navigating complex mobility networks. Rooted in a high-clarity, futuristic aesthetic, the interface blends structural minimalism with functional glassmorphism to present real-time transit telemetry, predictive arrival vectors, and dynamic crowding analytics without cognitive overload.

The visual tone is precise, forward-looking, and reliable. Visual density is strictly managed to privilege critical navigational decisions: high-contrast telemetry indicators, fluid spatial awareness, and predictive status updates. Glassmorphic floating surfaces interface over dynamic map canvas layers, maintaining situational awareness while ensuring legibility under variable outdoor lighting conditions.

## Colors
The palette balances infrastructural clarity with sharp predictive signals. Base canvas structures utilize cool, low-strain neutrals (`#F8FAFC`, `#F1F5F9`) to offset map noise, while deep navy (`#101828`) anchors typographic hierarchy and prominent navigation surfaces.

### Semantic Transit State Tokens
- **Operational / Low Density:** `#10B981` (Emerald). Applied to on-time schedules, optimal passenger loads, and active signal confirmations.
- **Advisory / Moderate Density:** `#F59E0B` (Amber). Applied to transit delays under 10 minutes, intermediate fleet capacity, and reroute warnings.
- **Disruption / High Density:** `#EF4444` (Rose). Reserved strictly for route cancellations, severe delays, full vehicle capacity, and incident flags.
- **Predictive Telemetry:** `#06B6D4` (Cyan). Applied to AI-generated arrival predictions, machine-learning path vectors, and live transit beacon pulses.

## Typography
Typographic rules emphasize rapid scannability under motion. Inter is deployed across all levels, utilizing tight tracking on headline roles to compress schedule headers, while maintaining neutral tracking across telemetry and label tokens to preserve legibility at glancing distances. Numeric data displays (countdown timers, vehicle route numbers, passenger tallies) should enforce tabular lining figures (`font-variant-numeric: tabular-nums`) to prevent layout shift during real-time telemetry updates.

## Layout & Spacing
The layout architecture follows an Android-first mental model prioritizing single-handed thumb-zone operation. The primary navigational anchor is a persistent bottom navigation bar coupled with layered bottom sheets over a full-bleed map viewport. 

- **Mobile (<600px):** Single-column fluid spatial model. Safe area bottom padding of 16px beneath the bottom navigation container. Map UI controls float 16px above docked sheets.
- **Tablet (600px - 1024px):** Dual-surface layout. The map canvas remains full-bleed; transit feeds, route schedules, and live telemetry decouple into a anchored 380px floating sheet on the leading edge.
- **Desktop / Terminal (>1024px):** Split-view system. Left-hand side anchored navigation dock (420px), persistent global map telemetry in main viewport.

## Elevation & Depth
Depth hierarchy separates dynamic spatial data from tactical operational controls:

- **Surface Tier 0 (Map Floor):** Non-elevated, full-canvas interactive background layer.
- **Surface Tier 1 (Docked Containers & Backgrounds):** Flat `#F8FAFC` or `#FFFFFF` planes framed by ultra-low contrast borders (`1px solid rgba(226, 232, 240, 0.8)`).
- **Surface Tier 2 (Floating Action Items & Cards):** Offset soft elevation: `box-shadow: 0 4px 20px -2px rgba(16, 24, 40, 0.06), 0 2px 6px -1px rgba(16, 24, 40, 0.04)`.
- **Surface Tier 3 (Glassmorphic Bottom Sheets):** Semi-transparent background `rgba(255, 255, 255, 0.88)` with `backdrop-filter: blur(16px)` and a top rim stroke `1px solid rgba(255, 255, 255, 0.6)`. Shadow: `0 -8px 32px -4px rgba(16, 24, 40, 0.08)`.
- **Surface Tier 4 (Overlays, Modals, Urgent Disruptions):** Deep focus elevation: `box-shadow: 0 20px 40px -8px rgba(16, 24, 40, 0.16)`.

## Shapes
Geometry uses clean, organic curvature to soften technical data presentation. Base cards, bottom sheets, and route cards adhere strictly to `rounded-2xl` (1rem). Small interactive nodes (status indicators, crowd level pills, predictive tags) utilize complete pill geometry (`rounded-full`) to immediately differentiate informative meta-chips from structural container cards.

## Components

### Buttons
- **Primary Action:** Background `#2563EB`, text `#FFFFFF`, 12px vertical padding, 20px horizontal padding, `rounded-xl`. Elevation: soft ambient shadow matching Tier 2. Active state: compressed scale (`scale(0.98)`).
- **Secondary Action:** Background `#F1F5F9`, text `#101828`, border `1px solid #E2E8F0`. Hover state triggers background shift to `#E2E8F0`.
- **Ghost Utility:** Borderless, text `#64748B`, reserved for map layer toggles and dismiss triggers.

### Transit Status Tags & Badges
- Pill-shaped (`rounded-full`) with uppercase tracking (`label-sm`).
- **Low Crowding / On Time:** Background `rgba(16, 185, 129, 0.12)`, text `#047857`, border `1px solid rgba(16, 185, 129, 0.2)`.
- **Delay / Moderate:** Background `rgba(245, 158, 11, 0.12)`, text `#B45309`, border `1px solid rgba(245, 158, 11, 0.2)`.
- **Severe Disruption:** Background `rgba(239, 68, 68, 0.12)`, text `#B91C1C`, border `1px solid rgba(239, 68, 68, 0.2)`.
- **AI Predicted:** Background `rgba(6, 182, 212, 0.12)`, text `#0E7490`, leading Sparkle/Pulse icon.

### Route Cards
- Background `#FFFFFF` with `rounded-2xl` contour and Tier 2 soft shadow.
- Interior layout incorporates route route designation badge (high-contrast `#101828` badge with bold white text), real-time countdown block, and live progress timeline bar.

### Glassmorphic Bottom Sheets
- Docked to screen bottom with handle grab bar (32px × 4px, `#CBD5E1`, centered 8px from top).
- Backdrop blur `16px`, background `rgba(255, 255, 255, 0.88)`.
- Snapping points at 25% (peeking ETA), 50% (route timeline), and 90% (full line interchange details).

### Interactive Transit Markers
- Circular pin design: 36px diameter with a 3px outer white boundary and contextual status core.
- Vehicle directional arrows embedded via SVG rotation.
- Predictive AI vehicles include a concentric animated pulse ring rendered in tertiary Cyan (`#06B6D4`).

### Input Fields & Search Bars
- Floating pill-shape or `rounded-xl` container with subtle border (`#E2E8F0`), interior background `#FFFFFF`, leading transit lens icon, trailing voice or clear icon.
- Focus state switches border to `#2563EB` with an ambient outer glow (`box-shadow: 0 0 0 3px rgba(37, 99, 235, 0.15)`).