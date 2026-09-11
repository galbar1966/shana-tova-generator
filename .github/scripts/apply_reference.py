from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = '''<style>
*{box-sizing:border-box}
html,body{margin:0;min-height:100%;font-family:Arial,sans-serif}
body{background:#f3f2f8;color:#202640;overflow-x:hidden}
.shell{width:min(100%,1024px);margin:0 auto;min-height:100vh;background:#fff;overflow:hidden;box-shadow:0 18px 60px rgba(28,24,70,.12)}
.card{position:relative;background:#fff;overflow:hidden}
.hero{position:relative;width:100%;aspect-ratio:2/3;background:#111218;overflow:hidden}
.hero img{width:100%;height:100%;display:block;object-fit:contain;object-position:center center;background:#111218}
.fact-card{position:absolute;z-index:5;top:4.6%;right:4%;width:40.5%;background:rgba(255,255,255,.80);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border:1px solid rgba(255,255,255,.68);border-radius:30px;padding:30px 28px 33px;box-shadow:0 14px 34px rgba(34,28,77,.13)}
.lead{display:flex;direction:rtl;flex-direction:row;align-items:center;justify-content:flex-start;gap:9px;color:#6727d4;font-family:Arial,sans-serif;font-size:clamp(36px,4.4vw,47px);font-weight:900;line-height:1.05;margin:0 0 24px;text-align:right;white-space:nowrap;letter-spacing:-.4px}
.bulb{font-size:.94em;line-height:1;flex:none}
.fact{font-family:Arial,sans-serif;font-size:clamp(23px,2.65vw,30px);line-height:1.42;font-weight:700;white-space:pre-line;color:#222943;text-align:right}
.lower{position:relative;z-index:8;width:87%;margin:-7.5% auto 28px;background:#fff;border-radius:34px;padding:18px 18px 24px;box-shadow:0 12px 38px rgba(31,28,75,.14)}
.punch{font-family:Arial,sans-serif;font-size:clamp(22px,2.65vw,30px);line-height:1.45;font-weight:700;white-space:pre-line;text-align:center;color:#202640;background:linear-gradient(135deg,#fbf8ff 0%,#f1e9fd 100%);border:0;border-radius:26px;padding:28px 34px;box-shadow:none}
.divider{display:flex;align-items:center;gap:18px;margin:27px 9% 18px;color:#9498ad}
.divider:before,.divider:after{content:"";height:1px;background:#d7d9e3;flex:1}
.divider span{font-size:30px;line-height:1;color:#9294a8}
.ending{text-align:center;color:#85899d;font-family:Arial,sans-serif;font-size:clamp(19px,2.2vw,25px);line-height:1.48;font-weight:700;padding:0 20px 4px}
.btn{display:block;width:58%;min-width:0;margin:25px auto 5px;border:0;border-radius:28px;padding:18px 24px;background:linear-gradient(135deg,#8738ef 0%,#6522ce 100%);color:#fff;font:900 clamp(24px,2.7vw,31px)/1.08 Arial,sans-serif;cursor:pointer;box-shadow:0 14px 30px rgba(98,32,202,.30)}
.ltr{direction:ltr;display:inline-block}
.brand{position:relative;background:linear-gradient(145deg,#20204a 0%,#2b2d64 100%);color:#fff;text-align:center;padding:54px 18px 60px;border-radius:50% 50% 0 0 / 6.5% 6.5% 0 0}
.brand-name{direction:ltr;color:#9747ec;font-family:Arial,sans-serif;font-size:clamp(52px,5.8vw,66px);font-weight:900;letter-spacing:-1.5px;line-height:1;margin-bottom:12px}
.brand-line{font-family:Arial,sans-serif;font-size:clamp(18px,1.9vw,23px);line-height:1.45;font-weight:700;color:#f1eff8}
.brand-joke{font-family:Arial,sans-serif;font-size:clamp(14px,1.55vw,18px);line-height:1.45;margin-top:7px;color:#d4d1df}
.brand-joke em{font-style:italic;font-weight:900;color:#fff}
.error{margin:24px;background:#fff;border-radius:24px;padding:30px 22px;text-align:center;font-size:18px;line-height:1.55}
@media(max-width:680px){
 body{background:#fff}.shell{width:100%;box-shadow:none}
 .hero{aspect-ratio:2/3}
 .fact-card{top:3.7%;right:3.7%;width:42.5%;padding:17px 14px 19px;border-radius:21px;background:rgba(255,255,255,.78)}
 .lead{font-size:clamp(24px,5.9vw,31px);margin-bottom:14px;gap:5px;letter-spacing:-.2px}
 .fact{font-size:clamp(15px,3.75vw,18.5px);line-height:1.4}
 .lower{width:88%;margin-top:-6.5%;margin-bottom:20px;padding:14px 12px 18px;border-radius:28px}
 .punch{font-size:clamp(16px,4vw,20px);line-height:1.46;padding:20px 17px;border-radius:20px}
 .divider{margin:20px 8% 14px}.divider span{font-size:23px}
 .ending{font-size:clamp(14px,3.7vw,17px);padding:0 8px}
 .btn{width:70%;font-size:clamp(19px,4.8vw,23px);padding:15px 18px;border-radius:23px;margin-top:18px}
 .brand{padding:36px 14px calc(42px + env(safe-area-inset-bottom));border-radius:50% 50% 0 0 / 5% 5% 0 0}
 .brand-name{font-size:40px}.brand-line{font-size:14px}.brand-joke{font-size:11.5px}
}
</style>'''

s = re.sub(r'<style>.*?</style>', css, s, count=1, flags=re.S)
s = re.sub(r'\s*<div class="dots">\.<br>\.<br>\.</div>', '', s, count=1)
s = s.replace('<div class="lead"><span>הידעת ש...</span><span class="bulb">💡</span></div>', '<div class="lead"><span class="bulb">💡</span><span>הידעת ש...</span></div>')
p.write_text(s, encoding='utf-8')
