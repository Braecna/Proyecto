---
name: Cognitive Clarity
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#444653'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#757684'
  outline-variant: '#c4c5d5'
  surface-tint: '#3755c3'
  primary: '#00288e'
  on-primary: '#ffffff'
  primary-container: '#1e40af'
  on-primary-container: '#a8b8ff'
  inverse-primary: '#b8c4ff'
  secondary: '#0058be'
  on-secondary: '#ffffff'
  secondary-container: '#2170e4'
  on-secondary-container: '#fefcff'
  tertiary: '#611e00'
  on-tertiary: '#ffffff'
  tertiary-container: '#872d00'
  on-tertiary-container: '#ffa583'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#dde1ff'
  primary-fixed-dim: '#b8c4ff'
  on-primary-fixed: '#001453'
  on-primary-fixed-variant: '#173bab'
  secondary-fixed: '#d8e2ff'
  secondary-fixed-dim: '#adc6ff'
  on-secondary-fixed: '#001a42'
  on-secondary-fixed-variant: '#004395'
  tertiary-fixed: '#ffdbce'
  tertiary-fixed-dim: '#ffb59a'
  on-tertiary-fixed: '#370e00'
  on-tertiary-fixed-variant: '#802a00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
  surface-card: '#FFFFFF'
  surface-base: '#F8FAFC'
  border-subtle: '#E2E8F0'
  text-primary: '#191C1E'
  text-muted: '#444653'
  feedback-error: '#BA1A1A'
  feedback-success: '#15803D'
  feedback-warning: '#B45309'
typography:
  display-lg:
    fontFamily: Inter
    fontSize: 48px
    fontWeight: '700'
    lineHeight: 56px
    letterSpacing: -0.02em
  display-lg-mobile:
    fontFamily: Inter
    fontSize: 32px
    fontWeight: '700'
    lineHeight: 40px
    letterSpacing: -0.01em
  headline-md:
    fontFamily: Inter
    fontSize: 24px
    fontWeight: '600'
    lineHeight: 32px
    letterSpacing: -0.01em
  headline-sm:
    fontFamily: Inter
    fontSize: 20px
    fontWeight: '600'
    lineHeight: 28px
  body-lg:
    fontFamily: Inter
    fontSize: 18px
    fontWeight: '400'
    lineHeight: 28px
  body-md:
    fontFamily: Inter
    fontSize: 16px
    fontWeight: '400'
    lineHeight: 24px
  body-sm:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: 20px
  label-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '500'
    lineHeight: 16px
    letterSpacing: 0.05em
  label-sm:
    fontFamily: Inter
    fontSize: 12px
    fontWeight: '600'
    lineHeight: 16px
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  gutter: 1.5rem
  margin: 2.5rem
  margin-mobile: 1rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 1.5rem
  space-xl: 2rem
---

## Brand & Style

The design system is centered on **Minimalism** and **Modern Corporate** aesthetics, engineered specifically for high-efficiency professional education, technical certifications, and corporate upskilling. It addresses the needs of ambitious professionals, engineers, and career-switchers who require an interface that minimizes cognitive load and elevates focus during intensive study sessions.

The visual language communicates authority, structural discipline, and momentum. It achieves this through precise whitespace distribution, crisp geometric typography, and an architecture organized into modular, digestible units. The tone is deliberate, objective, and dependable—eschewing playful clutter in favor of clinical clarity, reliable micro-interactions, and high contrast for deep instructional retention.

## Colors

The palette establishes an intellectual hierarchy using deep royal blues paired with high-luminance canvas neutrals to preserve optical comfort during extended reading:

- **Primary (`#1E40AF`):** The primary anchor for key conversion points, top-level navigation, active progress milestones, and prominent action buttons.
- **Secondary (`#3B82F6`):** Drives interactive states, progress indicator fills, active tabs, inline text anchors, and secondary visual accents.
- **Tertiary (`#872D00`):** An earthy amber-rust accent reserved for urgent certification deadlines, critical exam notices, or live session pings.
- **Neutral (`#F8FAFC`):** The canvas foundational neutral, providing a soft, glare-free background that contrasts seamlessly against pure white surfaces.

### Neutral and Surface Roles
- **Base Canvas (`#F8FAFC`):** Default viewport background that creates depth under components.
- **Card Surfaces (`#FFFFFF`):** High-priority learning units, active modules, and workspace containers.
- **Dividers & Outlines (`#E2E8F0`):** Low-contrast boundaries that separate density without visual friction.
- **Text Hierarchy:** Primary body and headline copy strictly uses `#191C1E`, while supporting metadata and helper labels rely on `#444653`.

## Typography

The design system implements **Inter** across all typographic tiers to ensure legibility across dense curricula, code snippets, and technical lesson plans.

- **Baseline System:** All line heights conform strictly to a 4px baseline grid.
- **Display Scales:** Reserved for marketing hero banners, certificate completion overviews, and onboarding landings. On mobile screens, display text falls back to `display-lg-mobile` to prevent awkward line breaks.
- **Headlines:** Used exclusively for module headings, lesson track identifiers, and analytical dashboards.
- **Body:** Standard body text is pinned to `body-md` (16px / 24px) for optimized scanning rhythm, while `body-sm` accommodates metadata and secondary instructional callouts.
- **Labels:** Uppercase tracking (`0.05em`) is applied to `label-md` for badges and status counters, guaranteeing immediate distinction from continuous prose.

