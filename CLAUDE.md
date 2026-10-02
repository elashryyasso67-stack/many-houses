# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

@AGENTS.md

For any Streamlit API, layout, or theming work, load the project skill `developing-with-streamlit` (`.claude/skills/`).

## Running and checking

Run from the repo root: `st.logo("images/...")` and the banner use relative paths.

There's no test suite, but Streamlit's `AppTest` (Streamlit 1.64.0 is installed) can drive a page headlessly for a quick check:

```bash
python3 -c 'from streamlit.testing.v1 import AppTest; at = AppTest.from_file("pages/home.py"); at.session_state.favorites = []; at.run(); print(at.exception, [s.value for s in at.subheader])'
```

Pages read `st.session_state.favorites` directly, and `app.py` normally creates it. So when you run a page on its own, seed `favorites`, and `selected_property` for details/contract pages, before calling `run()`.

## How the pieces connect

- **A property's `name` is its primary key.** Favorites and `selected_property` store names, and every page gets the record back with `next(p for p in properties if p["name"] == ...)`. Names must stay unique, and renaming a property breaks saved references to it.
- **Property record shape** (`data.py`): `name, image, place, rooms, bathrooms, price, area, type, latitude, longitude`, plus optional `image2`/`image3`. Property images are remote `picsum.photos` URLs. Only the logo and banner live in `images/`.
- **Each page calls its own `st.set_page_config`** and `st.logo(...)`. A new page needs both to match the others.
- **Login and register don't authenticate.** They check that the fields aren't empty, then `st.switch_page("pages/home.py")`. Nothing is stored.
- **State lives only in the session.** Favorites and form input disappear when the session ends. The contract page produces a `.txt` download and nothing else.

## Known issues (as of 2026-09-25)

- **The entry page goes blank after the first rerun.** `app.py` renders login with `import pages.login`. Python caches that import, so the login UI shows on the first run, but any interaction that triggers a rerun leaves the main page empty. You can reproduce this with `AppTest.from_file("app.py")` by calling `.run()` twice.
- **`data.py` no longer has a BOM,** whatever AGENTS.md says.
- **`use_container_width` is still used** in `login.py`, `register.py`, `faq.py`, `contract.py` and `favorites.py`, even though AGENTS.md calls it deprecated. Use `width="stretch"` / `width="content"` in new code.
