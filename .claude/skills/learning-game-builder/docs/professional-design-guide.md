# 전문적인 교육용 게임 디자인 가이드

학습 게임을 전문적인 교육 플랫폼 수준으로 만드는 디자인 시스템 가이드입니다.

## 🎨 디자인 시스템 구성

### 1. CSS 변수 시스템

```css
:root {
    /* 브랜드 색상 */
    --primary: #667eea;
    --primary-dark: #5568d3;
    --secondary: #764ba2;
    --accent: #f093fb;

    /* 시맨틱 색상 */
    --success: #10b981;
    --warning: #f59e0b;
    --error: #ef4444;
    --info: #3b82f6;

    /* 그레이 스케일 */
    --gray-50: #f9fafb;
    --gray-100: #f3f4f6;
    --gray-500: #6b7280;
    --gray-900: #111827;

    /* 레벨 색상 */
    --level-n5: #4ade80;  /* 녹색 - 초급 */
    --level-n4: #60a5fa;  /* 파랑 - 초중급 */
    --level-n3: #a78bfa;  /* 보라 - 중급 */
    --level-n2: #fb923c;  /* 주황 - 중상급 */
    --level-n1: #f87171;  /* 빨강 - 고급 */

    /* 타이포그래피 */
    --font-sans: 'Pretendard', -apple-system, sans-serif;

    /* 폰트 크기 */
    --text-xs: 0.75rem;    /* 12px */
    --text-sm: 0.875rem;   /* 14px */
    --text-base: 1rem;     /* 16px */
    --text-lg: 1.125rem;   /* 18px */
    --text-xl: 1.25rem;    /* 20px */
    --text-2xl: 1.5rem;    /* 24px */
    --text-3xl: 1.875rem;  /* 30px */
    --text-4xl: 2.25rem;   /* 36px */
    --text-5xl: 3rem;      /* 48px */

    /* 스페이싱 */
    --space-1: 0.25rem;    /* 4px */
    --space-2: 0.5rem;     /* 8px */
    --space-3: 0.75rem;    /* 12px */
    --space-4: 1rem;       /* 16px */
    --space-6: 1.5rem;     /* 24px */
    --space-8: 2rem;       /* 32px */
    --space-12: 3rem;      /* 48px */

    /* 그림자 */
    --shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
    --shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
    --shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1);
    --shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1);

    /* 보더 반경 */
    --radius-sm: 0.375rem;  /* 6px */
    --radius-md: 0.5rem;    /* 8px */
    --radius-lg: 0.75rem;   /* 12px */
    --radius-xl: 1rem;      /* 16px */
    --radius-2xl: 1.5rem;   /* 24px */

    /* 트랜지션 */
    --transition-fast: 150ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-base: 250ms cubic-bezier(0.4, 0, 0.2, 1);
    --transition-slow: 350ms cubic-bezier(0.4, 0, 0.2, 1);
}
```

### 2. 웹폰트 적용

```html
<!-- Pretendard - 한글 최적화 폰트 -->
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard/dist/web/static/pretendard.css">
```

```css
body {
    font-family: var(--font-sans);
    line-height: 1.6;
}
```

## 🏗️ 컴포넌트 디자인

### 1. 전문적인 헤더

```html
<header class="header">
    <div class="header-left">
        <button class="home-btn">🏠 <span>홈</span></button>
        <div class="logo">
            <span class="logo-icon">📚</span>
            <div class="logo-text">
                <span class="logo-main">JLPT Master</span>
                <span class="logo-sub">일본어 한자 학습 플랫폼</span>
            </div>
        </div>
    </div>
    <div class="header-stats">
        <div class="stat-item">
            <span class="stat-label">학습한 단어</span>
            <span class="stat-value primary">0</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">정답률</span>
            <span class="stat-value success">0%</span>
        </div>
        <div class="stat-item">
            <span class="stat-label">연속 학습</span>
            <span class="stat-value warning">0일</span>
        </div>
    </div>
</header>
```

```css
.header {
    background: white;
    border-radius: var(--radius-xl);
    padding: var(--space-4) var(--space-6);
    box-shadow: var(--shadow-lg);
    margin-bottom: var(--space-6);
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo-main {
    font-size: var(--text-xl);
    font-weight: 700;
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.stat-value {
    font-size: var(--text-lg);
    font-weight: 700;
}
```

