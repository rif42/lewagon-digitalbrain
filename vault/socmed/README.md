# Le Wagon Bali — Data &gt; AI Instagram Carousel

6 Instagram carousel slides at 1080 × 1350 px (4:5 aspect ratio).

deepseek api key
`sk-b150fc7d71fa47bf9b64ff5be5e43ce0`

## Files

- `dist/slide-01.png` through `dist/slide-06.png` — final PNG assets ready to post
- `slides/slide-01.html` through `slides/slide-06.html` — individual slide HTML files
- `slides/styles.css` — shared styles, colors, and typography
- `preview.html` — all slides in a grid for quick review
- `render-pngs.py` — Python script that renders each HTML file to PNG using Chrome
- `carousel-data-vs-ai-copy.md` — source copy (text matches exactly)

## How to re-export PNGs

Requires Chrome and Python with Pillow.

```powershell
python render-pngs.py
```

This renders each slide at 1080 × 1500 px in Chrome, then crops the top 1350 px to avoid headless viewport clipping.

## Design notes

- **Palette:** near-black charcoal (#141414) with warm Bali sunset accents in terracotta/coral (#e85d3f), sandy gold (#f4a460), and burnt amber (#d97706).
- **Typography:** Syne ExtraBold for headlines; Space Grotesk for body and labels. Both loaded from Google Fonts.
- **Style:** dark, confident, premium; one idea per slide; minimal text; subtle gradient mesh, noise texture, and geometric accents.
- **Final slide:** includes Le Wagon Bali logo mark, "Apply now" CTA button, and "Link in bio".

## Posting

Upload the 6 PNGs in order to Instagram as a carousel. The first slide works as the cover image. Use the caption from `carousel-data-vs-ai-copy.md`.
