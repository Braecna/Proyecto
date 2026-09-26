---
name: Cognitive Flow
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
  on-tertiary-fixed: '#380d00'
  on-tertiary-fixed-variant: '#802a00'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
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
  unit: 4px
  container-max: 1280px
  gutter: 24px
  margin-desktop: 40px
  margin-mobile: 16px
  stack-sm: 8px
  stack-md: 16px
  stack-lg: 32px
---

## Brand & Style

The design system is centered on **Minimalism** and **Modern Corporate** aesthetics, specifically tailored for a high-performance online learning environment. The target audience includes professionals and lifelong learners who require a distraction-free interface that prioritizes content absorption and cognitive ease.

The UI evokes a sense of clarity, intelligence, and progress. It utilizes expansive whitespace, a refined color palette, and a logical "card-based" architecture to organize complex course data into digestible modules. High-quality execution of subtle details—such as micro-interactions and consistent rhythmic spacing—builds trust and establishes the platform as a premium educational tool.

## Colors

This design system utilizes a structured blue hierarchy to drive functional clarity.
- **Primary (#1E40AF):** Reserved for high-emphasis actions, navigation headers, and primary branding elements.
- **Secondary (#3B82F6):** Used for interactive states, progress indicators, and link text.
- **Surface & Backgrounds:** A core white (#FFFFFF) is used for content cards, while a soft neutral gray (#F8FAFC) provides the base canvas for the application to create subtle depth.
- **Feedback:** Success (Green), Warning (Amber), and Error (Red) should be desaturated to maintain the professional tone.

## Typography

The design system leverages **Inter** for its exceptional legibility and systematic feel. The type scale is strictly enforced to ensure a clear information hierarchy:
- Use **Display** styles for landing page hero sections only.
- Use **Headline** styles for course titles and module headers.
- **Body-md** is the default for all instructional text.
- **Label** styles are specifically for metadata, badges, and small UI hints.
Vertical rhythm is maintained by ensuring all line-heights align to a 4px baseline grid.

## Layout & Spacing

The layout follows a **Fluid Grid** model with a maximum width constraint of 1280px for readability in long-form learning content.
- **Desktop (1024px+):** 12-column grid, 24px gutters, 40px side margins.
- **Tablet (768px - 1023px):** 8-column grid, 20px gutters, 24px side margins.
- **Mobile (Up to 767px):** 4-column grid, 16px gutters, 16px side margins.

A spacing scale based on 4px increments (4, 8, 12, 16, 24, 32, 48, 64) ensures consistent vertical rhythm. Content cards should utilize 'stack-lg' (32px) for internal padding to maintain the minimalist feel.

## Elevation & Depth

This design system uses **Tonal Layers** supplemented by **Ambient Shadows** to define the z-axis. 

1.  **Level 0 (Base):** The #F8FAFC background.
2.  **Level 1 (Cards/Containers):** White (#FFFFFF) surfaces with a very subtle, diffused shadow (0px 2px 4px rgba(0,0,0,0.05)) and a 1px border (#E2E8F0).
3.  **Level 2 (Hover States/Dropdowns):** Elevated cards use a more pronounced shadow (0px 10px 15px -3px rgba(0,0,0,0.1)) to indicate interactivity.
4.  **Level 3 (Modals):** High-contrast shadows with a backdrop blur (8px) on the Level 0 layer to focus attention.

## Shapes

The shape language is **Soft** and systematic. A standard 0.25rem (4px) radius is applied to small components like inputs and checkboxes. Larger components like course cards and hero sections utilize `rounded-lg` (8px) or `rounded-xl` (12px) to soften the professional aesthetic and make the environment feel approachable.

## Components

- **Buttons:** Primary buttons use a solid #1E40AF fill with white text. Secondary buttons use a #E2E8F0 ghost style or #3B82F6 outline. Padding is 12px 24px for standard actions.
- **Course Cards:** White background, 8px corner radius, 1px border. Contain a course thumbnail, title (Headline-sm), and a progress indicator.
- **Badges (Course Levels):** Small, pill-shaped labels with low-opacity backgrounds (e.g., light blue background with dark blue text). Use 'label-sm' typography.
- **Progress Indicators:** Horizontal 8px height bars. The track is #E2E8F0 and the fill is #3B82F6. Use a smooth CSS transition for percentage updates.
- **Input Fields:** 1px solid #E2E8F0 borders that transition to 1px solid #3B82F6 on focus with a 2px soft blue outer glow.
- **Lists:** Clean rows with 16px vertical padding, separated by 1px #E2E8F0 dividers. Iconography should be minimalist (24px size).