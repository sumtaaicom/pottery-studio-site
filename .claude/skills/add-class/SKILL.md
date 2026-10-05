---
name: add-class
description: 흙담 공방 홈페이지(index.html)의 "클래스·가격" 섹션에 새 원데이 클래스 카드를 기존 카드와 같은 모양으로 추가합니다. 사장님이 클래스 이름, 소요 시간, 정원, 가격을 알려 주며 새 클래스를 넣어 달라고 할 때 사용합니다. 예) "도자기 페인팅 클래스 추가해 줘. 1시간 30분, 최대 8명, 1인 35,000원"
---

# 새 원데이 클래스 카드 추가하기

`CLAUDE.md`의 규칙(쉬운 한국어, 디자인 유지, 사실 지어내지 않기, 사진 넣는 법, 화면 확인)을 모두 따릅니다.

## 1. 받을 정보

꼭 필요한 것 4가지입니다. 하나라도 빠졌으면 **추측하지 말고 물어봅니다.**

| 항목 | 예시 | 카드에 들어가는 곳 |
|---|---|---|
| 클래스 이름 | 도자기 페인팅 클래스 | `<h3>` |
| 소요 시간 | 약 1시간 30분 | `소요 시간` 줄 |
| 정원 | 최대 8명 | `정원` 줄 |
| 가격 | 1인 35,000원 | `.class-price` |

사장님이 말한 값을 그대로 씁니다. 표기만 기존 카드에 맞춥니다.
- 시간: "약 2시간", "약 2시간 30분"처럼 앞에 "약"을 붙입니다. "90분"이라고 하면 "약 1시간 30분"으로 씁니다.
- 정원: "최대 N명". 단독 수업이면 "2명 (단독)"처럼 씁니다.
- 가격: "1인 50,000원", "2인 100,000원"처럼 몇 명 기준인지와 쉼표를 넣습니다. 몇 명 기준인지 모르면 물어봅니다.

함께 말해 주면 넣고, 말하지 않았으면 **지어내지 않는** 것들:
- **결과물 개수**(예: 1~2점): 말하지 않았으면 `결과물` 줄을 빼고 TODO 주석을 남깁니다.
- **라벨**(예: 입문 추천, 가장 인기): 말하지 않았으면 `class-tag` 줄을 빼고 TODO 주석을 남깁니다. "인기" 같은 말은 사실이 아니면 쓰지 않습니다.
- **소개 문구**(`.class-desc`): 사장님이 준 내용으로만 한두 문장 씁니다. 받은 내용이 없으면 클래스 이름에서 알 수 있는 것만 담은 짧은 문장을 쓰고(경력, 재료 브랜드, 후기 같은 사실은 넣지 않음), TODO 주석으로 사장님 확인을 부탁합니다.
- **사진**: 아래 3번을 봅니다.

## 2. 카드 넣기

`index.html`의 `<div class="class-grid">` 안, **마지막 `</article>` 바로 뒤**에 넣습니다. 따로 순서를 말했다면 그 자리에 넣습니다.
일반 카드(`class-card`, 버튼은 `btn-ghost`)를 씁니다. 강조 카드(`class-card-featured`)는 이미 하나 있으므로, 사장님이 바꿔 달라고 하지 않으면 쓰지 않습니다.

```html
          <article class="class-card">
            <img class="class-photo" src="images/class-이름-600.jpg" srcset="images/class-이름-600.jpg 600w, images/class-이름-960.jpg 960w" sizes="(max-width: 720px) 92vw, (max-width: 900px) 46vw, 340px" alt="사진에 실제로 보이는 것" width="960" height="720" loading="lazy">
            <div class="class-body">
              <p class="class-tag">라벨</p>
              <h3>클래스 이름</h3>
              <p class="class-desc">소개 문구</p>
              <dl class="class-meta">
                <div><dt>소요 시간</dt><dd>약 N시간</dd></div>
                <div><dt>정원</dt><dd>최대 N명</dd></div>
                <div><dt>결과물</dt><dd>N점</dd></div>
              </dl>
              <p class="class-price">1인 00,000원</p>
              <a class="btn btn-ghost btn-block" href="https://pf.kakao.com/" target="_blank" rel="noopener">이 클래스 예약 문의</a>
            </div>
          </article>
```

- 들여쓰기는 옆 카드와 똑같이 맞춥니다.
- 예약 버튼 주소는 **옆 카드의 `pf.kakao.com` 주소를 그대로 복사**합니다(지금은 `https://pf.kakao.com/`).
- 빠진 정보는 이렇게 표시합니다.
  ```html
  <!-- TODO: 결과물 개수를 알려 주시면 "결과물" 줄을 넣을게요 -->
  ```
