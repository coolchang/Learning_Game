# 일본어 학습 게임 스킬 개발 기획서

## 문서 정보
- **프로젝트명**: Japanese Learning Game Skill
- **버전**: 1.0
- **작성일**: 2025-10-25
- **목적**: Claude Code 스킬로 일본어 학습 게임을 체계적으로 생성하는 시스템 개발

---

## 1. 프로젝트 개요 및 목표

### 1.1 프로젝트 비전
소리 중심의 효과적인 일본어 학습을 위한 게임화된 웹 애플리케이션을 자동 생성하는 Claude Code 스킬 개발

### 1.2 핵심 목표
- **학습 효과성**: 간격 반복 학습(SRS)과 음성 중심 학습으로 장기 기억 형성
- **몰입도**: 게임화 요소를 통한 지속적인 학습 동기 부여
- **재사용성**: 다양한 일본어 학습 게임을 빠르게 생성할 수 있는 스킬 프레임워크
- **확장성**: 웹에서 모바일로 확장 가능한 아키텍처

### 1.3 성공 지표
- 스킬을 사용하여 5분 내에 기본 학습 게임 생성 가능
- 학습자의 단어 기억률 향상 (SRS 적용)
- 게임화 요소로 인한 일일 재방문율 증가

---

## 2. 타겟 사용자 및 학습 시나리오

### 2.1 타겟 사용자
- **주 타겟**: 일본어 초급~중급 학습자 (JLPT N5-N3)
- **부 타겟**: 일본어 교육자 (학습 콘텐츠 제작)

### 2.2 사용자 페르소나

#### 페르소나 1: 자기주도 학습자
- 나이: 20-35세
- 목표: JLPT N5/N4 합격
- 학습 시간: 일 30분~1시간
- 니즈: 출퇴근 시간 활용, 즉각적 피드백, 진행도 추적

#### 페르소나 2: 일본어 교육자
- 나이: 30-50세
- 목표: 학생들을 위한 맞춤형 학습 게임 제작
- 니즈: 빠른 콘텐츠 생성, 학습 데이터 추적

### 2.3 핵심 학습 시나리오

#### 시나리오 A: 단어 학습
```
사용자 입력: "음식 관련 N5 단어 50개로 플래시카드 게임 만들어줘"

스킬 생성물:
- 음성 발음 지원 플래시카드
- 4지선다 퀴즈
- 타이핑 연습
- SRS 기반 복습 스케줄링
```

#### 시나리오 B: 회화 학습
```
사용자 입력: "레스토랑에서 주문하기 회화 연습 게임 만들어줘"

스킬 생성물:
- 대화 시뮬레이션
- 음성 인식 발음 평가
- 상황별 표현 학습
- 역할극 모드
```

#### 시나리오 C: 종합 복습
```
사용자 입력: "오늘 복습할 단어 게임 시작"

스킬 생성물:
- SRS 알고리즘 기반 복습 큐
- 다양한 게임 모드 믹스
- 진행도 및 성취도 시각화
```

---

## 3. 핵심 기능 및 게임 메커니즘 설계

### 3.1 학습 모드

#### 3.1.1 단어 학습 모드
1. **플래시카드**
   - 앞면: 일본어 단어 + 음성
   - 뒷면: 한국어 뜻 + 예문
   - 기능: 자동 음성 재생, 수동 재생, 속도 조절

2. **4지선다 퀴즈**
   - 음성 듣고 정답 선택
   - 한자 보고 읽기 선택
   - 뜻 보고 단어 선택

3. **타이핑 게임**
   - 음성 듣고 히라가나/로마자 입력
   - 실시간 정확도 체크
   - 타이머 챌린지

4. **매칭 게임**
   - 단어-뜻 매칭
   - 한자-읽기 매칭
   - 시간 제한 모드

#### 3.1.2 회화 학습 모드
1. **대화 시뮬레이션**
   - NPC 대화 재생
   - 선택지 기반 응답
   - 상황별 시나리오

2. **발음 연습**
   - 음성 인식 기반 평가
   - 발음 정확도 피드백
   - 억양 시각화

3. **빈칸 채우기**
   - 문맥 속 조사/표현 학습
   - 힌트 시스템
   - 오답 노트

### 3.2 게임 메커니즘

#### 3.2.1 진행 시스템
```
레벨 1 (초보) → 레벨 2 (견습) → ... → 레벨 10 (마스터)

경험치 획득:
- 정답: 10 XP
- 첫 시도 정답: 15 XP
- 연속 정답: +5 XP (콤보)
- 빠른 정답: +3 XP
```

#### 3.2.2 보상 시스템
1. **즉시 보상**
   - 정답 효과음 + 시각 효과
   - XP 획득 애니메이션
   - 연속 정답 콤보 표시

2. **단기 보상**
   - 일일 목표 달성 배지
   - 연속 학습 일수 (스트릭)
   - 일일 미션 보상

3. **장기 보상**
   - 레벨업 보상 (새 게임 모드 해금)
   - 마일스톤 배지 (100단어, 1000단어 등)
   - 리더보드 (선택적)

#### 3.2.3 게임화 요소
- **스트릭 시스템**: 연속 학습 일수 추적
- **일일 미션**: "오늘 20단어 학습", "5분 연속 학습" 등
- **배지 시스템**: 50+ 종류의 달성 배지
- **프로그레스 바**: 시각적 진행도 표시
- **사운드 피드백**: 정답/오답/레벨업 효과음

---

## 4. 학습 이론 및 SRS 알고리즘 설계

### 4.1 학습 이론적 기반

#### 4.1.1 간격 반복 학습 (Spaced Repetition)
- **원리**: 망각 곡선을 고려한 최적 복습 타이밍
- **효과**: 장기 기억 형성 극대화

#### 4.1.2 음성 중심 학습 (Audio-First Learning)
- **원리**: 듣기와 발음을 우선한 자연스러운 언어 습득
- **구현**: 모든 단어/문장에 음성 지원

#### 4.1.3 능동적 상기 (Active Recall)
- **원리**: 수동적 읽기보다 능동적 회상이 효과적
- **구현**: 퀴즈, 타이핑, 빈칸 채우기

#### 4.1.4 즉각적 피드백
- **원리**: 즉시 피드백으로 학습 효과 극대화
- **구현**: 실시간 정답/오답 표시, 설명 제공

### 4.2 SRS 알고리즘 설계

