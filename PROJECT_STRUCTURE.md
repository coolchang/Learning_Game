# Learning Game 프로젝트 구조 분석

**최종 업데이트**: 2025-10-25
**프로젝트 루트**: `/home/kim-h/work/Learning_Game`
**정리 상태**: ✅ **정리 완료** (Option 3: 현재 상태 유지 + 정리)

---

## 📁 프로젝트 개요

총 **5개의 주요 프로젝트**와 정리된 폴더 구조를 가지고 있습니다.

### 정리된 폴더 구조
```
Learning_Game/
├── business-english-game/      # 비즈니스 영어 학습 게임 (완성)
├── japanese-flashcard-game/    # 일본어 플래시카드 게임 (완성)
├── japanese-learning-game/     # 일본어 학습 게임 (미완성)
├── kanji-learning-game/        # 한자 학습 게임 (완성)
├── .claude/skills/
│   └── learning-game-builder/  # 노래 기반 학습 게임 스킬 (완성)
├── docs/                       # 📄 기획서 및 문서
├── tests/                      # 🧪 테스트 파일
└── venv/                       # Python 가상 환경
```

---

## 🎯 주요 프로젝트

### 1. 💼 Business English Game (비즈니스 영어 학습 게임)
**경로**: `/business-english-game/`
**상태**: ✅ **완성** (가장 최신, 가장 완성도 높음)
**유형**: Claude Skill + Standalone Game

#### 구조
```
business-english-game/
├── SKILL.md                          # Claude 스킬 정의
├── README.md                         # 사용 가이드
├── scripts/
│   ├── game_generator.py            # 기본 퀴즈 생성
│   ├── generate_advanced_game.py    # 15 스테이지 게임 생성
│   └── generate_enhanced_audio_game.py  # 오디오 개선 버전 생성
├── references/
│   ├── business_expressions.md      # 100+ 비즈니스 표현
│   ├── scenarios.md                 # 10+ 시나리오
│   ├── vocabulary_by_industry.md    # 업종별 어휘
│   └── advanced_expressions_stages.json  # 105개 고급 표현 (15 스테이지)
└── assets/
    ├── templates/
    │   ├── quiz-template.html       # 기본 퀴즈
    │   ├── stage-quiz-template.html # 스테이지 게임
    │   └── stage-quiz-enhanced-audio.html  # 오디오 개선 버전
    └── icons/
        ├── correct.svg
        ├── wrong.svg
        └── hint.svg
```

#### 기능
- ✅ 15개 진행형 스테이지
- ✅ 105개 고급 비즈니스 영어 표현
- ✅ 진행도 저장 (LocalStorage)
- ✅ 스테이지 언락 시스템
- ✅ ResponsiveVoice.js 통합 (고품질 음성)
- ✅ 6개 자연스러운 보이스 (US/UK/AU)
- ✅ Web Speech API 폴백
- ✅ 모바일 반응형

#### 생성 가능한 게임
1. **기본 퀴즈**: `python scripts/game_generator.py`
2. **15 스테이지 게임**: `python scripts/generate_advanced_game.py`
3. **오디오 개선 버전**: `python scripts/generate_enhanced_audio_game.py` ⭐ **추천**

---

### 2. 🎵 Learning Game Builder (범용 학습 게임 빌더)
**경로**: `/.claude/skills/learning-game-builder/`
**상태**: ✅ **완성** (Claude Skill)
**유형**: Claude Skill (노래 기반 학습 게임)

#### 구조
```
.claude/skills/learning-game-builder/
├── SKILL.md                    # 스킬 정의
├── README.md
├── templates/
│   ├── fill-in-blank-template.html
│   └── flashcard-template.html
└── references/
    └── game-design-patterns.md
```

#### 기능
- 한국어 노래 기반 학습 게임
- 가사 빈칸 채우기
- 어휘 플래시카드
- 순서 맞추기
- 번역 매칭

---

### 3. 🇯🇵 Japanese Learning Game
**경로**: `/japanese-learning-game/`
**상태**: ⚠️ **부분 완성** (구조만 있음)
**유형**: Claude Skill (미완성)

#### 구조
```
japanese-learning-game/
├── SKILL.md
├── assets/
│   └── game-template/
│       └── README.md
├── references/
└── scripts/
```

#### 상태
- SKILL.md 존재
- 템플릿/스크립트 미구현
- 기획 문서만 존재 (`japanese-learning-game-skill-planning.md`)

---

### 4. 🎴 Japanese Flashcard Game
**경로**: `/japanese-flashcard-game/`
**상태**: ✅ **완성** (Standalone HTML 게임)
**유형**: Standalone Game

#### 파일
```
japanese-flashcard-game/
├── README.md
├── index.html
├── game.html
├── japanese-game-v2.html
└── src/
```

#### 기능
- 일본어 플래시카드 게임
- 다중 버전 (v1, v2)
- 독립 실행형 HTML

---

### 5. 📝 Kanji Learning Game
**경로**: `/kanji-learning-game/`
**상태**: ✅ **완성** (Standalone HTML 게임) + ⭐ **오디오 개선**
**유형**: Standalone Game

