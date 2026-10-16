"""Turn the HTML and Markdown in docs/ into the PNGs and PDFs you print or share.

Run it from the repo root after you change anything in docs/:

    pip install playwright markdown-it-py
    python -m playwright install chromium     (skip this if Google Chrome is installed)
    python docs/build.py                      (builds everything)
    python docs/build.py poster               (or: diagrams, slides, plan, brand, social)

It also counts the "Student writes" boxes that are still empty, so you know what is left to fill in.
"""
import pathlib
import shutil
import sys
from markdown_it import MarkdownIt
from playwright.sync_api import sync_playwright

DOCS = pathlib.Path(__file__).parent.resolve()

# Output names.
PLAN = "manyhouses-marketing-plan"
SLIDES_PDF = "manyhouses-pitch-deck.pdf"
POSTER_PDF = "manyhouses-poster-1000x2000mm.pdf"
BRAND_PDF = "manyhouses-brand-guide.pdf"

# The poster is printed at 1000 x 2000 mm, with 5 mm of extra edge on each side for trimming.
POSTER_SIZE = ("1010mm", "2010mm")
POSTER_PIXELS = (3818, 7597)   # the same size at 96 pixels per inch

# Slides are 16:9, the same shape as a projector screen.
SLIDE_SIZE = ("1280px", "720px")

# The brand guide is one landscape page, A4 shaped.
BRAND_SIZE = ("1600px", "1131px")

TODO_MARK = "Student writes"


def open_page(browser, path, width, height, scale=1):
    page = browser.new_page(viewport={"width": width, "height": height}, device_scale_factor=scale)
    page.goto(path.as_uri())
    # "load" waits for the pictures and stylesheets; fonts.ready waits for the Google fonts.
    page.wait_for_load_state("load")
    page.evaluate("document.fonts.ready")
    return page


def build_diagrams(browser):
    # Every diagram HTML file has one .canvas box. Its size is the size of the PNG.
    for html in sorted((DOCS / "diagrams").glob("*.html")):
        page = open_page(browser, html, 2400, 1600, scale=3)
        page.locator(".canvas").screenshot(path=str(html.with_suffix(".png")))
        page.close()
        print("diagram  ", html.with_suffix(".png").name)


def build_poster(browser):
    width, height = POSTER_PIXELS
    page = open_page(browser, DOCS / "poster" / "poster.html", width, height)
    page.pdf(path=str(DOCS / "poster" / POSTER_PDF), width=POSTER_SIZE[0], height=POSTER_SIZE[1], print_background=True)
    page.close()
    # A small picture of the poster, for READMEs and chat messages.
    page = open_page(browser, DOCS / "poster" / "poster.html", width, height, scale=0.5)
    page.screenshot(path=str(DOCS / "poster" / "preview.png"))
    page.close()
    print("poster   ", POSTER_PDF + ", preview.png")


def build_slides(browser):
    page = open_page(browser, DOCS / "presentation" / "slides.html", 1280, 720)
    page.pdf(path=str(DOCS / SLIDES_PDF), width=SLIDE_SIZE[0], height=SLIDE_SIZE[1], print_background=True)
    page.close()
    print("slides   ", SLIDES_PDF)


def build_plan(browser):
    source = DOCS / (PLAN + ".md")
    markdown = MarkdownIt("commonmark", {"html": True}).enable("table")
    body = markdown.render(source.read_text(encoding="utf-8"))
    style = (DOCS / "assets" / "documentation.css").read_text(encoding="utf-8")
    html = ("<!DOCTYPE html><html lang='en'><head><meta charset='UTF-8'>"
            "<link rel='stylesheet' href='assets/brand.css'><style>" + style + "</style></head>"
            "<body><main>" + body + "</main></body></html>")
    # Saved next to the .md so the image links inside it still work.
    temp = DOCS / "_plan.html"
    temp.write_text(html, encoding="utf-8")
    page = open_page(browser, temp, 900, 1200)
    page.pdf(path=str(DOCS / (PLAN + ".pdf")), format="A4", print_background=True,
             margin={"top": "18mm", "bottom": "18mm", "left": "16mm", "right": "16mm"})
    page.close()
    temp.unlink()
    print("plan     ", PLAN + ".pdf")


def build_brand(browser):
    page = open_page(browser, DOCS / "brand" / "brand-guide.html", 1600, 1131)
    page.pdf(path=str(DOCS / "brand" / BRAND_PDF), width=BRAND_SIZE[0], height=BRAND_SIZE[1], print_background=True)
    page.close()
    print("brand    ", BRAND_PDF)


def build_social(browser):
    # Every post in social.html is a .post box with an id. Each one becomes social/<id>.png.
    page = open_page(browser, DOCS / "social" / "social.html", 2400, 2000)
    posts = page.locator(".post")
    for index in range(posts.count()):
        post = posts.nth(index)
        name = post.get_attribute("id")
        post.screenshot(path=str(DOCS / "social" / (name + ".png")))
        print("social   ", name + ".png")
    page.close()


def count_todos():
    files = [DOCS / (PLAN + ".md"), DOCS / "poster" / "poster.html", DOCS / "presentation" / "slides.html",
             DOCS / "brand" / "brand-guide.html", DOCS / "social" / "social.html"]
    files += sorted((DOCS / "diagrams").glob("*.html"))
    for path in files:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        # In the HTML files a box is a class="todo" tag. In the .md file it is the words themselves.
        if path.suffix == ".html":
            left = text.count('class="todo')
        else:
            left = text.count(TODO_MARK)
        if left > 0:
            print("to fill  ", path.relative_to(DOCS), "has", left, "'Student writes' boxes left")


with sync_playwright() as playwright:
    # Use Google Chrome if it is installed, so you can skip "playwright install chromium".
    if shutil.which("google-chrome"):
        browser = playwright.chromium.launch(channel="chrome")
    else:
        browser = playwright.chromium.launch()

    # With no word after build.py, build everything.
    wanted = sys.argv[1:]
    if len(wanted) == 0:
        wanted = ["diagrams", "social", "poster", "slides", "plan", "brand"]

    if "diagrams" in wanted:
        build_diagrams(browser)
    if "social" in wanted:
        build_social(browser)
    if "poster" in wanted:
        build_poster(browser)
    if "slides" in wanted:
        build_slides(browser)
    if "plan" in wanted:
        build_plan(browser)
    if "brand" in wanted:
        build_brand(browser)
    browser.close()

count_todos()