### 2. 레벨 선택 카드

```html
<div class="level-selection-card">
    <div class="level-selection-title">
        <span>📚</span> 레벨 선택
    </div>
    <div class="level-grid">
        <button class="level-btn level-n5">N5</button>
        <button class="level-btn level-n4">N4</button>
        <button class="level-btn level-n3">N3</button>
        <button class="level-btn level-n2">N2</button>
        <button class="level-btn level-n1">N1</button>
    </div>
</div>
```

```css
.level-selection-card {
    background: white;
    border-radius: var(--radius-xl);
    padding: var(--space-6);
    box-shadow: var(--shadow-md);
}

.level-btn {
    padding: var(--space-3) var(--space-4);
    border-radius: var(--radius-md);
    border: 2px solid var(--gray-200);
    background: white;
    font-size: var(--text-base);
    font-weight: 600;
    cursor: pointer;
    transition: var(--transition-base);
}

.level-btn.level-n5 {
    background: linear-gradient(135deg, #4ade80 0%, #22c55e 100%);
    color: white;
    border: none;
}
```

### 3. 모드 선택 카드 (심플 디자인)

**버전 1: 상세한 설명 포함 (공간 여유 있을 때)**

```html
<div class="mode-selection">
    <h2 class="mode-selection-title">학습 모드 선택</h2>
    <p class="mode-selection-subtitle">학습 스타일에 맞는 모드를 선택하세요</p>

    <div class="mode-grid">
        <button class="mode-card">
            <span class="mode-card-icon">🎓</span>
            <div class="mode-card-title">자동 학습</div>
            <div class="mode-card-description">
                단어, 의미, 예문을 순차적으로 학습합니다.
            </div>
            <span class="mode-card-badge">⏱️ 30분 권장</span>
        </button>
    </div>
</div>
```

```css
.mode-card {
    background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
    color: white;
    padding: var(--space-6);
    border-radius: var(--radius-lg);
    cursor: pointer;
    transition: var(--transition-base);
    text-align: left;
    position: relative;
    overflow: hidden;
}

.mode-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}

.mode-card-icon {
    font-size: var(--text-5xl);
    margin-bottom: var(--space-3);
}

.mode-card-title {
    font-size: var(--text-xl);
    font-weight: 700;
    margin-bottom: var(--space-2);
}

.mode-card-badge {
    display: inline-block;
    background: rgba(255, 255, 255, 0.2);
    padding: var(--space-1) var(--space-3);
    border-radius: var(--radius-full);
    font-size: var(--text-xs);
    font-weight: 600;
}
```

**버전 2: 심플 & 컴팩트 (공간 절약) ⭐ 추천**

```html
<div class="mode-selection">
    <div class="section-label">🎮 학습 모드 선택</div>
    <div class="mode-grid">
        <div class="mode-card recommended" onclick="startMode('auto-study')">
            <div class="mode-card-icon">🎓</div>
            <div class="mode-card-title">자동 학습</div>
            <span class="mode-card-badge">추천</span>
        </div>
        <div class="mode-card" onclick="startMode('flashcard')">
            <div class="mode-card-icon">📇</div>
            <div class="mode-card-title">플래시카드</div>
            <span class="mode-card-badge">5-10분</span>
        </div>
    </div>
</div>
```

```css
/* 심플 모드 선택 - 공간 최적화 */
.mode-selection {
    background: white;
    border-radius: var(--radius-lg);
    padding: var(--space-4);
    box-shadow: var(--shadow-md);
    margin-bottom: var(--space-4);
}

.mode-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: var(--space-2);
}

.mode-card {
    background: white;
    color: var(--gray-900);
    border: 2px solid var(--gray-200);
    padding: var(--space-3);
    border-radius: var(--radius-md);
    cursor: pointer;
    transition: var(--transition-base);
    text-align: center;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: var(--space-1);
}

.mode-card.recommended {
    border-color: var(--success);
    background: var(--success);
    color: white;
}

.mode-card:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}

.mode-card-icon {
    font-size: var(--text-3xl);
}

.mode-card-title {
    font-size: var(--text-base);
    font-weight: 600;
}

.mode-card-badge {
    font-size: var(--text-xs);
    opacity: 0.8;
}
```

### 4. 대시보드 카드

