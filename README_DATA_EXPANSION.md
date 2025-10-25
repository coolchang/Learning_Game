# 한자 학습 게임 - 2000+ 단어 확장 프로젝트

**작업일**: 2025-10-25
**목표**: JLPT 레벨별 한자 데이터를 2000+개로 확장하고 스테이지 시스템 구축

---

## 🎯 프로젝트 개요

### 목표 데이터 규모
- **N5**: 150단어 (5스테이지 × 30단어)
- **N4**: 300단어 (10스테이지 × 30단어)
- **N3**: 500단어 (10스테이지 × 50단어)
- **N2**: 600단어 (12스테이지 × 50단어)
- **N1**: 500단어 (10스테이지 × 50단어)
- **총합**: 2050단어, 47스테이지

---

## ✅ 완료된 작업 (Phase 1)

### 1. 초기 데이터 구조 생성
- ✅ `data/kanji-vocabulary.json` (153단어)
- ✅ N5 레벨 145단어 완전 작성
- ✅ N4-N1 샘플 데이터 (각 2단어)

### 2. HTML 통합
- ✅ 153단어를 HTML에 임베드
- ✅ 모든 학습 모드 동작 확인

---

## 🚧 현재 작업 중 (Phase 2)

### 스테이지 시스템 구축

#### 1. 파일 구조 설계
```
data/
├── vocabulary/
│   ├── n5.json          # 150단어 (5스테이지)
│   ├── n4.json          # 300단어 (10스테이지)
│   ├── n3.json          # 500단어 (10스테이지)
│   ├── n2.json          # 600단어 (12스테이지)
│   ├── n1.json          # 500단어 (10스테이지)
│   └── stages.json      # 스테이지 메타데이터
└── kanji-vocabulary.json  # 레거시 (삭제 예정)
```

#### 2. 스테이지 메타데이터 형식
```json
{
  "levels": {
    "N5": {
      "totalWords": 150,
      "stages": [
        {
          "id": "n5-s1",
          "name": "N5 Stage 1: 기본 숫자",
          "wordRange": [0, 29],
          "description": "1-10, 기본 숫자 단어"
        },
        // ... 5 stages total
      ]
    },
    "N4": { /* 10 stages */ },
    // ...
  }
}
```

#### 3. 개별 레벨 파일 형식 (n5.json)
```json
{
  "level": "N5",
  "totalWords": 150,
  "stages": 5,
  "words": [
    {
      "id": "n5-0001",
      "stage": 1,
      "word": "一",
      "reading": "いち",
      // ... (기존 구조 유지)
    }
  ]
}
```

---

## 📝 데이터 작성 계획

### Phase 2A: 스테이지 시스템 구축
- [x] 파일 구조 설계
- [ ] `data/vocabulary/stages.json` 생성
- [ ] 레벨별 JSON 파일 템플릿 생성
- [ ] N5 데이터를 `data/vocabulary/n5.json`으로 분리

### Phase 2B: N4-N1 데이터 확장
- [ ] N4: 298개 추가 단어 작성 (현재 2개 → 목표 300개)
- [ ] N3: 498개 추가 단어 작성 (현재 2개 → 목표 500개)
- [ ] N2: 598개 추가 단어 작성 (현재 2개 → 목표 600개)
- [ ] N1: 498개 추가 단어 작성 (현재 2개 → 목표 500개)

### Phase 2C: HTML 통합
- [ ] 외부 JSON 파일 로딩 함수 구현
- [ ] 스테이지 선택 UI 추가
- [ ] 레벨 + 스테이지 필터링 기능
- [ ] 진행도 저장/로드 기능

---

## 🎮 스테이지 시스템 UI 설계

### 레이아웃 구조
```
[헤더: 일본어 한자 학습 게임 JLPT]

[레벨 선택]
┌─────────────────────────────────────┐
│ [N5] [N4] [N3] [N2] [N1]           │
└─────────────────────────────────────┘

[스테이지 선택 - N5 예시]
┌─────────────────────────────────────┐
│ Stage 1  Stage 2  Stage 3           │
│ ✓ 30단어  🔒 30단어  🔒 30단어       │
│                                     │
│ Stage 4  Stage 5                    │
│ 🔒 30단어  🔒 30단어                 │
└─────────────────────────────────────┘

[학습 시작]
```

