#!/usr/bin/env python3
"""
Apply marketing_config.json values to all marketing documents.
Run: python3 apply_marketing_config.py
"""
import json
import re
from pathlib import Path

CONFIG_PATH = Path("marketing_config.json")

def load_config():
    with open(CONFIG_PATH) as f:
        return json.load(f)

def replace_placeholders(text, config):
    """Replace [PLACEHOLDER] patterns with config values."""
    c = config
    replacements = {
        # Competition
        r'\[COMPETITION NAME\]': c['competition']['name'],
        r'\[Competition Name\]': c['competition']['name'],
        r'\[Competition\]': c['competition']['name'],
        r'\[CompetitionName\]': c['competition']['name'].replace(' ', ''),
        r'\[DATE\]': c['competition']['date'],
        r'\[BOOTH #\]': c['competition']['booth_number'],
        r'\[DEADLINE\]': c['competition']['submission_deadline'],
        
        # Team
        r'\[FOUNDER NAME\]': c['team']['founder']['name'],
        r'\[CTO NAME\]': c['team']['cto']['name'],
        r'\[OPS NAME\]': c['team']['head_of_ops']['name'],
        r'\[Name\]': c['team']['founder']['name'],  # generic
        r'\[ADVISOR 1\]': c['team']['advisors'][0]['name'] if c['team']['advisors'] else '[ADVISOR]',
        r'\[Names if any\]': ', '.join([a['name'] for a in c['team']['advisors']]) if c['team']['advisors'] else '[Names]',
        r'\[Names \+ 1-line cred each\]': ', '.join([f"{a['name']} — {a['bio']}" for a in c['team']['advisors']]) if c['team']['advisors'] else '[Advisors]',
        r'\[Background: real estate / tech / Egypt market\]': c['team']['founder']['bio'],
        r'\[Background: full-stack, Streamlit, deployment\]': c['team']['cto']['bio'],
        r'\[Background: agent network, Cairo market, ops\]': c['team']['head_of_ops']['bio'],
        r'\[Background: agent network, Cairo market\]': c['team']['head_of_ops']['bio'],
        r'\[1 line: real estate / Egypt market / startup experience\]': c['team']['founder']['bio'],
        r'\[1 line: full-stack, Python, Streamlit, deployment\]': c['team']['cto']['bio'],
        r'\[1 line: agent network, Cairo market, ops\]': c['team']['head_of_ops']['bio'],
        
        # Metrics
        r'\[X\]': str(c['metrics']['demo_users']) if c['metrics']['demo_users'] != '[X]' else '[X]',
        r'\[X\] weeks': f"{c['metrics'].get('dev_weeks', '[X]')} weeks",
        r'\[X\] listings, \[X\] MAU, \[X\] GMV': f"{c['funding']['milestones']['listings']}, {c['funding']['milestones']['users']}, {c['funding']['milestones']['gmv']}",
        r'\[X\] MAU': c['funding']['milestones']['users'],
        r'\[X\] GMV': c['funding']['milestones']['gmv'],
        
        # Funding
        r'\[X\] to scale nationwide': c['funding']['raising'],
        r'\$\[XXX,XXX\]': c['funding']['raising'],
        
        # Contact
        r'\[GITHUB REPO URL\]': c['contact']['github'],
        r'\[LINKEDIN URL\]': c['contact']['linkedin'],
        r'\[TWITTER URL\]': c['contact']['twitter'],
        r'\[INSTAGRAM URL\]': c['contact']['instagram'],
        r'\[FACEBOOK URL\]': c['contact']['facebook'],
        r'\+20 XXX XXX XXXX': c['contact']['phone'],
        r'founder@manyhouses\.com': c['contact']['email'],
        r'Cairo, Egypt': c['contact']['address'],
        r'manyhouses\.com': c['contact']['website'],
        r'\[local URL or GitHub repo\]': c['contact']['github'],
        
        # Project
        r'\[COMPETITION NAME\]': c['competition']['name'],
    }
    
    result = text
    for pattern, replacement in replacements.items():
        result = re.sub(pattern, replacement, result)
    return result

def apply_to_file(filepath, config):
    path = Path(filepath)
    if not path.exists():
        print(f"⚠️  Not found: {filepath}")
        return
    
    content = path.read_text(encoding='utf-8')
    original = content
    content = replace_placeholders(content, config)
    
    if content != original:
        path.write_text(content, encoding='utf-8')
        print(f"✅ Updated: {filepath}")
    else:
        print(f"⏭️  No changes: {filepath}")

def main():
    config = load_config()
    print(f"Loaded config for: {config['project']['name']}")
    print("-" * 50)
    
    files = [
        "PITCH_DECK.md",
        "ONE_PAGER.md",
        "SOCIAL_ASSETS.md",
        "VIDEO_DEMO_SCRIPT.md",
        "pages/landing.py",
    ]
    
    for f in files:
        apply_to_file(f, config)
    
    print("-" * 50)
    print("Done! Fill marketing_config.json with real values, then re-run.")

if __name__ == "__main__":
    main()