#### 파일
```
kanji-learning-game/
├── kanji-game.html
└── kanji-game-standalone.html    # ⭐ 오디오 개선 버전
```

#### 기능
- ✅ 한자 학습 게임 (6가지 모드)
- ✅ Standalone 버전 (100단어)
- ✅ **예문 음성 재생** (플래시카드 뒷면)
- ✅ **ResponsiveVoice.js** 고품질 음성
- ✅ 음성 설정 UI (엔진/종류/속도/자동재생)
- ✅ Web Speech API 폴백

---

## 📄 기획/문서 파일 (`docs/`)

### 1. 비즈니스영어학습게임스킬_기획서.md
- **크기**: 11KB
- **내용**: Business English Game의 초기 기획서
- **상태**: 구현 완료

### 2. japanese-learning-game-skill-planning.md
- **크기**: 52KB
- **내용**: 일본어 학습 게임 상세 기획
- **상태**: 미구현

### 3. korean-song-learning-game-plan.md
- **크기**: 7KB
- **내용**: 한국 노래 학습 게임 기획
- **상태**: Learning Game Builder로 구현

### 4. implementation-roadmap.md
- **크기**: 7KB
- **내용**: 전체 구현 로드맵

### 5. sample-SKILL.md
- **크기**: 2.6KB
- **내용**: 스킬 예시 템플릿

---

## 🧪 테스트 파일 (`tests/`)

### 1. test-game-with-audio.html
- **크기**: 24KB
- **내용**: 오디오 기능 테스트용
- **상태**: 개발 중 테스트 파일

### 2. test-game.html
- **크기**: 17KB
- **내용**: 기본 퀴즈 테스트용
- **상태**: 개발 중 테스트 파일

---

## 🗂️ 기타

### venv/
- Python 가상 환경
- 스크립트 실행용

---

## 📊 프로젝트 우선순위

### 완성도 높음 (즉시 사용 가능)
1. ✅ **Business English Game** - 가장 완성도 높음, 모든 기능 구현
2. ✅ **Learning Game Builder Skill** - Claude Skill로 사용 가능
3. ✅ **Japanese Flashcard Game** - 독립 실행 가능
4. ✅ **Kanji Learning Game** - 독립 실행 가능

### 미완성 (추가 작업 필요)
5. ⚠️ **Japanese Learning Game** - 구조만 있음, 구현 필요

---

## 🎯 권장 정리 방안

### 방안 1: 프로젝트별 폴더 정리
```
Learning_Game/
├── 01-business-english-game/     # 비즈니스 영어 (완성)
├── 02-japanese-games/            # 일본어 관련 통합
│   ├── flashcard/
│   ├── kanji/
│   └── learning-skill/
├── 03-korean-song-game/          # 한국 노래 (스킬)
├── docs/                         # 모든 기획서
├── outputs/                      # 생성된 게임 파일
└── templates/                    # 공통 템플릿
```

### 방안 2: 용도별 분류
```
Learning_Game/
├── skills/                       # Claude Skills
│   ├── business-english/
│   ├── learning-game-builder/
│   └── japanese-learning/
├── games/                        # Standalone Games
│   ├── japanese-flashcard/
│   └── kanji-learning/
├── outputs/                      # 생성된 게임
└── docs/                         # 문서
```

### 방안 3: 현재 상태 유지 + 정리
- 테스트 파일 이동 → `tests/` 폴더
- 기획서 이동 → `docs/` 폴더
- 미완성 프로젝트 → `wip/` (Work in Progress)
- venv는 `.gitignore`

---

## 🚀 즉시 사용 가능한 것

1. **비즈니스 영어 학습** ⭐:
   ```bash
   # 게임 생성
   python business-english-game/scripts/generate_enhanced_audio_game.py

   # 브라우저로 열기 (생성 후)
   open advanced-business-english-ENHANCED-AUDIO.html
   ```

2. **한자 학습** ⭐ (오디오 개선):
   ```bash
   open kanji-learning-game/kanji-game-standalone.html
   ```

3. **일본어 플래시카드**:
   ```bash
   open japanese-flashcard-game/index.html
   ```

---

## 💡 완료 및 추천 사항

### ✅ 완료된 작업
- [x] 테스트 파일을 `tests/` 폴더로 이동
- [x] 기획서를 `docs/` 폴더로 이동
- [x] 프로젝트 구조 문서화 (PROJECT_STRUCTURE.md)
- [x] 한자 게임에 예문 음성 재생 기능 추가
- [x] ResponsiveVoice.js 통합으로 오디오 품질 개선

### 우선순위 1: 문서화 개선
- [ ] README.md 작성 (전체 프로젝트 설명 및 시작 가이드)
- [ ] 각 프로젝트별 README 개선

### 우선순위 2: 미완성 프로젝트 완성
- [ ] Japanese Learning Game 구현 (기획서는 docs/ 폴더에 존재)
- [ ] 공통 템플릿 추출 및 재사용

### 우선순위 3: 통합 및 최적화
- [ ] 스킬들을 통합 패키지로 만들기
- [ ] 공통 오디오 엔진 모듈화
- [ ] 테마/스타일 통일

---

**생성일**: 2025-10-25
**버전**: 1.0
