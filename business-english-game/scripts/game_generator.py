#!/usr/bin/env python3
"""
Business English Game Generator

Generates interactive HTML quiz games by combining templates with content from reference files.

Usage:
    python game_generator.py --type quiz --topic email --level intermediate --count 10
"""

import argparse
import json
import random
import re
from pathlib import Path
from typing import List, Dict, Any

# Get the skill directory (parent of scripts/)
SKILL_DIR = Path(__file__).parent.parent
TEMPLATES_DIR = SKILL_DIR / "assets" / "templates"
REFERENCES_DIR = SKILL_DIR / "references"


class GameGenerator:
    """Generates business English learning games"""

    def __init__(self):
        self.expressions = self._load_expressions()
        self.scenarios = self._load_scenarios()
        self.vocabulary = self._load_vocabulary()

    def _load_expressions(self) -> List[Dict]:
        """Load business expressions from markdown file"""
        # In production, parse the markdown file
        # For MVP, return sample data structure
        return [
            {
                "expression": "Dear Sir/Madam,",
                "category": "email",
                "subcategory": "opening",
                "difficulty": "beginner",
                "context": "Formal email to unknown recipient",
                "example": "Dear Sir/Madam, I am writing to inquire about..."
            },
            {
                "expression": "Could you please...?",
                "category": "email",
                "subcategory": "request",
                "difficulty": "beginner",
                "context": "Polite request",
                "example": "Could you please send me the updated document?"
            },
            {
                "expression": "I would appreciate it if you could...",
                "category": "email",
                "subcategory": "request",
                "difficulty": "intermediate",
                "context": "Polite formal request",
                "example": "I would appreciate it if you could review the contract."
            },
            {
                "expression": "I hope this email finds you well.",
                "category": "email",
                "subcategory": "opening",
                "difficulty": "intermediate",
                "context": "Polite opening",
                "example": "I hope this email finds you well. I wanted to follow up..."
            }
        ]

    def _load_scenarios(self) -> List[Dict]:
        """Load scenarios from markdown file"""
        return []  # Simplified for MVP

    def _load_vocabulary(self) -> List[Dict]:
        """Load industry vocabulary from markdown file"""
        return []  # Simplified for MVP

    def generate_quiz(
        self,
        topic: str = "email",
        difficulty: str = "intermediate",
        count: int = 10
    ) -> Dict[str, Any]:
        """
        Generate quiz data

        Args:
            topic: Email, meeting, presentation, etc.
            difficulty: beginner, intermediate, advanced
            count: Number of questions

        Returns:
            Dictionary with quiz data
        """

        # Filter expressions by topic and difficulty
        filtered = [
            e for e in self.expressions
            if e["category"] == topic and e["difficulty"] == difficulty
        ]

        if len(filtered) < count:
            # Fall back to including other difficulties if not enough questions
            filtered = [e for e in self.expressions if e["category"] == topic]

        # Generate questions
        questions = []
        for expr in random.sample(filtered, min(count, len(filtered))):
            question = self._create_question(expr, topic)
            questions.append(question)

        # Create quiz data structure
        quiz_data = {
            "title": f"Business {topic.title()} Quiz",
            "description": f"Test your knowledge of professional {topic} communication",
            "difficulty": difficulty.title(),
            "questions": questions
        }

        return quiz_data

    def _create_question(self, expression: Dict, topic: str) -> Dict:
        """Create a multiple-choice question from an expression"""

        # Different question types based on topic
        if topic == "email":
            return self._create_email_question(expression)
        elif topic == "meeting":
            return self._create_meeting_question(expression)
        else:
            return self._create_general_question(expression)

    def _create_email_question(self, expr: Dict) -> Dict:
        """Create an email-specific question"""

        subcategory = expr.get("subcategory", "general")

        if subcategory == "opening":
            question_text = "Which phrase is most appropriate for opening a formal business email?"
            context = "First-time email to a business contact"
        elif subcategory == "request":
            question_text = "What's the best way to make a polite request in a professional email?"
            context = "Requesting information from a colleague"
        elif subcategory == "closing":
            question_text = "Which closing phrase is most professional?"
            context = "Ending a formal business email"
        else:
            question_text = f"Which expression is most appropriate in this context?"
            context = expr.get("context", "Professional email communication")

        # Create wrong answers (simplified - in production, use more sophisticated logic)
        correct_answer = expr["expression"]
        wrong_answers = self._generate_wrong_answers(expr)

        # Combine and shuffle
        all_choices = [correct_answer] + wrong_answers
        random.shuffle(all_choices)
        correct_index = all_choices.index(correct_answer)

        return {
            "question": question_text,
            "context": context,
            "choices": all_choices,
            "correct": correct_index,
            "explanation": f"{correct_answer} is the most appropriate choice. {expr.get('context', '')}",
            "alternatives": f"Example: {expr.get('example', '')}"
        }

    def _create_meeting_question(self, expr: Dict) -> Dict:
        """Create a meeting-specific question"""
        # Similar structure to email questions
        return self._create_general_question(expr)

    def _create_general_question(self, expr: Dict) -> Dict:
        """Create a general question"""

        correct_answer = expr["expression"]
        wrong_answers = self._generate_wrong_answers(expr)

        all_choices = [correct_answer] + wrong_answers
        random.shuffle(all_choices)
        correct_index = all_choices.index(correct_answer)

        return {
            "question": f"Which expression is most appropriate for: {expr.get('context', 'this situation')}?",
            "context": expr.get("example", ""),
            "choices": all_choices,
            "correct": correct_index,
            "explanation": f"{correct_answer} is the most appropriate. {expr.get('context', '')}",
            "alternatives": ""
        }

    def _generate_wrong_answers(self, expr: Dict) -> List[str]:
        """Generate plausible wrong answers"""

        # Simplified wrong answer generation
        # In production, use more sophisticated logic based on common mistakes

        difficulty = expr.get("difficulty", "beginner")
        category = expr.get("category", "email")

        # Pool of wrong answers by category
        wrong_pools = {
            "email": {
                "opening": [
                    "Hey there!",
                    "Yo,",
                    "Hi,",
                    "What's up,"
                ],
                "request": [
                    "I need this now!",
                    "Send me the info.",
                    "Give me the details.",
                    "You should send me..."
                ],
                "closing": [
                    "See ya!",
                    "Bye,",
                    "Later,",
                    "Cheers mate,"
                ]
            }
        }

        subcategory = expr.get("subcategory", "general")
        pool = wrong_pools.get(category, {}).get(subcategory, [
            "This is too informal",
            "This is too casual",
            "This is inappropriate"
        ])

        # Select 3 random wrong answers
        return random.sample(pool, min(3, len(pool)))

    def save_game(self, quiz_data: Dict, output_path: Path):
        """
        Save quiz game as HTML file

        Args:
            quiz_data: Quiz data dictionary
            output_path: Path to save the HTML file
        """

        # Load template
        template_path = TEMPLATES_DIR / "quiz-template.html"
        with open(template_path, 'r', encoding='utf-8') as f:
            template = f.read()

        # Convert quiz data to JavaScript
        quiz_json = json.dumps(quiz_data, indent=8)

        # Replace the quizData in template
        # Find the quizData object in the template and replace it
        pattern = r'const quizData = \{[\s\S]*?\};'
        replacement = f'const quizData = {quiz_json};'

        html_content = re.sub(pattern, replacement, template, count=1)

        # Save to file
        output_path.parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html_content)

        print(f"✅ Game generated successfully: {output_path}")
        print(f"📊 {len(quiz_data['questions'])} questions")
        print(f"🎯 Topic: {quiz_data['title']}")
        print(f"📈 Difficulty: {quiz_data['difficulty']}")


