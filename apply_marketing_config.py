"""
Fill the placeholders in the marketing documents from marketing_config.json.
Run it from the repo root: python3 apply_marketing_config.py
"""
import json
import os

CONFIG_FILE = "marketing_config.json"

FILES_TO_FILL = [
    "PITCH_DECK.md",
    "ONE_PAGER.md",
    "SOCIAL_ASSETS.md",
    "VIDEO_DEMO_SCRIPT.md",
    "app_pages/landing.py",
]

# Each pair is (placeholder text in the documents, path to its value in the config).
PLACEHOLDERS = [
    ("[COMPETITION NAME]", ["competition", "name"]),
    ("[DATE]", ["competition", "date"]),
    ("[BOOTH #]", ["competition", "booth_number"]),
    ("[DEADLINE]", ["competition", "submission_deadline"]),
    ("[FOUNDER NAME]", ["team", "founder", "name"]),
    ("$[XXX,XXX]", ["funding", "raising"]),
    ("+20 XXX XXX XXXX", ["contact", "phone"]),
    ("founder@manyhouses.com", ["contact", "email"]),
    ("[GITHUB REPO URL]", ["contact", "github"]),
    ("[LINKEDIN URL]", ["contact", "linkedin"]),
    ("[TWITTER URL]", ["contact", "twitter"]),
    ("[INSTAGRAM URL]", ["contact", "instagram"]),
    ("[FACEBOOK URL]", ["contact", "facebook"]),
]


def load_config():
    # Read the settings file into a dictionary.
    with open(CONFIG_FILE, encoding="utf-8") as f:
        return json.load(f)


def find_value(config, path):
    # Follow the keys one at a time. Return None if any key is missing.
    value = config
    for key in path:
        if key not in value:
            return None
        value = value[key]
    return value


def make_replacements(config):
    # Keep only the placeholders that have a value in the config.
    replacements = []
    for placeholder, path in PLACEHOLDERS:
        value = find_value(config, path)
        if value is None:
            print(f"Skipping {placeholder}: no value in {CONFIG_FILE}")
        else:
            replacements.append((placeholder, str(value)))
    return replacements


def fill_file(path, replacements):
    if not os.path.exists(path):
        print(f"Not found: {path}")
        return

    with open(path, encoding="utf-8") as f:
        text = f.read()

    new_text = text
    for placeholder, value in replacements:
        new_text = new_text.replace(placeholder, value)

    if new_text == text:
        print(f"No changes: {path}")
    else:
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_text)
        print(f"Updated: {path}")


def main():
    config = load_config()
    print(f"Loaded config for: {find_value(config, ['project', 'name'])}")
    print("-" * 50)

    replacements = make_replacements(config)
    for path in FILES_TO_FILL:
        fill_file(path, replacements)

    print("-" * 50)
    print(f"Done! Fill {CONFIG_FILE} with real values, then run this again.")


if __name__ == "__main__":
    main()
