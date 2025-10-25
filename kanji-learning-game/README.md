# 🎌 JLPT 한자 학습 게임

일본어 능력시험(JLPT) N5~N1 레벨의 한자 어휘를 학습할 수 있는 인터랙티브 웹 애플리케이션입니다.

## ✨ 주요 기능

### 📚 방대한 어휘 데이터베이스
- **총 2050개의 JLPT 어휘** 수록
- N5(초급) ~ N1(고급)까지 체계적 구성
- 각 단어마다 한자 분해, 훈음, 예문 포함

### 🎯 레벨별 학습
| 레벨 | 난이도 | 단어 수 | 스테이지 수 |
|------|--------|---------|-------------|
| N5 | 초급 | 150개 | 5개 |
| N4 | 초중급 | 300개 | 10개 |
| N3 | 중급 | 500개 | 10개 |
| N2 | 중상급 | 600개 | 12개 |
| N1 | 고급 | 500개 | 10개 |

### 🎮 다양한 학습 모드

#### 1️⃣ 플래시카드 모드
- 카드 뒤집기로 의미 확인
- "안다/모른다" 분류 학습
- 진도 추적 및 통계

#### 2️⃣ 자동 재생 모드
- 단어 → 의미 → 예문 자동 재생
- TTS(Text-to-Speech) 음성 지원
- **스테이지/레벨 자동 전환**
- 일시정지/재개 기능

### 🔊 음성 지원
- ResponsiveVoice.js를 통한 일본어/한국어 TTS
- 단어, 의미, 예문 순차 재생
- 자연스러운 발음 학습

### 📊 학습 진도 관리
- 레벨별 진도 표시
- 스테이지별 학습 현황
- 실시간 통계 (학습한 단어/총 단어)

## 🚀 시작하기

### 필요 조건
- Python 3.x (로컬 서버용)
- 모던 웹 브라우저 (Chrome, Firefox, Safari, Edge)

### 설치 및 실행

1. **저장소 클론**
```bash
git clone https://github.com/yourusername/kanji-learning-game.git
cd kanji-learning-game
```

2. **로컬 서버 시작**
```bash
python3 -m http.server 8000
```

3. **브라우저에서 접속**
```
http://localhost:8000/kanji-game-standalone.html
```

### 데이터 재생성 (선택사항)

어휘 데이터를 수정하거나 재생성하려면:

```bash
# 1. 어휘 데이터 생성
python3 scripts/generate_kanji_data.py

# 2. 레벨별로 분할
python3 scripts/split_vocabulary.py
```

## 📖 사용 방법

### 레벨 및 스테이지 선택
1. 상단에서 학습할 레벨(N5~N1) 선택
2. 하단에서 스테이지 선택
3. 학습 모드 선택 (플래시카드 또는 자동 재생)

### 플래시카드 모드
- **스페이스바**: 카드 뒤집기
- **←**: 모른다
- **→**: 안다
- **S**: 음성 재생

### 자동 재생 모드
- **스페이스바**: 일시정지/재개
- **ESC**: 중단
- 자동으로 다음 스테이지/레벨로 진행

## 📁 프로젝트 구조

```
kanji-learning-game/
├── kanji-game-standalone.html    # 메인 게임 파일 (단일 HTML)
├── README.md                      # 이 파일
├── CHANGELOG.md                   # 작업 일지
├── data/
│   ├── kanji-vocabulary.json     # 전체 어휘 통합 파일
│   └── vocabulary/
│       ├── stages.json            # 스테이지 메타데이터
│       ├── n5.json               # N5 레벨 어휘
│       ├── n4.json               # N4 레벨 어휘
│       ├── n3.json               # N3 레벨 어휘
│       ├── n2.json               # N2 레벨 어휘
│       └── n1.json               # N1 레벨 어휘
└── scripts/
    ├── generate_kanji_data.py    # 어휘 데이터 생성 스크립트
    └── split_vocabulary.py       # 레벨별 분할 스크립트
```

## 🎨 특징

### 한자 분해 학습
각 단어의 한자를 구성 요소별로 분해하여 제공:
- 한자 표기
- 한글 훈음
- 일본어 음독

예시:
```
概念 (개념)
├─ 概: 개 (대략 개) - がい
└─ 念: 념 (생각 념) - ねん
```

### 실용적인 예문
모든 단어에 실생활 예문 포함:
- 일본어 예문
- 한국어 번역
- 자연스러운 문맥

## 🔧 기술 스택

- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **TTS**: ResponsiveVoice.js
- **Data**: JSON
- **Python**: 데이터 생성 및 관리

## 📊 데이터 품질

✅ JLPT 공식 기준 준수
✅ 실용적인 예문
✅ 정확한 한자 훈음
✅ 자연스러운 번역
✅ 체계적인 난이도 구성

## 🤝 기여하기

기여를 환영합니다! 다음 방법으로 참여할 수 있습니다:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### 어휘 추가/수정
- `scripts/generate_kanji_data.py`에서 어휘 데이터 수정
- 정확한 형식 준수
- 예문 및 번역 품질 확인

## 📝 라이선스

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 감사의 말

- JLPT 공식 가이드라인
- ResponsiveVoice.js
- 일본어 학습 커뮤니티

## 📞 문의

이슈나 제안사항이 있으시면 GitHub Issues를 이용해주세요.

---

**Happy Learning! 頑張って！ 화이팅! 🎌📚**