### 기능 요구사항
1. **진행도 표시**: 각 스테이지의 학습 완료율
2. **잠금 해제**: 이전 스테이지 80% 이상 완료 시 다음 스테이지 해제
3. **레벨 전환**: 레벨 간 자유롭게 이동 가능
4. **스테이지 정보**: 각 스테이지의 주제/내용 표시

---

## 🔧 기술 스펙

### 데이터 로딩
```javascript
// 동적 로딩
async function loadVocabularyByLevel(level) {
    const response = await fetch(`data/vocabulary/${level.toLowerCase()}.json`);
    return await response.json();
}

// 스테이지 메타데이터
async function loadStagesMetadata() {
    const response = await fetch('data/vocabulary/stages.json');
    return await response.json();
}
```

### 스테이지 필터링
```javascript
function getStageWords(levelData, stageNumber) {
    return levelData.words.filter(w => w.stage === stageNumber);
}
```

### 진행도 저장
```javascript
// LocalStorage 구조
{
  "progress": {
    "N5": {
      "s1": { "completed": 30, "total": 30, "accuracy": 95 },
      "s2": { "completed": 15, "total": 30, "accuracy": 82 },
      // ...
    },
    "N4": { /* ... */ }
  }
}
```

---

## 📂 파일 변경 사항

### 생성할 파일
1. `data/vocabulary/stages.json` - 스테이지 메타데이터
2. `data/vocabulary/n5.json` - N5 레벨 150단어
3. `data/vocabulary/n4.json` - N4 레벨 300단어
4. `data/vocabulary/n3.json` - N3 레벨 500단어
5. `data/vocabulary/n2.json` - N2 레벨 600단어
6. `data/vocabulary/n1.json` - N1 레벨 500단어
7. `scripts/generate_stages.py` - 스테이지 데이터 생성 스크립트
8. `scripts/split_vocabulary.py` - 기존 데이터를 레벨별로 분리

### 수정할 파일
1. `kanji-game-standalone.html`
   - 외부 JSON 로딩 추가
   - 스테이지 선택 UI 추가
   - 진행도 관리 기능 추가
2. `scripts/generate_kanji_data.py`
   - N4-N1 데이터 확장

### 삭제할 파일
1. `data/kanji-vocabulary.json` (레거시, 레벨별 파일로 대체)

---

## 🚀 실행 계획

### Step 1: 스테이지 메타데이터 생성
```bash
python scripts/generate_stages.py
```
→ `data/vocabulary/stages.json` 생성

### Step 2: 기존 데이터 분리
```bash
python scripts/split_vocabulary.py
```
→ N5 145단어를 `data/vocabulary/n5.json`으로 이동

### Step 3: N4-N1 데이터 확장
```bash
python scripts/generate_kanji_data.py --level N4 --words 300
python scripts/generate_kanji_data.py --level N3 --words 500
python scripts/generate_kanji_data.py --level N2 --words 600
python scripts/generate_kanji_data.py --level N1 --words 500
```

### Step 4: HTML 통합 및 테스트
- HTML 파일 수정
- 브라우저에서 스테이지 시스템 테스트
- 진행도 저장/로드 테스트

---

## 📊 진행 상황

| 작업 | 상태 | 진행률 |
|------|------|--------|
| 스테이지 시스템 설계 | 진행 중 | 80% |
| 파일 구조 설계 | 완료 | 100% |
| stages.json 생성 | 대기 | 0% |
| N5 데이터 분리 | 대기 | 0% |
| N4 데이터 작성 | 대기 | 0% |
| N3 데이터 작성 | 대기 | 0% |
| N2 데이터 작성 | 대기 | 0% |
| N1 데이터 작성 | 대기 | 0% |
| HTML 스테이지 UI | 대기 | 0% |
| 진행도 시스템 | 대기 | 0% |

---

## 💡 참고사항

- 각 스테이지는 학습하기 적당한 크기로 설계 (30-50단어)
- 스테이지별로 주제/테마를 설정하여 체계적 학습 가능
- 외부 JSON 파일로 분리하여 유지보수 용이
- 진행도 추적으로 학습 동기 부여

---

**최종 업데이트**: 2025-10-25
**버전**: 1.0 (Phase 2 진행 중)
