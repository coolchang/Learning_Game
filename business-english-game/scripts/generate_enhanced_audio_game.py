#!/usr/bin/env python3
"""
Enhanced Audio - Advanced Business English Game Generator

Generates game with ResponsiveVoice.js integration for superior audio quality
"""

import json
from pathlib import Path

SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "assets" / "templates"
REFERENCES_DIR = SKILL_DIR / "references"


def generate_enhanced_game(output_path: Path):
    """Generate the enhanced audio version of the game"""

    print("🎮 Generating Enhanced Audio Business English Game...")
    print("🔊 Using ResponsiveVoice.js for premium audio quality")
    print("📊 15 Stages × 7 Questions = 105 Advanced Expressions\n")

    # Load stage data
    data_file = REFERENCES_DIR / "advanced_expressions_stages.json"
    with open(data_file, 'r', encoding='utf-8') as f:
        game_data = json.load(f)

    print(f"✅ Loaded {len(game_data['stages'])} stages")

    # Load enhanced template
    template_file = TEMPLATES_DIR / "stage-quiz-enhanced-audio.html"
    with open(template_file, 'r', encoding='utf-8') as f:
        template = f.read()

    # Convert to JavaScript
    game_json = json.dumps(game_data, indent=8)

    # Replace gameData
    start_marker = 'const gameData = {'
    end_marker = '};\n\n        // Enhanced Voice Settings'

    start_idx = template.find(start_marker)
    end_idx = template.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("Could not find gameData section in template")

    html_content = (
        template[:start_idx] +
        f'const gameData = {game_json};' +
        '\n\n        // Enhanced Voice Settings' +
        template[end_idx + len(end_marker):]
    )

    # Save
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ Enhanced game generated: {output_path}")
    print(f"\n🎵 Audio Features:")
    print(f"   • ResponsiveVoice.js (Premium Quality)")
    print(f"   • 6 Natural Voices (US/UK/AU - Male/Female)")
    print(f"   • Web Speech API Fallback")
    print(f"   • Adjustable Speed (0.7x - 1.3x)")
    print(f"   • Real-time Engine Switching")
    print(f"\n📚 Game Features:")
    print(f"   • 15 Progressive Stages")
    print(f"   • 105 Advanced Expressions")
    print(f"   • Progress Tracking")
    print(f"   • Stage Unlock System")
    print(f"   • Mobile-Friendly Design")
    print(f"\n🎯 Topics Covered:")
    print(f"   • Email Writing (Stages 1-3)")
    print(f"   • Meeting Participation (Stages 4-6)")
    print(f"   • Presentations (Stages 7-9)")
    print(f"   • Negotiations (Stages 10-12)")
    print(f"   • Advanced Communication (Stages 13-15)")
    print(f"\n✨ Open {output_path} in your browser!")
    print(f"   Recommended: Use 'Enhanced Voice' in audio settings for best quality")


def main():
    output_file = Path.cwd() / "advanced-business-english-ENHANCED-AUDIO.html"
    generate_enhanced_game(output_file)
    return 0


if __name__ == "__main__":
    exit(main())
