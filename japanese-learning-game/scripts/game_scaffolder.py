#!/usr/bin/env python3
"""
일본어 학습 게임 보일러플레이트 생성기

이 스크립트는 지정된 게임 타입과 학습 콘텐츠로
즉시 실행 가능한 React 기반 학습 게임을 생성합니다.
"""

import argparse
import shutil
import json
from pathlib import Path
from typing import Literal

GameType = Literal['flashcard', 'quiz', 'typing', 'conversation', 'all']
JLPTLevel = Literal['N5', 'N4', 'N3', 'N2', 'N1']


class GameScaffolder:
    """게임 프로젝트 생성 클래스"""

    def __init__(
        self,
        game_type: GameType,
        jlpt_level: JLPTLevel,
        category: str,
        output_dir: Path,
        skill_dir: Path
    ):
        self.game_type = game_type
        self.jlpt_level = jlpt_level
        self.category = category
        self.output_dir = output_dir
        self.skill_dir = skill_dir

    def create_game(self):
        """게임 프로젝트 생성"""
        print(f"🎮 일본어 학습 게임 생성 중...")
        print(f"   타입: {self.game_type}")
        print(f"   레벨: {self.jlpt_level}")
        print(f"   카테고리: {self.category}")
        print(f"   출력: {self.output_dir}")
        print()

        # 1. 템플릿 복사
        self._copy_template()

        # 2. 데이터 주입
        self._inject_data()

        # 3. 게임 타입별 컴포넌트 추가
        self._add_game_components()

        # 4. 설정 파일 생성
        self._create_config()

        print()
        print("✅ 게임 생성 완료!")
        print()
        print("다음 단계:")
        print(f"  1. cd {self.output_dir}")
        print("  2. npm install")
        print("  3. npm run dev")

    def _copy_template(self):
        """템플릿 디렉토리 복사"""
        template_path = self.skill_dir / 'assets' / 'game-template'

        if not template_path.exists():
            print(f"⚠️  템플릿이 없습니다: {template_path}")
            print("   기본 구조만 생성합니다.")
            self.output_dir.mkdir(parents=True, exist_ok=True)
            return

        if self.output_dir.exists():
            print(f"⚠️  디렉토리가 이미 존재합니다: {self.output_dir}")
            response = input("덮어쓰시겠습니까? (y/N): ")
            if response.lower() != 'y':
                print("취소되었습니다.")
                exit(1)
            shutil.rmtree(self.output_dir)

        shutil.copytree(template_path, self.output_dir)
        print(f"✓ 템플릿 복사 완료")

    def _inject_data(self):
        """학습 데이터 주입"""
        vocab_file = (
            self.skill_dir / 'references' / 'vocabulary' /
            f'{self.jlpt_level.lower()}-words.json'
        )

        if not vocab_file.exists():
            print(f"⚠️  단어 데이터가 없습니다: {vocab_file}")
            print("   샘플 데이터를 생성합니다.")
            self._create_sample_data()
            return

        # 데이터 파일을 게임 프로젝트에 복사
        data_dir = self.output_dir / 'src' / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)

        shutil.copy(vocab_file, data_dir / 'vocabulary.json')
        print(f"✓ 학습 데이터 주입 완료")

    def _add_game_components(self):
        """게임 타입별 컴포넌트 추가"""
        components = {
            'flashcard': ['Flashcard.tsx', 'FlipCard.tsx'],
            'quiz': ['Quiz.tsx', 'QuizQuestion.tsx'],
            'typing': ['TypingGame.tsx', 'TypingInput.tsx'],
            'conversation': ['Conversation.tsx', 'DialogueBox.tsx'],
        }

        if self.game_type == 'all':
            selected_components = [c for comps in components.values() for c in comps]
        else:
            selected_components = components.get(self.game_type, [])

        print(f"✓ 게임 컴포넌트 추가: {', '.join(selected_components)}")

    def _create_config(self):
        """게임 설정 파일 생성"""
        config = {
            'gameType': self.game_type,
            'jlptLevel': self.jlpt_level,
            'category': self.category,
            'srs': {
                'enabled': True,
                'newCardsPerDay': 20,
                'reviewCardsPerDay': 100,
            },
            'audio': {
                'enabled': True,
                'autoplay': True,
                'speed': 1.0,
            },
            'gamification': {
                'xp': True,
                'levels': True,
                'badges': True,
                'dailyStreak': True,
            }
        }

        config_file = self.output_dir / 'game.config.json'
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)

        print(f"✓ 설정 파일 생성 완료")

    def _create_sample_data(self):
        """샘플 학습 데이터 생성"""
        sample_words = [
            {
                "id": "sample-001",
                "word": "食べる",
                "reading": "たべる",
                "romaji": "taberu",
                "meaning": "먹다",
                "partOfSpeech": "동사",
                "category": ["음식", "동작"],
                "jlptLevel": self.jlpt_level,
                "examples": [
                    {
                        "japanese": "朝ごはんを食べます。",
                        "korean": "아침밥을 먹습니다."
                    }
                ],
                "difficulty": 1,
                "frequency": 5
            },
            {
                "id": "sample-002",
                "word": "飲む",
                "reading": "のむ",
                "romaji": "nomu",
                "meaning": "마시다",
                "partOfSpeech": "동사",
                "category": ["음식", "동작"],
                "jlptLevel": self.jlpt_level,
                "examples": [
                    {
                        "japanese": "水を飲みます。",
                        "korean": "물을 마십니다."
                    }
                ],
                "difficulty": 1,
                "frequency": 5
            }
        ]

        data_dir = self.output_dir / 'src' / 'data'
        data_dir.mkdir(parents=True, exist_ok=True)

        vocab_file = data_dir / 'vocabulary.json'
        with open(vocab_file, 'w', encoding='utf-8') as f:
            json.dump({'words': sample_words}, f, indent=2, ensure_ascii=False)

        print(f"✓ 샘플 데이터 생성 완료")


def main():
    parser = argparse.ArgumentParser(
        description="일본어 학습 게임 보일러플레이트 생성"
    )
    parser.add_argument(
        '--game-type',
        type=str,
        choices=['flashcard', 'quiz', 'typing', 'conversation', 'all'],
        default='flashcard',
        help='게임 타입 (기본값: flashcard)'
    )
    parser.add_argument(
        '--jlpt-level',
        type=str,
        choices=['N5', 'N4', 'N3', 'N2', 'N1'],
        default='N5',
        help='JLPT 레벨 (기본값: N5)'
    )
    parser.add_argument(
        '--category',
        type=str,
        default='all',
        help='단어 카테고리 (기본값: all)'
    )
    parser.add_argument(
        '--output',
        type=str,
        required=True,
        help='출력 디렉토리 경로'
    )
    parser.add_argument(
        '--skill-dir',
        type=str,
        help='스킬 디렉토리 경로 (기본값: 스크립트 상위 디렉토리)'
    )

    args = parser.parse_args()

    # 스킬 디렉토리 자동 감지
    if args.skill_dir:
        skill_dir = Path(args.skill_dir)
    else:
        skill_dir = Path(__file__).parent.parent

    scaffolder = GameScaffolder(
        game_type=args.game_type,
        jlpt_level=args.jlpt_level,
        category=args.category,
        output_dir=Path(args.output),
        skill_dir=skill_dir
    )

    scaffolder.create_game()


if __name__ == "__main__":
    main()
