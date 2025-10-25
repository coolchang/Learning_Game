#!/usr/bin/env python3
"""
Advanced Business English Stage Game Generator

Generates a complete 15-stage learning game with 105 advanced expressions.
"""

import json
import re
from pathlib import Path

# Get directories
SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "assets" / "templates"
REFERENCES_DIR = SKILL_DIR / "references"


def generate_advanced_game(output_path: Path):
    """Generate the complete advanced business English game"""

    print("🎮 Generating Advanced Business English Game...")
    print("📊 15 Stages × 7 Questions = 105 Advanced Expressions")

    # Load the stage data
    data_file = REFERENCES_DIR / "advanced_expressions_stages.json"
    with open(data_file, 'r', encoding='utf-8') as f:
        game_data = json.load(f)

    print(f"✅ Loaded {len(game_data['stages'])} stages")

    # Load template
    template_file = TEMPLATES_DIR / "stage-quiz-template.html"
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()

    # Convert game data to JavaScript
    game_json = json.dumps(game_data, indent=8)

    # Replace the gameData in template
    # Find the start and end positions
    start_marker = 'const gameData = {'
    end_marker = '};\n\n        // Voice Settings'

    start_idx = template.find(start_marker)
    end_idx = template.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("Could not find gameData section in template")

    # Replace the section
    html_content = (
        template[:start_idx] +
        f'const gameData = {game_json};' +
        '\n\n        // Voice Settings' +
        template[end_idx + len(end_marker):]
    )

    # Save to file
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"✅ Game generated successfully: {output_path}")
    print(f"\n📚 Game Features:")
    print(f"   • 15 Progressive Stages")
    print(f"   • 105 Advanced Expressions")
    print(f"   • Progress Tracking (saved locally)")
    print(f"   • Stage Unlock System")
    print(f"   • Audio Pronunciation (US/UK/AU)")
    print(f"   • Mobile-Friendly Design")
    print(f"\n🎯 Topics Covered:")
    print(f"   • Email Writing (Stages 1-3)")
    print(f"   • Meeting Participation (Stages 4-6)")
    print(f"   • Presentations (Stages 7-9)")
    print(f"   • Negotiations (Stages 10-12)")
    print(f"   • Advanced Communication (Stages 13-15)")
    print(f"\n✨ Open {output_path} in your browser to start learning!")


def main():
    # Default output path
    output_file = Path.cwd() / "advanced-business-english-game.html"

    generate_advanced_game(output_file)
    return 0


if __name__ == "__main__":
    exit(main())
