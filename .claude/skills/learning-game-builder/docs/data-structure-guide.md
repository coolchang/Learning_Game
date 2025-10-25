# 데이터 구조 가이드

언어 학습 게임 개발을 위한 데이터 구조 및 스키마 가이드입니다.

## 1. 노래 데이터 구조

### 완전한 노래 데이터 스키마

```json
{
  "id": "song-001",
  "title": "노래 제목",
  "artist": "가수명",
  "album": "앨범명 (optional)",
  "year": 2024,
  "genre": "k-pop",
  "difficulty": "beginner",
  "duration": "3:45",
  "source": {
    "youtube": "https://youtube.com/watch?v=...",
    "spotify": "spotify:track:...",
    "credits": "출처 및 라이선스 정보"
  },
  "lyrics": [
    {
      "line": 1,
      "korean": "한국어 가사",
      "romanization": "Han-gugeo gasa",
      "translation": "English translation",
      "timestamp": "00:00:10.5"
    }
  ],
  "vocabulary": [
    {
      "word": "단어",
      "romanization": "daneo",
      "meaning": "word",
      "pos": "noun",
      "level": "beginner",
      "frequency": 5,
      "example": "이 단어를 알아요",
      "exampleTranslation": "I know this word"
    }
  ],
  "grammarPoints": [
    {
      "pattern": "~(으)ㄴ/는",
      "meaning": "present tense modifier",
      "example": "예쁜 꽃",
      "explanation": "Used to modify nouns with present tense verbs/adjectives"
    }
  ],
  "culturalNotes": [
    {
      "topic": "문화적 맥락",
      "description": "이 노래는 한국의 ... 문화를 다룹니다",
      "references": ["URL1", "URL2"]
    }
  ],
  "tags": ["love", "friendship", "spring"],
  "targetLevel": "A1-A2"
}
```

### 최소 노래 데이터 (간단 버전)

```json
{
  "title": "노래 제목",
  "artist": "가수",
  "difficulty": "beginner",
  "lyrics": [
    { "korean": "가사", "translation": "translation" }
  ],
  "vocabulary": [
    { "word": "단어", "meaning": "word", "pos": "noun" }
  ]
}
```

## 2. 가사 빈칸 채우기 게임 데이터

### 기본 구조

```json
{
  "songTitle": "노래 제목",
  "artist": "가수",
  "difficulty": "초급",
  "lyrics": [
    { "text": "안녕하세요 " },
    {
      "blank": {
        "word": "친구",
        "hint": "함께 노는 사람",
        "pos": "명사",
        "alternatives": ["동료", "벗"]
      }
    },
    { "text": "들" }
  ]
}
```

### 난이도별 빈칸 선택 전략

**초급 (Beginner)**
- 고빈도 명사 (친구, 사랑, 집)
- 기본 동사 (가다, 오다, 먹다)
- 간단한 형용사 (좋다, 나쁘다)
- 3-5글자 단어

**중급 (Intermediate)**
- 형용사, 부사
- 문법 조사 (을/를, 이/가)
- 복합 동사
- 5-7글자 단어

**고급 (Advanced)**
- 숙어, 관용구
- 문법 패턴
- 추상 명사
- 8+ 글자 복잡한 단어

## 3. 어휘 플래시카드 데이터

### 플래시카드 스키마

```json
{
  "topic": "주제명",
  "description": "학습 목표 설명",
  "cards": [
    {
      "korean": "한국어 단어",
      "romanization": "romanization",
      "meaning": "English meaning",
      "pos": "noun|verb|adjective|adverb|particle",
      "level": "beginner|intermediate|advanced",
      "example": "예문",
      "exampleTranslation": "Example translation",
      "audioUrl": "audio/word.mp3 (optional)",
      "imageUrl": "images/word.jpg (optional)",
      "synonyms": ["유의어1", "유의어2"],
      "antonyms": ["반의어1"],
      "relatedWords": ["관련어1", "관련어2"],
      "mnemonic": "암기 팁 (optional)"
    }
  ]
}
```

### 간격 반복 학습 (Spaced Repetition) 데이터

```json
{
  "userId": "user-123",
  "vocabulary": [
    {
      "wordId": "word-001",
      "lastReviewed": "2024-01-15T10:30:00Z",
      "nextReview": "2024-01-18T10:30:00Z",
      "reviewCount": 3,
      "confidence": 0.8,
      "interval": 3
    }
  ]
}
```

## 4. 문법 포인트 데이터