```html
<div class="dashboard">
    <div class="dashboard-card">
        <div class="card-header">
            <h3 class="card-title">학습 진도</h3>
            <span class="card-icon">📊</span>
        </div>
        <div class="card-content">
            <div class="progress-bar">
                <div class="progress-fill" style="width: 45%"></div>
            </div>
            <p>150개 중 68개 완료 (45%)</p>
        </div>
    </div>

    <div class="dashboard-card">
        <div class="card-header">
            <h3 class="card-title">오늘의 목표</h3>
            <span class="card-icon">🎯</span>
        </div>
        <div class="card-content">
            <p class="stat-large">30 / 50</p>
            <p>단어 완료</p>
        </div>
    </div>
</div>
```

```css
.dashboard {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: var(--space-6);
}

.dashboard-card {
    background: white;
    border-radius: var(--radius-xl);
    padding: var(--space-6);
    box-shadow: var(--shadow-md);
    transition: var(--transition-base);
}

.dashboard-card:hover {
    box-shadow: var(--shadow-xl);
    transform: translateY(-2px);
}
```

## 📐 레이아웃 패턴

### 1. 컨테이너

```css
.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: var(--space-6);
}
```

### 2. 그리드 레이아웃

```css
/* 2열 그리드 */
.grid-2 {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-4);
}

/* 3열 그리드 */
.grid-3 {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--space-4);
}

/* 반응형 그리드 */
.grid-responsive {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: var(--space-4);
}
```

### 3. Flexbox 레이아웃

```css
/* 수평 중앙 정렬 */
.flex-center {
    display: flex;
    justify-content: center;
    align-items: center;
}

/* 양 끝 정렬 */
.flex-between {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

/* 수직 스택 */
.flex-col {
    display: flex;
    flex-direction: column;
    gap: var(--space-4);
}
```

## 🎯 브랜딩 요소

### 1. 로고 디자인

```html
<div class="logo">
    <span class="logo-icon">📚</span>
    <div class="logo-text">
        <span class="logo-main">JLPT Master</span>
        <span class="logo-sub">일본어 한자 학습 플랫폼</span>
    </div>
</div>
```

**브랜드 아이덴티티:**
- 아이콘: 교육 관련 이모지 (📚, 🎓, 📝)
- 메인 색상: 그라데이션 (보라→분홍)
- 서브 텍스트: 명확한 가치 제안

### 2. 레벨 뱃지

```html
<span class="level-badge level-n5">🌱 N5 초급</span>
<span class="level-badge level-n4">🌿 N4 초중급</span>
<span class="level-badge level-n3">🌳 N3 중급</span>
<span class="level-badge level-n2">🏔️ N2 중상급</span>
<span class="level-badge level-n1">🗻 N1 고급</span>
```

```css
.level-badge {
    display: inline-flex;
    align-items: center;
    gap: var(--space-2);
    padding: var(--space-2) var(--space-4);
    border-radius: var(--radius-full);
    font-size: var(--text-sm);
    font-weight: 600;
}

.level-badge.level-n5 {
    background: var(--level-n5);
    color: white;
}
```

## 📱 반응형 디자인

### 모바일 우선 (Mobile First)

```css
/* 모바일 (기본) */
.container {
    padding: var(--space-4);
}

/* 태블릿 (768px 이상) */
@media (min-width: 768px) {
    .container {
        padding: var(--space-6);
    }

    .grid-responsive {
        grid-template-columns: repeat(2, 1fr);
    }
}

/* 데스크톱 (1024px 이상) */
@media (min-width: 1024px) {
    .container {
        padding: var(--space-8);
    }

    .grid-responsive {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

## ✨ 마이크로 인터랙션

### 1. 호버 효과

```css
.interactive-card {
    transition: var(--transition-base);
}

.interactive-card:hover {
    transform: translateY(-4px);
    box-shadow: var(--shadow-xl);
}
```

### 2. 클릭 피드백

```css
.button {
    transition: var(--transition-fast);
}

.button:active {
    transform: scale(0.98);
}
```

### 3. 로딩 애니메이션

```css
@keyframes pulse {
    0%, 100% {
        opacity: 1;
    }
    50% {
        opacity: 0.5;
    }
}

.loading {
    animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}
```

## 🎨 전문적인 색상 활용

### 1. 의미 전달

```css
/* 성공 */
.success-message {
    background: var(--success);
    color: white;
}

