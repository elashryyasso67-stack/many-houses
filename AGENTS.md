# AGENTS.md

## Project Overview

**manyhouses** — Streamlit real estate property listing app for Egyptian properties.

## Running the App

```bash
streamlit run app.py
```

No `requirements.txt`, `pyproject.toml`, or `setup.py` exists. Dependencies (`streamlit`, `pandas`) are already installed.

## Architecture

- **Entry point**: `app.py` — initializes `st.session_state.favorites` and imports `pages.login` to initialize the `pages` package.
- **Data module**: `data.py` — holds a hardcoded `properties` list of 12 properties across 10 Egyptian cities. All pages import via `from data import properties`.
- **Pages**: `pages/login.py`, `pages/register.py`, `pages/home.py`, `pages/details.py`, `pages/contract.py`, `pages/about.py`, `pages/contact_us.py`, `pages/favorites.py`, `pages/faq.py`
- **Navigation**: Legacy Streamlit `st.switch_page("pages/xxx.py")`. `st.session_state.selected_property` passes the selected property name from `home.py` to `details.py` and `contract.py`.

## Theming

- **`.streamlit/config.toml`** has white-black-gold theme: primary `#D4AF37`, background `#FFFFFF`, sidebar `#111111`. Edit here for colors/fonts/borders — never custom CSS for theming.
- **Fonts**: `Inter` for body, `Playfair Display` for headings.
- **Icons**: Material Symbols (`:material/icon_name:`) throughout. Valid names use underscores. Check `/home/ibrahim/.local/lib/python3.12/site-packages/streamlit/material_icon_names.py` for valid names.

## Favorites System

- `st.session_state.favorites` is a list of property name strings.
- Initialized in `app.py`.
- Favorite heart button appears on home page cards and details page.
- `pages/favorites.py` displays all saved properties with view/details buttons.
- `pages/login.py` and `pages/register.py` have buttons to navigate to Favorites page.

## Key Conventions & Gotchas

- **`use_container_width` is deprecated** in Streamlit 1.64+. Use `width="stretch"` or `width="content"`.
- **`pages/details.py`** requires `st.session_state.selected_property`; otherwise shows "No property selected" and stops.
- **`data.py`** has a BOM character at line 1 — strip with `sed -i '1s/^\xEF\xBB\xBF//' data.py` if it causes issues.
- **Material icon names use underscores** (`person_add`, `description`), not hyphens. `file_document` is NOT valid — use `description`. `currency` is NOT valid — use `attach_money`. `property` is NOT valid — use `house`. `city` is NOT valid — use `home`. `faq` is NOT valid — use `help`. `sun` is NOT valid — use `sunny`. `river` is NOT valid — use `water`. `building` is NOT valid — use `construction`.
- **Details page** uses `st.expander` for gallery, details, and map sections to save space.
- **Home page** uses `st.container(horizontal=True, border=True)` with `st.columns(len(row_items))` for responsive property rows.
- **Login/Register** use `st.container(border=True)`, centered layout, `st.divider()`, `use_container_width=True` on buttons.

## No Tests

No test files or test framework exists. Testing is manual via `streamlit run app.py`.
