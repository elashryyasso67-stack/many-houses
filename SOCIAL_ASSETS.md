# Social Media Assets Specs

**Brand Colors:** Gold `#D4AF37` | White `#FFFFFF` | Dark `#111111` | Light Gold `#FFF8E7`
**Fonts:** Playfair Display (headings) | Inter (body)
**Icons:** Material Symbols (same as app)

---

## Asset Checklist (Priority Order)

### 1. LinkedIn Post (1200×628) — *Highest Priority*
**Use:** Competition announcement, demo day recap, team intro
**Variants:**
- A: "We're competing at [COMPETITION NAME]!" + app screenshot
- B: "The problem with Egyptian real estate" + problem/solution carousel
- C: Team photo + "Meet the builders"

### 2. Twitter/X Post (1600×900) — *High Priority*
**Use:** Live-tweeting demo, thread about market, video clips
**Variants:**
- A: Single image + hook tweet
- B: Thread starter (1/🧵) with app GIF
- C: Video clip (see video demo spec)

### 3. Instagram Feed Post (1080×1080) — *Medium Priority*
**Use:** Visual storytelling, property showcase, behind-the-scenes
**Variants:**
- A: Hero property shot + "Verified listings in 10 cities"
- B: Carousel: Problem → Solution → Demo → CTA
- C: Team/office candid

### 4. Instagram Story (1080×1920) — *Medium Priority*
**Use:** Day-of-competition updates, polls, countdown
**Variants:**
- A: Countdown timer sticker
- B: "Swipe up" to demo (when deployed)
- C: Q&A sticker about Egyptian real estate

### 5. Facebook Post (1200×630) — *Lower Priority*
**Use:** Community groups, Egyptian expat networks
**Variants:**
- A: Arabic + English bilingual post
- B: Property photo album (carousel)

### 6. WhatsApp Share Image (800×800) — *Niche but High Impact*
**Use:** Direct sharing in family/friend groups (huge in Egypt)
**Content:** One strong property photo + "Verified listings. No hidden fees." + QR code to demo

---

## Design Templates (Canva/Figma Specs)

### Template 1: Hero Announcement
```
┌─────────────────────────────────────┐
│  [Logo]                    [Competition Badge]  │
│                                     │
│  ┌─────────────────────────────┐   │
│  │    APP SCREENSHOT/GIF       │   │
│  │   (Home page with props)    │   │
│  └─────────────────────────────┘   │
│                                     │
│  manyhouses                         │
│  Verified Egyptian Real Estate      │
│                                     │
│  [CTA Button] Explore Properties    │
│                                     │
│  #EgyptRealEstate #PropTech #Startup│
└─────────────────────────────────────┘
```

### Template 2: Problem/Solution Carousel (LinkedIn/Twitter)
**Slide 1:** "Finding a home in Egypt shouldn't be this hard" + 😤 emoji
**Slide 2:** "Fake listings on Facebook" → Screenshot of messy group
**Slide 3:** "Hidden fees at signing" → 💸 emoji
**Slide 4:** "Enter manyhouses" + Logo reveal
**Slide 5:** "Verified • National • Transparent" + 3 icons
**Slide 6:** App demo GIF
**Slide 7:** "We're at [COMPETITION NAME] — come see us!" + Booth #/Link

### Template 3: Metric Flex
```
┌─────────────────────────────────────┐
│        10+ Cities Covered           │
│        4 Property Types             │
│        0 Hidden Fees                │
│        12 Sample Listings           │
│                                     │
│        [App Screenshot]             │
│                                     │
│        manyhouses.com               │
└─────────────────────────────────────┘
```

---

## Copy Bank (Ready-to-Use)

### Headlines (Pick One)
- "Your trusted partner for Egyptian real estate"
- "Verified listings. Transparent pricing. All of Egypt."
- "Stop scrolling Facebook groups. Start finding homes."
- "From Cairo to Siwa — one search, verified results."
- "The way Egyptians buy property just changed."

### Short Hooks (Twitter/Threads)
- "Egypt needs 12M homes by 2030. Buyers still use Facebook groups. 🤯 We built manyhouses to fix this."
- "Verified listings. Zero hidden fees. 10 Egyptian cities. One app. 🇪🇬"
- "Just generated a contract in-app for a villa in Hurghada. No agent fees. No surprises. This is manyhouses."

### Hashtag Sets
**Primary:** #EgyptRealEstate #PropTechEgypt #ManyHouses #VerifiedListings
**Competition:** #[COMPETITIONNAME] #DemoDay #StartupEgypt
**Niche:** #CairoRealEstate #RedSeaProperty #NewCapital #ExpatEgypt
**Arabic:** #عقارات_مصر #شقق_للبيع #فيلات_مصر #العاصمة_الإدارية

