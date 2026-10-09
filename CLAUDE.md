# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

For any Streamlit API, layout, or theming work, load the project skill `developing-with-streamlit` (`.claude/skills/`).

## Running and checking

Run from the repo root: `st.logo("images/...")` and the banner use relative paths.

There's no test suite, but Streamlit's `AppTest` (Streamlit 1.64.0) can drive the whole app headlessly. Start from `app.py` so the menu is built, then switch to the screen you want:

```bash
python3 -c 'from streamlit.testing.v1 import AppTest; at = AppTest.from_file("app.py").run(); at.switch_page("app_pages/home.py").run(); print(at.exception, len(at.subheader))'
```

Two things to know about AppTest:

- It does not keep the current page across widget reruns. Set the widget (`.input(...)`, `.click()`), then call `at.switch_page(page).run()` for the page you are testing.
- `app_pages/details.py` is not in the menu until a property is picked. Switching to it before that raises `ValueError`. That is the intended behaviour.

## How the pieces connect

- **A property's `name` is its primary key.** Favorites and `selected_property` store names. `find_property(name)` in `data.py` returns the record, or `None`. Names must stay unique, and renaming a property breaks saved references to it.
- **Property record shape** (`data.py`): `name, image, place, rooms, bathrooms, price, area, type, latitude, longitude`, plus optional `image2`/`image3`. Property photos are remote `picsum.photos` URLs. Only the logo and banner live in `images/`.
- **`app.py` owns the menu.** Each screen is an `st.Page` in that file. A new screen needs an `st.Page` there and a file in `app_pages/`. Its own `st.set_page_config` call goes at the top of the file.
- **Login and register don't authenticate.** They check that the fields aren't empty, then `st.switch_page("app_pages/home.py")`. Nothing is stored.
- **State lives only in the session.** Favorites and form input disappear when the session ends. The contract page produces a `.txt` download and nothing else.

## Known issues (as of 2026-10-09)

The tracked list is in `ISSUES.md`. The most visible items:

- **The Gallery on the details page is always empty.** Only one property has the `image2` key, and it is an empty string.
- **Some copy describes features the app does not have** (verified listings, ownership checks, saving favorites across visits, comparing properties). The landing page is trimmed. The About and FAQ pages and the marketing documents are not yet. See `ISSUES.md`.
- **Contact details are placeholders** (`+20 100 000 0000`, `support@manyhouses.com`), and the testimonials are sample quotes.
