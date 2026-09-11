from pathlib import Path
import re

p = Path('index.html')
s = p.read_text(encoding='utf-8')

css = '''<style>
@import url('https://fonts.googleapis.com/css2?family=Rubik:wght@400;500;600;700;800;900&display=swap');
*{box-sizing:border-box}
html,body{margin:0;min-height:100%;font-family:'Rubik',Arial,sans-serif}
body{background:#efedf5;color:#202640;overflow-x:hidden}
.shell{width:min(100%,1024px);margin:0 auto;background:#fff;box-shadow:0 18px 60px rgba(28,24,70,.12)}
.card{position:relative;width:100%;aspect-ratio:2/3;background:#fff;overflow:hidden}
.hero{position:absolute;inset:0 auto auto 0;width:100%;height:58.6%;background:#e9e7ef;overflow:hidden}
.hero img{width:100%;height:100%;display:block;object-fit:cover;object-position:44% 48%}
.fact-card{position:absolute;z-index:6;top:6%;right:4.4%;width:43.5%;max-height:29%;background:rgba(255,255,255,.94);backdrop-filter:blur(3px);-webkit-backdrop-filter:blur(3px);border-radius:3%;padding:3.2% 3.1% 3.4%;box-shadow:0 14px 36px rgba(34,28,77,.14);overflow:hidden}
.lead{display:flex;direction:rtl;align-items:center;justify-content:flex-start;gap:2.2%;margin:0 0 6.3%;color:#6b27d8;font-family:'Rubik',Arial,sans-serif;font-size:min(4.9vw,50px);font-weight:800;line-height:1;text-align:right;white-space:nowrap;letter-spacing:0}
.bulb{font-size:1em;line-height:1;flex:none}
.fact{font-family:'Rubik',Arial,sans-serif;font-size:min(3.0vw,31px);line-height:1.42;font-weight:500;white-space:pre-line;color:#222943;text-align:right;overflow:hidden}
.lower{position:absolute;z-index:8;left:6.4%;top:50.1%;width:87.2%;height:31.8%;margin:0;background:#fff;border-radius:3.2% 3.2% 2.6% 2.6%;box-shadow:0 12px 38px rgba(31,28,75,.14);overflow:hidden}
.punch{position:absolute;left:1.7%;right:1.7%;top:2.2%;height:32.5%;display:flex;align-items:center;justify-content:center;padding:2.3% 4%;font-family:'Rubik',Arial,sans-serif;font-size:min(2.9vw,30px);line-height:1.35;font-weight:600;white-space:pre-line;text-align:center;color:#202640;background:linear-gradient(135deg,#faf7ff 0%,#efe6fb 100%);border-radius:2.7%;overflow:hidden}
.divider{position:absolute;left:9%;right:9%;top:39.8%;display:flex;align-items:center;gap:2%;margin:0;color:#9498ad}
.divider:before,.divider:after{content:"";height:1px;background:#d7d9e3;flex:1}
.divider span{font-size:min(3vw,30px);line-height:1;color:#9294a8}
.ending{position:absolute;left:7%;right:7%;top:47.3%;height:18%;display:flex;align-items:center;justify-content:center;text-align:center;color:#85899d;font-family:'Rubik',Arial,sans-serif;font-size:min(2.35vw,24px);line-height:1.45;font-weight:500;overflow:hidden}
.btn{position:absolute;left:50%;bottom:7.2%;transform:translateX(-50%);display:block;width:55.5%;height:19.6%;margin:0;border:0;border-radius:999px;padding:0 3%;background:linear-gradient(135deg,#8738ef 0%,#6522ce 100%);color:#fff;font:800 min(2.9vw,30px)/1.05 'Rubik',Arial,sans-serif;cursor:pointer;box-shadow:0 14px 30px rgba(98,32,202,.30)}
.ltr{direction:ltr;display:inline-block}
.brand{position:absolute;z-index:7;left:0;bottom:0;width:100%;height:16.8%;background:linear-gradient(145deg,#20204a 0%,#2b2d64 100%);color:#fff;text-align:center;padding-top:5%;border-radius:50% 50% 0 0 / 8% 8% 0 0;overflow:hidden}
.brand-name{direction:ltr;color:#9847ee;font-family:'Rubik',Arial,sans-serif;font-size:min(5.9vw,60px);font-weight:900;letter-spacing:-1px;line-height:1;margin-bottom:1.1%}
.brand-line{font-family:'Rubik',Arial,sans-serif;font-size:min(2.05vw,21px);line-height:1.4;font-weight:600;color:#f2eff8}
.brand-joke{font-family:'Rubik',Arial,sans-serif;font-size:min(1.6vw,16.5px);line-height:1.4;margin-top:.7%;color:#d8d4e3}
.brand-joke em{font-style:normal;font-weight:inherit;color:inherit}
.error{margin:24px;background:#fff;border-radius:24px;padding:30px 22px;text-align:center;font-size:18px;line-height:1.55}
@media(max-width:680px){
 body{background:#fff}.shell{width:100%;box-shadow:none}
 .lead{font-size:4.9vw}.fact{font-size:3vw}
 .punch{font-size:2.9vw}.ending{font-size:2.35vw}.btn{font-size:2.9vw}
 .brand-name{font-size:5.9vw}.brand-line{font-size:2.05vw}.brand-joke{font-size:1.6vw}
}
</style>'''

s = re.sub(r'<style>.*?</style>', css, s, count=1, flags=re.S)
s = re.sub(r'\s*<div class="dots">\.<br>\.<br>\.</div>', '', s, count=1)
s = s.replace('<div class="lead"><span>הידעת ש...</span><span class="bulb">💡</span></div>', '<div class="lead"><span class="bulb">💡</span><span>הידעת ש...</span></div>')

helper = '''\n function fitBox(el,maxPx,minPx){\n  if(!el)return;\n  let px=maxPx; el.style.fontSize=px+"px";\n  while((el.scrollHeight>el.clientHeight+1 || el.scrollWidth>el.clientWidth+1) && px>minPx){px-=0.5;el.style.fontSize=px+"px";}\n }\n function fitCurrent(){\n  const w=Math.min(document.querySelector('.shell')?.clientWidth || window.innerWidth || 1024,1024);\n  fitBox(fact,Math.min(31,w*0.030),10.5);\n  fitBox(punch,Math.min(30,w*0.029),9.5);\n }\n'''
if 'function fitBox(' in s:
    s = re.sub(r'\n function fitBox\(.*?\n function fitCurrent\(\)\{.*?\n \}\n', helper, s, count=1, flags=re.S)
else:
    s = s.replace(' function draw(){', helper + ' function draw(){', 1)

if 'requestAnimationFrame(fitCurrent)' not in s:
    s = re.sub(r'(punch\.textContent=.*?;)(animalImage\.alt=)', r'\1requestAnimationFrame(fitCurrent);\2', s, count=1)
if "window.addEventListener('resize'" not in s:
    s = s.replace("next.addEventListener('click',draw);draw();", "next.addEventListener('click',draw);window.addEventListener('resize',()=>requestAnimationFrame(fitCurrent));draw();", 1)

p.write_text(s, encoding='utf-8')
