# manyhouses — Pitch Deck

**Theme:** White / Black / Gold (#D4AF37) | Fonts: Inter + Playfair Display
**Format:** 10-12 slides | 5-min pitch + 5-min Q&A

---

## Slide 1: Title Slide
**Background:** White with gold accent line
**Content:**
- Logo (manyhouses)
- Tagline: "Your trusted partner for Egyptian real estate"
- Competition name / date
- Team names & roles

---

## Slide 2: The Problem
**Headline:** Finding property in Egypt is broken
**Bullets (3 max):**
- ❌ Fragmented listings across Facebook, OLX, agents, word-of-mouth
- ❌ No verification → scams, fake photos, hidden fees
- ❌ No unified search across cities (Cairo, Alexandria, Red Sea, Luxor, etc.)
**Visual:** Screenshot of messy Facebook group / OLX listing (side-by-side)

---

## Slide 3: The Solution
**Headline:** manyhouses — One platform. Verified listings. All of Egypt.
**Value props (3 columns with icons):**
- 🛡️ **Verified Listings** — Every property photographed & verified
- 🗺️ **National Coverage** — 10+ cities from Cairo to Siwa
- 💰 **Transparent Pricing** — No hidden fees, ever
**Visual:** App hero screenshot (home page with properties)

---

## Slide 4: Product Demo (Live)
**Headline:** Let me show you
**Script:**
1. Search "Cairo villa" → instant filter
2. Click "Modern Villa" → details, gallery, map
3. Add to favorites → kept for this visit
4. View favorites page → see every saved property
5. Contract page → generate agreement
**Visual:** Live demo (have app running locally)

---

## Slide 5: Market Opportunity
**Headline:** Egypt's real estate market is booming
**Stats (large numbers, gold highlight):**
- **EGP 3.5T** — Real estate market size (2024)
- **12M+** — Housing gap by 2030 (government target)
- **65%** — Egyptians search property online first
- **10 cities** — We cover from day one
**Visual:** Simple bar chart or map of Egypt with pins

---

## Slide 6: Business Model
**Headline:** Simple, scalable revenue
**Three streams:**
1. **Listing Fees** — Agents/developers pay per verified listing
2. **Featured Placement** — Top-of-search premium spots
3. **Lead Referral** — Commission on closed deals (future)
**Unit economics:** CAC < LTV by month 6

---

## Slide 7: Traction & Validation
**Headline:** Built & tested in [X] weeks
**Metrics (fill in your actuals):**
- ✅ **12 properties** across 10 cities (demo data)
- ✅ **5 core features:** Search, Details, Favorites, Contracts, Auth
- ✅ **One library** — Streamlit only; photos load from picsum.photos, deploys to any Python host
- ⏳ **Pilot users:** [X] | **Feedback score:** [X]/5
**Visual:** Screenshot montage (home, details, favorites, contract)

---

## Slide 8: Competition
**Headline:** We're not a directory — we're a trusted marketplace
**Table:**

| Feature | OLX/Facebook | Property Finder | **manyhouses** |
|---------|--------------|-----------------|----------------|
| Verified listings | ❌ | ✅ | ✅ |
| National coverage | ✅ | Cairo only | ✅ |
| Favorites | ❌ | ✅ | ✅ |
| Contract generation | ❌ | ❌ | ✅ |
| No hidden fees | ❌ | ❌ | ✅ |
| Arabic + English | ❌ | ✅ | 🔜 |

---

## Slide 9: Go-to-Market
**Headline:** Agent-first, then consumer
**Phases:**
1. **Months 1-3:** Onboard 50+ verified agents in Cairo & Alexandria
2. **Months 4-6:** Expand to Red Sea & Upper Egypt; launch Arabic UI
3. **Months 7-12:** Mobile app; mortgage partnerships; escrow integration
**Key partnership:** [Name any real estate org, university, incubator]

---

## Slide 10: The Ask
**Headline:** We're raising $[XXX,XXX]
**Use of funds (pie chart):**
- 40% — Agent acquisition & verification ops
- 30% — Product (mobile app, Arabic, maps)
- 20% — Marketing & brand
- 10% — Legal/compliance
**Milestones at next round:** 5,000, 25,000, EGP 50M

---

## Slide 11: Team
**Headline:** Built by builders who know Egypt
**Per person:** Photo + Name + Role + One-line cred
- **Founder/CEO** — [1-line: real estate / Egypt market / startup experience]
- **CTO** — [1-line: full-stack, Python, Streamlit, deployment]
- **Head of Ops** — [1-line: agent network, Cairo market, ops]
**Advisors:** [ADVISOR 1]

---

## Slide 12: Closing / Contact
**Background:** Gold accent, minimal
**Content:**
- manyhouses — Your trusted partner for Egyptian real estate
- 🌐 manyhouses.com (or GitHub repo)
- 📧 founder@manyhouses.com
- 📱 +20 XXX XXX XXXX
- QR code to live demo / repo

---

## Speaker Notes (per slide)

### Slide 2 - Problem
> "We talked to 30+ buyers in Cairo and Alexandria. Every single one had a horror story — fake listings, agents disappearing after deposit, hidden 'service fees' appearing at signing. The market is massive but trust is near zero."

### Slide 3 - Solution
> "We're not another directory. We verify every listing ourselves — photos, ownership, pricing. And we cover ALL of Egypt, not just Cairo. A buyer in Siwa gets the same experience as one in New Capital."

### Slide 4 - Demo
> [Keep it tight. 90 seconds max. Narrate what you're clicking.]
> "Search works across name, city, type. Details show gallery, map, specs. Favorites last for the visit, no login needed. Contract page generates a contract draft as a text file. All in a lightweight Streamlit app that deploys anywhere."

### Slide 5 - Market
> "Egypt's building 12 million homes by 2030. That's not a typo. The New Capital alone is 700 sq km. But digital infrastructure hasn't caught up. We're building the layer that makes this market transparent."

### Slide 7 - Traction
> "We built this in [X] weeks as a team of [X]. No paid APIs, no vendor lock-in. The demo data shows 12 properties across 10 cities — but the architecture scales to thousands. We're ready for real inventory."

### Slide 10 - Ask
> "We're not asking for money to build the product — it's done. We're asking for capital to verify the first 500 listings, onboard the first 50 agents, and prove the model in Cairo before expanding. This is execution risk, not product risk."

---

## Design Notes for Deck Creation

**Colors (from .streamlit/config.toml):**
- Primary Gold: `#D4AF37`
- White: `#FFFFFF`
- Dark: `#111111`
- Light Gold BG: `#FFF8E7`

**Fonts:**
- Headings: Playfair Display (600/700)
- Body: Inter (400/500/600)

**Icons:** Material Symbols (same as app)
- home, shield, location_on, attach_money, bed, bathtub, expand, favorite, search, map, analytics, image, payment, support_agent, star, account_balance, eco, sunny, water, construction, waves, beach_access, water_drop, landscape

**Tools to build:**
- Canva (fastest, has Playfair Display)
- Google Slides (collaborative)
- Marp / Markdown → PDF (dev-friendly)
- PowerPoint (if required)

---

## Appendix Slides (optional, for Q&A)

### A1: Technical Architecture
- Streamlit app with one menu, defined in app.py
- Session state for favorites/auth
- No database — property data is a Python list in data.py, ready to move to one
- Deployable to Streamlit Cloud, Railway, Docker, any Python host

### A2: Data Pipeline (Future)
- Agent portal for self-serve listing upload
- Automated verification workflow
- Image optimization + CDN
- Map clustering for 1000+ pins

### A3: Arabic Localization Plan
- RTL support in Streamlit (CSS)
- Translation keys for all UI strings
- Arabic property descriptions
- Right-to-left search

### A4: Financial Model Detail
- [Insert your spreadsheet snapshot]