# Business English Game Skill

An interactive learning game generator for business English practice. This Claude skill automatically creates HTML-based quiz games covering emails, meetings, presentations, and more.

## Overview

This skill enables Claude to generate customized business English learning games with:
- **Multiple game types**: Quiz, drag-drop, scenario simulations
- **Various topics**: Emails, meetings, presentations, negotiations, phone calls
- **Difficulty levels**: Beginner, intermediate, advanced
- **Industry-specific**: IT, finance, marketing, HR, and more

## Quick Start

### Using the Skill with Claude

Once installed, simply ask Claude to create a game:

```
You: "Create a business email writing quiz for beginners"
```

Claude will automatically:
1. Select appropriate content from the references
2. Choose the right template
3. Generate a complete HTML game
4. Save it for immediate use

### Manual Game Generation

You can also use the script directly:

```bash
python scripts/game_generator.py \
    --type quiz \
    --topic email \
    --level intermediate \
    --count 10
```

**Parameters:**
- `--type`: Game type (quiz, drag-drop, scenario)
- `--topic`: Subject matter (email, meeting, presentation, negotiation, phone)
- `--level`: Difficulty (beginner, intermediate, advanced)
- `--count`: Number of questions (default: 10)
- `--output`: Output file path (optional)
- `--industry`: Industry focus (IT, finance, marketing, etc.)

## Examples

### Example 1: Email Writing Quiz
```bash
python scripts/game_generator.py --topic email --level beginner --count 10
```
Creates a 10-question quiz on business email etiquette.

### Example 2: IT Marketing Game
```bash
python scripts/game_generator.py \
    --topic presentation \
    --level advanced \
    --industry IT \
    --count 15
```
Creates a 15-question advanced quiz on IT product presentations.

## Content Structure

### References (Content Database)
- `business_expressions.md`: 100+ business English expressions by category
- `scenarios.md`: 10+ realistic business scenarios
- `vocabulary_by_industry.md`: Industry-specific terminology

### Templates
- `quiz-template.html`: Interactive multiple-choice quiz
- More templates coming: drag-drop, scenario simulations

### Scripts
- `game_generator.py`: Main game generation engine

## Customization

### Adding New Expressions

Edit `references/business_expressions.md`:

```markdown
| Expression | Context | Example |
|-----------|---------|---------|
| Your new phrase | When to use | Example sentence |
```

### Adding New Scenarios

Edit `references/scenarios.md` following the existing format.

### Adding Industries

Edit `references/vocabulary_by_industry.md` to add new industry vocabularies.

## Features

✅ **Self-contained HTML games** - No dependencies, works offline
✅ **Immediate feedback** - Learn from mistakes in real-time
✅ **Mobile-friendly** - Responsive design works on all devices
✅ **Progress tracking** - See your score and improvement
✅ **Detailed explanations** - Understand why answers are correct/incorrect
✅ **🔊 Audio Pronunciation** - Listen to questions and answers with adjustable speed and accent (US/UK/AU)

## File Structure

```
business-english-game/
├── SKILL.md                           # Skill definition
├── README.md                          # This file
├── scripts/
│   └── game_generator.py             # Game generation script
├── references/
│   ├── business_expressions.md       # Expression database
│   ├── scenarios.md                  # Scenario templates
│   └── vocabulary_by_industry.md     # Industry vocabulary
└── assets/
    ├── templates/
    │   └── quiz-template.html        # Quiz game template
    └── icons/
        ├── correct.svg               # Checkmark icon
        ├── wrong.svg                 # X icon
        └── hint.svg                  # Question mark icon
```

## Requirements

- Python 3.7+
- No external dependencies (uses only Python standard library)
- Modern web browser to play games (Chrome, Edge, Safari, Firefox)
- Web Speech API support for pronunciation features (available in most modern browsers)

## Troubleshooting

### Game doesn't generate
- Check that all reference files exist
- Ensure topic and difficulty level are valid
- Verify Python 3.7+ is installed

### Questions seem too easy/hard
- Adjust the `--level` parameter
- Edit reference files to add more appropriate content

### Want different question types
- Currently only quiz format is supported
- Drag-drop and scenario templates coming soon

## Roadmap

### Phase 2
- [ ] Drag-and-drop matching games
- [ ] Scenario simulation templates
- [ ] Fill-in-the-blank exercises

### Phase 3
- [ ] Progress saving and tracking
- [ ] Adaptive difficulty
- [ ] Pronunciation practice (with audio)

### Phase 4
- [ ] Multi-player mode
- [ ] Leaderboards
- [ ] Custom theme support

## Contributing

To extend this skill:

1. **Add content**: Edit files in `references/`
2. **Add templates**: Create new HTML templates in `assets/templates/`
3. **Enhance generator**: Modify `scripts/game_generator.py`

## Support

For issues or questions:
- Check the `SKILL.md` for detailed usage instructions
- Review example games in the repository
- Consult reference files for content structure

## License

This skill is provided as-is for educational and professional development purposes.

---

**Created with ❤️ for business English learners worldwide**
