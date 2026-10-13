# kotoSay · Pitch Deck

Pitch deck for the **Tokyo Global Innovation Challenge 2026**. Built from
`docs/Tokyo Global Innovation Challenge - Idea Brainstroming 5.docx`.

**To present, open `index.html`** in any modern browser (Chrome, Edge, Safari or
Firefox). It's one self-contained file with no internet connection needed, so you can
email it, put it on a USB stick or upload it anywhere.

## Presenting

| Action | How |
| --- | --- |
| Next / previous | `→` `←`, `Space` / `Shift+Space`, `Page Down` / `Page Up`, or a presenter clicker |
| Swipe | Drag or flick the slide (touch, mouse or trackpad). It follows your finger and springs into place |
| First / last slide | `Home` / `End` |
| Full screen | `F`, or the button in the floating bar |
| Jump to a slide | Click a dot in the floating bar, or open `index.html#9` (slide 9) |

The floating control bar hides after a few seconds. Move the mouse to bring it back.

**Demo video (slide 3):** it starts from the beginning every time you reach the slide and
pauses when you leave. The first play has sound, so you hear kotoSay speak the translation
at about 17 seconds. After that it loops on mute so it doesn't keep talking over you.
Use the speaker button below the phone to turn sound on or off, and click the video to
pause it. Browsers only allow sound after you've pressed a key or clicked on the page. If
you open the deck straight onto slide 3, it plays muted until you press the speaker
button.

The avatar recording plays in a second phone on the right of slide 3. It stays
muted and pauses when you leave the slide. Click either recording to pause or
resume it. With reduced motion enabled, use each phone’s play button.

## Saving as a PDF

Open `index.html` in Chrome or Edge, press `Ctrl+P` and choose **Save as PDF**.
Set **Margins: None** and turn on **Background graphics**. You get one slide per
page, 13 pages in 16:9.

## Folder structure

```
Tokyo Global Innovative Challenge/
├── index.html          ← the deck (generated: don't edit by hand)
├── build.py            ← bundles src/ into index.html
├── README.md
├── src/
│   ├── template.html   ← page shell + floating controls
│   ├── slides/         ← one file per slide, in deck order
│   │   ├── 01-social-issue.html
│   │   ├── 02-stories.html
│   │   ├── 03-hero.html
│   │   ├── 04-how-it-works.html
│   │   ├── 05-impact.html
│   │   ├── 06-validation.html
│   │   ├── 07-traction.html
│   │   ├── 08-market.html
│   │   ├── 09-competition.html   ← comparison matrix
│   │   ├── 10-business-model.html
│   │   ├── 11-growth.html
│   │   ├── 12-team.html
│   │   └── 13-closing.html
│   ├── assets/
│   │   ├── sources/    ← source screenshots shown on slide 2 (inlined at build)
│   │   ├── team/       ← team photos shown on slide 12 (inlined at build)
│   │   └── video/      ← demo recording + poster frame for slide 3 (inlined at build)
│   ├── styles/
│   │   ├── tokens.css  ← colours, fonts, radii
│   │   ├── base.css    ← type scale, bold-keyword style
│   │   ├── deck.css    ← stage, controls, print
│   │   └── slides.css  ← per-slide layouts
│   └── scripts/
│       ├── spring.js   ← spring physics, momentum, rubber-banding
│       └── deck.js     ← navigation, gestures, keyboard
└── docs/
    ├── Tokyo Global Innovation Challenge - Idea Brainstroming 5.docx
    ├── competitor-notes.md   ← sources behind the comparison matrix
    └── sources.md            ← full references for the stories on slide 2
```

## Editing

1. Change the files in `src/`. Slide text is in `src/slides/`, and slides are
   ordered by their file-name prefix (`01-`, `02-` and so on).
2. Rebuild: `python build.py`. To rebuild automatically on every save, run
   `python build.py --watch`. It needs only Python 3.8+, with no packages.
3. Refresh `index.html` in the browser.

Writing conventions used in the slides:

- **Bold keywords:** wrap them in `<strong>` sparingly in body text. Headlines
  stay white so they read as complete thoughts.
- **Entrance animation:** add `data-reveal` to an element. `style="--i:2"` staggers it
  (higher means later).
- **Images:** put them in `src/assets/` and reference them as `src="assets/…"`.
  `build.py` embeds them into `index.html`, so it still works as a single file.
- **Sizes** are in `cqw` (1% of the slide width), so the slide scales as one piece.
  At the 1600 × 900 reference, `1cqw` is 16px.

## Design notes

Uses Apple's interface principles (WWDC *Designing Fluid Interfaces*):

- Slide changes run on a **spring** (damping 1.0, response 0.42s), not a fixed-length
  animation. You can grab a moving slide or reverse direction at any moment.
- Releasing a drag **projects momentum** to choose the next slide and passes your
  finger's speed to the spring. The first and last slides **rubber-band** at the edges.
- Controls float on a **translucent material** and react on press.
- Type is size-specific: tight negative tracking on big headings, neutral on body text,
  with the system font (SF Pro on Apple devices, Segoe UI on Windows).
- **Accessibility:** "Reduce motion" switches slides to a cross-fade. "Reduce
  transparency" and "Increase contrast" are respected. Every text colour meets 4.5:1
  contrast.
- Two colours carry meaning throughout: **vermilion `#f25c3b`** is sign → voice (and
  the brand), and **teal `#1aa898`** is text → sign (the avatar's reply).

## chee visual refresh

The 13-slide refresh keeps kotoSay’s black, vermilion and teal identity. It adds brighter source images and team portraits, shorter headlines, visible validation metrics, an estimate with explicit market assumptions, a simpler roadmap, and a primary pilot-partner ask. The opening pairs a soft 3D hand with an editable 21-point MediaPipe overlay. Navigation, reduced motion, the real demo video and self-contained offline export are preserved.

Three soft 3D stickers illustrate everyday access and two-way communication. Their saved files and complete generation prompts are in [src/assets/stickers/README.md](src/assets/stickers/README.md). They are decorative illustrations and do not replace product or community evidence. No external fonts or runtime dependencies were added.
