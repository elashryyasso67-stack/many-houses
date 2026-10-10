# Issues

Local tracker. Tags: feature, bug, refactor, docs, performance.

## Open

### 1. [bug] Gallery on the details page is always empty
Only the first property has an `image2` key, and it is an empty string. The Gallery expander in `app_pages/details.py` therefore shows nothing for every property.
- Option A: add a second photo for each property in `data.py`.
- Option B: remove the Gallery expander.

### 2. [docs] Copy says the app verifies listings
The app checks nothing. Still open in:
- `app_pages/about.py`: "Verified Listings" card ("Every property is verified and photographed").

Decision needed: keep "verified" as the company promise (and make it true with real process), or change the wording.

### 3. [docs] FAQ says accounts save favorites
`app_pages/faq.py`: "creating an account lets you save favorites and manage your inquiries". Accounts store nothing, and favorites last only for the browser tab.

### 4. [docs] Promises the app doesn't keep
- FAQ: "Our team will respond within 24 hours."
- About: "Every property is verified and photographed."
- Marketing docs: "compare properties across cities side by side", "favorites persist across sessions", "ready-to-sign PDF".

### 5. [feature] Accounts do not exist
Sign in and Register check only that boxes are filled. If real accounts are wanted later, that needs a database, password hashing and a logged-in state. Those are the kid-simple exceptions to add back, with notes in README Limits.

### 6. [feature] Contact us sends nothing
The form shows a thank-you but nothing is delivered. Decide how messages should arrive (email, a database, or a WhatsApp link).

### 7. [docs] Placeholder values still in use
- Phone `+20 100 000 0000` and email `support@manyhouses.com` appear in FAQ, About, Contact us, Landing and README.
- Testimonials on About and Landing are sample quotes. Replace them with real client feedback before launch.

### 8. [docs] Footer social links are plain text
The Landing footer lists LinkedIn, Facebook, Instagram and Twitter as text with no links. Add the real URLs once they exist.

## Done in the kid-simple rebuild (2026-10-09)

- Removed the `import pages.login` trick that left the main page blank after a rerun. The menu is now one `st.navigation` list in `app.py`.
- Removed the pandas dependency. The map takes a plain dictionary.
- Removed `use_container_width` everywhere. Buttons use `width="stretch"`.
- Moved the screens from `pages/` to `app_pages/`, so Streamlit does not add its own automatic sidebar.
- Deleted the marketing script and its JSON settings. The four marketing documents are now short and plain, with blanks only the team can fill in.
- Trimmed the landing page: CSS now only for layout, colours and fonts come from `config.toml`, and copy that promised missing features was cut.
