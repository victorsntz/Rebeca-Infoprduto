import math, random, sys
S=sys.argv[1]
BODY=('M540,712 C520,710 506,708 494,700 C486,690 474,690 470,702 C467,714 468,726 472,736 '
      'C462,754 460,778 470,798 C478,816 470,840 452,862 C430,890 420,930 424,980 '
      'C428,1040 410,1100 392,1160 C370,1220 360,1290 372,1350 L708,1350 '
      'C720,1290 710,1220 688,1160 C670,1100 652,1040 656,980 C660,930 650,890 628,862 '
      'C610,840 602,816 610,798 C620,778 618,754 608,736 C612,726 613,714 610,702 '
      'C606,690 594,690 586,700 C574,708 560,710 540,712 Z')
TAIL='M680,1338 C760,1352 840,1342 884,1310 C910,1290 906,1260 884,1256'

def rosettes(seed):
    random.seed(seed); out=[]
    for _ in range(40):
        x=random.uniform(474,606); y=random.uniform(718,830); r=random.uniform(2.5,5.5)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{r:.1f}" ry="{r*0.8:.1f}" fill="#2A1A10" opacity=".85"/>')
    for i in range(22):
        y=830+i*24; x=540+random.uniform(-6,6)
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{random.uniform(4,7):.1f}" ry="{random.uniform(8,12):.1f}" fill="#2A1A10" opacity=".8"/>')
    placed=[]
    for _ in range(2500):
        x=random.uniform(360,720); y=random.uniform(830,1350)
        if abs(x-540)<14: continue
        t=(y-830)/520; R=9+t*14+random.uniform(-2,3)
        if any((x-a)**2+(y-b)**2 < (R+c+6)**2 for a,b,c in placed): continue
        placed.append((x,y,R))
        rot=random.uniform(0,360); k=random.choice([3,4,4,5]); segs=[]
        for j in range(k):
            a0=rot+j*360/k+random.uniform(-10,10); a1=a0+360/k*random.uniform(.45,.7)
            x0=x+R*math.cos(math.radians(a0)); y0=y+R*0.85*math.sin(math.radians(a0))
            x1=x+R*math.cos(math.radians(a1)); y1=y+R*0.85*math.sin(math.radians(a1))
            segs.append(f'<path d="M{x0:.1f},{y0:.1f} A{R:.1f},{R*0.85:.1f} 0 0 1 {x1:.1f},{y1:.1f}" stroke="#2A1A10" stroke-width="{R*0.42:.1f}" fill="none" stroke-linecap="round" opacity=".88"/>')
        out.append(f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{R*0.6:.1f}" ry="{R*0.5:.1f}" fill="#A8743E" opacity=".55"/>'+''.join(segs))
        if len(placed)>190: break
    return ''.join(out)

def onca(uid):
    petals=''.join(f'<path transform="rotate({a})" d="M0,0 C-14,-10 -18,-34 -6,-46 C2,-52 12,-50 16,-40 C22,-26 14,-8 0,0Z" fill="url(#pet{uid})" stroke="#5A0812" stroke-width="1" opacity=".97"/>' for a in range(0,360,72))
    veins=''.join(f'<path transform="rotate({a})" d="M0,-6 C-2,-18 -1,-30 2,-38" stroke="#5A0812" stroke-width="1.2" fill="none" opacity=".6"/>' for a in range(0,360,72))
    return f'''<svg viewBox="0 0 1080 1350" width="1080" height="1350" style="position:absolute;inset:0">
<defs>
  <linearGradient id="fur{uid}" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#B8915E"/><stop offset=".5" stop-color="#E2C493"/><stop offset="1" stop-color="#B08856"/></linearGradient>
  <radialGradient id="shade{uid}" cx=".5" cy=".35" r=".75"><stop offset=".55" stop-color="#000" stop-opacity="0"/><stop offset="1" stop-color="#3A1A0C" stop-opacity=".45"/></radialGradient>
  <clipPath id="clip{uid}"><path d="{BODY}"/></clipPath>
  <filter id="org{uid}"><feTurbulence type="fractalNoise" baseFrequency=".08" numOctaves="2" seed="{uid}" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="5"/></filter>
  <filter id="hair{uid}" x="-5%" y="-5%" width="110%" height="110%"><feTurbulence type="fractalNoise" baseFrequency=".9 .05" numOctaves="2" seed="{uid+4}" result="n"/><feDisplacementMap in="SourceGraphic" in2="n" scale="3"/></filter>
  <radialGradient id="pet{uid}" cx=".2" cy=".5" r=".9"><stop offset="0" stop-color="#4A0610"/><stop offset=".5" stop-color="#8E1220"/><stop offset="1" stop-color="#B21E2C"/></radialGradient>
</defs>
<g filter="url(#hair{uid})">
  <path d="{TAIL}" stroke="url(#fur{uid})" stroke-width="34" fill="none" stroke-linecap="round"/>
  <path d="{TAIL}" stroke="#2A1A10" stroke-width="30" fill="none" stroke-dasharray="12 26" opacity=".8"/>
  <path d="{BODY}" fill="url(#fur{uid})"/>
  <g clip-path="url(#clip{uid})">
    <path d="M540,716 C548,860 552,1100 546,1350" stroke="#F3DDB0" stroke-width="64" opacity=".22" fill="none"/>
    <g filter="url(#org{uid})">{rosettes(uid)}</g>
    <path d="M470,880 C500,900 520,930 528,970 M610,880 C580,900 560,930 552,970" stroke="#7A5530" stroke-width="3" fill="none" opacity=".35"/>
    <rect x="350" y="680" width="380" height="680" fill="url(#shade{uid})"/>
  </g>
  <path d="M474,704 C474,714 476,724 480,732 C488,724 490,712 486,702 Z" fill="#2A1A10" opacity=".9"/>
  <path d="M606,704 C606,714 604,724 600,732 C592,724 590,712 594,702 Z" fill="#2A1A10" opacity=".9"/>
  <path d="M471,708 C473,698 479,694 484,698" stroke="#F3E2C0" stroke-width="2" fill="none" opacity=".8"/>
  <path d="M609,708 C607,698 601,694 596,698" stroke="#F3E2C0" stroke-width="2" fill="none" opacity=".8"/>
</g>
<g transform="translate(604 724) rotate(-18) scale(1.1)">{petals}{veins}<circle r="7" fill="#5A0812"/>
  <path d="M0,0 C6,-14 10,-24 18,-30" stroke="#E9B44A" stroke-width="2.2" fill="none"/>
  <circle cx="18" cy="-30" r="3" fill="#F2C75C"/><circle cx="14" cy="-34" r="2" fill="#F2C75C"/><circle cx="21" cy="-35" r="2" fill="#F2C75C"/></g>
</svg>'''

def post(pid, bg):
    return f'''<div class="post" id="{pid}" style="background:{bg}">{onca(int(pid[1:]))}<div class="grain"></div>
  <div class="at">@rebecafortunato__</div>
  <div class="t">seja forte<br>e corajosa.<small>Josué 1:9</small></div></div>'''

page=f'''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file:///home/user/Rebeca-Infoprduto/site/assets/brand.css">
<style>
body{{margin:0;background:#333}}
.post{{width:1080px;height:1350px;position:relative;overflow:hidden;margin:0 0 20px;font-family:var(--serif)}}
.grain{{position:absolute;inset:0;opacity:.13;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}}
.at{{position:absolute;left:0;right:0;top:110px;text-align:center;font-family:var(--sans);font-size:22px;letter-spacing:.26em;text-transform:uppercase;color:#F3E2CF;opacity:.8}}
.t{{position:absolute;left:0;right:0;top:440px;text-align:center;color:#F6EADB;font-family:var(--serif);font-size:54px;line-height:1.18}}
.t small{{display:block;margin-top:22px;font-family:var(--sans);font-size:20px;letter-spacing:.28em;text-transform:uppercase;color:#E8C27A;opacity:.9}}
</style></head><body>
{post('p1','radial-gradient(120% 90% at 50% 40%,#650A12 0%,#56060D 60%,#45040A 100%)')}
{post('p2','radial-gradient(120% 90% at 50% 40%,#4E1621 0%,#3F1019 60%,#300B12 100%)')}
</body></html>'''
open(S+'/onca.html','w',encoding='utf-8').write(page); print('ok')