/* 경고 */
.warning-message {
    background: var(--warning);
    color: white;
}

/* 오류 */
.error-message {
    background: var(--error);
    color: white;
}
```

### 2. 계층적 구조

```css
/* 중요한 요소 */
.primary-action {
    background: var(--primary);
    color: white;
}

/* 보조 요소 */
.secondary-action {
    background: transparent;
    border: 2px solid var(--primary);
    color: var(--primary);
}

/* 비활성 요소 */
.disabled {
    background: var(--gray-200);
    color: var(--gray-500);
    cursor: not-allowed;
}
```

## 🚀 자동 생성 예시

```javascript
// CSS 변수 기반 컴포넌트 생성
function generateProfessionalHeader(config) {
    return `
    <header class="header">
        <div class="logo">
            <span class="logo-icon">${config.icon}</span>
            <div class="logo-text">
                <span class="logo-main">${config.title}</span>
                <span class="logo-sub">${config.subtitle}</span>
            </div>
        </div>
        <div class="header-stats">
            ${config.stats.map(stat => `
                <div class="stat-item">
                    <span class="stat-label">${stat.label}</span>
                    <span class="stat-value ${stat.color}">${stat.value}</span>
                </div>
            `).join('')}
        </div>
    </header>
    `;
}

// 사용 예시
const header = generateProfessionalHeader({
    icon: '📚',
    title: 'JLPT Master',
    subtitle: '일본어 한자 학습 플랫폼',
    stats: [
        { label: '학습한 단어', value: '150', color: 'primary' },
        { label: '정답률', value: '85%', color: 'success' },
        { label: '연속 학습', value: '7일', color: 'warning' }
    ]
});
```

## 📐 공간 최적화 가이드 (Space Optimization)

학습 화면에서 **스크롤 없이** 콘텐츠를 표시하는 것이 학습자 경험에 매우 중요합니다.

### 원칙

1. **컨트롤 영역 최소화** - 버튼, 진행 상태 표시를 최소 공간으로
2. **콘텐츠 영역 최대화** - 학습 내용이 화면의 대부분을 차지
3. **스크롤 제거** - `overflow: hidden` + flexbox로 화면에 완벽히 맞춤
4. **반응형 텍스트** - `clamp()`로 화면 크기에 맞춰 자동 조정

### 자동학습 모드 풀스크린 패턴 ⭐

```css
/* 1. 컨테이너 - 전체 화면 사용 */
.auto-study-container {
    width: 100%;
    height: calc(100vh - 100px);  /* 헤더 제외 */
    display: flex;
    flex-direction: column;
    padding: var(--space-2);
    box-sizing: border-box;
    gap: var(--space-2);
}

/* 2. 진행 상태 - 최소 공간 */
.auto-study-progress {
    font-size: var(--text-sm);
    font-weight: 600;
    color: var(--primary);
    padding: var(--space-1) 0;
    flex-shrink: 0;  /* 고정 크기 */
}

/* 3. 컨트롤 버튼 - 컴팩트 */
.auto-study-controls {
    display: flex;
    justify-content: center;
    gap: var(--space-2);
    padding: 0;  /* 패딩 제거 */
    flex-shrink: 0;  /* 고정 크기 */
}

.auto-study-btn {
    padding: var(--space-1) var(--space-3);
    font-size: var(--text-xs);
    font-weight: 600;
    border: none;
    border-radius: var(--radius-md);
    cursor: pointer;
    white-space: nowrap;
}

/* 4. 학습 카드 - 남은 공간 모두 사용 */
.auto-study-card {
    background: white;
    border: 2px solid var(--primary);
    border-radius: var(--radius-xl);
    padding: var(--space-4);
    flex: 1;  /* ⭐ 남은 공간 모두 차지 */
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    min-height: 0;  /* ⭐ flexbox 축소 허용 */
    overflow: hidden;  /* ⭐ 스크롤 제거 */
}

/* 5. 카드 내 요소 - 축소 가능 */
.auto-study-card > * {
    flex-shrink: 1;  /* ⭐ 공간 부족 시 자동 축소 */
    min-height: 0;
}

