#!/usr/bin/env python3
"""
Update kanji-game-standalone.html to use JSON vocabulary data
Replaces embedded data with JSON file loading
"""

import json
import re
from pathlib import Path

def main():
    # Paths
    html_file = Path(__file__).parent.parent / "kanji-game-standalone.html"
    json_file = Path(__file__).parent.parent / "data" / "kanji-vocabulary.json"
    backup_file = html_file.with_suffix('.html.backup')

    print("🔄 Updating HTML file to use JSON data...")

    # Load JSON data
    with open(json_file, 'r', encoding='utf-8') as f:
        vocab_data = json.load(f)

    print(f"✅ Loaded {vocab_data['totalWords']} words from JSON")

    # Read HTML file
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Backup original file
    with open(backup_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"💾 Created backup: {backup_file}")

    # Convert JSON to JavaScript
    vocab_json_str = json.dumps(vocab_data, ensure_ascii=False, separators=(',', ':'))

    # Pattern to find and replace VOCABULARY_DATA
    # We'll look for: const VOCABULARY_DATA = {...};
    pattern = r'const VOCABULARY_DATA = \{[^}]*"words":\[[^\]]*\]\};'

    # Simpler approach: Find the start and end markers
    start_marker = '    <script>'

    # Find where the script tag starts
    script_start = html_content.find(start_marker)
    if script_start == -1:
        print("❌ Could not find script tag")
        return 1

    # Find the const VOCABULARY_DATA line
    vocab_data_start = html_content.find('const VOCABULARY_DATA = ', script_start)
    if vocab_data_start == -1:
        print("❌ Could not find VOCABULARY_DATA")
        return 1

    # Find the end of this assignment (look for }; followed by newline and whitespace)
    # The data ends with }]};
    vocab_data_end = html_content.find('}]};', vocab_data_start)
    if vocab_data_end == -1:
        print("❌ Could not find end of VOCABULARY_DATA")
        return 1

    vocab_data_end += 3  # Include the }]};

    # Replace the embedded data
    new_vocab_line = f'const VOCABULARY_DATA = {vocab_json_str};'

    new_html = (
        html_content[:vocab_data_start] +
        new_vocab_line +
        html_content[vocab_data_end + 1:]  # Skip the newline
    )

    # Write updated HTML
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)

    print(f"✅ Updated HTML file with {vocab_data['totalWords']} words")
    print(f"📊 Distribution:")
    for level, count in vocab_data['levels'].items():
        print(f"   {level}: {count} words")
    print(f"\n✨ File updated successfully!")
    print(f"   Original backed up to: {backup_file.name}")

    return 0

if __name__ == "__main__":
    exit(main())
