# 레벨/스테이지 시스템 아키텍처

계층적 학습 구조 설계 및 구현 가이드

## 🏗️ 아키텍처 개요

```
Level (레벨)
  ├── Stage 1 (스테이지)
  │   ├── Word 1
  │   ├── Word 2
  │   └── Word N
  ├── Stage 2
  │   └── ...
  └── Stage M
```

## 📊 레벨 시스템 설계

### 1. 레벨 정의

#### JLPT (일본어)
```javascript
const JLPT_LEVELS = {
  N5: {
    difficulty: 1,
    targetWords: 150,
    description: "초급 - 기본 한자와 어휘"
  },
  N4: {
    difficulty: 2,
    targetWords: 300,
    description: "초중급 - 일상 회화"
  },
  N3: {
    difficulty: 3,
    targetWords: 500,
    description: "중급 - 일상 및 비즈니스"
  },
  N2: {
    difficulty: 4,
    targetWords: 600,
    description: "중상급 - 전문적 내용"
  },
  N1: {
    difficulty: 5,
    targetWords: 500,
    description: "고급 - 고급 어휘 및 한자"
  }
};
```

#### HSK (중국어)
```javascript
const HSK_LEVELS = {
  HSK1: { targetWords: 150, description: "기초" },
  HSK2: { targetWords: 300, description: "초급" },
  HSK3: { targetWords: 600, description: "중급" },
  HSK4: { targetWords: 1200, description: "중상급" },
  HSK5: { targetWords: 2500, description: "고급" },
  HSK6: { targetWords: 5000, description: "최상급" }
};
```

#### CEFR (유럽 언어 표준)
```javascript
const CEFR_LEVELS = {
  A1: { targetWords: 500, description: "기초 사용자" },
  A2: { targetWords: 1000, description: "초급 사용자" },
  B1: { targetWords: 2000, description: "중급 사용자" },
  B2: { targetWords: 3000, description: "중상급 사용자" },
  C1: { targetWords: 4000, description: "고급 사용자" },
  C2: { targetWords: 5000, description: "숙련된 사용자" }
};
```

### 2. 스테이지 분할 알고리즘

#### 기본 분할 공식
```python
def calculate_stages(total_words, words_per_stage=30):
    """최적 스테이지 수 계산"""

    # 1. 기본 계산
    total_stages = (total_words + words_per_stage - 1) // words_per_stage

    # 2. 최소/최대 제약
    if total_words < 30:
        return 1  # 최소 1개 스테이지

    # 3. 균등 분배
    words_per_stage_adjusted = total_words // total_stages

    return {
        "totalStages": total_stages,
        "wordsPerStage": words_per_stage_adjusted,
        "remainder": total_words % total_stages
    }
```

#### 스테이지 크기 권장사항
| 레벨 | 스테이지 크기 | 이유 |
|------|--------------|------|
| 초급 (N5, HSK1) | 20-30개 | 학습 부담 최소화 |
| 중급 (N3, HSK3) | 30-50개 | 적당한 학습량 |
| 고급 (N1, HSK6) | 50-100개 | 효율성 우선 |

### 3. 메타데이터 구조 (stages.json)

```json
{
  "version": "1.0",
  "totalStages": 47,
  "totalWords": 2050,
  "levels": {
    "N5": {
      "difficulty": 1,
      "totalWords": 150,
      "totalStages": 5,
      "wordsPerStage": 30,
      "stages": [
        {
          "stageNumber": 1,
          "name": "기본 숫자와 시간",
          "wordRange": "1-30",
          "wordCount": 30,
          "description": "숫자, 요일, 시간 표현"
        },
        {
          "stageNumber": 2,
          "name": "일상 동사",
          "wordRange": "31-60",
          "wordCount": 30
        }
      ]
    },
    "N4": {
      "difficulty": 2,
      "totalWords": 300,
      "totalStages": 10,
      "wordsPerStage": 30,
      "stages": [...]
    }
  }
}
```

