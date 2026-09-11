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
.hero{position:relative;width:100%;aspect-ratio:2/3;background:#eceaf2;overflow:hidden}
.hero img{width:100%;height:100%;display:block;object-fit:contain;object-position:center top;background:#eceaf2}
.fact-card{position:absolute;z-index:6;top:6%;right:4.4%;width:43.4%;height:auto;max-height:46%;background:rgba(255,255,255,.96);border-radius:min(3vw,30px);padding:min(2.4vw,25px) min(2.7vw,28px) min(2.6vw,27px);box-shadow:0 14px 36px rgba(34,28,77,.13);overflow:hidden}
.lead{display:flex;direction:rtl;flex-direction:row;align-items:center;justify-content:flex-start;gap:min(1vw,10px);color:#6727d4;font-family:Arial,sans-serif;font-size:clamp(26px,4.7vw,48px);font-weight:700;line-height:1;margin:0 0 min(1.8vw,18px);text-align:right;white-space:nowrap;letter-spacing:0}
.bulb{font-size:.95em;line-height:1;flex:none}
.fact{font-family:Arial,sans-serif;font-size:clamp(15px,2.8vw,29px);line-height:1.34;font-weight:700;white-space:pre-line;color:#222943;text-align:right;overflow:hidden}
.lower{position:relative;z-index:8;width:87%;height:min(47.5vw,486px);margin:-75% auto min(2.5vw,26px);background:#fff;border-radius:min(3.4vw,35px);padding:min(1vw,10px) min(1.5vw,15px);box-shadow:0 12px 38px rgba(31,28,75,.14)}
.punch{position:absolute;top:min(.9vw,9px);left:min(1.5vw,15px);right:min(1.5vw,15px);height:min(16.2vw,166px);font-family:Arial,sans-serif;font-size:clamp(14px,2.7vw,28px);line-height:1.28;font-weight:700;white-space:pre-line;text-align:center;color:#202640;background:linear-gradient(135deg,#faf7ff 0%,#f0e7fb 100%);border:0;border-radius:min(2.5vw,26px);padding:min(2vw,20px) min(2.5vw,26px);overflow:hidden;display:flex;align-items:center;justify-content:center}
.divider{position:absolute;top:min(19.1vw,196px);left:9%;right:9%;display:flex;align-items:center;gap:min(1.8vw,18px);margin:0;color:#9498ad}
.divider:before,.divider:after{content:"";height:1px;background:#d7d9e3;flex:1}
.divider span{font-size:clamp(18px,2.8vw,29px);line-height:1;color:#9294a8}
.ending{position:absolute;top:min(23.1vw,237px);left:6%;right:6%;height:min(8vw,82px);display:flex;align-items:center;justify-content:center;text-align:center;color:#85899d;font-family:Arial,sans-serif;font-size:clamp(13px,2.15vw,22px);line-height:1.34;font-weight:700;padding:0 min(2vw,20px);overflow:hidden}
.btn{position:absolute;left:50%;bottom:min(3.7vw,38px);transform:translateX(-50%);display:block;width:55%;height:min(9.2vw,94px);min-width:0;margin:0;border:0;border-radius:min(3vw,30px);padding:0 min(2vw,20px);background:linear-gradient(135deg,#8536ec 0%,#6826d2 100%);color:#fff;font:900 clamp(18px,2.8vw,29px)/1.02 Arial,sans-serif;cursor:pointer;box-shadow:0 14px 30px rgba(98,32,202,.28)}
.ltr{direction:ltr;display:inline-block}
.brand{position:relative;background:linear-gradient(145deg,#20204a 0%,#2b2d64 100%);color:#fff;text-align:center;padding:min(5.2vw,53px) 18px min(5.8vw,59px);border-radius:50% 50% 0 0 / 6.5% 6.5% 0 0}
.brand-name{direction:ltr;color:#9747ec;font-family:Arial,sans-serif;font-size:clamp(40px,5.8vw,60px);font-weight:900;letter-spacing:-1.5px;line-height:1;margin-bottom:min(1.1vw,11px)}
.brand-line{font-family:Arial,sans-serif;font-size:clamp(14px,1.9vw,20px);line-height:1.4;font-weight:700;color:#f1eff8}
.brand-joke{font-family:Arial,sans-serif;font-size:clamp(11px,1.55vw,16px);line-height:1.4;margin-top:min(.7vw,7px);color:#d4d1df}
.brand-joke em{font-style:normal;font-weight:inherit;color:inherit}
.error{margin:24px;background:#fff;border-radius:24px;padding:30px 22px;text-align:center;font-size:18px;line-height:1.55}
@media(max-width:680px){
 body{background:#fff}.shell{width:100%;box-shadow:none}
 .fact-card{top:6%;right:4.4%;width:43.4%;height:auto;max-height:46%;padding:2.4vw 2.7vw 2.6vw;border-radius:3vw}
 .lead{font-size:4.7vw;margin-bottom:1.8vw;gap:1vw;letter-spacing:0}
 .fact{font-size:2.8vw;line-height:1.34}
 .lower{width:87%;height:47.5vw;margin-top:-75%;margin-bottom:2.5vw;border-radius:3.4vw}
 .punch{font-size:2.7vw;line-height:1.28}
 .ending{font-size:2.15vw;line-height:1.34}
 .btn{font-size:2.8vw}
 .brand-name{font-size:5.8vw}.brand-line{font-size:1.9vw}.brand-joke{font-size:1.55vw}
}
</style>'''

s = re.sub(r'<style>.*?</style>', css, s, count=1, flags=re.S)
s = re.sub(r'\s*<div class="dots">\.<br>\.<br>\.</div>', '', s, count=1)
s = s.replace('<div class="lead"><span>הידעת ש...</span><span class="bulb">💡</span></div>', '<div class="lead"><span class="bulb">💡</span><span>הידעת ש...</span></div>')

helper = '''\n function fitBox(el,maxPx,minPx){\n  if(!el)return;\n  let px=maxPx; el.style.fontSize=px+"px";\n  while((el.scrollHeight>el.clientHeight+1 || el.scrollWidth>el.clientWidth+1) && px>minPx){px-=0.5;el.style.fontSize=px+"px";}\n }\n function fitCurrent(){\n  const w=Math.min(window.innerWidth||1024,1024);\n  fitBox(fact,Math.min(29,w*0.028),10);\n  fitBox(punch,Math.min(28,w*0.027),9);\n }\n'''
if 'function fitBox(' not in s:
    s = s.replace(' function draw(){', helper + ' function draw(){', 1)

if 'requestAnimationFrame(fitCurrent)' not in s:
    s = re.sub(r'(punch\.textContent=.*?;)(animalImage\.alt=)', r'\1requestAnimationFrame(fitCurrent);\2', s, count=1)
    s = s.replace("next.addEventListener('click',draw);draw();", "next.addEventListener('click',draw);window.addEventListener('resize',()=>requestAnimationFrame(fitCurrent));draw();", 1)

p.write_text(s, encoding='utf-8')