#### 4.2.1 SuperMemo SM-2 기반 알고리즘
```python
# 간격 계산 공식
def calculate_next_interval(quality, repetition, easiness, interval):
    """
    quality: 0-5 (사용자 응답 품질)
      5: 완벽
      4: 약간 고민 후 정답
      3: 어렵게 정답
      2: 틀렸지만 알 것 같음
      1: 틀렸고 어려움
      0: 완전히 모름

    repetition: 연속 정답 횟수
    easiness: 난이도 계수 (1.3-2.5)
    interval: 현재 복습 간격 (일)
    """

    if quality < 3:
        # 틀린 경우: 처음부터 다시
        repetition = 0
        interval = 1
    else:
        if repetition == 0:
            interval = 1
        elif repetition == 1:
            interval = 6
        else:
            interval = interval * easiness

        repetition += 1

    # 난이도 계수 조정
    easiness = easiness + (0.1 - (5 - quality) * (0.08 + (5 - quality) * 0.02))
    easiness = max(1.3, min(2.5, easiness))

    return {
        'interval': interval,
        'repetition': repetition,
        'easiness': easiness,
        'next_review': now + timedelta(days=interval)
    }
```

#### 4.2.2 카드 상태 관리
```
[New] → [Learning] → [Review] → [Mastered]
          ↑              ↓
          └──── [Lapsed] ←┘

- New: 처음 보는 카드 (간격: 즉시)
- Learning: 학습 중 (간격: 1일, 3일)
- Review: 복습 중 (간격: 6일, 14일, 30일...)
- Lapsed: 잊어버림 (간격: 1일로 초기화)
- Mastered: 숙달 (간격: 90일+)
```

#### 4.2.3 일일 학습량 조절
```javascript
const dailyQueue = {
  newCards: 20,        // 신규 카드 최대
  reviewCards: 100,    // 복습 카드 최대

  priority: [
    'overdue',         // 기한 지난 복습
    'due_today',       // 오늘 복습
    'new_cards'        // 신규 학습
  ]
}
```

### 4.3 난이도 적응 시스템
```javascript
// 사용자 실력 추적
const userProficiency = {
  accuracy: 0.85,      // 정답률
  avgResponseTime: 3.2, // 평균 응답 시간 (초)

  // 난이도 자동 조절
  adjustDifficulty() {
    if (accuracy > 0.9 && avgResponseTime < 3) {
      return 'increase'; // 더 어려운 단어 제공
    } else if (accuracy < 0.7) {
      return 'decrease'; // 더 쉬운 단어 제공
    }
    return 'maintain';
  }
}
```

---

## 5. 기술 스택 및 아키텍처 설계

### 5.1 기술 스택

#### 5.1.1 프론트엔드
```
Core:
- React 18+ (UI 프레임워크)
- TypeScript (타입 안정성)
- Vite (빌드 도구)

상태 관리:
- Zustand (경량 상태 관리)
- React Query (서버 상태 관리)

UI/스타일:
- Tailwind CSS (유틸리티 CSS)
- Framer Motion (애니메이션)
- Radix UI (접근성 높은 컴포넌트)

오디오:
- Web Speech API (TTS)
- Howler.js (효과음 관리)
- Web Audio API (고급 오디오 처리)
```

#### 5.1.2 백엔드 (선택적)
```
- Firebase / Supabase (BaaS)
  - Authentication
  - Realtime Database
  - Cloud Functions
  - Cloud Storage

대안 (Self-hosted):
- Node.js + Express
- PostgreSQL
- Redis (캐싱)
```

#### 5.1.3 모바일 확장
```
- React Native (코드 재사용)
- Expo (개발 도구)
- Native Audio API
```

### 5.2 시스템 아키텍처

#### 5.2.1 클라이언트 아키텍처
```
┌─────────────────────────────────────────┐
│         Presentation Layer              │
│  ┌──────────┐  ┌──────────┐            │
│  │ Game UI  │  │ Progress │            │
│  │Components│  │ Dashboard│            │
│  └──────────┘  └──────────┘            │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│         Business Logic Layer            │
│  ┌──────────┐  ┌──────────┐            │
│  │   SRS    │  │  Game    │            │
│  │  Engine  │  │ Logic    │            │
│  └──────────┘  └──────────┘            │
└─────────────────────────────────────────┘
                  ↓
┌─────────────────────────────────────────┐
│           Data Layer                    │
│  ┌──────────┐  ┌──────────┐            │
│  │  Local   │  │  Cloud   │            │
│  │ Storage  │  │  Sync    │            │
│  └──────────┘  └──────────┘            │
└─────────────────────────────────────────┘
```

#### 5.2.2 데이터 흐름
```
사용자 입력
    ↓
Game Component
    ↓
게임 로직 처리
    ↓
SRS Engine 업데이트
    ↓
State 업데이트 (Zustand)
    ↓
Local Storage 저장
    ↓
Cloud Sync (백그라운드)
```

#### 5.2.3 오프라인 우선 아키텍처
```javascript
// Progressive Web App
- Service Worker (오프라인 캐싱)
- IndexedDB (로컬 데이터베이스)
- Background Sync (네트워크 복구 시 동기화)

// 동기화 전략
const syncStrategy = {
  mode: 'offline-first',

  write: async (data) => {
    await saveToLocal(data);      // 1. 로컬 저장 (즉시)
    await queueForSync(data);     // 2. 동기화 큐에 추가
  },

  read: async () => {
    const local = await loadFromLocal();  // 로컬 우선
    syncInBackground();                   // 백그라운드 동기화
    return local;
  }
}
```

### 5.3 모듈 구조
```
src/
├── components/          # React 컴포넌트
│   ├── games/          # 게임 컴포넌트
│   │   ├── Flashcard.tsx
│   │   ├── MultipleChoice.tsx
│   │   ├── TypingGame.tsx
│   │   └── Matching.tsx
│   ├── ui/             # 공통 UI
│   └── layout/         # 레이아웃
│
├── hooks/              # Custom React Hooks
│   ├── useAudio.ts
│   ├── useSRS.ts
│   └── useGameState.ts
│
├── lib/                # 핵심 로직
│   ├── srs/           # SRS 엔진
│   │   ├── algorithm.ts
│   │   ├── scheduler.ts
│   │   └── types.ts
│   ├── audio/         # 오디오 시스템
│   │   ├── tts.ts
│   │   ├── player.ts
│   │   └── recorder.ts
│   └── game/          # 게임 로직
│       ├── scoring.ts
│       ├── progression.ts
│       └── achievements.ts
│
├── data/              # 학습 데이터
│   ├── vocabulary/    # 단어 데이터
│   ├── conversations/ # 회화 데이터
│   └── schemas/       # 데이터 스키마
│
├── stores/            # 상태 관리
│   ├── gameStore.ts
│   ├── userStore.ts
│   └── srsStore.ts
│
└── utils/             # 유틸리티
    ├── storage.ts
    ├── sync.ts
    └── helpers.ts
```