```json
{
  "grammarPoints": [
    {
      "id": "grammar-001",
      "pattern": "~(으)ㄴ/는",
      "level": "beginner",
      "category": "modifier",
      "meaning": "present tense noun modifier",
      "formation": {
        "verb": "stem + 는",
        "adjective": "stem + (으)ㄴ"
      },
      "examples": [
        {
          "korean": "가는 사람",
          "romanization": "ganeun saram",
          "translation": "the person who goes",
          "breakdown": "가다 (to go) → 가는"
        }
      ],
      "commonMistakes": [
        {
          "wrong": "가ㄴ 사람",
          "right": "가는 사람",
          "explanation": "Verbs use 는, not ㄴ"
        }
      ],
      "relatedGrammar": ["grammar-002", "grammar-005"]
    }
  ]
}
```

## 5. 사용자 진도 추적 데이터

```json
{
  "userId": "user-123",
  "profile": {
    "name": "학습자",
    "level": "intermediate",
    "studyGoal": "daily",
    "targetHoursPerWeek": 5
  },
  "progress": {
    "songsCompleted": 12,
    "vocabularyLearned": 245,
    "gamesPlayed": 58,
    "totalStudyTime": 1840,
    "currentStreak": 7,
    "longestStreak": 21
  },
  "achievements": [
    {
      "id": "first-song",
      "name": "첫 노래 완료",
      "earnedAt": "2024-01-10T14:20:00Z"
    }
  ],
  "recentActivity": [
    {
      "type": "game",
      "gameType": "fill-in-blank",
      "songId": "song-005",
      "score": 85,
      "completedAt": "2024-01-15T16:45:00Z"
    }
  ]
}
```

## 6. 게임 설정 데이터

```json
{
  "gameConfig": {
    "fillInBlank": {
      "hintsAllowed": 3,
      "timeLimit": null,
      "showRomanization": true,
      "caseSensitive": false,
      "allowTypos": true,
      "typoTolerance": 1
    },
    "flashcards": {
      "autoFlip": false,
      "flipDelay": 2,
      "shuffleCards": true,
      "reviewMode": "spaced-repetition"
    },
    "general": {
      "soundEnabled": true,
      "animations": true,
      "theme": "light",
      "language": "ko"
    }
  }
}
```

## 7. 파일 구조 권장사항

```
project/
├── data/
│   ├── songs/
│   │   ├── song-001.json
│   │   ├── song-002.json
│   │   └── index.json (songs list)
│   ├── vocabulary/
│   │   ├── beginner.json
│   │   ├── intermediate.json
│   │   └── advanced.json
│   ├── grammar/
│   │   └── patterns.json
│   └── users/
│       └── user-{id}.json
├── games/
│   ├── fill-in-blank.html
│   ├── flashcards.html
│   └── matching.html
└── assets/
    ├── audio/
    ├── images/
    └── styles/
```

## 8. API 응답 형식 (향후 백엔드 연동)

```json
{
  "status": "success",
  "data": {
    "song": { /* song object */ },
    "game": { /* game data */ }
  },
  "meta": {
    "timestamp": "2024-01-15T10:30:00Z",
    "version": "1.0"
  }
}
```

## 9. 에러 처리

```json
{
  "status": "error",
  "error": {
    "code": "SONG_NOT_FOUND",
    "message": "요청한 노래를 찾을 수 없습니다",
    "details": {
      "songId": "song-999"
    }
  }
}
```

## 10. 데이터 검증 체크리스트

데이터를 추가할 때 다음을 확인하세요:

- [ ] 모든 필수 필드가 존재하는가?
- [ ] 한글 인코딩이 올바른가? (UTF-8)
- [ ] 로마자 표기가 정확한가?
- [ ] 번역이 맥락에 맞는가?
- [ ] 난이도 레벨이 적절한가?
- [ ] 예문이 실제로 사용되는 표현인가?
- [ ] 품사(POS) 태그가 정확한가?
- [ ] 저작권 출처가 명시되어 있는가?

## 11. 성능 최적화 팁

- 큰 데이터는 lazy loading 사용
- 자주 쓰는 데이터는 LocalStorage에 캐싱
- 이미지는 최적화 및 lazy loading
- 오디오 파일은 압축 (MP3, 128kbps)
- JSON 파일 크기 모니터링 (권장: 100KB 이하)

## 12. 버전 관리

데이터 스키마에 버전 추가:

```json
{
  "schemaVersion": "1.0",
  "data": { /* actual data */ }
}
```

버전 변경 시 마이그레이션 스크립트 제공.
