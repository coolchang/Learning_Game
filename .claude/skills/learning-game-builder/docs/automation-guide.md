# 학습 게임 자동화 가이드

학습 게임 개발의 전 과정을 자동화하는 방법을 안내합니다.

## 🎯 자동화 목표

**수동 작업 8시간 → 자동화 5분**

## 📋 완전 자동화 체크리스트

### 1. 프로젝트 초기화 (⭐⭐⭐⭐⭐)
```bash
# 자동 생성 항목
project/
├── index.html              # 랜딩 페이지
├── game.html              # 메인 게임
├── data/
│   └── vocabulary/        # 데이터 디렉토리
├── scripts/               # Python 스크립트
├── README.md              # 프로젝트 문서
├── CHANGELOG.md           # 작업 일지
└── .gitignore            # Git 설정

# Claude Code 명령
"JLPT 학습 게임 프로젝트 구조 생성해줘"
```

### 2. 데이터 생성 파이프라인 (⭐⭐⭐⭐⭐)
```python
# generate_vocabulary.py - 자동 생성
def generate_jlpt_vocabulary(level, count):
    """레벨별 어휘 생성"""
    return [
        {
            "word": "単語",
            "reading": "たんご",
            "romaji": "tango",
            "meaning": "단어",
            "kanji_breakdown": [...],
            "pos": "noun",
            "example_jp": "新しい単語を覚える",
            "example_kr": "새로운 단어를 외우다",
            "level": 5
        },
        # ... count개
    ]

# split_by_level.py - 자동 생성
def split_vocabulary_by_level(all_words):
    """레벨별로 분할"""
    levels = {
        "N5": all_words[:150],
        "N4": all_words[150:450],
        "N3": all_words[450:950],
        "N2": all_words[950:1550],
        "N1": all_words[1550:2050]
    }
    return levels

# split_by_stage.py - 자동 생성
def split_into_stages(level_words, words_per_stage=30):
    """스테이지별로 분할"""
    stages = []
    for i in range(0, len(level_words), words_per_stage):
        stages.append({
            "stageNumber": len(stages) + 1,
            "words": level_words[i:i+words_per_stage]
        })
    return stages
```

### 3. 게임 코드 생성 (⭐⭐⭐⭐⭐)
```javascript
// 자동 생성되는 핵심 컴포넌트

// 1. 레벨 선택 시스템
function generateLevelButtons(levels) {
    return levels.map(level => `
        <button onclick="selectLevel('${level}')"
                class="level-btn">
            ${level}
        </button>
    `).join('');
}

// 2. 스테이지 시스템
function generateStageButtons(stages) {
    return stages.map(stage => `
        <button onclick="selectStage(${stage.number})"
                class="stage-btn">
            Stage ${stage.number}
        </button>
    `).join('');
}

// 3. 자동 진행 로직
async function autoAdvanceToNextStage() {
    const nextStage = findNextStage();
    if (nextStage) {
        await loadStage(nextStage);
        startAutoPlay();
        return true;
    }

    const nextLevel = findNextLevel();
    if (nextLevel) {
        await loadLevel(nextLevel);
        startAutoPlay();
        return true;
    }

    showCompletionScreen();
    return false;
}
```

### 4. 메타데이터 생성 (⭐⭐⭐⭐⭐)
```python
# generate_stages_metadata.py - 자동 생성
def generate_stages_metadata(levels_data):
    """stages.json 자동 생성"""
    metadata = {
        "version": "1.0",
        "totalStages": 0,
        "totalWords": 0,
        "levels": {}
    }

    for level_name, words in levels_data.items():
        total_words = len(words)
        words_per_stage = 30 if level_name in ["N5", "N4"] else 50
        total_stages = (total_words + words_per_stage - 1) // words_per_stage

        metadata["levels"][level_name] = {
            "totalWords": total_words,
            "totalStages": total_stages,
            "wordsPerStage": words_per_stage,
            "stages": [
                {
                    "stageNumber": i + 1,
                    "wordRange": f"{i*words_per_stage + 1}-{min((i+1)*words_per_stage, total_words)}",
                    "wordCount": min(words_per_stage, total_words - i*words_per_stage)
                }
                for i in range(total_stages)
            ]
        }

        metadata["totalStages"] += total_stages
        metadata["totalWords"] += total_words

    return metadata
```

### 5. GitHub 배포 자동화 (⭐⭐⭐⭐⭐)
```bash
# deploy_github_pages.sh - 자동 생성
#!/bin/bash

echo "🚀 GitHub Pages 자동 배포 시작..."

# 1. Git 초기화
git init
git add .
git commit -m "Initial commit: JLPT Learning Game

- 2050개 단어 학습 시스템
- 5개 레벨 (N5-N1)
- 47개 스테이지
- 플래시카드 + 자동 재생 모드

🤖 Generated with Claude Code"

# 2. GitHub 저장소 연결
git branch -M main
git remote add origin $GITHUB_REPO_URL
git push -u origin main

# 3. GitHub Pages 설정 (gh CLI 사용)
gh repo edit --enable-pages --pages-branch main --pages-path /

# 4. 배포 완료 URL 출력
echo "✅ 배포 완료!"
echo "🌐 URL: https://$(git config remote.origin.url | sed 's/.*github.com\///' | sed 's/\.git//')"
```