- CSS는 고치지 않습니다. 기존 `.class-card` 모양을 그대로 씁니다.

## 3. 사진

- **사진을 올려 줬으면**: `CLAUDE.md` 4번 "사진 넣는 법"대로 4:3 비율 `-600.jpg`, `-960.jpg`를 만듭니다. 파일 이름은 `class-영문이름`으로 짓습니다(예: `class-painting`).
  ```bash
  convert images/class-painting.jpg -resize 1600x1600\> images/class-painting.jpg
  convert images/class-painting.jpg -resize 600x450^ -gravity center -extent 600x450 -quality 75 images/class-painting-600.jpg
  convert images/class-painting.jpg -resize 960x720^ -gravity center -extent 960x720 -quality 75 images/class-painting-960.jpg
  ```
  손님 얼굴이 나오면 촬영 동의를 받았는지 먼저 물어봅니다. `README.md`의 "지금 들어간 실제 사진" 목록도 고칩니다.
- **사진이 없으면**: 다른 자리표시 이미지(`images/entrance.svg`)와 같은 모양으로 `images/class-영문이름.svg`(1200×900)를 만들고 `<img>`에는 `src`만 씁니다(`srcset`, `sizes` 없이 `width="1200" height="900"`, `loading="lazy"`는 그대로).
  alt는 "○○ 클래스 사진 자리"처럼 쓰고, `<!-- TODO: 실제 사진으로 바꿔 주세요 -->` 주석을 답니다. `README.md` 사진 표에도 한 줄 추가합니다.

## 4. 함께 고칠 곳

- **`CLAUDE.md` 3번의 카카오톡 링크 개수**: 카드가 하나 늘면 `pf.kakao.com` 링크도 하나 늘어납니다. "클래스 카드 N개", "지금 N곳"의 숫자를 실제 링크 개수에 맞게 고칩니다. 맨 위 TODO 주석에도 `pf.kakao.com` 글자가 있으므로, 주석은 빼고 링크(`href=`)만 셉니다.
  ```bash
  grep -c 'href="https://pf.kakao.com' index.html
  ```
- **페이지 설명**: `<meta name="description">`, `og:description`에 클래스 종류를 나열하고 있다면 새 클래스도 넣을지 사장님께 물어봅니다(글자 수가 길어지므로 마음대로 바꾸지 않습니다).
- **`.class-guide` 안내 문장**(카드 아래 "어떤 걸 할지 모르겠다면?")은 손대지 않고, 새 클래스를 넣을지 물어만 봅니다.

## 5. 확인

1. 점검: `echo '{}' | python3 .claude/hooks/check-site.py` 가 아무것도 출력하지 않아야 합니다(깨진 링크, 없는 사진, 빠진 alt가 없다는 뜻).
2. `CLAUDE.md` 5번대로 **375px, 768px, 1280px** 화면을 찍어 봅니다. 레이아웃이 바뀌므로 768px도 꼭 봅니다. 사진은 저장소 밖 임시 폴더에 둡니다.
   - `playwright screenshot --full-page`로 찍으면 `loading="lazy"` 사진이 아직 안 받아져 빈 칸으로 찍힐 수 있습니다(특히 휴대폰 너비). 기존 카드 사진도 비어 있다면 고장이 아니라 이 때문이니, 페이지를 끝까지 내린 뒤 다시 찍어 확인합니다.
   - 카드 모양(둥근 모서리, 사진, 알약 버튼)이 옆 카드와 같은지
   - 휴대폰에서 가로로 밀리지 않는지(사진 가로가 375px인지)
   - **카드 개수에 따라 줄이 어떻게 놓이는지**: PC는 한 줄에 3개, 태블릿은 강조 카드 1개 + 2개씩, 휴대폰은 1개씩입니다. 4번째 카드는 PC에서 아랫줄에 혼자 놓입니다. 이 모양을 사장님께 그대로 알려 드리고, 배치를 바꾸고 싶은지 물어봅니다(CSS는 허락받고 고칩니다).

## 6. 마무리 보고

쉬운 한국어로 짧게 알려 줍니다.
- 추가한 카드 내용(이름, 시간, 정원, 가격)
- TODO로 비워 둔 곳과 사장님이 알려 줘야 할 것(결과물, 라벨, 사진, 소개 문구 확인)
- 화면 확인 결과(확인 못 한 것은 못 했다고)
- 커밋 메시지 예: `클래스 카드에 도자기 페인팅 클래스 추가`