---

## 6. 데이터 구조 및 콘텐츠 설계

### 6.1 핵심 데이터 모델

#### 6.1.1 단어 카드 (VocabularyCard)
```typescript
interface VocabularyCard {
  id: string;

  // 기본 정보
  word: string;              // "食べる"
  reading: string;           // "たべる"
  romaji: string;           // "taberu"
  meaning: string;          // "먹다"

  // 추가 정보
  partOfSpeech: string;     // "동사"
  jlptLevel: 'N5' | 'N4' | 'N3' | 'N2' | 'N1';
  category: string[];       // ["음식", "동작"]

  // 예문
  examples: {
    japanese: string;
    korean: string;
    audio?: string;
  }[];

  // 오디오
  audio: {
    word: string;           // URL or base64
    slow?: string;          // 느린 발음
  };

  // 관련 단어
  related: string[];        // 관련 단어 ID
  antonyms?: string[];      // 반의어
  synonyms?: string[];      // 유의어

  // 메타데이터
  difficulty: number;       // 1-5
  frequency: number;        // 사용 빈도
  tags: string[];
}
```

#### 6.1.2 SRS 학습 데이터 (StudyCard)
```typescript
interface StudyCard {
  cardId: string;           // VocabularyCard ID
  userId: string;

  // SRS 상태
  status: 'new' | 'learning' | 'review' | 'lapsed' | 'mastered';

  // SRS 파라미터
  easiness: number;         // 1.3 - 2.5
  interval: number;         // 다음 복습까지 일수
  repetitions: number;      // 연속 정답 횟수

  // 스케줄
  nextReview: Date;
  lastReview: Date;
  createdAt: Date;

  // 학습 이력
  history: {
    timestamp: Date;
    quality: 0 | 1 | 2 | 3 | 4 | 5;
    responseTime: number;   // 밀리초
    gameMode: string;       // 어떤 게임으로 학습했는지
  }[];

  // 통계
  stats: {
    totalReviews: number;
    correctCount: number;
    incorrectCount: number;
    averageResponseTime: number;
    masteryScore: number;   // 0-100
  };
}
```

#### 6.1.3 회화 시나리오 (ConversationScenario)
```typescript
interface ConversationScenario {
  id: string;
  title: string;            // "레스토랑에서 주문하기"
  description: string;
  category: string;         // "일상", "여행", "비즈니스"
  jlptLevel: 'N5' | 'N4' | 'N3' | 'N2' | 'N1';

  // 대화 흐름
  dialogues: {
    id: string;
    speaker: 'user' | 'npc';
    character?: string;     // NPC 이름

    // 텍스트
    japanese: string;
    reading: string;
    korean: string;

    // 오디오
    audio: string;

    // 선택지 (user 턴인 경우)
    choices?: {
      id: string;
      japanese: string;
      korean: string;
      audio: string;
      nextDialogueId: string;
      feedback?: string;    // 선택 시 피드백
    }[];
  }[];

  // 학습 포인트
  keyPhrases: {
    phrase: string;
    meaning: string;
    usage: string;
  }[];

  // 난이도
  difficulty: number;
  estimatedTime: number;    // 분
}
```

#### 6.1.4 사용자 프로필 (UserProfile)
```typescript
interface UserProfile {
  userId: string;
  username: string;
  email?: string;

  // 학습 설정
  settings: {
    dailyGoal: number;          // 일일 학습 카드 수
    newCardsPerDay: number;     // 신규 카드 수
    audioAutoplay: boolean;
    audioSpeed: number;         // 0.5 - 2.0
    interfaceLanguage: 'ko' | 'en' | 'ja';
  };

  // 진행도
  progress: {
    currentLevel: number;
    currentXP: number;
    totalXP: number;
    streak: number;             // 연속 학습 일수
    longestStreak: number;
    studyDays: number;          // 총 학습 일수
  };

  // 통계
  stats: {
    totalCards: number;
    masteredCards: number;
    learningCards: number;

    totalStudyTime: number;     // 분
    averageAccuracy: number;

    byLevel: {
      [key: string]: {          // 'N5', 'N4', etc.
        total: number;
        mastered: number;
      }
    };
  };

  // 게임화
  achievements: string[];       // 달성한 배지 ID
  badges: {
    id: string;
    unlockedAt: Date;
  }[];

  // 메타
  createdAt: Date;
  lastLoginAt: Date;
}
```

#### 6.1.5 게임 세션 (GameSession)
```typescript
interface GameSession {
  id: string;
  userId: string;
  gameMode: string;             // 'flashcard', 'quiz', 'typing', etc.

  // 세션 정보
  startedAt: Date;
  endedAt?: Date;
  duration: number;             // 초

  // 카드 목록
  cards: string[];              // StudyCard IDs

  // 결과
  results: {
    cardId: string;
    correct: boolean;
    quality: 0 | 1 | 2 | 3 | 4 | 5;
    responseTime: number;
    attempts: number;
  }[];

  // 통계
  summary: {
    totalCards: number;
    correctCards: number;
    accuracy: number;
    averageResponseTime: number;
    xpEarned: number;
  };

  // 게임 상태
  combo: number;                // 최대 연속 정답
  perfectAnswers: number;       // 첫 시도 정답
}
```

### 6.2 학습 콘텐츠 구조

#### 6.2.1 JLPT 레벨별 단어 데이터베이스
```
data/vocabulary/
├── n5/
│   ├── basic-greetings.json       (50 words)
│   ├── numbers.json               (100 words)
│   ├── time-date.json             (80 words)
│   ├── food-drinks.json           (120 words)
│   ├── daily-activities.json      (150 words)
│   ├── family.json                (40 words)
│   └── ... (총 800 words)
│
├── n4/
│   ├── emotions.json              (100 words)
│   ├── weather.json               (60 words)
│   ├── travel.json                (150 words)
│   ├── shopping.json              (120 words)
│   └── ... (총 1,500 words)
│
├── n3/
│   └── ... (총 3,000 words)
│
└── metadata.json                  (카테고리, 태그 정의)
```

#### 6.2.2 회화 시나리오 데이터베이스
```
data/conversations/
├── daily-life/
│   ├── greeting-introduction.json
│   ├── shopping-convenience.json
│   ├── restaurant-ordering.json
│   └── asking-directions.json
│
├── travel/
│   ├── airport-checkin.json
│   ├── hotel-checkin.json
│   ├── taxi-directions.json
│   └── sightseeing.json
│
├── business/
│   ├── self-introduction.json
│   ├── phone-calls.json
│   └── meetings.json
│
└── metadata.json
```