## 🎮 게임 플로우 구현

### 1. 레벨 선택 UI

```javascript
async function initializeLevelSelection() {
    const levelsContainer = document.getElementById('levels');
    const levels = Object.keys(stagesMetadata.levels);

    levelsContainer.innerHTML = levels.map(level => `
        <button class="level-btn level-${level.toLowerCase()}"
                onclick="selectLevel('${level}')">
            <div class="level-name">${level}</div>
            <div class="level-info">
                ${stagesMetadata.levels[level].totalWords}개 단어
                · ${stagesMetadata.levels[level].totalStages}개 스테이지
            </div>
        </button>
    `).join('');
}
```

### 2. 스테이지 선택 UI

```javascript
async function displayStages(level) {
    const stagesContainer = document.getElementById('stages');
    const levelData = stagesMetadata.levels[level];

    stagesContainer.innerHTML = levelData.stages.map(stage => `
        <button class="stage-btn"
                onclick="selectStage(${stage.stageNumber})">
            <div class="stage-number">Stage ${stage.stageNumber}</div>
            <div class="stage-name">${stage.name || ''}</div>
            <div class="stage-progress">
                ${stage.wordCount}개 단어
            </div>
        </button>
    `).join('');
}
```

### 3. 자동 진행 로직

```javascript
async function autoAdvanceToNextStage() {
    if (!stagesMetadata) return false;

    const currentLevel = selectedLevel;
    const levelMeta = stagesMetadata.levels[currentLevel];

    // 1. 현재 레벨에서 다음 스테이지 찾기
    const currentStageIndex = levelMeta.stages.findIndex(
        s => s.stageNumber === selectedStage
    );

    if (currentStageIndex < levelMeta.stages.length - 1) {
        // 다음 스테이지로 이동
        const nextStage = levelMeta.stages[currentStageIndex + 1];

        updateStatus(`⏭️ 다음 스테이지로 이동 중... (Stage ${nextStage.stageNumber})`);

        await new Promise(resolve => setTimeout(resolve, 2000));
        await selectStage(nextStage.stageNumber);

        startAutoPlay();
        return true;
    }

    // 2. 다음 레벨 찾기
    const levels = Object.keys(stagesMetadata.levels);
    const currentLevelIndex = levels.indexOf(currentLevel);

    if (currentLevelIndex < levels.length - 1) {
        // 다음 레벨로 이동
        const nextLevel = levels[currentLevelIndex + 1];

        updateStatus(`🎯 다음 레벨로 이동 중... (${nextLevel})`);

        await new Promise(resolve => setTimeout(resolve, 3000));
        await selectLevel(nextLevel);

        startAutoPlay();
        return true;
    }

    // 3. 모든 레벨 완료
    showCompletionScreen();
    return false;
}
```

## 📊 데이터 구조

### 1. 레벨 데이터 (n5.json 예시)

```json
[
  {
    "word": "一",
    "reading": "いち",
    "romaji": "ichi",
    "meaning": "하나, 일",
    "kanji_breakdown": [
      {
        "kanji": "一",
        "korean_hanja": "일",
        "korean_meaning": "한 일",
        "japanese_reading": "いち"
      }
    ],
    "pos": "수사",
    "example_jp": "一つください",
    "example_kr": "하나 주세요",
    "level": 5
  }
]
```

### 2. 진도 추적 (LocalStorage)

```javascript
// 진도 저장
function saveProgress(level, stage, wordIndex) {
    const progress = {
        currentLevel: level,
        currentStage: stage,
        currentWord: wordIndex,
        lastUpdated: new Date().toISOString()
    };

    localStorage.setItem('learningProgress', JSON.stringify(progress));
}

// 진도 불러오기
function loadProgress() {
    const saved = localStorage.getItem('learningProgress');
    return saved ? JSON.parse(saved) : null;
}

// 레벨별 완료 상태
function getLevelCompletion(level) {
    const completed = JSON.parse(localStorage.getItem(`completed_${level}`)) || [];
    const total = stagesMetadata.levels[level].totalStages;

    return {
        completed: completed.length,
        total: total,
        percentage: (completed.length / total * 100).toFixed(1)
    };
}
```

