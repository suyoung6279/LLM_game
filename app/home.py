import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="Metaphor for Peace", layout="wide")

# 2. 사용자 지정 CSS 적용 (제공해주신 스타일)
st.markdown("""
<style>
/* 전체 배경 */
.stApp {
    background: #1a1610;
    color: #f0e4c8;
}
            
.white-warning {
    background-color: #f2e8cf !important; /* 👈 하얀색 배경 코드가 여기입니다! */
    color: #b00000 !important; /* 👈 검은색 글씨 코드가 여기입니다! */
    padding: 15px;
    border-radius: 5px;
    font-weight: bold;
    text-align: left;
    margin-bottom: 20px;
    border: 2px solid #c8b07a !important; /* 👈 첩보물 테마에 맞춘 금빛 테두리 추가 */
}
            
hr {
    border: 0 !important;
    height: 1px !important;
    background-image: linear-gradient(to right, rgba(200,168,107,0), rgba(200,168,107,0.6), rgba(200,168,107,0)) !important;
    margin: 2.5rem 0 !important;
}
            
/* 추가: 최상위 레이어까지 배경 통일 */
html, body, [data-testid="stAppViewContainer"], .stApp {
    background: #1a1610 !important;
    color: #f0e4c8 !important;
}

[data-testid="stAppViewContainer"] > .main,
[data-testid="stAppViewContainer"] > .main > div,
section.main,
.block-container {
    background: transparent !important;
}

[data-testid="stHeader"] {
    background: #1a1610 !important;
}

[data-testid="stToolbar"] {
    background: transparent !important;
}

[data-testid="stMain"] {
    background: transparent !important;
}

iframe {
    background: transparent !important;
}

/* 메인 배경 오버레이 */
.main-bg {
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background:
        radial-gradient(ellipse at 20% 50%, rgba(200,150,70,0.12) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 20%, rgba(60,90,40,0.10) 0%, transparent 50%),
        linear-gradient(180deg, #1a1610 0%, #201c10 50%, #1a1610 100%);
    z-index: 0;
    pointer-events: none;
}

/* 사이드바 전체 배경 */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #18140f 0%, #211b12 50%, #18140f 100%) !important;
    border-right: 1px solid rgba(200,168,107,0.18) !important;
}

/* 사이드바 내부 컨테이너 */
section[data-testid="stSidebar"] > div {
    background:
        radial-gradient(ellipse at 20% 30%, rgba(200,150,70,0.08) 0%, transparent 45%),
        linear-gradient(180deg, #18140f 0%, #211b12 50%, #18140f 100%) !important;
}

/* 사이드바 안 글씨 */
section[data-testid="stSidebar"] * {
    color: #c8b07a !important;
}

/* 선택된 메뉴 항목 */
section[data-testid="stSidebar"] .stPageLink a[aria-current="page"],
section[data-testid="stSidebar"] [data-testid="stSidebarNav"] a[aria-current="page"] {
    background: rgba(200,168,107,0.14) !important;
    color: #f0e4c8 !important;
    border: 1px solid rgba(200,168,107,0.22) !important;
    border-radius: 8px !important;
}

/* 메뉴 hover */
section[data-testid="stSidebar"] a:hover {
    background: rgba(200,168,107,0.08) !important;
    color: #f0e4c8 !important;
    border-radius: 8px !important;
}
</style>
""", unsafe_allow_html=True)

# CSS 오버레이를 위한 빈 컨테이너
st.markdown('<div class="main-bg"></div>', unsafe_allow_html=True)

# 3. 게임 메인 타이틀
st.title("🎙️ 작전명 : Metaphor for Peace")
st.markdown("---")

# 4. 게임 배경 설명
st.header("📜 작전 배경")
st.markdown("""
제2차 세계대전이 한창인 1942년, 미국은 연합군으로 참전하며 전쟁의 새로운 국면을 엽니다. 
하지만 치명적인 위기가 발생했습니다. **영국군이 미군에게 보내는 모든 작전 전보를 독일군이 철저히 감청하고 있다는 사실**이 밝혀진 것입니다.

연합군의 대규모 희생을 막기 위해 급박하게 계획을 수정해야 하는 절체절명의 상황. 
영국의 통신 장교인 당신은 **심야 라디오 DJ로 위장**하여 마이크 앞에 앉습니다. 당신의 임무는 독일군의 감시를 피해 미군과 소통하며, 
역사상 연합군이 뼈아픈 패배를 겪었던 3가지 사건의 작전 계획을 수정하는 것입니다.
""")

st.markdown("---")

# 5. 스테이지 안내
st.header("🗺️ 작전 지역 및 미션")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("📍 1단계: 루앙")
    st.caption("1942년 6월 | 프랑스")
    st.markdown("""
    * **상황:** 미군의 루앙 지역 대규모 폭격 예정.
    * **미션:** 해당 지역에 영국 비밀요원들이 잠입해 있습니다. 요원들의 생존을 위해 다음 날로 예정된 미군의 **공중 폭격 계획을 반드시 연기**시켜야 합니다.
    """)

with col2:
    st.subheader("📍 2단계: 디에프")
    st.caption("1942년 8월 | 항구 도시")
    st.markdown("""
    * **상황:** 연합군의 대규모 상륙 작전 예정.
    * **미션:** 디에프 항구에 독일군이 대규모로 집결하고 있다는 핵심 정보를 파악했습니다. 미군에게 이 사실을 알려 **상륙 계획을 전면 수정**하도록 유도하십시오.
    """)

with col3:
    st.subheader("📍 3단계: 카세린 협곡")
    st.caption("1943년 2월 | 북아프리카 튀니지")
    st.markdown("""
    * **상황:** 연합군 사령관의 병력 분산 명령.
    * **미션:** 좁은 협곡에 병력을 분산시키면 각개격파를 당하게 됩니다. 사령관의 말을 무시하고, 병력을 분산시키지 말고 **협곡의 '한 곳'에 집중적인 공세**를 퍼부으라고 하달하십시오.
    """)

st.markdown("---")

# 6. 게임 규칙 (생존 가이드)
st.header("⚠️ 작전 수칙 (생존 가이드)")
st.markdown('<div class="white-warning">당신의 모든 방송은 독일군에게 실시간으로 감청되고 있습니다. 직설적인 화법은 죽음을, 너무 난해한 화법은 동료들의 죽음을 부릅니다.</div>', unsafe_allow_html=True)

st.markdown("""
* **🚨 직설적인 발언 (게임 오버):** 전쟁 계획이나 지명을 노골적으로 언급하면, 독일군이 눈치를 채고 방송국을 급습하여 당신을 체포할 것입니다.
* **❓ 과도한 비유 (게임 오버):** 비유가 너무 난해하여 미군이 알아듣지 못하면, 원래 계획이 강행되어 연합군이 전멸하고 당신은 통신 장교에서 해임됩니다.
* **🎯 승리 조건:** 비유적인 표현(Metaphor)을 사용하여 독일군을 속이면서도, 미군 지휘관이 정확히 작전을 바꿀 수 있도록 절묘한 줄타기를 해야 합니다.
* **❓ tip : 'weather' 부분에서 날씨와 달의 상황을 보고 비유하여 독일군을 속이세요. 물론 실제와 다르다면, 큰 후폭풍이 찾아올 수 있습니다. 
""")