#### 6.2.3 오디오 에셋 구조
```
public/audio/
├── words/
│   ├── n5/
│   │   └── [word-id].mp3
│   └── n4/
│       └── [word-id].mp3
│
├── sfx/                         # 효과음
│   ├── correct.mp3
│   ├── wrong.mp3
│   ├── levelup.mp3
│   ├── combo.mp3
│   └── achievement.mp3
│
└── tts/                         # 동적 생성 TTS 캐시
    └── [hash].mp3
```

### 6.3 데이터 샘플

#### 6.3.1 단어 데이터 샘플 (N5 - 음식)
```json
{
  "category": "food-drinks",
  "jlptLevel": "N5",
  "words": [
    {
      "id": "n5-food-001",
      "word": "食べる",
      "reading": "たべる",
      "romaji": "taberu",
      "meaning": "먹다",
      "partOfSpeech": "동사",
      "category": ["음식", "동작"],
      "examples": [
        {
          "japanese": "朝ごはんを食べます。",
          "reading": "あさごはんをたべます。",
          "korean": "아침밥을 먹습니다.",
          "audio": "/audio/examples/n5-food-001-ex1.mp3"
        }
      ],
      "audio": {
        "word": "/audio/words/n5/n5-food-001.mp3",
        "slow": "/audio/words/n5/n5-food-001-slow.mp3"
      },
      "related": ["n5-food-002", "n5-food-010"],
      "difficulty": 1,
      "frequency": 5,
      "tags": ["일상", "필수", "동사"]
    },
    {
      "id": "n5-food-002",
      "word": "飲む",
      "reading": "のむ",
      "romaji": "nomu",
      "meaning": "마시다",
      "partOfSpeech": "동사",
      "category": ["음식", "동작"],
      "examples": [
        {
          "japanese": "水を飲みます。",
          "reading": "みずをのみます。",
          "korean": "물을 마십니다.",
          "audio": "/audio/examples/n5-food-002-ex1.mp3"
        }
      ],
      "audio": {
        "word": "/audio/words/n5/n5-food-002.mp3"
      },
      "related": ["n5-food-001", "n5-food-015"],
      "difficulty": 1,
      "frequency": 5,
      "tags": ["일상", "필수", "동사"]
    }
  ]
}
```

#### 6.3.2 회화 시나리오 샘플
```json
{
  "id": "conv-restaurant-001",
  "title": "레스토랑에서 주문하기",
  "description": "레스토랑에서 메뉴를 보고 음식을 주문하는 상황",
  "category": "일상",
  "jlptLevel": "N5",
  "difficulty": 2,
  "estimatedTime": 5,

  "dialogues": [
    {
      "id": "d1",
      "speaker": "npc",
      "character": "웨이터",
      "japanese": "いらっしゃいませ。何名様ですか？",
      "reading": "いらっしゃいませ。なんめいさまですか？",
      "korean": "어서오세요. 몇 분이세요?",
      "audio": "/audio/conv/rest-001-d1.mp3"
    },
    {
      "id": "d2",
      "speaker": "user",
      "choices": [
        {
          "id": "c1",
          "japanese": "一人です。",
          "korean": "한 명입니다.",
          "audio": "/audio/conv/rest-001-d2-c1.mp3",
          "nextDialogueId": "d3",
          "feedback": "완벽해요! 一人 (ひとり)는 '한 명'이라는 뜻입니다."
        },
        {
          "id": "c2",
          "japanese": "二人です。",
          "korean": "두 명입니다.",
          "audio": "/audio/conv/rest-001-d2-c2.mp3",
          "nextDialogueId": "d3",
          "feedback": "좋아요! 二人 (ふたり)는 '두 명'이라는 뜻입니다."
        }
      ]
    },
    {
      "id": "d3",
      "speaker": "npc",
      "character": "웨이터",
      "japanese": "こちらへどうぞ。",
      "reading": "こちらへどうぞ。",
      "korean": "이쪽으로 오세요.",
      "audio": "/audio/conv/rest-001-d3.mp3"
    }
  ],

  "keyPhrases": [
    {
      "phrase": "いらっしゃいませ",
      "meaning": "어서오세요",
      "usage": "손님을 맞이할 때 사용하는 정중한 표현"
    },
    {
      "phrase": "何名様ですか",
      "meaning": "몇 분이세요?",
      "usage": "레스토랑에서 인원수를 물을 때"
    }
  ]
}
```

---

## 7. UI/UX 및 게임화 요소 설계

### 7.1 UI 디자인 원칙

#### 7.1.1 핵심 원칙
1. **명확성 (Clarity)**: 학습 상황과 진행도를 명확히 표시
2. **일관성 (Consistency)**: 모든 게임 모드에서 일관된 UI/UX
3. **접근성 (Accessibility)**: 다양한 사용자를 위한 접근성 고려
4. **반응성 (Responsiveness)**: 모바일/태블릿/데스크톱 지원

#### 7.1.2 디자인 시스템
```typescript
// 색상 팔레트
const colors = {
  primary: {
    50: '#eff6ff',
    500: '#3b82f6',
    600: '#2563eb',
  },
  success: '#10b981',    // 정답
  error: '#ef4444',      // 오답
  warning: '#f59e0b',    // 주의

  // 게임화 요소
  xp: '#8b5cf6',         // XP 바
  streak: '#f97316',     // 스트릭
  level: '#eab308',      // 레벨
}

// 타이포그래피
const typography = {
  japanese: {
    fontFamily: "'Noto Sans JP', sans-serif",
    sizes: {
      word: '3rem',
      sentence: '1.5rem',
      reading: '1.25rem',
    }
  },
  korean: {
    fontFamily: "'Noto Sans KR', sans-serif",
    sizes: {
      heading: '2rem',
      body: '1rem',
      caption: '0.875rem',
    }
  }
}
```

### 7.2 화면 구조

