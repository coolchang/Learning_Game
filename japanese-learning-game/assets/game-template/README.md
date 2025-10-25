# 일본어 학습 게임 템플릿

SRS(Spaced Repetition System)와 게임화 요소를 갖춘 React 기반 일본어 학습 게임 템플릿입니다.

## 특징

- **SRS 시스템**: SuperMemo SM-2 알고리즘 기반 최적화된 복습 스케줄
- **음성 학습**: 모든 단어와 문장에 음성 지원
- **게임화**: XP, 레벨, 배지, 일일 스트릭 시스템
- **다양한 게임 모드**:
  - 플래시카드
  - 4지선다 퀴즈
  - 타이핑 게임
  - 회화 시뮬레이션
- **오프라인 우선**: PWA 지원, 로컬 스토리지
- **진행도 추적**: 상세한 학습 통계 및 대시보드

## 시작하기

### 필수 요구사항

- Node.js 18+
- npm 또는 yarn

### 설치

\`\`\`bash
npm install
\`\`\`

### 개발 서버 실행

\`\`\`bash
npm run dev
\`\`\`

브라우저에서 http://localhost:5173 을 엽니다.

### 빌드

\`\`\`bash
npm run build
\`\`\`

빌드된 파일은 `dist/` 디렉토리에 생성됩니다.

## 프로젝트 구조

\`\`\`
src/
├── components/          # React 컴포넌트
│   ├── games/          # 게임 컴포넌트
│   │   ├── Flashcard.tsx
│   │   ├── Quiz.tsx
│   │   ├── TypingGame.tsx
│   │   └── Conversation.tsx
│   ├── ui/             # 공통 UI 컴포넌트
│   └── layout/         # 레이아웃 컴포넌트
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
├── stores/            # Zustand 상태 관리
│   ├── gameStore.ts
│   ├── userStore.ts
│   └── srsStore.ts
│
├── data/              # 학습 데이터
│   ├── vocabulary.json
│   └── conversations.json
│
└── utils/             # 유틸리티
    ├── storage.ts
    ├── sync.ts
    └── helpers.ts
\`\`\`

## 설정

### game.config.json

게임 설정은 루트의 `game.config.json` 파일에서 수정할 수 있습니다:

\`\`\`json
{
  "gameType": "flashcard",
  "jlptLevel": "N5",
  "srs": {
    "newCardsPerDay": 20,
    "reviewCardsPerDay": 100
  },
  "audio": {
    "enabled": true,
    "autoplay": true,
    "speed": 1.0
  },
  "gamification": {
    "xp": true,
    "levels": true,
    "badges": true,
    "dailyStreak": true
  }
}
\`\`\`

### 학습 데이터 추가

`src/data/vocabulary.json`에 단어를 추가하거나 수정할 수 있습니다:

\`\`\`json
{
  "id": "n5-001",
  "word": "食べる",
  "reading": "たべる",
  "romaji": "taberu",
  "meaning": "먹다",
  "partOfSpeech": "동사",
  "category": ["음식", "동작"],
  "jlptLevel": "N5",
  "examples": [...],
  "difficulty": 1,
  "frequency": 5
}
\`\`\`

## 기술 스택

- **Frontend**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **Animation**: Framer Motion
- **State Management**: Zustand
- **Audio**: Howler.js + Web Speech API
- **UI Components**: Radix UI
- **PWA**: vite-plugin-pwa

## 라이센스

MIT

## 기여

이슈 및 PR은 언제든지 환영합니다!
