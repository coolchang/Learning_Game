# 학습 게임 배포 가이드

학습 게임을 온라인으로 배포하는 자동화된 방법을 안내합니다.

## 🎯 배포 옵션

### 1. GitHub Pages (권장 ⭐⭐⭐⭐⭐)
- ✅ 무료
- ✅ HTTPS 자동 지원
- ✅ 커스텀 도메인 가능
- ✅ Git 버전 관리 통합

### 2. Netlify
- ✅ 무료 티어 제공
- ✅ 자동 배포 (Git 연동)
- ✅ 빠른 CDN

### 3. Vercel
- ✅ 무료 티어 제공
- ✅ 초고속 배포
- ✅ 서버리스 함수 지원

## 🚀 GitHub Pages 자동 배포

### 방법 1: 완전 자동 배포 (스크립트)

```bash
#!/bin/bash
# deploy_github_pages.sh

echo "🚀 GitHub Pages 자동 배포 시작..."

# 1. 저장소 URL 확인
if [ -z "$1" ]; then
    echo "사용법: ./deploy_github_pages.sh <GitHub-저장소-URL>"
    exit 1
fi

REPO_URL=$1

# 2. index.html 랜딩 페이지 생성
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="0; url=kanji-game-standalone.html">
    <title>JLPT 한자 학습 게임</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            text-align: center;
        }
        h1 {
            font-size: 2.5em;
            margin-bottom: 20px;
        }
        a {
            display: inline-block;
            padding: 15px 40px;
            background: white;
            color: #667eea;
            text-decoration: none;
            border-radius: 30px;
            font-weight: bold;
            font-size: 1.1em;
            transition: all 0.3s;
        }
        a:hover {
            transform: scale(1.05);
            box-shadow: 0 5px 20px rgba(0,0,0,0.3);
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎌 JLPT 한자 학습 게임</h1>
        <p>페이지를 자동으로 로딩 중...</p>
        <a href="kanji-game-standalone.html">게임 시작하기</a>
    </div>
</body>
</html>
EOF

# 3. .gitignore 생성
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
.Python
venv/

# IDE
.vscode/
.idea/
.DS_Store

# Logs
*.log

# Temporary files
*.tmp
.cache/
EOF

# 4. Git 초기화
git init
git add .
git commit -m "Initial commit: Learning Game

🎮 학습 게임 프로젝트
- 자동 생성된 학습 콘텐츠
- 레벨/스테이지 시스템
- 진도 추적 기능

🤖 Generated with Claude Code
Co-Authored-By: Claude <noreply@anthropic.com>"

# 5. GitHub에 푸시
git branch -M main
git remote add origin $REPO_URL
git push -u origin main

# 6. GitHub Pages 활성화 (gh CLI 사용)
if command -v gh &> /dev/null; then
    gh repo edit --enable-pages --pages-branch main --pages-path /
    echo "✅ GitHub Pages가 자동으로 활성화되었습니다!"
else
    echo "⚠️  GitHub CLI (gh)가 설치되지 않았습니다."
    echo "수동으로 활성화하세요: Settings > Pages > Source: main branch"
fi

# 7. 배포 URL 출력
REPO_NAME=$(basename $REPO_URL .git)
USERNAME=$(echo $REPO_URL | sed 's|.*github.com[:/]\([^/]*\)/.*|\1|')

echo ""
echo "✅ 배포 완료!"
echo "🌐 URL: https://${USERNAME}.github.io/${REPO_NAME}/"
echo ""
echo "⏰ GitHub Pages 빌드에 1-2분 소요됩니다."
```

**사용 방법:**
```bash
chmod +x deploy_github_pages.sh
./deploy_github_pages.sh https://github.com/yourusername/your-repo.git
```

### 방법 2: 수동 배포 (단계별)

#### Step 1: Git 초기화
```bash
cd your-project-directory
git init
git add .
git commit -m "Initial commit"
```

#### Step 2: GitHub 저장소 생성
```bash
# GitHub CLI 사용
gh repo create your-repo-name --public --source=. --remote=origin --push

# 또는 웹에서 저장소 생성 후
git remote add origin https://github.com/yourusername/your-repo.git
git branch -M main
git push -u origin main
```

#### Step 3: GitHub Pages 활성화
1. GitHub 저장소 페이지 방문
2. **Settings** 탭 클릭
3. 왼쪽 메뉴에서 **Pages** 클릭
4. Source: **main** branch 선택
5. **Save** 클릭

#### Step 4: 배포 확인
- URL: `https://yourusername.github.io/your-repo-name/`
- 빌드 시간: 1-2분

### 방법 3: GitHub Actions 자동 배포

`.github/workflows/deploy.yml` 생성:

```yaml
name: Deploy to GitHub Pages

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Setup Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.x'

      - name: Generate Data
        run: |
          cd scripts
          python generate_kanji_data.py
          python split_vocabulary.py

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./
```

## 🌐 커스텀 도메인 설정

### 1. 도메인 구매 (예: Namecheap, GoDaddy)

### 2. DNS 설정
```
Type: CNAME
Name: www
Value: yourusername.github.io
```

