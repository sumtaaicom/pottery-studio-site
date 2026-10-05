#!/usr/bin/env python3
# 작업이 끝날 때마다(Stop 훅) index.html을 점검하는 스크립트입니다.
# 점검하는 것
#   1. 깨진 내부 링크: href="#이름"인데 페이지에 id="이름"이 없는 경우
#   2. 없는 사진 파일: src, srcset에 적힌 파일이 images/ 등에 실제로 없는 경우
#   3. 사진 설명(alt)이 없거나 비어 있는 <img>
# 문제가 있으면 Claude에게 "멈추지 말고 고치라"고 알려 줍니다.
# 같은 문제가 고쳐지지 않고 또 나오면, 무한 반복을 막기 위해 화면에 경고만 띄웁니다.
import json
import os
import sys
from html.parser import HTMLParser

# 주소 앞부분이 이것이면 바깥 링크라서 파일 점검을 건너뜁니다
EXTERNAL = ("http://", "https://", "//", "data:", "mailto:", "tel:")


class Checker(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.anchors = []  # (줄 번호, 이름)
        self.files = []    # (줄 번호, 파일 경로)
        self.no_alt = []   # (줄 번호, src)

    def handle_starttag(self, tag, attrs):
        line = self.getpos()[0]
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        href = a.get("href") or ""
        if href.startswith("#") and len(href) > 1:
            self.anchors.append((line, href[1:]))
        if tag in ("img", "source"):
            if a.get("src"):
                self.files.append((line, a["src"]))
            for part in (a.get("srcset") or "").split(","):
                part = part.strip()
                if part:
                    self.files.append((line, part.split()[0]))
        if tag == "img":
            alt = a.get("alt")
            if alt is None or not alt.strip():
                self.no_alt.append((line, a.get("src") or "(src 없음)"))


def main():
    try:
        payload = json.load(sys.stdin)
    except Exception:
        payload = {}
    root = os.environ.get("CLAUDE_PROJECT_DIR") or os.getcwd()
    page = os.path.join(root, "index.html")
    if len(sys.argv) > 1:  # 시험할 때 다른 파일을 넣어 볼 수 있게
        page = os.path.abspath(sys.argv[1])
    if not os.path.isfile(page):
        return
    base = os.path.dirname(page)

    c = Checker()
    with open(page, encoding="utf-8") as f:
        c.feed(f.read())

    problems = []
    for line, name in c.anchors:
        if name not in c.ids:
            problems.append(f"{line}번째 줄: 내부 링크 #{name} 가 가리키는 id=\"{name}\" 가 페이지에 없어요")
    seen = set()
    for line, path in c.files:
        if path.startswith(EXTERNAL) or (line, path) in seen:
            continue
        seen.add((line, path))
        clean = path.split("?")[0].split("#")[0]
        if not os.path.isfile(os.path.join(base, clean)):
            problems.append(f"{line}번째 줄: 사진 파일 {path} 이(가) 없어요")
    for line, src in c.no_alt:
        problems.append(f"{line}번째 줄: 사진 {src} 에 설명(alt)이 없거나 비어 있어요")

    if not problems:
        return

    listing = "\n".join("- " + p for p in problems)
    if payload.get("stop_hook_active"):
        # 이미 한 번 고치라고 했는데도 남아 있으면, 계속 붙잡지 않고 알리기만 합니다
        print(json.dumps({
            "systemMessage": "index.html 점검: 아직 남은 문제가 있어요\n" + listing
        }, ensure_ascii=False))
        return
    print(json.dumps({
        "decision": "block",
        "reason": (
            "index.html 자동 점검에서 문제를 찾았어요. 아래를 고친 뒤 마무리해 주세요. "
            "사진 파일이 정말 없다면 지어내지 말고, 사장님께 어떤 사진을 넣을지 물어봐 주세요. "
            "alt는 사진에 실제로 보이는 것을 한국어로 씁니다.\n" + listing
        ),
        "systemMessage": "index.html 점검에서 문제 " + str(len(problems)) + "개를 찾아 고치는 중이에요",
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