#### 7.2.1 메인 대시보드
```
┌─────────────────────────────────────────┐
│  [Logo]                   [Settings] 👤 │
├─────────────────────────────────────────┤
│                                         │
│  안녕하세요, 학습자님! 👋                  │
│  연속 학습 7일째 🔥                       │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  오늘의 학습 진행도                  │  │
│  │  ████████████░░░░░   15 / 20      │  │
│  │                                   │  │
│  │  복습 대기: 12장                    │  │
│  │  신규 단어: 8장                     │  │
│  └───────────────────────────────────┘  │
│                                         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │ 단어    │  │ 회화    │  │ 복습    │ │
│  │ 학습    │  │ 연습    │  │ 게임    │ │
│  └─────────┘  └─────────┘  └─────────┘ │
│                                         │
│  최근 학습 통계 📊                        │
│  정답률: 87% | 평균 시간: 3.2초           │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  배지 & 업적                        │  │
│  │  🏆 🎯 ⭐ 🎖️ ...                   │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

#### 7.2.2 플래시카드 게임 화면
```
┌─────────────────────────────────────────┐
│  ← 돌아가기              진행: 5 / 20    │
├─────────────────────────────────────────┤
│                                         │
│            ┌───────────┐                │
│            │  Level 3  │  Combo: 🔥 5   │
│            └───────────┘                │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │                                 │    │
│  │         食べる                   │    │
│  │         [🔊 재생]                │    │
│  │                                 │    │
│  │         たべる                   │    │
│  │                                 │    │
│  └─────────────────────────────────┘    │
│                                         │
│          [카드 뒤집기 👆]                 │
│                                         │
│  ────────────────────────────────────   │
│  XP: ████████░░░░ 180 / 250            │
│                                         │
└─────────────────────────────────────────┘
```

#### 7.2.3 퀴즈 게임 화면
```
┌─────────────────────────────────────────┐
│  문제 3 / 10                   ⏱️ 00:45  │
├─────────────────────────────────────────┤
│                                         │
│  들리는 단어의 뜻은? 🔊 [자동 재생]        │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  A. 먹다                        │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  B. 마시다                      │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  C. 자다                        │    │
│  └─────────────────────────────────┘    │
│                                         │
│  ┌─────────────────────────────────┐    │
│  │  D. 가다                        │    │
│  └─────────────────────────────────┘    │
│                                         │
│  힌트 💡 | 건너뛰기 ⏭️                    │
└─────────────────────────────────────────┘
```

### 7.3 애니메이션 및 피드백

#### 7.3.1 정답 피드백
```typescript
const correctFeedback = {
  visual: [
    '✅ 페이드인',
    '녹색 테두리 애니메이션',
    '반짝이는 파티클 효과',
    '+15 XP 숫자 상승 애니메이션'
  ],
  audio: 'correct.mp3',
  haptic: 'light',  // 모바일

  message: [
    '완벽해요! 🎉',
    '정답입니다! ✨',
    '훌륭해요! 🌟',
    '대단해요! 💯'
  ]
}
```

#### 7.3.2 오답 피드백
```typescript
const incorrectFeedback = {
  visual: [
    '흔들림 애니메이션 (shake)',
    '빨간색 테두리',
    '정답 표시 (페이드인)'
  ],
  audio: 'wrong.mp3',
  haptic: 'medium',

  message: '정답은 "${correct}" 입니다.',
  explanation: '${word}는 ${meaning}라는 뜻입니다.',

  action: {
    retry: true,
    showExample: true,
  }
}
```

#### 7.3.3 레벨업 효과
```typescript
const levelUpAnimation = {
  trigger: 'XP 임계값 도달',

  sequence: [
    '화면 중앙에 큰 숫자 등장',
    '"레벨 업!" 텍스트 애니메이션',
    '폭죽 파티클 효과',
    '레벨 배지 애니메이션',
    '보상 목록 표시'
  ],

  audio: 'levelup.mp3',
  duration: 3000,  // ms

  rewards: {
    xpBonus: 50,
    unlockedFeatures: ['새 게임 모드'],
    badge: 'level-5-badge'
  }
}
```

### 7.4 게임화 상세 설계

#### 7.4.1 배지 시스템
```typescript
const achievements = {
  // 학습량 배지
  wordMaster: [
    { id: 'words-10', name: '첫 걸음', requirement: 10, icon: '🎯' },
    { id: 'words-50', name: '학습자', requirement: 50, icon: '📚' },
    { id: 'words-100', name: '수집가', requirement: 100, icon: '🏆' },
    { id: 'words-500', name: '마스터', requirement: 500, icon: '👑' },
    { id: 'words-1000', name: '전설', requirement: 1000, icon: '🌟' },
  ],

  // 스트릭 배지
  consistency: [
    { id: 'streak-3', name: '꾸준함', requirement: 3, icon: '🔥' },
    { id: 'streak-7', name: '열정', requirement: 7, icon: '💪' },
    { id: 'streak-30', name: '습관', requirement: 30, icon: '⭐' },
    { id: 'streak-100', name: '전념', requirement: 100, icon: '💎' },
  ],

  // 정확도 배지
  accuracy: [
    { id: 'perfect-10', name: '완벽주의자', requirement: '10개 연속 정답', icon: '💯' },
    { id: 'quick-draw', name: '번개', requirement: '평균 2초 이내', icon: '⚡' },
  ],

  // 특수 배지
  special: [
    { id: 'night-owl', name: '올빼미', requirement: '자정 이후 학습', icon: '🦉' },
    { id: 'early-bird', name: '아침형 인간', requirement: '오전 6시 전 학습', icon: '🐦' },
    { id: 'completionist', name: '완주자', requirement: 'N5 전체 완료', icon: '🎓' },
  ]
}
```

#### 7.4.2 일일 미션 시스템
```typescript
const dailyMissions = {
  missions: [
    {
      id: 'daily-20',
      title: '20장 학습하기',
      description: '오늘 20장의 카드를 학습하세요',
      progress: 15,
      target: 20,
      reward: { xp: 50, badge: null },
      status: 'in_progress'
    },
    {
      id: 'daily-streak',
      title: '연속 학습 유지',
      description: '오늘 하루도 학습을 완료하세요',
      progress: 0,
      target: 1,
      reward: { xp: 30, badge: null },
      status: 'pending'
    },
    {
      id: 'daily-perfect',
      title: '완벽한 정답',
      description: '5개 이상 첫 시도에 정답',
      progress: 3,
      target: 5,
      reward: { xp: 40, badge: null },
      status: 'in_progress'
    }
  ],

  refreshTime: '00:00',  // 자정에 리셋

  bonusReward: {
    condition: '모든 일일 미션 완료',
    xp: 100,
    badge: 'daily-hero'
  }
}
```

#### 7.4.3 프로그레스 시각화
```typescript
const progressVisualization = {
  // 원형 프로그레스
  circularProgress: {
    type: 'radial',
    showPercentage: true,
    colors: {
      completed: '#10b981',
      inProgress: '#3b82f6',
      pending: '#e5e7eb'
    }
  },

  // 레벨 프로그레스 바
  levelProgress: {
    currentXP: 180,
    nextLevelXP: 250,
    level: 3,

    visualElements: [
      '프로그레스 바',
      '현재 XP / 필요 XP 텍스트',
      '레벨 아이콘',
      '다음 레벨까지 남은 양'
    ]
  },

  // 히트맵 (학습 활동)
  activityHeatmap: {
    type: 'calendar',
    period: '1년',
    colorScale: ['#ebedf0', '#c6e48b', '#7bc96f', '#239a3b', '#196127'],
    data: 'dailyStudyCount'
  },

  // 통계 차트
  statsCharts: [
    {
      type: 'line',
      title: '학습 추이',
      data: 'cardsPerDay',
      period: '30일'
    },
    {
      type: 'bar',
      title: '카테고리별 진행도',
      data: 'categoryMastery'
    },
    {
      type: 'pie',
      title: 'JLPT 레벨 분포',
      data: 'levelDistribution'
    }
  ]
}
```

---

## 8. 스킬 구조 및 리소스 설계

### 8.1 스킬 디렉토리 구조
```
japanese-learning-game/
├── SKILL.md                           # 스킬 메인 문서
│
├── scripts/                           # 실행 가능한 스크립트
│   ├── srs_algorithm.py              # SRS 알고리즘 구현
│   ├── audio_generator.py            # TTS 음성 생성
│   ├── data_importer.py              # 학습 데이터 가져오기
│   └── game_scaffolder.py            # 게임 보일러플레이트 생성
│
├── references/                        # 참고 문서
│   ├── vocabulary/                   # 단어 데이터베이스
│   │   ├── n5-words.json            # N5 800 단어
│   │   ├── n4-words.json            # N4 1,500 단어
│   │   ├── n3-words.json            # N3 3,000 단어
│   │   └── schema.md                # 데이터 스키마 문서
│   │
│   ├── conversations/                # 회화 시나리오
│   │   ├── daily-life.json
│   │   ├── travel.json
│   │   ├── business.json
│   │   └── schema.md
│   │
│   ├── srs-guide.md                 # SRS 구현 가이드
│   ├── gamification-guide.md        # 게임화 설계 가이드
│   ├── audio-implementation.md      # 오디오 구현 가이드
│   └── ui-components.md             # UI 컴포넌트 가이드
│
├── assets/                           # 템플릿 및 에셋
│   ├── game-template/               # React 게임 보일러플레이트
│   │   ├── package.json
│   │   ├── vite.config.ts
│   │   ├── tsconfig.json
│   │   ├── src/
│   │   │   ├── components/
│   │   │   │   ├── games/          # 게임 컴포넌트
│   │   │   │   ├── ui/             # UI 컴포넌트
│   │   │   │   └── layout/
│   │   │   ├── lib/                # 핵심 로직
│   │   │   │   ├── srs/
│   │   │   │   ├── audio/
│   │   │   │   └── game/
│   │   │   ├── stores/             # 상태 관리
│   │   │   ├── hooks/              # Custom hooks
│   │   │   └── utils/
│   │   └── public/
│   │       └── audio/
│   │           └── sfx/            # 효과음
│   │
│   ├── ui-kit/                     # UI 컴포넌트 라이브러리
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── ProgressBar.tsx
│   │   └── ...
│   │
│   └── design-system/              # 디자인 시스템
│       ├── colors.ts
│       ├── typography.ts
│       └── animations.ts
│
└── examples/                        # 사용 예시
    ├── basic-flashcard.md
    ├── quiz-game.md
    └── conversation-practice.md
