from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="Aemchira | Graph Database Portfolio",
    page_icon="🕸️",
    layout="centered",
)

ASSETS = Path(__file__).parent / "assets"

PROFILE = {
    "name": "เอมจิรา",
    "name_en": "Aemchira Ouamcharoen",
    "student_id": "051",
    "role": "นักศึกษาคณะวิทยาการคอมพิวเตอร์ ชั้นปีที่ 4",
    "university": "มหาวิทยาลัยราชภัฏนครปฐม",
    "location": "นครปฐม, ประเทศไทย",
    "graduation": "2027",
    "skills": [
        "Business Intelligence",
        "Data Warehousing",
        "Machine Learning",
        "IoT",
        "Graph Database (Neo4j / Cypher)",
        "PDPA",
    ],
}

COLAB_1 = "https://colab.research.google.com/drive/140LavhaXaDszvLG9X9HfgHlC3yCC0OQh?usp=sharing"
COLAB_3 = "https://colab.research.google.com/drive/1rXVBCoQ5nrMVGQkQJlZKUBXpd7gw9Fan?usp=sharing"
COLAB_4 = "https://colab.research.google.com/drive/1zk9jCTZgKqJCYWHcH8JM6PlcFc9Q1ST6?usp=sharing"
DRINKGRAPH_APP = "https://grapdb051-gqou54ls42fpzbjkht67c4.streamlit.app/"
DRINKGRAPH_REPO = "https://github.com/aemchira2548/grapDB051"

st.markdown(
    """
    <style>
    .block-container { padding-top: 2rem; max-width: 820px; }
    .hero {
        background: linear-gradient(135deg, #0f766e 0%, #155e75 100%);
        color: #fff; border-radius: 18px; padding: 2rem 2rem 1.6rem;
        margin-bottom: 1.2rem;
    }
    .hero h1 { margin: 0; font-size: 2rem; color: #fff; }
    .hero .sub { opacity: .9; margin-top: .3rem; font-size: 1.02rem; }
    .chips { margin-top: 1rem; }
    .chip {
        display: inline-block; background: rgba(255,255,255,.16);
        border-radius: 999px; padding: .2rem .8rem; margin: 0 .35rem .4rem 0;
        font-size: .85rem;
    }
    .num {
        display: inline-flex; align-items: center; justify-content: center;
        width: 2rem; height: 2rem; border-radius: 50%;
        background: #0f766e; color: #fff; font-weight: 700; margin-right: .6rem;
    }
    .hw-title { font-size: 1.15rem; font-weight: 700; }
    .tag {
        display: inline-block; font-size: .75rem; border-radius: 6px;
        padding: .1rem .5rem; margin-right: .3rem;
        background: rgba(15,118,110,.12); color: #0f766e;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

chips = "".join(f'<span class="chip">{s}</span>' for s in PROFILE["skills"])
st.markdown(
    f"""
    <div class="hero">
        <h1>{PROFILE["name"]}</h1>
        <div class="sub">{PROFILE["name_en"]} · รหัส {PROFILE["student_id"]}</div>
        <div class="sub">{PROFILE["role"]} · {PROFILE["university"]}</div>
        <div class="sub">📍 {PROFILE["location"]} · คาดว่าจะสำเร็จการศึกษา {PROFILE["graduation"]}</div>
        <div class="chips">{chips}</div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.subheader("📚 วิชา Graph Database — ผลงานทั้งหมด")
st.caption("การบ้านชิ้นที่ 1–4 และโปรเจกต์ DrinkGraph (ชิ้นที่ 5)")


def file_button(label: str, filename: str, mime: str, key: str):
    path = ASSETS / filename
    if path.exists():
        st.download_button(
            label, data=path.read_bytes(), file_name=filename, mime=mime, key=key,
            use_container_width=True,
        )
    else:
        st.warning(f"ไม่พบไฟล์ {filename}")


def header(n: int, title: str, tags: list[str]):
    tag_html = "".join(f'<span class="tag">{t}</span>' for t in tags)
    st.markdown(
        f'<div><span class="num">{n}</span><span class="hw-title">{title}</span></div>'
        f'<div style="margin:.4rem 0 .6rem">{tag_html}</div>',
        unsafe_allow_html=True,
    )


# 1
with st.container(border=True):
    header(1, "การบ้านชิ้นที่ 1", ["Google Colab"])
    st.link_button("เปิด Notebook บน Colab", COLAB_1, use_container_width=True)

# 2
with st.container(border=True):
    header(2, "การบ้านชิ้นที่ 2 — ออกแบบ Node/Relationship และเขียน Cypher", ["PDF", "Neo4j", "Cypher"])
    st.write(
        "โมเดลกราฟระบบแนะนำชมรม: Node (Student, Club, Interest) และ Relationship "
        "(FRIEND_OF, MEMBER_OF, INTERESTED_IN, FOCUSES_ON) พร้อมข้อมูลตัวอย่างและคำสั่ง Cypher"
    )
    file_button("⬇️ ดาวน์โหลดไฟล์ PDF", "051-aemchira.pdf", "application/pdf", "hw2")

# 3
with st.container(border=True):
    header(3, "การบ้านชิ้นที่ 3", ["Google Colab"])
    st.link_button("เปิด Notebook บน Colab", COLAB_3, use_container_width=True)

# 4
with st.container(border=True):
    header(4, "การบ้านชิ้นที่ 4", ["Google Colab"])
    st.link_button("เปิด Notebook บน Colab", COLAB_4, use_container_width=True)

# 5
with st.container(border=True):
    header(5, "โปรเจกต์ DrinkGraph — ระบบแนะนำเครื่องดื่มจากกราฟความชอบ", ["Neo4j Aura", "Streamlit", "Cypher"])
    st.write(
        "ดูว่าคนที่ชอบเหมือนคุณดื่มอะไร แล้วเลือกแก้วถัดไปอย่างมีเหตุผล "
        "ด้วยการแนะนำจากกราฟความชอบ"
    )
    c1, c2 = st.columns(2)
    with c1:
        st.link_button("🚀 เปิดเว็บแอป DrinkGraph", DRINKGRAPH_APP, use_container_width=True)
    with c2:
        st.link_button("💻 ซอร์สโค้ดบน GitHub", DRINKGRAPH_REPO, use_container_width=True)
    c3, c4 = st.columns(2)
    with c3:
        file_button("⬇️ สไลด์นำเสนอ (PDF)", "DrinkGraph.pdf", "application/pdf", "dg_pdf")
    with c4:
        file_button(
            "⬇️ สไลด์นำเสนอ (PowerPoint)",
            "DrinkGraph.pptx",
            "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            "dg_pptx",
        )

st.divider()
st.caption("© 2026 Aemchira · Graph Database coursework")