### 6. 문서 자동 생성 (⭐⭐⭐⭐⭐)
```markdown
# README.md 템플릿 - 자동 생성
# 🎌 {PROJECT_NAME}

{DESCRIPTION}

## ✨ 주요 기능

- **총 {TOTAL_WORDS}개 단어** 수록
- {LEVEL_SYSTEM} 체계적 구성
- {TOTAL_STAGES}개 스테이지

## 🎮 학습 모드

1. 플래시카드 모드
2. 자동 재생 모드

## 🚀 시작하기

\`\`\`bash
python3 -m http.server 8000
\`\`\`

---
🤖 Generated with learning-game-builder skill
```

## 🔄 자동화 워크플로우 예시

### 예시 1: JLPT 한자 게임 (실제 작업)

**사용자 입력:**
```
JLPT N5-N1 한자 학습 게임 만들어줘.
2000개 단어, GitHub Pages로 배포까지.
```

**Claude Code 자동 실행 (5분):**
```
Step 1: 프로젝트 구조 생성 ✅ (10초)
Step 2: Python 스크립트 생성 ✅ (20초)
  - generate_kanji_data.py
  - split_vocabulary.py
Step 3: 데이터 생성 실행 ✅ (1분)
  - python generate_kanji_data.py → 2050개 단어 생성
  - python split_vocabulary.py → 레벨/스테이지 분할
Step 4: 게임 HTML 생성 ✅ (30초)
  - kanji-game-standalone.html (플래시카드 + 자동재생)
Step 5: 메타데이터 생성 ✅ (5초)
  - stages.json (47개 스테이지)
Step 6: 문서 생성 ✅ (10초)
  - README.md
  - CHANGELOG.md
Step 7: Git 배포 ✅ (2분)
  - git init
  - git push
  - GitHub Pages 설정
Step 8: URL 제공 ✅
  - https://coolchang.github.io/Learning_Game/

총 소요 시간: 5분 ⚡
```

### 예시 2: HSK 중국어 게임

**사용자 입력:**
```
HSK 1-6급 중국어 학습 게임 만들어줘.
5000개 단어, 병음과 한자 포함.
```

**자동화 단계:**
```python
# 1. 레벨 설계
levels = {
    "HSK1": {"words": 150, "stages": 5},
    "HSK2": {"words": 300, "stages": 10},
    "HSK3": {"words": 600, "stages": 12},
    "HSK4": {"words": 1200, "stages": 24},
    "HSK5": {"words": 1500, "stages": 30},
    "HSK6": {"words": 2500, "stages": 50}
}

# 2. 데이터 생성 (AI로 5000개 단어)
vocabulary = generate_hsk_vocabulary(levels)

# 3. 게임 코드 생성
game_html = generate_game_template(
    language="Chinese",
    levels=levels,
    features=["flashcard", "pinyin", "stroke_order"]
)

# 4. 배포
deploy_to_github_pages()
```

## 💡 자동화 베스트 프랙티스

### 1. 파라미터 기반 생성
```yaml
# game_config.yaml
game:
  type: vocabulary_learning
  language: Japanese
  test_system: JLPT
  levels:
    - name: N5
      words: 150
      stages: 5
    - name: N4
      words: 300
      stages: 10
  features:
    - flashcard
    - auto_play
    - tts
    - progress_tracking
  deployment:
    platform: github_pages
```

### 2. 템플릿 기반 코드 생성
```python
def generate_game_from_template(config):
    """설정 파일로 게임 자동 생성"""
    template = load_template("vocabulary-game-template.html")

    # 템플릿 변수 치환
    game_code = template.format(
        TITLE=config['game']['title'],
        LEVELS=json.dumps(config['game']['levels']),
        FEATURES=config['game']['features']
    )

    return game_code
```

### 3. 검증 자동화
```python
def validate_generated_data(data):
    """생성된 데이터 품질 자동 검증"""
    checks = [
        check_word_count(data),
        check_required_fields(data),
        check_encoding(data),
        check_examples(data),
        check_level_distribution(data)
    ]

    return all(checks)
```

## 🎯 자동화 수준별 가이드

### Level 1: 기본 자동화 (⭐)
- 프로젝트 폴더 구조 생성
- 템플릿 HTML 복사

### Level 2: 데이터 자동화 (⭐⭐⭐)
- Python 스크립트로 데이터 생성
- 레벨/스테이지 자동 분할

### Level 3: 완전 자동화 (⭐⭐⭐⭐⭐)
- 데이터 생성 + 게임 코드 + 배포
- 한 번에 온라인 서비스까지

## 📊 자동화 ROI

| 작업 | 수동 | 자동 | 절감 |
|------|------|------|------|
| 프로젝트 구조 | 30분 | 10초 | 99% |
| 데이터 생성 (2000개) | 4시간 | 1분 | 98% |
| 게임 코드 | 2시간 | 30초 | 99% |
| 배포 설정 | 1시간 | 2분 | 96% |
| 문서 작성 | 30분 | 10초 | 99% |
| **총계** | **8시간** | **5분** | **98%** |

## 🚀 다음 단계

1. **스킬 사용 시작**: "JLPT 게임 만들어줘" → Claude Code에 요청
2. **커스터마이징**: 생성된 코드 수정
3. **배포**: GitHub Pages로 공개
4. **피드백**: 자동화 개선 제안

---

**이 가이드로 학습 게임 개발 속도를 10배 향상시키세요!** ⚡