```

### 8.2 SKILL.md 구조
```markdown
---
name: japanese-learning-game
description: Create effective Japanese learning games with SRS, audio-first approach, and gamification. Use when building vocabulary flashcards, conversation practice, or quiz games for Japanese learners (JLPT N5-N3).
---

# Japanese Learning Game Skill

## Purpose
이 스킬은 음성 중심의 일본어 학습 게임을 빠르게 생성합니다. 간격 반복 학습(SRS), 게임화 요소, 그리고 진행도 추적 기능이 통합되어 있습니다.

## When to Use
- 일본어 단어 학습 게임 생성 요청 시
- 회화 연습 게임 생성 요청 시
- JLPT 학습 도구 개발 요청 시
- 게임화된 언어 학습 앱 요청 시

## Core Features
1. **SRS 시스템**: `scripts/srs_algorithm.py` 활용
2. **음성 지원**: `scripts/audio_generator.py` 활용
3. **게임 템플릿**: `assets/game-template/` 사용
4. **학습 데이터**: `references/vocabulary/` 참조

## Workflow

### 1. 요구사항 파악
사용자 요청 분석:
- 게임 유형 (플래시카드, 퀴즈, 타이핑 등)
- 학습 범위 (JLPT 레벨, 카테고리)
- 특수 요구사항 (모바일 지원 등)

### 2. 프로젝트 생성
```bash
python scripts/game_scaffolder.py \
  --game-type flashcard \
  --jlpt-level N5 \
  --category food \
  --output ./my-japanese-game
```

### 3. 데이터 통합
- `references/vocabulary/n5-words.json`에서 필요한 단어 추출
- `scripts/data_importer.py`로 데이터 변환

### 4. SRS 통합
- `scripts/srs_algorithm.py`를 프로젝트에 복사
- 상태 관리에 SRS 로직 통합

### 5. 오디오 설정
- `scripts/audio_generator.py`로 TTS 생성
- 또는 Web Speech API 사용

### 6. UI 커스터마이징
- `assets/ui-kit/`의 컴포넌트 활용
- `assets/design-system/`의 스타일 적용

## Reference Files

### 학습 데이터가 필요한 경우
- `references/vocabulary/` - JLPT 레벨별 단어
- `references/conversations/` - 회화 시나리오

### SRS 구현 가이드가 필요한 경우
- `references/srs-guide.md` 참조

### 게임화 설계가 필요한 경우
- `references/gamification-guide.md` 참조

## Examples
자세한 사용 예시는 `examples/` 디렉토리 참조
```

### 8.3 핵심 스크립트 설계

#### 8.3.1 SRS 알고리즘 스크립트
```python
# scripts/srs_algorithm.py
"""
SuperMemo SM-2 기반 간격 반복 학습 알고리즘
독립 실행 및 임포트 가능
"""

from datetime import datetime, timedelta
from typing import TypedDict

class SRSCard(TypedDict):
    easiness: float
    interval: int
    repetitions: int
    next_review: datetime

def calculate_next_review(
    quality: int,  # 0-5
    card: SRSCard
) -> SRSCard:
    """
    다음 복습 일정 계산

    Args:
        quality: 응답 품질 (0=완전히 모름, 5=완벽)
        card: 현재 SRS 카드 상태

    Returns:
        업데이트된 SRS 카드 상태
    """
    # ... (앞서 설계한 알고리즘 구현)
    pass

def get_due_cards(
    cards: list[SRSCard],
    current_time: datetime = None
) -> list[SRSCard]:
    """복습 시간이 된 카드 반환"""
    pass

# CLI 인터페이스
if __name__ == "__main__":
    import argparse
    # ... 독립 실행 로직