/* 6. 반응형 폰트 크기 */
.auto-study-word {
    font-size: clamp(2.5rem, 7vw, 5rem);  /* 최소 2.5rem, 최대 5rem */
    font-weight: 700;
    color: var(--primary);
    margin-bottom: var(--space-1);
    line-height: 1.1;  /* 타이트한 줄간격 */
}

.auto-study-reading {
    font-size: clamp(1.2rem, 3.5vw, 2rem);
    color: var(--gray-600);
    margin-bottom: var(--space-1);
    line-height: 1.2;
}

.auto-study-meaning {
    font-size: clamp(1.5rem, 4vw, 2.5rem);
    font-weight: 700;
    color: var(--gray-900);
    margin: var(--space-1) 0;
    line-height: 1.2;
}

.auto-study-example {
    margin-top: var(--space-1);
    padding: var(--space-2);
    background: var(--gray-50);
    border-radius: var(--radius-md);
    font-size: clamp(0.8rem, 2vw, 1.1rem);
    line-height: 1.4;
    max-width: 90%;
}
```

### 모바일 최적화

```css
@media (max-width: 768px) {
    .auto-study-container {
        height: calc(100vh - 50px);  /* 더 많은 공간 확보 */
        padding: var(--space-1);
        gap: var(--space-1);
    }

    .auto-study-card {
        padding: var(--space-2);
    }

    .auto-study-word {
        font-size: clamp(2rem, 6vw, 4rem);
        margin-bottom: 0.25rem;
    }

    .auto-study-reading {
        font-size: clamp(1rem, 3vw, 1.5rem);
        margin-bottom: 0.25rem;
    }

    .auto-study-meaning {
        font-size: clamp(1.2rem, 3.5vw, 2rem);
        margin: 0.25rem 0;
    }

    .auto-study-example {
        padding: var(--space-1);
        margin-top: 0.25rem;
        font-size: clamp(0.7rem, 1.8vw, 1rem);
    }

    .auto-study-btn {
        padding: var(--space-1) var(--space-2);
        font-size: 0.65rem;
    }

    .auto-study-progress {
        font-size: 0.7rem;
        padding: 0.25rem 0;
    }
}
```

### 공간 최적화 체크리스트

- [ ] `flex: 1`로 콘텐츠 영역이 남은 공간 모두 사용
- [ ] `flex-shrink: 0`로 컨트롤 영역 크기 고정
- [ ] `overflow: hidden`으로 스크롤 완전 차단
- [ ] `clamp()`로 반응형 폰트 크기 자동 조정
- [ ] 모든 padding/margin을 최소화 (`var(--space-1)`, `var(--space-2)`)
- [ ] `line-height` 타이트하게 (1.1~1.4)
- [ ] 모바일에서 더 많은 공간 확보 (`calc(100vh - 50px)`)

### 공간 배분 예시

```
데스크톱 (100vh):
┌─────────────────────┐
│ 헤더 (100px)        │
├─────────────────────┤
│ 진행 상태 (30px)    │
│ 컨트롤 버튼 (40px)  │
├─────────────────────┤
│                     │
│   학습 카드 영역     │
│   (flex: 1)         │
│   [스크롤 없음]     │
│                     │
└─────────────────────┘

모바일 (100vh):
┌─────────────────────┐
│ 헤더 (50px)         │
├─────────────────────┤
│ 상태+버튼 (50px)    │
├─────────────────────┤
│                     │
│   학습 카드 영역     │
│   (더 넓은 공간)    │
│                     │
└─────────────────────┘
```

## 📊 Before & After

| 요소 | 기본 디자인 | 전문적인 디자인 |
|------|------------|----------------|
| 폰트 | 시스템 폰트 | Pretendard 웹폰트 |
| 색상 | 하드코딩 | CSS 변수 시스템 |
| 레이아웃 | 단순 중앙 배치 | 카드 기반 그리드 |
| 헤더 | 단순 타이틀 | 브랜딩 + 통계 |
| 버튼 | 평면 디자인 | 그라데이션 + 호버 효과 |
| 간격 | 고정값 (px) | 변수 기반 (rem) |
| 공간 활용 | 스크롤 발생 | 풀스크린 최적화 ⭐ |
| 모드 선택 | 상세 설명 | 심플 & 컴팩트 ⭐ |

---

**이 디자인 시스템을 사용하면 학습 게임이 전문적인 교육 플랫폼 수준으로 향상됩니다!** 🎓
