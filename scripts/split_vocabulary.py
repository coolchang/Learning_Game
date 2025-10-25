#!/usr/bin/env python3
"""
Split kanji-vocabulary.json into level-specific files with stage assignments
"""

import json
from pathlib import Path

def split_vocabulary():
    """Split vocabulary data by level and assign stages"""

    # Paths
    script_dir = Path(__file__).parent
    project_dir = script_dir.parent
    data_dir = project_dir / "data"
    vocab_dir = data_dir / "vocabulary"

    source_file = data_dir / "kanji-vocabulary.json"
    stages_file = vocab_dir / "stages.json"

    print("📂 Reading source vocabulary file...")
    with open(source_file, 'r', encoding='utf-8') as f:
        source_data = json.load(f)

    print(f"✅ Loaded {source_data['totalWords']} words")

    print("\n📂 Reading stages metadata...")
    with open(stages_file, 'r', encoding='utf-8') as f:
        stages_data = json.load(f)

    # Group words by level
    words_by_level = {
        'N5': [],
        'N4': [],
        'N3': [],
        'N2': [],
        'N1': []
    }

    for word in source_data['words']:
        level = word.get('level', 'N5')
        words_by_level[level].append(word)

    print("\n📊 Words per level:")
    for level, words in words_by_level.items():
        print(f"   {level}: {len(words)} words")

    # Process each level
    for level in ['N5', 'N4', 'N3', 'N2', 'N1']:
        words = words_by_level[level]
        if not words:
            print(f"\n⚠️  Skipping {level} (no words)")
            continue

        print(f"\n🔧 Processing {level}...")

        # Get stage info from metadata
        level_meta = stages_data['levels'][level]
        total_words = len(words)

        # Adjust stages based on actual word count
        if total_words < 30:
            # Very few words, use 1 stage
            actual_stages = 1
            words_per_stage = total_words
        elif total_words <= 50:
            # 30-50 words: divide into ~10 words per stage
            actual_stages = (total_words + 9) // 10  # Round up
            words_per_stage = (total_words + actual_stages - 1) // actual_stages
        else:
            # Use metadata values for larger datasets
            words_per_stage = level_meta['wordsPerStage']
            actual_stages = level_meta['totalStages']

        # Assign stage numbers to words
        for i, word in enumerate(words):
            stage_number = (i // words_per_stage) + 1
            word['stage'] = min(stage_number, actual_stages)  # Cap at max stages

        # Create level data structure
        level_data = {
            "level": level,
            "totalWords": len(words),
            "totalStages": actual_stages,
            "wordsPerStage": words_per_stage,
            "words": words
        }

        # Write to file
        output_file = vocab_dir / f"{level.lower()}.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(level_data, f, ensure_ascii=False, indent=2)

        print(f"   ✅ Created {output_file.name}")
        print(f"   📊 {len(words)} words across {actual_stages} stages")

        # Show stage distribution
        stage_counts = {}
        for word in words:
            stage = word['stage']
            stage_counts[stage] = stage_counts.get(stage, 0) + 1

        print(f"   📈 Stage distribution:")
        for stage_num in sorted(stage_counts.keys()):
            count = stage_counts[stage_num]
            print(f"      Stage {stage_num}: {count} words")

    print("\n✨ Vocabulary split completed!")
    print(f"\n📂 Created files:")
    for level in ['N5', 'N4', 'N3', 'N2', 'N1']:
        file_path = vocab_dir / f"{level.lower()}.json"
        if file_path.exists():
            print(f"   - {file_path}")

if __name__ == "__main__":
    split_vocabulary()
