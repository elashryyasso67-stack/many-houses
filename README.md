# manyhouses

A small web app for looking at properties across Egypt: search the listings, save favorites, read the FAQ, send a contact message, and make a contract draft.

It is built to be easy to read. A curious 12-year-old should be able to open any file and explain what it does.

## What it does

- **Sign in / Register**: check that the boxes are filled in, then go to the listings. Nothing is saved.
- **Properties**: search by name, city or type. Each property has a card with its photo, price and details.
- **Property details**: one property with its photo, four key numbers, details and a map.
- **Favorites**: the properties you have saved with the heart button.
- **Contract**: fill in a form for one property and download a contract draft as a text file.
- **FAQ, About, Contact us**: information pages. Contact us checks the form and says thank you. It does not send anything.
- **Welcome**: the landing page for the project.

## How it works

The app is one Python program that uses [Streamlit](https://streamlit.io) to draw the web pages.

- `app.py` starts everything. It keeps the list of favorites and builds the menu on the left.
- `data.py` holds the list of 12 properties. Each property has a name, which is its ID, and the details of that property.
- `app_pages/` has one file for each screen. Each file draws its own screen and nothing else.
- `.streamlit/config.toml` holds the colours and fonts (gold, white and black).
- `images/` holds the logo and the banner. Property photos come from picsum.photos.
- `marketing/` holds four short marketing documents: a one-pager, a pitch deck, social posts and a demo video script.
- `docs/` holds the project documentation.

When you press **View Details**, the app remembers which property you picked. The Property details screen then appears in the menu and opens on that property.

Favorites and what you type into forms last only while your browser tab is open. Close the tab or refresh the page and they are gone.

## Run it

This was tested with Python 3.12.

```bash
pip install -r requirements.txt
streamlit run app.py
```

Then open the address Streamlit prints, usually http://localhost:8501.

## Deploy it

The app runs on [Streamlit Community Cloud](https://streamlit.io/cloud):

1. Push this folder to a GitHub repository.
2. In Streamlit Community Cloud, create a new app from that repository.
3. Set the main file to `app.py`. It reads `requirements.txt` on its own.

Any other host that runs a Python web app works too. Start it with `streamlit run app.py`.

## Limits

These are the choices made to keep the code simple. Each one can be changed later.

- **There are no real accounts.** Sign in and Register only check that the boxes are not empty. No password is checked and nothing is saved, so anyone can get in.
- **Nothing is stored.** There is no database. The property list is written in `data.py`, and favorites and form input last only while the browser tab is open.
- **There is no admin and no roles.** Every visitor sees the same menu.
- **Contact us sends nothing.** The form checks the boxes and shows a thank-you message. The WhatsApp option does not contact anyone.
- **The contract is a draft.** It is a text file with the details you typed. It is not a legal document, and a lawyer should review it before signing.
- **Photos are placeholders.** Property photos come from picsum.photos and are random pictures, not the properties themselves.
- **The Gallery is empty.** Only one property has a second photo slot, and that slot is empty.
- **Errors are prevented, not handled.** The code uses plain `if` checks, such as "is this box empty?". There is no `try`/`except`, so a photo that fails to load shows the browser's broken-image icon.
- **Text boxes have no length limit.** Nothing outside the app reads them, so no limit is set.
- **Contact details and testimonials are placeholders.** The phone number (+20 100 000 0000), the email address, and the client quotes on the About and Landing pages are sample values. Replace them before launch.
- **No `services/` folder.** The code keeps each screen in its own file, with the property lookup in `data.py`. Simpler to read for one person, but harder to grow.
- **The map uses Streamlit's built-in map.** It shows one pin for each property.
- **Only Streamlit is installed.** It is pinned to version 1.64.0 in `requirements.txt`, the version this code was tested with.
- **No secrets.** The app calls no paid service and needs no API key.

See `ISSUES.md` for the list of copy and feature gaps still to fix.
