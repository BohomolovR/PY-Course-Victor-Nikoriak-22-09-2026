# /design — Django UI Design Review & Improvements

Apply design recommendations from `DESIGN_FOUNDATIONS.md` to a Django project in this course.

## What this skill does

Reviews the project's templates and CSS against the principles in
`module_5/lesson_HTML_CSS_Bootstrap/DESIGN_FOUNDATIONS.md` and applies targeted fixes.

## Design Checklist (from DESIGN_FOUNDATIONS.md)

### §1 CRAP Principles
- [ ] **Proximity** — related elements grouped with tight spacing; more space *between* groups
- [ ] **Alignment** — no "eyeballed" positioning; use Bootstrap grid / flexbox consistently
- [ ] **Repetition** — same button style, same card style, same color usage across all pages
- [ ] **Contrast** — WCAG minimum 4.5:1 for body text, 3:1 for large text and UI elements

### §1 Typography
- [ ] Body `font-size: 1rem` (16px minimum), `line-height: 1.5–1.6`
- [ ] `-webkit-font-smoothing: antialiased` for crisper rendering
- [ ] Section labels ≥ 0.7rem (never below 11px)
- [ ] Max 2–3 font weights in use

### §1 Visual Hierarchy
- [ ] One `.btn-primary` per page (the main action)
- [ ] Secondary actions use `.btn-outline-secondary`
- [ ] Destructive actions use `.btn-outline-danger` (not `.btn-danger`)
- [ ] Max 3 levels of visual hierarchy per view

### §2 Information Architecture
- [ ] Breadcrumbs on detail pages (`<nav aria-label="breadcrumb">`)
- [ ] Active nav state (`request.resolver_match.url_name`)
- [ ] Empty states with clear CTA button (not a blank page)

### §6 Forms
- [ ] Labels always visible (never placeholder-only)
- [ ] Required fields marked with `<span class="text-danger">*</span>`
- [ ] Error state uses Bootstrap `is-invalid` + `invalid-feedback`
- [ ] Cancel button is NOT the same color as Save

### §7 Dashboard
- [ ] KPI / count indicator near the section title
- [ ] Empty state component with actionable CTA
- [ ] Sidebar shows active state for current page

### §8 Common Mistakes to Avoid
- [ ] No layout shift on hover (no `padding-left` animation that moves content)
- [ ] No `container` inside already-padded `.main-content` (double-padding)
- [ ] No inline color values for semantic states — use CSS variables
- [ ] No logic in templates beyond simple conditionals

## How to apply

1. Read the project's `app.css` and main templates
2. Run through the checklist above
3. Fix issues in priority order:
   - **High:** contrast failures, missing labels, no empty state
   - **Medium:** typography, hover effects, visual hierarchy
   - **Low:** spacing tweaks, badge counts, footer
4. Do NOT rewrite everything — apply minimal targeted fixes
5. Test each URL after changes

## Design tokens for dark theme (Notes App)

```css
--text-secondary: #9a9ac0;   /* WCAG 4.5:1 on #1e1e2e */
--accent: #7c6efa;            /* primary interactive color */
--card-bg: #1e1e2e;
--sidebar-bg: #16161e;
```

## Bootstrap utility reminders

- Spacing scale: `0=0` `1=0.25rem` `2=0.5rem` `3=1rem` `4=1.5rem` `5=3rem`
- Text contrast helpers: `.text-body-secondary` (Bootstrap 5.3 dark mode aware)
- Focus ring: `.focus-ring` or custom `outline: 2px solid var(--accent)`
- Card body padding default: `1rem` — use `p-3` / `p-4` to control