def main():
    """Main entry point"""

    parser = argparse.ArgumentParser(
        description="Generate business English learning games"
    )

    parser.add_argument(
        "--type",
        default="quiz",
        choices=["quiz", "drag-drop", "scenario"],
        help="Type of game to generate"
    )

    parser.add_argument(
        "--topic",
        default="email",
        choices=["email", "meeting", "presentation", "negotiation", "phone"],
        help="Topic/scenario for the game"
    )

    parser.add_argument(
        "--level",
        default="intermediate",
        choices=["beginner", "intermediate", "advanced"],
        help="Difficulty level"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=10,
        help="Number of questions"
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=None,
        help="Output file path (default: auto-generated)"
    )

    parser.add_argument(
        "--industry",
        default=None,
        help="Industry-specific vocabulary (e.g., IT, finance, marketing)"
    )

    args = parser.parse_args()

    # Generate default output path if not provided
    if args.output is None:
        filename = f"business-{args.topic}-{args.level}-quiz.html"
        args.output = Path.cwd() / filename

    # Create generator
    generator = GameGenerator()

    # Generate quiz data
    print(f"🎮 Generating {args.type} game...")
    print(f"📚 Topic: {args.topic}")
    print(f"📊 Difficulty: {args.level}")
    print(f"🔢 Questions: {args.count}")

    if args.type == "quiz":
        quiz_data = generator.generate_quiz(
            topic=args.topic,
            difficulty=args.level,
            count=args.count
        )

        # Save the game
        generator.save_game(quiz_data, args.output)

        print(f"\n✨ Open {args.output} in your browser to play!")
    else:
        print(f"❌ Game type '{args.type}' not yet implemented.")
        print("   Currently only 'quiz' type is supported.")
        return 1

    return 0


if __name__ == "__main__":
    exit(main())
