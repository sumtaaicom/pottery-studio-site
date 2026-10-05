# pottery-studio-site
웹 Claude Code 강의 예시 — 동네 원데이 도자기 공방 홈페이지

## 구성
- `index.html` — 한 페이지 홈페이지. 섹션 순서: 히어로 → 이런 하루를 보내요 → 클래스·가격 → 진행 방식 → 작품·후기 → 공방 소개 → 자주 묻는 질문 → 예약 방법 → 오시는 길
- `style.css` — 스타일 (휴대폰/태블릿/PC 반응형, 휴대폰 하단 고정 예약 버튼 포함)
- `images/` — 사진 자리표시 이미지와 실제 사진. `og-image.jpg`는 카카오톡·인스타그램 등으로 링크를 보낼 때 뜨는 대표 사진(1200×630)
- `robots.txt` · `sitemap.xml` — 검색엔진(구글, 네이버)에게 "읽어 가도 돼요, 페이지는 이거예요"라고 알려 주는 파일
- `favicon.ico` · `favicon.svg` · `apple-touch-icon.png` — 브라우저 탭, 검색 결과, 아이폰 홈 화면에 뜨는 작은 아이콘
- `.claude/` — Claude Code 자동화 설정 (홈페이지 화면과는 상관없음)
  - `settings.json` + `hooks/check-site.py` — Claude가 작업을 마칠 때마다 `index.html`의 깨진 내부 링크(`#…`), 없는 사진 파일, 설명(alt)이 빠진 사진을 점검하고, 문제가 있으면 고치게 하는 훅(자동 실행 설정)
  - `skills/add-class/SKILL.md` — "○○ 클래스 추가해 줘, 시간·정원·가격은 …"이라고 하면 같은 모양의 클래스 카드를 추가하는 스킬(작업 순서 안내서)

## 홈페이지 주소
지금 주소는 `https://pottery-studio-site-mu.vercel.app/` 입니다(Vercel로 배포).
주소가 바뀌면(예: 직접 산 도메인으로 옮길 때) 아래를 모두 같이 바꿔 주세요.
- `index.html` 맨 위 `<head>` 안의 vercel.app 주소 5곳(canonical, og:url, og:image, 구조화 데이터의 url·image)
- `robots.txt`의 Sitemap 줄, `sitemap.xml`의 loc

빌드 없이 `index.html`을 브라우저로 열면 됩니다. `TODO` 주석이 달린 주소·연락처·카카오톡 채널 주소·선생님 소개는 실제 정보로 바꿔 주세요.

## 사진 바꾸는 법
`images/`의 SVG는 모두 자리표시 이미지예요. 각 이미지에 어떤 사진이 들어갈지 적혀 있습니다.
실제 사진(예: `hero-wide.jpg`)을 `images/`에 넣고, `index.html`에서 같은 이름의 `.svg`를 `.jpg`로 바꿔 주세요.
사진은 가로 1600px 정도로 줄여서 넣으면 페이지가 빨리 열립니다.

### 지금 들어간 실제 사진
`hero-wheel` · `class-wheel` · `class-handbuild` · `class-couple-mugs` · `studio` · `work-1`~`work-3`은 실제 사진으로 바뀌었어요.
올려 주신 원본(`이름.jpg`)은 그대로 두고, 자리 비율에 맞게 잘라 작게 만든 파일(`이름-600.jpg`처럼 끝에 가로 크기가 붙은 파일)을 페이지에서 씁니다.
휴대폰은 작은 파일을, 큰 화면은 큰 파일을 알아서 받아 가요. 원본을 바꾸면 작은 파일도 다시 만들어야 합니다.
공유용 대표 사진 `og-image.jpg`는 `hero-wheel.jpg`를 1200×630으로 잘라 만들었어요. 맨 위 사진을 바꾸면 이 파일도 다시 만들어 주세요.

| 파일 | 들어갈 사진 | 비율 |
|---|---|---|
| `hero-wide` / `hero-mobile` | 흙 묻은 두 손이 물레 위 컵을 세우는 장면 | 16:9 / 4:5 |
| `class-handbuilding` · `class-couple` · `class-wheel` | 클래스별 완성품 | 4:3 |
| `class-painting` | 도자기 페인팅 클래스 완성품 (아직 자리표시 이미지) | 4:3 |
| `moment-couple` · `moment-solo` · `moment-friends` | 커플 · 혼자 온 손님 · 친구들 (얼굴이 나오면 촬영 동의 필수) | 1:1 |
| `step-1` ~ `step-6` | 도착 · 시범 · 만들기 · 꾸미기 · 기념 사진 · 완성 그릇 | 1:1 |
| `work-1` ~ `work-6` | 손님 작품 | 1:1 |
| `studio` · `teacher` · `entrance` | 공방 내부 · 선생님 · 입구와 간판 | 4:3 · 4:5 · 4:3 |

후기 섹션은 실제 후기가 생길 때까지 '첫 손님을 기다려요' 문구로 비워 두었습니다.
