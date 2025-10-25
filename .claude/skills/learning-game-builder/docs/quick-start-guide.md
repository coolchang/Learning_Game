# 빠른 시작 가이드

이 스킬을 사용하여 한국어 학습 게임을 만드는 방법입니다.

## 🎯 5분 만에 첫 게임 만들기

### 1단계: 스킬 활성화

Claude Code에서 다음과 같이 요청하세요:

```
한국어 노래로 학습 게임 만들고 싶어
```

또는

```
가사 빈칸 채우기 게임 만들어줘
```

### 2단계: 게임 유형 선택

스킬이 다음과 같은 옵션을 제공합니다:

1. **가사 빈칸 채우기** - 가장 인기있는 게임
2. **어휘 플래시카드** - 단어 집중 학습
3. **순서 맞추기** - 가사 순서 배열
4. **번역 매칭** - 한영 매칭
5. **커스텀** - 나만의 게임 설계

### 3단계: 게임 코드 받기

스킬이 완전히 작동하는 HTML 파일을 생성합니다:
- 즉시 브라우저에서 실행 가능
- 모바일/데스크톱 반응형
- 아름다운 UI/UX
- 샘플 데이터 포함

### 4단계: 커스터마이징

생성된 코드에서 다음을 수정:
- 게임 데이터 (가사, 어휘)
- 색상 및 스타일
- 난이도 설정
- 게임 규칙

## 📋 사용 시나리오

### 시나리오 1: 빈칸 채우기 게임

```
개발자: "가사 빈칸 채우기 게임 만들어줘. 초급 레벨로"

스킬 응답:
1. fill-in-blank-template.html 제공
2. 샘플 노래 데이터 JSON 제공
3. 통합 방법 설명
4. 커스터마이징 가이드

결과: 즉시 사용 가능한 게임!
```

### 시나리오 2: 내 노래 데이터로 게임 만들기

```
개발자: "이 가사로 게임 데이터 만들어줘:
         안녕하세요 친구들
         오늘도 좋은 날"

스킬 응답:
1. 가사 분석
2. 주요 어휘 추출 (안녕하세요, 친구, 오늘, 좋은, 날)
3. 빈칸 위치 제안
4. JSON 데이터 생성
5. 게임에 적용하는 방법 설명
```

### 시나리오 3: 플래시카드 만들기

```
개발자: "이 노래에서 어휘 플래시카드 만들어줘"

스킬 응답:
1. flashcard-template.html 제공
2. 어휘 데이터 추출 및 JSON 생성
3. 로마자 표기 추가
4. 예문 생성
5. 사용 방법 설명
```

## 🛠️ 개발 워크플로우

### 완전한 게임 개발 프로세스

#### Phase 1: 기획 (5-10분)
1. 게임 유형 결정
2. 대상 학습자 레벨 정의
3. 학습 목표 설정

#### Phase 2: 데이터 준비 (20-30분)
1. 노래 선택
2. 가사 입력
3. 어휘 추출
4. 번역 추가
5. JSON 파일 생성

#### Phase 3: 게임 생성 (5분)
1. 템플릿 선택
2. 데이터 통합
3. 브라우저에서 테스트

#### Phase 4: 커스터마이징 (10-30분)
1. UI 스타일 조정
2. 게임 규칙 수정
3. 추가 기능 구현
4. 모바일 최적화

#### Phase 5: 배포 (5-10분)
1. 최종 테스트
2. 파일 최적화
3. 호스팅 (GitHub Pages, Netlify, etc.)

## 💡 자주 하는 질문

### Q1: 음악 파일은 어떻게 추가하나요?

```javascript
// HTML5 Audio 사용
<audio id="song-audio" src="path/to/song.mp3"></audio>

<button onclick="document.getElementById('song-audio').play()">
  재생
</button>
```

### Q2: 난이도를 어떻게 조절하나요?

난이도별 빈칸 선택 전략:

```javascript
// 초급: 명사 위주
const beginnerWords = lyrics.filter(word => word.pos === 'noun');

// 중급: 동사, 형용사 추가
const intermediateWords = lyrics.filter(word =>
  ['noun', 'verb', 'adjective'].includes(word.pos)
);

// 고급: 모든 품사 + 조사
const advancedWords = lyrics;
```

### Q3: 여러 노래를 하나의 게임에 넣으려면?

```javascript
const songDatabase = [
  { id: 1, title: "노래1", data: { /* song 1 data */ } },
  { id: 2, title: "노래2", data: { /* song 2 data */ } },
];

function selectSong(songId) {
  const song = songDatabase.find(s => s.id === songId);
  loadGame(song.data);
}
```

### Q4: 사용자 진도를 저장하려면?

```javascript
// LocalStorage 사용
function saveProgress(userId, progress) {
  localStorage.setItem(
    `user_${userId}_progress`,
    JSON.stringify(progress)
  );
}

function loadProgress(userId) {
  const data = localStorage.getItem(`user_${userId}_progress`);
  return data ? JSON.parse(data) : null;
}
```

### Q5: 다른 언어로도 사용 가능한가요?

네! 데이터 구조는 언어 독립적입니다:

```json
{
  "language": "ja",
  "lyrics": [
    {
      "japanese": "こんにちは",
      "romanization": "konnichiwa",
      "translation": "hello"
    }
  ]
}
```

## 🎨 커스터마이징 예제

### 색상 테마 변경

```html
<style>
  /* 기본 파란색 → 보라색으로 변경 */
  .bg-blue-600 { background-color: #7c3aed !important; }
  .text-blue-600 { color: #7c3aed !important; }
  .border-blue-600 { border-color: #7c3aed !important; }
</style>
```

### 타이머 추가

```javascript
let timeRemaining = 60; // 60초

const timer = setInterval(() => {
  timeRemaining--;
  document.getElementById('timer').textContent = timeRemaining;

  if (timeRemaining <= 0) {
    clearInterval(timer);
    alert('시간 종료!');
    checkAnswers();
  }
}, 1000);
```

### 점수 시스템 추가

```javascript
let score = 0;
const pointsPerCorrect = 10;
const bonusForPerfect = 50;

function calculateScore() {
  score = correctCount * pointsPerCorrect;
  if (correctCount === totalBlanks) {
    score += bonusForPerfect; // 완벽 보너스
  }
  return score;
}
```

## 📦 패키지 구조 예제

```
my-korean-learning-game/
├── index.html              # 메인 페이지
├── games/
│   ├── fill-in-blank.html
│   └── flashcards.html
├── data/
│   ├── songs/
│   │   ├── song1.json
│   │   └── song2.json
│   └── config.json
├── assets/
│   ├── css/
│   │   └── custom.css
│   ├── js/
│   │   └── game-logic.js
│   └── audio/
│       ├── song1.mp3
│       └── correct.mp3
└── README.md
```

## 🚀 배포 옵션

### 1. GitHub Pages (무료)
```bash
git init
git add .
git commit -m "Initial commit"
git push origin main

# Settings > Pages > Source: main branch
```

### 2. Netlify (무료)
```bash
# Drag & drop 폴더
# 또는 CLI:
npm install -g netlify-cli
netlify deploy
```

### 3. Vercel (무료)
```bash
npm i -g vercel
vercel
```

## 📚 추가 리소스

- 데이터 구조: `docs/data-structure-guide.md`
- 템플릿: `templates/`
- 예제: `examples/`
- 기획안: `../korean-song-learning-game-plan.md`

## 🤝 다음 단계

1. ✅ 첫 게임 만들기
2. ⬜ 3곡 데이터 추가
3. ⬜ UI 커스터마이징
4. ⬜ 친구와 테스트
5. ⬜ 피드백 수집
6. ⬜ 개선 및 추가 기능
7. ⬜ 배포!

---

**지금 바로 시작하세요!**

Claude Code에서:
```
가사 빈칸 채우기 게임 만들어줘
```