## Layout & Spacing

The layout architecture relies on a **Fluid Grid** model bound by an absolute maximum container width of 1280px to preserve comfortable line lengths for instructional reading and code environments.

### Breakpoints & Grids
- **Desktop (1024px+):** 12-column layout, 24px (`1.5rem`) gutters, 40px (`2.5rem`) outer canvas margins. Sidebars for course navigation span 3 columns, leaving 9 columns for active media and transcript content.
- **Tablet (768px - 1023px):** 8-column layout, 20px gutters, 24px outer canvas margins. Curricula draw-downs convert to slide-over panels.
- **Mobile (Up to 767px):** 4-column layout, 16px gutters, 16px (`1rem`) outer canvas margins. Content stacks vertically into full-width cards.

### Spacing Scale
Layout spaces conform to a 4px unit multiplier:
- `space-xs` (4px): Micro-spacing between icon badges and adjacent inline labels.
- `space-sm` (8px): Gaps within form controls, button groups, and compact tags.
- `space-md` (16px): Structural gutters within list rows, cards, and input clusters.
- `space-lg` (24px): Standard internal padding for containers and course modules.
- `space-xl` (32px): Deep padding for primary exam cards and section separation.

## Elevation & Depth

Visual depth is communicated primarily through **Tonal Layers** combined with **Ambient Diffused Shadows** and subtle hairline strokes, avoiding heavy drops to preserve a corporate, clean atmosphere.

- **Level 0 (Canvas Base):** Rendered with neutral `#F8FAFC`. Zero elevation, zero shadows.
- **Level 1 (Cards, Tables & Panels):** Pure white (`#FFFFFF`) containers resting on `#F8FAFC`, reinforced by a 1px solid border (`#E2E8F0`) and an ambient shadow: `0 1px 3px 0 rgba(0, 0, 0, 0.04), 0 1px 2px 0 rgba(0, 0, 0, 0.02)`.
- **Level 2 (Interactive Hover & Floating Controls):** Course cards on hover, popovers, and sticky navigation headers elevate slightly with: `0 10px 15px -3px rgba(0, 0, 0, 0.06), 0 4px 6px -2px rgba(0, 0, 0, 0.03)`.
- **Level 3 (Modals & Focus Dialogs):** High-priority overlays use an ambient drop: `0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)`, combined with an 8px backdrop blur (`backdrop-filter: blur(8px)`) over `#00000040`.

## Shapes

The shape system utilizes a **Soft** profile (roundedness level `1`), balancing technical precision with modern accessibility.

- **Default Radius (4px / `0.25rem`):** Applied systematically to small utility controls, text fields, checkboxes, data tables, and inline code snippets.
- **Container Radius (8px / `0.5rem` / `rounded-lg`):** Applied to course cards, video player wrappers, code exercise panels, and modal containers.
- **Pill Radius (`9999px` / `rounded-full`):** Reserved exclusively for dynamic progress badges, skill tags, live status indicators, and circular avatar containers.

## Components

### Buttons
- **Primary:** Background `#1E40AF`, text `#FFFFFF`, 4px radius. 12px vertical and 24px horizontal padding (`space-sm` to `space-lg`). Interactive hover transitions to `#1E3A8A` with a 150ms ease curve.
- **Secondary:** Transparent fill with a 1px border in `#E2E8F0`, text `#1E40AF`. Hover state shifts background to `#F1F5F9`.
- **Tertiary / Ghost:** Text `#3B82F6`, zero border, zero background. Padding 8px 12px. Used for breadcrumbs, skips, and secondary module collapse triggers.

### Form Inputs & Selects
- 1px continuous border in `#E2E8F0` on white background, 4px border radius.
- Height fixed at 40px for single-line inputs with 8px 12px internal padding.
- **Focus State:** Border changes directly to `#3B82F6` accompanied by a 2px semi-transparent ring (`rgba(59, 130, 246, 0.2)`).

### Course & Module Cards
- White surface `#FFFFFF`, 1px border `#E2E8F0`, 8px corner radius.
- Contains course cover thumbnail (16:9 ratio), category badge, course title in `headline-sm`, mentor signature, and lesson count.
- Padding inside is consistently 24px (`space-lg`).

### Progress Trackers & Meters
- Linear bars have a fixed 8px height, rounded to 4px.
- Track utilizes `#E2E8F0`, while the completed progress bar uses `#3B82F6` with an ease-out transition on percentage update.
- Stepper components display numerical indicators inside 24px circular badges with 1px border.

### Badges & Status Chips
- Pill-shaped (`rounded-full`) with 4px vertical and 10px horizontal padding.
- Color combinations use 10% opacity tints: Technical tracks use `#DBEAFE` background with `#1E40AF` text; active alerts use `#FEE2E2` with `#BA1A1A` text.
- Text uses `label-sm` font weight (600).

### Lists & Curriculum Trees
- Flat structure with alternating row hover states (`#F8FAFC`).
- Separated by hairline 1px dividers (`#E2E8F0`).
- Left-aligned status indicators (check circle for completed, lock icon for upcoming modules) scaled strictly to 20px.