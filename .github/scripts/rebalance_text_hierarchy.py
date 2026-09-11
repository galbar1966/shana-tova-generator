from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')

replacements = {
    ".fact-card{top:5.2vw;right:3.2vw;width:54%;max-height:none;border-radius:5.2vw;padding:3.8vw 3.5vw 4vw;background:linear-gradient(270deg,rgba(255,255,255,.50) 0%,rgba(255,255,255,.37) 70%,rgba(255,255,255,.22) 100%);overflow:visible}":
    ".fact-card{top:5vw;right:50%;transform:translateX(50%);width:66%;max-height:none;border-radius:5.2vw;padding:4.2vw 4.4vw 4.5vw;background:linear-gradient(270deg,rgba(255,255,255,.56) 0%,rgba(255,255,255,.43) 72%,rgba(255,255,255,.25) 100%);overflow:visible}",

    ".lead{font-size:clamp(21px,6vw,29px);margin-bottom:2.4vw;font-weight:700;line-height:1.05;gap:.32em}":
    ".lead{font-size:clamp(23px,6.6vw,31px);margin-bottom:2.8vw;font-weight:800;line-height:1.05;gap:.32em;justify-content:center}",

    ".fact{font-size:clamp(13.5px,3.75vw,18px);line-height:1.30;white-space:normal;overflow:visible;overflow-wrap:normal;word-break:normal}":
    ".fact{font-size:clamp(14.5px,4.05vw,19px);line-height:1.34;font-weight:600;white-space:normal;overflow:visible;overflow-wrap:normal;word-break:normal;text-align:center}",

    ".punch{position:relative;left:auto;right:auto;top:auto;height:auto;min-height:24vw;padding:4.4vw 4vw;font-size:clamp(15px,4.05vw,19.5px);line-height:1.36;border-radius:5vw;overflow:visible}":
    ".punch{position:relative;left:auto;right:auto;top:auto;height:auto;min-height:20vw;padding:3.8vw 4vw;font-size:clamp(14px,3.65vw,18px);line-height:1.34;font-weight:600;border-radius:5vw;overflow:visible}",

    ".fact-card{width:55%;right:2.2vw;padding-left:3vw;padding-right:3vw}":
    ".fact-card{width:68%;right:50%;transform:translateX(50%);padding-left:4vw;padding-right:4vw}",

    ".lead{font-size:5.8vw}":
    ".lead{font-size:6.4vw}",

    ".fact{font-size:3.65vw}":
    ".fact{font-size:3.9vw}",

    ".punch{font-size:3.9vw}":
    ".punch{font-size:3.55vw}"
}

changed = False
for old, new in replacements.items():
    if old in s:
        s = s.replace(old, new, 1)
        changed = True

if not changed:
    raise SystemExit('No hierarchy selectors matched current index.html')

p.write_text(s, encoding='utf-8')