### Arabic Copy (For Local Reach)
- **Headline:** "شريكك الموثوق في العقارات المصرية"
- **Subhead:** "إعلانات موثقة • أسعار شفافة • تغطية وطنية"
- **CTA:** "ابحث عن عقارك الآن"

---

## Visual Asset Sources

### App Screenshots Needed
1. **Home page** — Full grid with 3 properties visible (desktop)
2. **Details page** — Gallery open + map visible
3. **Favorites page** — 3+ saved properties
4. **Contract page** — Generated agreement preview
5. **Mobile view** — Same pages on phone (Chrome DevTools device toolbar)

### Property Photos
- Use existing picsum.photos URLs from `data.py` (they're consistent)
- Or: Take screenshots of actual app with real property images

### Team Photos
- Professional headshots (or clean selfies with good lighting)
- Group shot at laptop/whiteboard
- Candid "building" shots

### Logo Files Needed
- `many_houses_logo.jpeg` (already in images/)
- Transparent PNG version
- White-on-dark version
- Gold-on-white version
- Favicon (32×32)

---

## Production Workflow (This Week)

| Day | Task | Tool | Output |
|-----|------|------|--------|
| Mon | Take app screenshots | Chrome DevTools + Figma | 5+ PNGs @ 2x |
| Tue | Build templates | Canva (Brand Kit) | 6 template files |
| Wed | Create assets from templates | Canva | 15+ final images |
| Thu | Arabic versions | Canva (duplicate + translate) | 8+ Arabic assets |
| Fri | Video thumbnail + GIFs | Ezgif / ScreenToGif | 3 GIFs, 1 thumbnail |
| Sat | Review + organize | Google Drive folder | Shared folder with naming convention |

---

## File Naming Convention

```
manyhouses_[platform]_[variant]_[date]_[lang].[ext]

Examples:
manyhouses_linkedin_hero_20250115_en.png
manyhouses_twitter_thread_01_20250115_en.png
manyhouses_instagram_carousel_03_20250115_ar.png
manyhouses_whatsapp_share_20250115_en.png
manyhouses_video_thumbnail_20250115_en.jpg
```

---

## Canva Brand Kit Setup (Do First)

1. **Colors:** Add `#D4AF37`, `#111111`, `#FFFFFF`, `#FFF8E7`
2. **Fonts:** Upload Playfair Display (Google Fonts) + Inter (Google Fonts)
3. **Logos:** Upload all logo variants
4. **Templates:** Create 3 base templates (Hero, Carousel, Metric)
5. **Share:** Add team members as editors

---

## Quick Win: Animated GIFs (High Engagement)

**Tools:** ScreenToGif (Windows), Kap (Mac), or Chrome extension
**Specs:** 800px wide, 15-30s loop, <5MB

**GIF 1:** Search → Filter → Click Details → Map
**GIF 2:** Add to Favorites → Go to Favorites page → Compare
**GIF 3:** Contract page → Fill form → Generate PDF

---

## Competition-Day Social Kit

**Pre-event (Day -1):**
- Countdown story
- "Tomorrow we demo at [COMPETITION NAME]!" post
- Team prep photo

**During event:**
- Live tweet thread (1 tweet per slide of deck)
- Story: "On stage in 5 min!"
- Photo at booth/stage (tag competition handle)
- Short video clip (30s) of demo

**Post-event (Day +1):**
- Recap carousel: Problem → Demo → Feedback → Next steps
- Thank you post (tag judges, organizers, supporters)
- "We're hiring/raising/building" CTA

---

## Tools & Resources

| Purpose | Tool | Cost |
|---------|------|------|
| Design | Canva Pro | $12/mo (or free) |
| Screenshots | Chrome DevTools | Free |
| GIF Recording | ScreenToGif / Kap | Free |
| Video Clips | OBS / Loom | Free |
| Arabic Translation | DeepL / Google Translate | Free |
| QR Code Generator | qr-code-generator.com | Free |
| Asset Organization | Google Drive / Notion | Free |

---

## Approval Checklist (Before Posting)

- [ ] Logo visible and correct
- [ ] Colors match brand (#D4AF37 gold)
- [ ] Fonts: Playfair Display / Inter
- [ ] No typos (English + Arabic)
- [ ] CTA clear (link works when deployed)
- [ ] Hashtags relevant + not spammy
- [ ] Tag competition + organizers
- [ ] Alt text for accessibility
- [ ] File size <5MB (LinkedIn/Twitter)
- [ ] Saved in Drive with naming convention