```

#### 8.3.2 게임 생성 스크립트
```python
# scripts/game_scaffolder.py
"""
일본어 학습 게임 보일러플레이트 생성기
"""

import argparse
import shutil
from pathlib import Path

def create_game(
    game_type: str,
    jlpt_level: str,
    category: str,
    output_dir: Path
):
    """
    게임 프로젝트 생성

    Args:
        game_type: 'flashcard', 'quiz', 'typing', 'conversation'
        jlpt_level: 'N5', 'N4', 'N3', 'N2', 'N1'
        category: 단어 카테고리
        output_dir: 출력 디렉토리
    """

    # 1. 템플릿 복사
    template_path = Path(__file__).parent.parent / 'assets/game-template'
    shutil.copytree(template_path, output_dir)

    # 2. 데이터 주입
    # ...

    # 3. 게임 타입별 컴포넌트 추가
    # ...

    print(f"✅ 게임 생성 완료: {output_dir}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--game-type', required=True)
    parser.add_argument('--jlpt-level', default='N5')
    parser.add_argument('--category', default='all')
    parser.add_argument('--output', required=True)

    args = parser.parse_args()
    create_game(
        args.game_type,
        args.jlpt_level,
        args.category,
        Path(args.output)
    )
```

### 8.4 참고 문서 구조

#### 8.4.1 SRS 가이드
```markdown
# references/srs-guide.md

# SRS 시스템 구현 가이드

## 개요
이 문서는 일본어 학습 게임에 SRS를 통합하는 방법을 설명합니다.

## 빠른 시작
\`\`\`typescript
import { calculateNextReview } from './lib/srs/algorithm'

// 카드 복습 처리
const updatedCard = calculateNextReview(quality, currentCard)
\`\`\`

## 상세 구현
... (구체적인 구현 방법)
```

#### 8.4.2 UI 컴포넌트 가이드
```markdown
# references/ui-components.md

# UI 컴포넌트 가이드

## 사용 가능한 컴포넌트

### FlashCard
\`\`\`tsx
<FlashCard
  word="食べる"
  reading="たべる"
  meaning="먹다"
  audio="/audio/taberu.mp3"
  onFlip={() => {}}
/>
\`\`\`

### QuizQuestion
...
```

---

## 9. 개발 로드맵 및 마일스톤

### 9.1 개발 단계

#### Phase 1: 스킬 기반 구조 (2주)
**목표**: 스킬의 기본 구조와 핵심 리소스 완성

**작업 항목**:
- [ ] 스킬 디렉토리 구조 생성
- [ ] SKILL.md 작성
- [ ] SRS 알고리즘 스크립트 개발
- [ ] N5 단어 데이터베이스 (800 단어)
- [ ] 기본 회화 시나리오 (10개)

**산출물**:
- 패키징 가능한 스킬 v0.1
- 기본 문서화

#### Phase 2: 게임 템플릿 개발 (3주)
**목표**: 재사용 가능한 게임 보일러플레이트 완성

**작업 항목**:
- [ ] React + TypeScript 프로젝트 설정
- [ ] 플래시카드 컴포넌트
- [ ] 퀴즈 컴포넌트
- [ ] 타이핑 게임 컴포넌트
- [ ] SRS 엔진 통합
- [ ] 로컬 스토리지 구현
- [ ] 기본 UI/UX

**산출물**:
- `assets/game-template/` 완성
- 3가지 게임 모드 동작

#### Phase 3: 오디오 시스템 (2주)
**목표**: 음성 중심 학습 지원

**작업 항목**:
- [ ] Web Speech API 통합
- [ ] 오디오 플레이어 컴포넌트
- [ ] TTS 생성 스크립트
- [ ] 효과음 추가
- [ ] 오디오 캐싱 시스템

**산출물**:
- 모든 단어에 음성 지원
- 효과음 시스템

#### Phase 4: 게임화 시스템 (2주)
**목표**: 몰입도 증가 요소 추가

**작업 항목**:
- [ ] XP 및 레벨 시스템
- [ ] 배지 시스템
- [ ] 일일 미션
- [ ] 스트릭 추적
- [ ] 프로그레스 시각화
- [ ] 애니메이션 효과

**산출물**:
- 완전한 게임화 시스템
- 50+ 배지

#### Phase 5: 데이터 확장 (2주)
**목표**: 학습 콘텐츠 확장

**작업 항목**:
- [ ] N4 단어 데이터베이스 (1,500 단어)
- [ ] N3 단어 데이터베이스 (3,000 단어)
- [ ] 회화 시나리오 확장 (30개)
- [ ] 카테고리 분류 개선
- [ ] 예문 추가

**산출물**:
- 5,300+ 단어
- 30+ 회화 시나리오

#### Phase 6: 고급 기능 (3주)
**목표**: 차별화 기능 추가

**작업 항목**:
- [ ] 회화 시뮬레이션 모드
- [ ] 발음 평가 (Web Speech Recognition)
- [ ] 클라우드 동기화
- [ ] 통계 대시보드
- [ ] 모바일 최적화

**산출물**:
- 고급 학습 기능
- PWA 지원

#### Phase 7: 테스트 및 최적화 (2주)
**목표**: 안정성 및 성능 개선

**작업 항목**:
- [ ] 단위 테스트
- [ ] 통합 테스트
- [ ] 성능 최적화
- [ ] 접근성 개선
- [ ] 버그 수정

**산출물**:
- 테스트 커버리지 80%+
- 성능 개선

#### Phase 8: 문서화 및 배포 (1주)
**목표**: 스킬 완성 및 배포

**작업 항목**:
- [ ] 사용자 가이드 작성
- [ ] API 문서화
- [ ] 예제 프로젝트
- [ ] 스킬 패키징
- [ ] 배포

**산출물**:
- 완성된 스킬 v1.0
- 완전한 문서

### 9.2 마일스톤

| 마일스톤 | 기간 | 완료 조건 | 핵심 산출물 |
|---------|------|----------|-----------|
| **M1: 스킬 기반** | 2주 | 스킬 구조 완성, 기본 데이터 | SKILL.md, SRS 스크립트, N5 단어 |
| **M2: 기본 게임** | 5주 | 3가지 게임 모드 동작 | 게임 템플릿, SRS 통합 |
| **M3: 음성 지원** | 7주 | 모든 게임에 음성 지원 | 오디오 시스템 |
| **M4: 게임화** | 9주 | 완전한 게임화 시스템 | XP, 배지, 미션 |
| **M5: 콘텐츠 확장** | 11주 | N5-N3 데이터 완성 | 5,300+ 단어, 30+ 시나리오 |
| **M6: 고급 기능** | 14주 | 차별화 기능 완성 | 회화 시뮬레이션, 클라우드 동기화 |
| **M7: 품질 보증** | 16주 | 테스트 및 최적화 완료 | 테스트 커버리지, 성능 개선 |
| **M8: 배포** | 17주 | 스킬 v1.0 릴리스 | 패키징된 스킬, 문서 |

### 9.3 우선순위 조정 (MVP)

시간이 제한적인 경우 MVP (Minimum Viable Product):

**MVP 포함 사항** (8주):
- ✅ 플래시카드 게임 1종
- ✅ SRS 시스템
- ✅ N5 단어 800개
- ✅ 기본 음성 지원 (Web Speech API)
- ✅ 간단한 게임화 (XP, 레벨)
- ✅ 로컬 스토리지

**MVP 이후 추가**:
- 추가 게임 모드
- N4, N3 데이터
- 고급 게임화
- 클라우드 동기화
- 모바일 최적화

---

## 10. 성공 지표 및 평가

### 10.1 스킬 성능 지표

#### 10.1.1 개발 효율성
- **목표**: 스킬 사용 시 5분 내 기본 게임 생성
- **측정**: 프로젝트 생성부터 실행까지 소요 시간

#### 10.1.2 재사용성
- **목표**: 80% 이상의 코드 재사용
- **측정**: 새 게임 생성 시 재사용된 코드 비율

### 10.2 학습 효과 지표

#### 10.2.1 기억 정착률
- **목표**: SRS 사용 시 90일 후 80% 유지율
- **측정**: 학습 후 90일 뒤 테스트 정답률

#### 10.2.2 학습 속도
- **목표**: 전통적 방법 대비 30% 빠른 습득
- **측정**: 동일 단어 수 습득까지 소요 시간

### 10.3 사용자 참여 지표

#### 10.3.1 재방문율
- **목표**: 일일 재방문율 60%+
- **측정**: DAU / MAU 비율

#### 10.3.2 학습 지속성
- **목표**: 평균 스트릭 7일 이상
- **측정**: 사용자별 평균 연속 학습 일수

#### 10.3.3 세션 시간
- **목표**: 평균 세션 15분
- **측정**: 평균 학습 세션 시간

### 10.4 기술적 지표

#### 10.4.1 성능
- **로딩 시간**: 초기 로딩 < 3초
- **응답 시간**: 상호작용 < 100ms
- **번들 크기**: < 500KB (gzipped)

#### 10.4.2 품질
- **테스트 커버리지**: > 80%
- **버그 밀도**: < 1 버그 / 1000 LOC
- **접근성**: WCAG 2.1 AA 준수

---

## 11. 리스크 및 대응 방안

### 11.1 기술적 리스크

| 리스크 | 영향도 | 확률 | 대응 방안 |
|--------|--------|------|-----------|
| Web Speech API 브라우저 호환성 | 높음 | 중간 | 폴백으로 외부 TTS API 제공 |
| 오프라인 오디오 용량 문제 | 중간 | 높음 | On-demand 다운로드, 압축 최적화 |
| SRS 알고리즘 효과 미검증 | 중간 | 중간 | A/B 테스트, 파라미터 조정 기능 |
| 모바일 성능 저하 | 높음 | 중간 | 코드 스플리팅, 레이지 로딩 |

### 11.2 콘텐츠 리스크

| 리스크 | 영향도 | 확률 | 대응 방안 |
|--------|--------|------|-----------|
| 단어 데이터 부정확성 | 높음 | 낮음 | 크라우드소싱 검증, 전문가 리뷰 |
| 음성 발음 품질 | 중간 | 중간 | 네이티브 음성 녹음, TTS 품질 개선 |
| 콘텐츠 부족 | 낮음 | 낮음 | 단계적 확장, 커뮤니티 기여 |

### 11.3 사용자 경험 리스크

| 리스크 | 영향도 | 확률 | 대응 방안 |
|--------|--------|------|-----------|
| 학습 동기 저하 | 높음 | 중간 | 게임화 강화, 소셜 기능 추가 |
| 학습 곡선 가파름 | 중간 | 중간 | 온보딩 튜토리얼, 단계별 안내 |
| 플랫폼 호환성 문제 | 중간 | 낮음 | 크로스 브라우저 테스트 |

---

## 12. 향후 확장 계획

### 12.1 단기 확장 (3-6개월)
- **모바일 앱**: React Native 포팅
- **소셜 기능**: 친구와 경쟁, 리더보드
- **AI 튜터**: 챗봇 기반 회화 연습
- **커스텀 덱**: 사용자 직접 단어 세트 생성

### 12.2 중기 확장 (6-12개월)
- **N2, N1 콘텐츠**: 고급 학습자 지원
- **문법 학습**: 문법 포인트별 게임
- **읽기 연습**: 지문 읽기 및 이해
- **커뮤니티 기능**: 학습 노트 공유

### 12.3 장기 확장 (12개월+)
- **다국어 지원**: 한국어 외 영어, 중국어 인터페이스
- **타 언어 확장**: 중국어, 스페인어 등
- **교육 기관 버전**: 교사용 대시보드, 학급 관리
- **AI 개인화**: 학습 패턴 분석 및 맞춤 추천

---

## 13. 부록

### 13.1 기술 스택 상세

#### 프론트엔드 라이브러리
```json
{
  "dependencies": {
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "zustand": "^4.4.0",
    "@tanstack/react-query": "^5.0.0",
    "framer-motion": "^10.0.0",
    "howler": "^2.2.3",
    "@radix-ui/react-*": "^1.0.0"
  },
  "devDependencies": {
    "vite": "^5.0.0",
    "typescript": "^5.0.0",
    "tailwindcss": "^3.0.0",
    "vitest": "^1.0.0",
    "@testing-library/react": "^14.0.0"
  }
}
```

### 13.2 데이터 스키마 상세

#### VocabularyCard JSON Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "required": ["id", "word", "reading", "meaning"],
  "properties": {
    "id": { "type": "string" },
    "word": { "type": "string" },
    "reading": { "type": "string" },
    "romaji": { "type": "string" },
    "meaning": { "type": "string" },
    "partOfSpeech": { "type": "string" },
    "jlptLevel": {
      "type": "string",
      "enum": ["N5", "N4", "N3", "N2", "N1"]
    }
  }
}
```

### 13.3 참고 자료
- [SuperMemo Algorithm](https://www.supermemo.com/en/archives1990-2015/english/ol/sm2)
- [JLPT Official](https://www.jlpt.jp/)
- [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API)
- [Gamification in Education](https://www.researchgate.net)

---

## 문서 버전 이력
- v1.0 (2025-10-25): 초안 작성
