# AGENTS.md

## Project Overview

**manyhouses** — a Streamlit app that lists Egyptian properties. It is written **kid-simple**: a curious 12-year-old should be able to read any file top to bottom and explain it back.

## Running the App

```bash
pip install -r requirements.txt
streamlit run app.py
```

`requirements.txt` pins `streamlit==1.64.0`, the version this code was tested with. Nothing else is installed.

## Kid-Simple Rules (keep these when you change anything)

### Code

- Plain variables. Plain functions with verb names (`find_property`, `pick_property`).
- Loops and `if`s instead of comprehensions, decorators, classes, type hints and generators.
- One short comment above anything a kid would ask "why?" about, in kid words.
- Constants at the top of the file in CAPITALS, with a comment saying why the number is what it is (`CARDS_PER_ROW`).
- Repetition beats abstraction when it keeps a file readable on its own. The same few lines of favorite-button code in three screens is fine.

### Libraries

- Standard library first. Streamlit is the only library. Anything new must do a job plain code can't do in about 10 lines.
- Pin the versions you tested.

### Layout

- `app.py` is the one entry file. It sets up favorites and builds the menu.
- `app_pages/` holds one direct script per screen. Each imports only what it uses.
- `data.py` holds the property list and `find_property`.
- There is **no `services/` folder**. The owner chose to keep everything in the screen files and `data.py`, instead of the kid-simple default of one service file per topic.

### Behaviour

- Validate with plain `if` checks where a user will hit a problem (empty boxes, end date before start date, no search match). Show a friendly message.
- No `try`/`except` anywhere. Errors are prevented with `if` checks.
- Design inside external limits instead of handling their errors.
- Every simplification that removes safety or capability goes in the README's **Limits** section, in plain words.

### UI

- Friendly sentence-case labels, icons on menu items.
- One highlighted primary button per screen (`type="primary"`).
- Hide what the user can't use instead of showing it and refusing (Property details is hidden until a property is picked).

## Architecture

- **Entry point**: `app.py` — creates `st.session_state.favorites`, calls `st.logo`, and builds one menu with `st.navigation`. Each screen is an `st.Page` pointing at a file in `app_pages/`. The first screen (Sign in) is the default.
- **Data**: `data.py` — `PROPERTIES` (12 dictionaries across 10 Egyptian cities, 4 property types) and `find_property(name)`.
- **Screens** (`app_pages/`): `login.py`, `register.py`, `landing.py`, `home.py`, `details.py`, `favorites.py`, `contract.py`, `faq.py`, `about.py`, `contact_us.py`.
- **Navigation**: `st.switch_page("app_pages/xxx.py")`. When a property is picked, the "View Details" button sets `st.session_state.selected_property` in an `on_click` callback first. The callback runs before the page redraws, so the menu already includes Details when the switch happens.
- **Marketing**: the four documents in `marketing/` are plain text. Edit them by hand. There is no script.
- **Folders**: `marketing/` holds the marketing documents and their script. `docs/` holds the project documentation. The root holds only app code and the instruction and README files.

## Theming

- **`.streamlit/config.toml`** has the white-black-gold theme: primary `#D4AF37`, background `#FFFFFF`, sidebar `#111111`, and the fonts. Edit colours and fonts there.
- `app_pages/landing.py` keeps only a few CSS rules, for layout. Do not add more theming CSS.
- **Fonts**: `Inter` for body, `Playfair Display` for headings.
- **Icons**: Material Symbols (`:material/icon_name:`). Names use underscores. Check `/home/ibrahim/.local/lib/python3.12/site-packages/streamlit/material_icon_names.py` before using a new one.

## Favorites

- `st.session_state.favorites` is a list of property names. It lasts only as long as the browser session.
- Heart buttons appear on home cards and the details page. `app_pages/favorites.py` lists saved properties with View Details and remove buttons.

## Key Conventions & Gotchas

- **Use `width="stretch"` or `width="content"`**, never `use_container_width` (deprecated since Streamlit 1.64).
- **Property `name` is the ID.** Favorites and `selected_property` store names. Keep names unique, and renaming one breaks saved references.
- **Material icon names**: `file_document`, `currency`, `property`, `city`, `faq`, `sun`, `river` and `building` are NOT valid. Use `description`, `attach_money`, `house`, `home`, `help`, `sunny`, `water` and `construction`.
- **Login and Register don't authenticate.** They check that the boxes aren't empty and store nothing.
- **Gallery** on the details page shows only when a property has `image2`. Only the first property has the key, and it is empty, so the box is empty today.

## No Tests

There is no test suite. Check changes by running the app, or with Streamlit's `AppTest` (see CLAUDE.md).