## 🎨 UI/UX 디자인 패턴

### 1. 레벨별 색상 테마

```css
/* N5 - 녹색 (초급) */
.level-n5 {
    background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
}

/* N4 - 파란색 (초중급) */
.level-n4 {
    background: linear-gradient(135deg, #60a5fa 0%, #3b82f6 100%);
}

/* N3 - 보라색 (중급) */
.level-n3 {
    background: linear-gradient(135deg, #a78bfa 0%, #8b5cf6 100%);
}

/* N2 - 주황색 (중상급) */
.level-n2 {
    background: linear-gradient(135deg, #fb923c 0%, #f97316 100%);
}

/* N1 - 빨간색 (고급) */
.level-n1 {
    background: linear-gradient(135deg, #f87171 0%, #ef4444 100%);
}
```

### 2. 진도 바 시각화

```javascript
function updateProgressBar(current, total) {
    const percentage = (current / total * 100).toFixed(1);
    const progressBar = document.getElementById('progress-bar');

    progressBar.style.width = `${percentage}%`;
    progressBar.textContent = `${current} / ${total} (${percentage}%)`;
}
```

## 🔄 스테이지 전환 애니메이션

```css
@keyframes stageTransition {
    0% {
        opacity: 1;
        transform: translateX(0);
    }
    50% {
        opacity: 0;
        transform: translateX(-50px);
    }
    100% {
        opacity: 1;
        transform: translateX(0);
    }
}

.stage-transition {
    animation: stageTransition 0.5s ease-in-out;
}
```

## 📈 난이도 조정 전략

### 1. 레벨별 학습량
```python
DIFFICULTY_SETTINGS = {
    "beginner": {
        "words_per_session": 10,
        "review_frequency": "high",
        "hints": "enabled"
    },
    "intermediate": {
        "words_per_session": 20,
        "review_frequency": "medium",
        "hints": "optional"
    },
    "advanced": {
        "words_per_session": 50,
        "review_frequency": "low",
        "hints": "disabled"
    }
}
```

### 2. 적응형 난이도
```javascript
function adjustDifficulty(userPerformance) {
    if (userPerformance.accuracy > 0.9) {
        // 너무 쉬움 - 단어 수 증가
        increaseWordsPerStage();
    } else if (userPerformance.accuracy < 0.6) {
        // 너무 어려움 - 단어 수 감소
        decreaseWordsPerStage();
    }
}
```

## 🎯 베스트 프랙티스

### 1. 스테이지 크기 결정
```python
def optimal_stage_size(level_difficulty, total_words):
    """레벨 난이도에 따른 최적 스테이지 크기"""

    if level_difficulty <= 2:  # 초급
        return min(30, total_words)
    elif level_difficulty <= 4:  # 중급
        return min(50, total_words)
    else:  # 고급
        return min(100, total_words)
```

### 2. 레벨 간 균형
```python
def balance_levels(total_words, num_levels):
    """레벨별 단어 수 균형있게 분배"""

    # 지수 분포 (초급에 더 많이)
    distribution = [
        0.1,  # 10%
        0.15, # 15%
        0.25, # 25%
        0.3,  # 30%
        0.2   # 20%
    ]

    return [int(total_words * ratio) for ratio in distribution]
```

## 📦 완성 예시

### JLPT 한자 학습 게임 (실제 구현)
```
총 단어: 2050개
총 스테이지: 47개

N5: 150개 (5 stages × 30 words)
N4: 300개 (10 stages × 30 words)
N3: 500개 (10 stages × 50 words)
N2: 600개 (12 stages × 50 words)
N1: 500개 (10 stages × 50 words)

온라인: https://coolchang.github.io/Learning_Game/
```

---

**이 아키텍처로 체계적인 학습 시스템을 구축하세요!** 🏗️
