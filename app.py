import base64

import streamlit as st

st.set_page_config(
    page_title="Aemchira | ผลงานวิชาระบบฐานข้อมูลขั้นสูง",
    page_icon="🕸️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

COLAB_1 = "https://colab.research.google.com/drive/140LavhaXaDszvLG9X9HfgHlC3yCC0OQh?usp=sharing"
COLAB_3 = "https://colab.research.google.com/drive/1rXVBCoQ5nrMVGQkQJlZKUBXpd7gw9Fan?usp=sharing"
COLAB_4 = "https://colab.research.google.com/drive/1zk9jCTZgKqJCYWHcH8JM6PlcFc9Q1ST6?usp=sharing"
APP_URL = "https://grapdb051-gqou54ls42fpzbjkht67c4.streamlit.app/"
REPO_URL = "https://github.com/aemchira2548/grapDB051"

# Files in ./static are served at <app url>/app/static/<file> (enableStaticServing).
PDF_HW2 = "app/static/051-aemchira.pdf"
PDF_DG = "app/static/DrinkGraph.pdf"
PPTX_DG = "app/static/DrinkGraph.pptx"
PHOTO = "app/static/profile.jpg"

# Connector lines for the hero graph (kept in a data URI so the CSS has no raw "<").
_LINES = (
    "<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 560 440'>"
    "<defs><linearGradient id='g' x1='0' y1='0' x2='1' y2='1'>"
    "<stop offset='0' stop-color='#7C5CFF'/><stop offset='1' stop-color='#22D3EE'/></linearGradient></defs>"
    "<g stroke='url(#g)' stroke-width='2.5' stroke-linecap='round' opacity='.75'>"
    "<line x1='280' y1='220' x2='110' y2='90'/><line x1='280' y1='220' x2='95' y2='330'/>"
    "<line x1='280' y1='220' x2='300' y2='400'/><line x1='280' y1='220' x2='470' y2='340'/>"
    "<line x1='280' y1='220' x2='450' y2='80'/></g></svg>"
)
LINES_URI = "data:image/svg+xml;base64," + base64.b64encode(_LINES.encode()).decode()

CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Prompt:wght@600;700;800&family=IBM+Plex+Sans+Thai:wght@400;500;600&display=swap');

:root {
  --bg: #090A1E;
  --txt: #EEF0FF;
  --mut: #A9ADD3;
  --violet: #7C5CFF;
  --cyan: #22D3EE;
  --pink: #FF5CA8;
  --gold: #FFC24B;
  --glass: rgba(255,255,255,.055);
  --rim: rgba(255,255,255,.13);
}

[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stDecoration"], footer, #MainMenu { display: none !important; }
.stApp {
  background:
    radial-gradient(900px 520px at 85% -5%, rgba(124,92,255,.40), transparent 60%),
    radial-gradient(700px 480px at -5% 30%, rgba(34,211,238,.20), transparent 60%),
    radial-gradient(800px 500px at 60% 105%, rgba(255,92,168,.20), transparent 60%),
    radial-gradient(rgba(255,255,255,.07) 1px, transparent 1.4px) 0 0 / 28px 28px,
    var(--bg);
  color: var(--txt);
}
.block-container { max-width: 1120px !important; padding: 3.2rem 1.5rem 4rem !important; }
[data-testid="stHtml"] { width: 100%; }

.pf { font-family: 'IBM Plex Sans Thai', system-ui, sans-serif; color: var(--txt); line-height: 1.7; }
.pf * { box-sizing: border-box; }
.pf h1, .pf h2, .pf h3, .big, .nd { font-family: 'Prompt', 'IBM Plex Sans Thai', sans-serif; }

/* ---------- hero ---------- */
.hero { display: grid; grid-template-columns: 1.1fr 1fr; gap: 2rem; align-items: center; padding-bottom: 4.5rem; }
.pill {
  display: inline-block; padding: .3rem 1rem; border-radius: 999px; font-size: .9rem; font-weight: 500;
  background: var(--glass); border: 1px solid var(--rim); color: var(--cyan); margin-bottom: 1.2rem;
}
.hero h1 { font-weight: 800; font-size: clamp(2.6rem, 6.4vw, 4.9rem); line-height: 1.12; margin: 0 0 1.3rem; letter-spacing: -.02em; }
.hero h1 span {
  background: linear-gradient(100deg, var(--violet) 0%, var(--cyan) 55%, var(--pink) 100%);
  -webkit-background-clip: text; background-clip: text; color: transparent;
}
.hero p.lead { font-size: 1.12rem; color: var(--mut); max-width: 33rem; margin: 0 0 1.6rem; }
.pf ul.who, .pf ul.tags { padding-left: 0 !important; margin-left: 0 !important; }
.who { display: flex; flex-wrap: wrap; gap: .6rem; margin: 0 0 1.8rem; padding: 0; }
.who li { list-style: none; padding: .45rem 1rem; border-radius: 12px; background: var(--glass); border: 1px solid var(--rim); font-size: .93rem; }
.cta { display: flex; flex-wrap: wrap; gap: .8rem; }

/* ---------- hero graph ---------- */
.net { position: relative; width: 100%; aspect-ratio: 560 / 440; background: url("__LINES__") center / 100% 100% no-repeat; }
.net .nd {
  position: absolute; transform: translate(-50%, -50%); border-radius: 50%;
  display: flex; align-items: center; justify-content: center; text-decoration: none !important;
  font-weight: 800; color: #fff !important; width: 11%; aspect-ratio: 1;
  font-size: clamp(1.1rem, 2.8vw, 1.7rem);
  background: linear-gradient(135deg, var(--violet), var(--cyan));
  box-shadow: 0 0 0 5px rgba(9,10,30,.9), 0 0 34px rgba(124,92,255,.75);
  opacity: 0; animation: pop .5s ease-out forwards;
  transition: filter .2s;
}
.net a.nd:hover { filter: brightness(1.25) saturate(1.2); }
.net a.nd:focus-visible { outline: 3px solid var(--gold); outline-offset: 4px; }
.net .me {
  width: 40%; padding: 6px; background: conic-gradient(from 200deg, var(--violet), var(--cyan), var(--pink), var(--violet));
  box-shadow: 0 0 0 6px rgba(9,10,30,.9), 0 0 70px rgba(124,92,255,.7);
  animation: pop .5s ease-out .05s forwards, glow 3.5s ease-in-out 1s infinite;
}
.net .me img { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; display: block; }
.net .gold { width: 15%; background: linear-gradient(135deg, var(--gold), var(--pink)); color: #1b1030 !important;
  box-shadow: 0 0 0 5px rgba(9,10,30,.9), 0 0 40px rgba(255,194,75,.7); font-size: clamp(1.3rem, 3.4vw, 2.1rem); }
.net .cap { position: absolute; transform: translateX(-50%); font-size: .85rem; font-weight: 500; color: var(--gold); opacity: 0; animation: pop .5s ease-out 1.5s forwards; }
.me { left: 50%; top: 50%; }
.n1 { left: 19.6%; top: 20.5%; animation-delay: .5s !important; }
.n2 { left: 17%; top: 75%; animation-delay: .65s !important; }
.n3 { left: 53.6%; top: 90.9%; animation-delay: .8s !important; }
.n4 { left: 84%; top: 77.3%; animation-delay: .95s !important; }
.n5 { left: 80.4%; top: 18.2%; animation-delay: 1.1s !important; }
@keyframes pop { from { opacity: 0; } to { opacity: 1; } }
@keyframes glow { 0%, 100% { box-shadow: 0 0 0 6px rgba(9,10,30,.9), 0 0 50px rgba(124,92,255,.55); }
                  50% { box-shadow: 0 0 0 6px rgba(9,10,30,.9), 0 0 95px rgba(34,211,238,.65); } }
@media (prefers-reduced-motion: reduce) { .net .nd, .net .cap { animation: none !important; opacity: 1; } }

/* ---------- buttons ---------- */
.btn {
  display: inline-block; text-decoration: none !important; font-weight: 600; font-size: .96rem;
  padding: .62rem 1.35rem; border-radius: 999px; color: var(--txt) !important;
  border: 1.5px solid var(--rim); background: var(--glass); transition: transform .15s, border-color .15s, filter .15s;
}
.btn:hover { border-color: var(--cyan); transform: translateY(-2px); }
.btn.main { border: none; color: #fff !important; background: linear-gradient(100deg, var(--violet), #4F7BFF 60%, var(--cyan)); box-shadow: 0 10px 30px -10px rgba(124,92,255,.9); }
.btn.main:hover { filter: brightness(1.15); }
.btn.gold { border: none; color: #1b1030 !important; background: linear-gradient(100deg, var(--gold), var(--pink)); box-shadow: 0 10px 30px -10px rgba(255,92,168,.8); }
.btn:focus-visible { outline: 3px solid var(--gold); outline-offset: 3px; }

/* ---------- works ---------- */
.works h2 { font-weight: 800; font-size: clamp(1.8rem, 4vw, 2.5rem); margin: 0 0 1.6rem; letter-spacing: -.01em; scroll-margin-top: 1.5rem; }
.grid { display: grid; grid-template-columns: 1fr 1fr; gap: 1.2rem; }
.card {
  position: relative; border-radius: 24px; padding: 1.7rem 1.7rem 1.8rem; overflow: hidden;
  background: var(--glass); border: 1px solid var(--rim); backdrop-filter: blur(10px);
  transition: transform .2s, border-color .2s, box-shadow .2s; scroll-margin-top: 1.5rem;
}
.card:hover { transform: translateY(-5px); border-color: rgba(124,92,255,.8); box-shadow: 0 24px 60px -24px rgba(124,92,255,.75); }
.big {
  font-weight: 800; font-size: 5.2rem; line-height: .95; margin-bottom: .6rem; letter-spacing: -.04em;
  background: linear-gradient(135deg, var(--violet), var(--cyan)); -webkit-background-clip: text; background-clip: text; color: transparent;
}
.card h3 { font-weight: 700; font-size: 1.3rem; line-height: 1.4; margin: 0 0 .4rem; }
.card .sub { color: var(--mut); margin: 0 0 1.2rem; font-size: .98rem; }
.acts { display: flex; flex-wrap: wrap; gap: .6rem; }
.card.proj {
  grid-column: 1 / -1; display: grid; grid-template-columns: auto 1fr; column-gap: 2.2rem; padding: 2.2rem 2.2rem 2.3rem;
  border: 1.5px solid transparent;
  background: linear-gradient(#10112b, #10112b) padding-box, linear-gradient(135deg, var(--gold), var(--pink), var(--violet)) border-box;
  box-shadow: 0 30px 80px -40px rgba(255,92,168,.7);
}
.card.proj:hover { border-color: transparent; box-shadow: 0 30px 90px -30px rgba(255,92,168,.9); }
.card.proj .big { font-size: 8rem; margin: 0; background: linear-gradient(135deg, var(--gold), var(--pink)); -webkit-background-clip: text; background-clip: text; color: transparent; }
.card.proj h3 { font-size: 1.7rem; }
.card.proj .tags { display: flex; flex-wrap: wrap; gap: .5rem; margin: 0 0 1rem; padding: 0; }
.card.proj .tags li { list-style: none; font-size: .82rem; padding: .15rem .75rem; border-radius: 999px; border: 1px solid rgba(255,194,75,.5); color: var(--gold); }

.foot { margin-top: 3rem; padding-top: 1.6rem; border-top: 1px solid var(--rim); color: var(--mut); font-size: .92rem; }

@media (max-width: 820px) {
  .hero { grid-template-columns: 1fr; padding-bottom: 2.5rem; }
  .net { max-width: 460px; margin: 0 auto; }
  .grid { grid-template-columns: 1fr; }
  .card.proj { grid-template-columns: 1fr; padding: 1.6rem; }
  .card.proj .big { font-size: 5.5rem; margin-bottom: .5rem; }
  .big { font-size: 4rem; }
}
</style>
"""


def btn(label, href, kind="", download=False, view=False):
    if view:
        # local PDF: open it in a new tab instead of downloading
        extra = ' target="_blank" rel="noopener noreferrer"'
    elif download:
        extra = " download"
    elif href.startswith("http"):
        # Streamlit Cloud serves apps inside an iframe; external sites (Colab, GitHub) refuse
        # to load there, so they must open in a new tab.
        extra = ' target="_blank" rel="noopener noreferrer"'
    else:
        extra = ""
    return f'<a class="btn {kind}" href="{href}"{extra}>{label}</a>'


def card(n, title, sub, acts):
    return (
        f'<article class="card" id="hw{n}"><div class="big">{n}</div>'
        f"<h3>{title}</h3><p class='sub'>{sub}</p><div class='acts'>{acts}</div></article>"
    )


CARDS = "".join(
    [
        card(1, "การบ้านชิ้นที่ 1", "สมุดงานบน Google Colab", btn("เปิดใน Colab", COLAB_1, "main")),
        card(
            2,
            "ออกแบบกราฟระบบแนะนำชมรม",
            "กำหนด Node (Student, Club, Interest) และ Relationship "
            "(FRIEND_OF, MEMBER_OF, INTERESTED_IN, FOCUSES_ON) พร้อมข้อมูลตัวอย่างและคำสั่ง Cypher",
            btn("เปิดดู PDF", PDF_HW2, "main", view=True),
        ),
        card(3, "การบ้านชิ้นที่ 3", "สมุดงานบน Google Colab", btn("เปิดใน Colab", COLAB_3, "main")),
        card(4, "การบ้านชิ้นที่ 4", "สมุดงานบน Google Colab", btn("เปิดใน Colab", COLAB_4, "main")),
    ]
)

PROJECT = (
    '<article class="card proj" id="hw5"><div class="big">5</div><div>'
    "<ul class='tags'><li>Neo4j Aura</li><li>Cypher</li><li>Streamlit</li></ul>"
    "<h3>DrinkGraph ระบบแนะนำเครื่องดื่มจากกราฟความชอบ</h3>"
    "<p class='sub'>ดูว่าคนที่ชอบเหมือนคุณดื่มอะไร แล้วเลือกแก้วถัดไปอย่างมีเหตุผล</p>"
    f"<div class='acts'>{btn('ลองใช้งานเว็บแอป', APP_URL, 'gold')}"
    f"{btn('ดูโค้ดบน GitHub', REPO_URL)}"
    f"{btn('สไลด์ PDF', PDF_DG, view=True)}"
    f"{btn('สไลด์ PowerPoint', PPTX_DG, download=True)}</div></div></article>"
)

HERO_GRAPH = f"""
<div class="net" role="group" aria-label="เอมจิรากับผลงาน 5 ชิ้น">
  <div class="nd me"><img src="{PHOTO}" alt="เอมจิรา"></div>
  <a class="nd n1" href="#hw1" aria-label="การบ้านชิ้นที่ 1">1</a>
  <a class="nd n2" href="#hw2" aria-label="การบ้านชิ้นที่ 2">2</a>
  <a class="nd n3" href="#hw3" aria-label="การบ้านชิ้นที่ 3">3</a>
  <a class="nd n4" href="#hw4" aria-label="การบ้านชิ้นที่ 4">4</a>
  <a class="nd n5 gold" href="#hw5" aria-label="โปรเจกต์ DrinkGraph">5</a>
  <span class="cap" style="left:80.4%;top:30%">DrinkGraph</span>
</div>
"""

PAGE = f"""
{CSS.replace("__LINES__", LINES_URI)}
<div class="pf">
  <section class="hero">
    <div>
      <span class="pill">วิชา ระบบฐานข้อมูลขั้นสูง (7142202)</span>
      <h1>ผลงานของ<br><span>เอมจิรา</span></h1>
      <p class="lead">การบ้าน 4 ชิ้นและโปรเจกต์ DrinkGraph ที่ทำตลอดวิชา รวมไว้ที่เดียว กดตัวเลขในกราฟเพื่อข้ามไปดูแต่ละชิ้นได้</p>
      <ul class="who">
        <li>Aemchira Ouamcharoen รหัส 664245051</li>
        <li>วิทยาการคอมพิวเตอร์ ปี 4 ม.ราชภัฏนครปฐม</li>
      </ul>
      <div class="cta">{btn('ดูผลงานทั้งหมด', '#works', 'main')}{btn('ลองใช้ DrinkGraph', APP_URL)}</div>
    </div>
    {HERO_GRAPH}
  </section>

  <section class="works" id="works">
    <h2>ผลงานทั้งหมด</h2>
    <div class="grid">{CARDS}{PROJECT}</div>
  </section>

  <p class="foot">ทำด้วย Neo4j, Cypher, Streamlit และ Google Colab</p>
</div>
"""

st.html(PAGE)
