# Visual Audit & Enhancement Plan
## MIPLY Website - Design Standardization

---

## Executive Summary

This plan outlines a comprehensive visual audit of the MIPLY website to ensure all secondary pages match the design standards established in [`index.html`](../index.html). The homepage serves as the gold standard for layout variety, engaging design, typography, color palette, and spacing.

---

## Design Standards from index.html (Gold Standard)

### 1. Clean, Open Backgrounds
- Uses `bg-dot-grid` for subtle texture
- Minimal clutter, generous white space
- Elements breathe freely

### 2. Generous Spacing
- Sections: `py-20`, `py-24`
- Content gaps: `gap-12`, `gap-8`
- Clear breathing room between elements

### 3. Visual Hierarchy
- Clear section headers with badges
- Mix of `font-hand` (Kalam) and `Inter` for typography
- Strategic use of `marker-highlight` and `pen-strike`

### 4. Layout Variety
- Split layouts (grid with col-span)
- Centered content sections
- Grid layouts for cards

### 5. Engaging Design Elements
- `sketch-card` with organic borders
- `sticky-note` for emphasis
- Icons and visual accents

### 6. Color Palette
- Consistent theme colors (blue, red, yellow, dark)
- CSS variables for easy theming

### 7. Minimal Boxing
- Elements breathe, not overly contained
- Cards used purposefully, not excessively

---

## Issues Identified by Page

### what-is-mip.html

#### Issue 1: Tech Stack Section (Lines 247-334)
**Problem:** Too many sticky notes in a row causing potential horizontal scrolling and visual clutter.

**Current Layout:**
```
[Sticky: Data] + [Sticky: Automation] + [Sticky: AI] = [Card: Results]
```

**Proposed Solution:**
- Simplify to a 3-column grid layout
- Use sketch cards instead of sticky notes for better consistency
- Remove the mathematical formula visual for cleaner presentation
- Add visual arrows between cards for flow

#### Issue 2: "The Problem" Section (Lines 76-127)
**Problem:** Nested sketch cards within the main section creates excessive boxing.

**Proposed Solution:**
- Remove outer container boxing
- Use open layout with generous spacing
- Keep individual cards but remove nested structure

#### Issue 3: "The 5 Outcome Lenses" (Lines 168-245)
**Problem:** 5 cards in a grid creates uneven layout.

**Proposed Solution:**
- Rearrange to 3 cards + 2 cards layout (like index.html)
- Add a sticky note break between rows
- Better visual balance

---

### guild.html

#### Issue 1: "What the Guild Is" Section (Lines 62-90)
**Problem:** A sketch card containing other cards - excessive nesting.

**Proposed Solution:**
- Remove outer sketch card wrapper
- Use open layout with centered content
- Keep individual cards but remove nesting

#### Issue 2: Process Section (Lines 92-160)
**Problem:** Complex connecting lines may not translate well to mobile view.

**Proposed Solution:**
- Simplify connecting line implementation
- Use responsive design that hides lines on mobile
- Consider numbered badges instead of lines

#### Issue 3: "Who Thrives" Section (Lines 225-273)
**Problem:** Three cards with potential redundancy in messaging.

**Proposed Solution:**
- Simplify card content
- Use more visual differentiation
- Consider combining related concepts

---

### join.html

#### Issue 1: FAQ Section (Lines 202-273)
**Problem:** Many stacked cards creating visual clutter.

**Proposed Solution:**
- Increase spacing between FAQ items
- Use alternating background colors
- Simplify card styling

#### Issue 2: Application Form (Lines 276-340)
**Problem:** Form wrapped in sticky note makes it feel cramped.

**Proposed Solution:**
- Remove sticky note wrapper
- Use clean, open layout
- Keep form elements with generous spacing

---

### build-log.html

#### Issue 1: Case Study Metric Boxes (Lines 106-123, 214-231)
**Problem:** 4 small metric boxes in a 2x2 grid feel cramped.

**Proposed Solution:**
- Use larger, more prominent metric displays
- Consider horizontal layout or single column
- Add visual emphasis to key metrics

#### Issue 2: Visual Side of Case Studies (Lines 132-165, 240-273)
**Problem:** Nested elements create excessive boxing.

**Proposed Solution:**
- Simplify visual side layout
- Remove unnecessary nested containers
- Use cleaner presentation

---

## Implementation Plan

### Phase 1: what-is-mip.html
1. Simplify Tech Stack section
2. Remove excessive boxing in "The Problem"
3. Improve "The 5 Outcome Lenses" layout

### Phase 2: guild.html
1. Simplify "What the Guild Is" section
2. Fix process section connecting lines
3. Clean up "Who Thrives" section

### Phase 3: join.html
1. Improve FAQ section spacing
2. Simplify application form presentation

### Phase 4: build-log.html
1. Improve case study layouts
2. Simplify visual side of case studies

### Phase 5: Consistency Review
1. Review all pages for consistent spacing
2. Review all pages for consistent visual hierarchy
3. Test responsive behavior
4. Final review

---

## Design Principles to Apply

1. **Open Over Enclosed**: Prefer open layouts over boxed containers
2. **Generous Spacing**: Use `py-20`, `py-24`, `gap-12`, `gap-8`
3. **Visual Hierarchy**: Clear headings, badges, markers
4. **Purposeful Cards**: Use cards only when they add value
5. **Consistent Typography**: Mix of `font-hand` and `Inter`
6. **Engaging Elements**: Sketch cards, sticky notes, icons used strategically
7. **Mobile First**: Ensure all layouts work well on mobile

---

## Success Criteria

- All secondary pages match index.html design standards
- No excessive boxing or nested containers
- Consistent spacing across all pages
- Clean, open backgrounds throughout
- Improved visual hierarchy
- Better mobile responsiveness
- Polished, professional user experience

---

## Files to Modify

1. [`what-is-mip.html`](../what-is-mip.html)
2. [`guild.html`](../guild.html)
3. [`join.html`](../join.html)
4. [`build-log.html`](../build-log.html)

---

## Notes

- No changes needed to [`index.html`](../index.html) (gold standard)
- No changes needed to [`src/style.css`](../src/style.css) (design system is solid)
- Focus is on applying existing design patterns consistently
