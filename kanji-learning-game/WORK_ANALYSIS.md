# 한자 학습 게임 개발 작업 분석

## 🎯 프로젝트 목표
JLPT N5-N1 레벨의 한자 어휘 학습을 위한 인터랙티브 웹 게임 개발

---

## 📊 작업 단계별 분석

### 1단계: 프로젝트 초기 설정
```
작업 내용:
- HTML 게임 파일 생성 (kanji-game-standalone.html)
- 기본 데이터 구조 설계
- 초기 어휘 265개로 시작

자동화 가능성: ⭐⭐⭐⭐⭐
→ 템플릿 기반 프로젝트 구조 자동 생성 가능
```

### 2단계: 데이터 생성 파이프라인 구축
```
작업 내용:
- generate_kanji_data.py: 어휘 데이터 생성
- split_vocabulary.py: 레벨/스테이지별 분할
- 2050개 어휘 데이터 생성

자동화 가능성: ⭐⭐⭐⭐⭐
→ 파라미터 기반 데이터 생성 스크립트 자동화 완전 가능
```

### 3단계: 게임 메커니즘 구현
```
작업 내용:
- 플래시카드 모드
- 자동 재생 모드
- TTS 음성 지원
- 진도 추적

자동화 가능성: ⭐⭐⭐⭐⭐
→ 컴포넌트 기반 코드 생성 가능
```

### 4단계: 자동 진행 시스템
```
작업 내용:
- 스테이지 완료 → 다음 스테이지
- 레벨 완료 → 다음 레벨
- 전체 완료 화면

자동화 가능성: ⭐⭐⭐⭐
→ 로직 패턴화하여 재사용 가능
```

### 5단계: 배포 및 문서화
```
작업 내용:
- GitHub 저장소 설정
- GitHub Pages 배포
- README, CHANGELOG 작성

자동화 가능성: ⭐⭐⭐⭐⭐
→ 템플릿 기반 문서 자동 생성 가능
```

---

## 🏗️ 핵심 아키텍처 패턴

### 데이터 구조 패턴
```
레벨 시스템:
├── levels (N5, N4, N3, N2, N1)
│   ├── totalWords
│   ├── totalStages
│   └── stages[]
│       ├── stageNumber
│       ├── name
│       ├── wordRange
│       └── wordCount

어휘 데이터:
├── word (한자 표기)
├── reading (히라가나)
├── romaji (로마자)
├── meaning (한국어 의미)
├── kanji_breakdown (한자 분해)
├── pos (품사)
├── example_jp (일본어 예문)
├── example_kr (한국어 번역)
└── level (난이도)
```

### 게임 플로우 패턴
```
1. 레벨 선택 → 2. 스테이지 선택 → 3. 모드 선택 → 4. 학습
                                                    ↓
                        6. 다음 레벨/완료 ← 5. 스테이지 완료
```

### 파일 구조 패턴
```
project/
├── index.html              # 랜딩 페이지
├── game.html              # 메인 게임
├── data/
│   ├── all-data.json      # 통합 데이터
│   └── vocabulary/
│       ├── stages.json    # 메타데이터
│       └── [level].json   # 레벨별 데이터
└── scripts/
    ├── generate_data.py   # 데이터 생성
    └── split_data.py      # 데이터 분할
```

---

## 🔄 재사용 가능한 컴포넌트

### 1. 데이터 생성기
```python
class VocabularyGenerator:
    def __init__(self, language, levels, target_count):
        self.language = language
        self.levels = levels
        self.target_count = target_count

    def generate(self):
        # 레벨별 어휘 생성
        pass

    def export_json(self):
        # JSON 파일 생성
        pass
```

**자동화 포인트**: 언어, 레벨 시스템, 목표 개수만 입력하면 자동 생성

### 2. 스테이지 분할기
```python
class StageDivider:
    def __init__(self, words_per_stage, total_words):
        self.words_per_stage = words_per_stage
        self.total_words = total_words

    def calculate_stages(self):
        # 최적 스테이지 수 계산
        pass

    def distribute(self):
        # 단어를 스테이지별로 분배
        pass
```

**자동화 포인트**: 스테이지당 단어 수만 설정하면 자동 분할

### 3. 게임 템플릿
```javascript
class LearningGame {
    constructor(config) {
        this.levels = config.levels;
        this.modes = config.modes;
        this.autoAdvance = config.autoAdvance;
    }

    initializeLevelSelection() { }
    initializeStageSelection() { }
    initializeModes() { }
    handleAutoAdvance() { }
}
```

**자동화 포인트**: 설정만 입력하면 게임 로직 자동 생성

### 4. UI 컴포넌트
```javascript
// 레벨 선택 버튼
function generateLevelButtons(levels) { }

// 스테이지 버튼
function generateStageButtons(stages) { }

// 플래시카드
function createFlashcard(word) { }

// 진도 바
function updateProgress(current, total) { }
```

**자동화 포인트**: 데이터만 넘기면 UI 자동 생성