### 3. GitHub에서 설정
1. Settings > Pages
2. Custom domain: `www.yourdomain.com`
3. Save

### 4. HTTPS 강제 활성화
- ✅ Enforce HTTPS 체크

## 🚀 Netlify 배포

### 자동 배포 (Git 연동)

```bash
# 1. Netlify CLI 설치
npm install -g netlify-cli

# 2. 로그인
netlify login

# 3. 배포
netlify init

# 프롬프트 답변:
# - Create new site
# - Team: (선택)
# - Site name: your-game-name
# - Build command: (공백)
# - Publish directory: ./

# 4. 자동 배포 확인
# Git push할 때마다 자동 배포됨
```

### 드래그 앤 드롭 배포 (간편)

1. https://app.netlify.com/drop 방문
2. 프로젝트 폴더를 드래그 앤 드롭
3. 즉시 배포 완료!

## ⚡ Vercel 배포

```bash
# 1. Vercel CLI 설치
npm install -g vercel

# 2. 로그인
vercel login

# 3. 배포
vercel

# 프롬프트 답변:
# - Setup and deploy: Yes
# - Scope: (선택)
# - Link to existing project: No
# - Project name: your-game-name
# - Directory: ./
# - Override settings: No

# 4. 프로덕션 배포
vercel --prod
```

## 📊 배포 후 체크리스트

### 1. 기능 테스트
- [ ] 모든 레벨 선택 가능
- [ ] 스테이지 로딩 정상
- [ ] 플래시카드 작동
- [ ] 자동 재생 작동
- [ ] TTS 음성 재생
- [ ] 진도 저장/불러오기
- [ ] 모바일에서 정상 작동

### 2. 성능 최적화
```bash
# 1. 이미지 압축
# 2. JSON 파일 크기 확인 (권장: <100KB per file)
# 3. CSS/JS 압축

# PageSpeed Insights 테스트
https://pagespeed.web.dev/
```

### 3. SEO 최적화
```html
<!-- index.html에 추가 -->
<meta name="description" content="JLPT N5-N1 한자 학습 게임. 2050개 단어로 일본어 마스터하기">
<meta name="keywords" content="JLPT, 한자, 일본어, 학습, 게임">
<meta property="og:title" content="JLPT 한자 학습 게임">
<meta property="og:description" content="2050개 JLPT 어휘로 일본어 학습">
<meta property="og:image" content="./preview.png">
```

## 🔧 배포 문제 해결

### 문제 1: 404 에러
**원인**: GitHub Pages가 index.html을 찾지 못함
**해결**:
```bash
# index.html이 루트에 있는지 확인
ls -la index.html

# 없으면 생성
echo '<meta http-equiv="refresh" content="0; url=game.html">' > index.html
```

### 문제 2: JSON 로딩 실패
**원인**: CORS 정책
**해결**:
```javascript
// 상대 경로 사용
fetch('./data/vocabulary/n5.json')
  .then(response => response.json())
  .then(data => console.log(data));
```

### 문제 3: 배포 후 변경사항 반영 안 됨
**원인**: 브라우저 캐시
**해결**:
```bash
# 1. 강제 새로고침 (Ctrl + Shift + R)
# 2. 버전 쿼리 추가
<script src="game.js?v=1.0.1"></script>
```

## 📈 배포 후 모니터링

### Google Analytics 추가
```html
<!-- index.html에 추가 -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

### 사용자 피드백 수집
```html
<!-- 피드백 버튼 추가 -->
<a href="https://github.com/yourusername/your-repo/issues"
   target="_blank"
   class="feedback-btn">
   피드백 보내기
</a>
```

## 🎯 배포 비교표

| 항목 | GitHub Pages | Netlify | Vercel |
|------|-------------|---------|--------|
| 무료 | ✅ | ✅ (100GB/월) | ✅ (100GB/월) |
| 속도 | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| 설정 난이도 | 쉬움 | 매우 쉬움 | 쉬움 |
| 커스텀 도메인 | ✅ | ✅ | ✅ |
| HTTPS | ✅ | ✅ | ✅ |
| 자동 배포 | ✅ | ✅ | ✅ |
| 빌드 시간 | 1-2분 | 30초 | 30초 |
| 서버리스 함수 | ❌ | ✅ | ✅ |

**권장**: 정적 사이트는 **GitHub Pages**, 고급 기능 필요 시 **Netlify/Vercel**

## 📝 배포 완료 후 README 업데이트

```markdown
## 🌐 온라인 데모

**라이브 데모**: https://yourusername.github.io/your-repo/

## 🚀 로컬 실행

\`\`\`bash
# 1. 저장소 클론
git clone https://github.com/yourusername/your-repo.git
cd your-repo

# 2. 로컬 서버 시작
python3 -m http.server 8000

# 3. 브라우저에서 접속
http://localhost:8000
\`\`\`

## 📱 모바일 지원

✅ 모든 모바일 브라우저 지원
✅ 반응형 디자인
✅ 터치 제스처 지원
```

---

**5분 만에 온라인 학습 게임 서비스 오픈!** 🚀