---

## 🎨 UI/UX 개선 필요 사항

### 현재 문제점
1. ❌ 단조로운 색상 (파란색 위주)
2. ❌ 버튼 디자인 평범함
3. ❌ 레벨 구분이 시각적으로 명확하지 않음
4. ❌ 모바일 반응형 미흡
5. ❌ 애니메이션 부족

### 개선 방향
1. ✅ 레벨별 색상 테마 (N5=녹색, N4=파랑, N3=보라, N2=주황, N1=빨강)
2. ✅ 카드 플립 애니메이션 개선
3. ✅ 진도 바 시각화 강화
4. ✅ 모바일 최적화
5. ✅ 마이크로 인터랙션 추가

---

## 🤖 자동화 가능한 작업 목록

### 높은 우선순위 (⭐⭐⭐⭐⭐)
- [ ] 프로젝트 구조 자동 생성
- [ ] 데이터 스키마 기반 생성 스크립트 생성
- [ ] 게임 HTML/CSS/JS 템플릿 생성
- [ ] GitHub 저장소 초기화 및 배포 설정
- [ ] README/CHANGELOG 자동 생성

### 중간 우선순위 (⭐⭐⭐)
- [ ] 레벨/스테이지 구조 자동 계산
- [ ] UI 컴포넌트 자동 생성
- [ ] 테마 색상 자동 적용
- [ ] 반응형 CSS 자동 생성

### 낮은 우선순위 (⭐)
- [ ] 어휘 데이터 AI 생성 (품질 검증 필요)
- [ ] 예문 자동 생성 (검수 필요)

---

## 📝 학습 게임 개발 워크플로우 (이상적)

### 사용자 입력
```yaml
game_config:
  type: "vocabulary_learning"
  language: "Japanese"
  levels:
    - name: "N5"
      difficulty: 1
      target_words: 150
    - name: "N4"
      difficulty: 2
      target_words: 300
    # ...

  stages:
    words_per_stage: 30

  modes:
    - flashcard
    - auto_play

  features:
    - tts
    - auto_advance
    - progress_tracking

  deployment:
    platform: "github_pages"
    repository: "user/repo"
```

### 자동화 출력
```
1. ✅ 프로젝트 폴더 구조 생성
2. ✅ 데이터 생성 스크립트 생성
3. ✅ 게임 HTML/CSS/JS 생성
4. ✅ 샘플 데이터 생성
5. ✅ README, CHANGELOG 생성
6. ✅ Git 초기화 및 커밋
7. ✅ GitHub Pages 배포 설정
8. ✅ 온라인 URL 제공
```

**시간**: 수동 (8시간) → 자동 (5분)

---

## 🎯 스킬 업데이트 목표

### 기존 스킬 범위
- 노래 가사 기반 학습 게임 (fill-in-blank, matching)

### 확장할 범위
- ✅ 어휘 학습 게임 (flashcard, auto-play)
- ✅ 레벨 시스템 (난이도별 분류)
- ✅ 스테이지 시스템 (학습량 분할)
- ✅ 자동 진행 시스템
- ✅ 데이터 생성 파이프라인
- ✅ 대량 콘텐츠 생성 자동화

### 추가할 기능
- 🆕 다양한 언어 지원 (일본어, 중국어, 영어 등)
- 🆕 다양한 학습 모드 템플릿
- 🆕 UI 테마 시스템
- 🆕 배포 자동화
- 🆕 데이터 검증 도구

---

## 💡 핵심 인사이트

### 패턴 발견
1. **계층적 데이터 구조**가 핵심 (레벨 > 스테이지 > 단어)
2. **메타데이터 분리**가 유연성 제공 (stages.json)
3. **모드 시스템**으로 다양한 학습 스타일 지원
4. **자동 진행**이 사용자 편의성 크게 향상
5. **Python 스크립트**로 대량 데이터 효율적 생성

### 재사용 가능한 코드
- 레벨 선택 UI (모든 레벨 기반 게임에 적용)
- 스테이지 시스템 (모든 단계별 학습에 적용)
- 플래시카드 컴포넌트 (모든 암기 학습에 적용)
- 자동 재생 로직 (모든 순차 학습에 적용)
- TTS 통합 (모든 언어 학습에 적용)

### 개선 필요한 부분
- UI 디자인 자동화 (현재는 수동)
- 데이터 품질 검증 (현재는 믿음 기반)
- 반응형 디자인 체계화
- 접근성 (a11y) 고려

---

## 🚀 다음 단계

1. **learning-game-builder 스킬 업데이트**
   - 이번 작업 패턴 통합
   - 템플릿 추가
   - 자동화 스크립트 추가

2. **UI 디자인 개선**
   - 레벨별 색상 테마
   - 애니메이션 추가
   - 모바일 최적화

3. **스킬 테스트**
   - 새로운 게임으로 스킬 검증
   - 자동화 워크플로우 테스트

4. **문서화**
   - 스킬 사용 가이드 작성
   - 예제 추가
