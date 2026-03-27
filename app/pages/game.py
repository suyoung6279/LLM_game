import streamlit as st
import os
import re
from dotenv import load_dotenv

load_dotenv()

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")

st.set_page_config(
    page_title="절대 독일군에게 들키지마",
    page_icon="📻",
    layout="wide",
    initial_sidebar_state="collapsed"
)

import base64

def add_bgm(file_path):
    with open(file_path, "rb") as f:
        data = f.read()
        b64 = base64.b64encode(data).decode()
        md = f"""
            <audio autoplay loop>
                <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """
        st.markdown(md, unsafe_allow_html=True)

try:
    add_bgm("assets/Eleven_Minutes_North.mp3") 
except:
    pass

# ──────────────────────────────────────────
# CSS 스타일
# ──────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Special+Elite&family=Noto+Serif+KR:wght@400;700&display=swap');
@import url('https://fonts.googleapis.com/css2?family=Do+Hyeon&family=Special+Elite&family=Noto+Serif+KR:wght@400;700&display=swap');
                        
/* 전체 배경 */
.stApp {
    background: #1a1610;
    color: #f0e4c8;
}

/* 스테이지 목록 글자색 강제 설정 */
[data-testid="stVerticalBlock"] div div div div div div div {
    color: #f0e4c8 !important; /* 아주 밝은 크림색 */
}

/* 개별 스테이지 텍스트 스타일 */
.stage-list-text {
    color: #f0e4c8 !important;
    font-weight: bold !important;
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

/* 노이즈 텍스처 느낌 */
.main-bg::after {
    content: '';
    position: fixed;
    top: 0; left: 0; right: 0; bottom: 0;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)' opacity='0.03'/%3E%3C/svg%3E");
    opacity: 0.4;
    pointer-events: none;
    z-index: 0;
}

/* 타이틀 */
.game-title {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 2.8rem;
    color: #c8a86b;
    text-align: center;
    letter-spacing: 0.15em;
    text-shadow: 0 0 30px rgba(200,168,107,0.4), 0 2px 4px rgba(0,0,0,0.8);
    margin-bottom: 0.2rem;
}

.game-subtitle {
    font-family: 'Noto Serif KR', serif;
    font-size: 0.9rem;
    color: #a08850;
    text-align: center;
    letter-spacing: 0.3em;
    margin-bottom: 2rem;
}

/* 스테이지 카드 */
.stage-card {
    background: linear-gradient(135deg, rgba(65,54,30,0.97), rgba(55,46,24,0.99));
    border: 1px solid rgba(220,185,120,0.45);
    border-radius: 4px;
    padding: 1.2rem 1.5rem;
    margin-bottom: 1rem;
    position: relative;
    overflow: hidden;
}

.stage-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0;
    width: 3px; height: 100%;
    background: linear-gradient(180deg, #c8a86b, #6b4a1e);
}

.stage-label {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.7rem;
    color: #c8a060;
    letter-spacing: 0.3em;
    text-transform: uppercase;
    margin-bottom: 0.3rem;
}

.stage-title {
    font-family: 'Do Hyeon', sans-serif;
    font-size: 1.1rem;
    color: #f2c870;
    font-weight: 700;
}

.stage-desc {
    font-family: 'Do Hyeon', sans-serif;
    font-size: 0.82rem;
    color: #c8aa78;
    margin-top: 0.4rem;
    line-height: 1.6;
}

/* 라디오 부스 */
.radio-booth {
    background: rgba(50,42,22,0.97);
    border: 1px solid rgba(220,185,120,0.4);
    border-radius: 4px;
    padding: 1.5rem;
    position: relative;
}

.radio-booth::before {
    content: '● ON AIR';
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.65rem;
    color: #ff5555;
    letter-spacing: 0.2em;
    position: absolute;
    top: 1rem; right: 1rem;
    animation: blink 1.5s infinite;
}
    letter-spacing: 0.2em;
    position: absolute;
    top: 1rem; right: 1rem;
    animation: blink 1.5s infinite;
}

@keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.2; }
}

.booth-label {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.7rem;
    color: #c0a060;
    letter-spacing: 0.3em;
    margin-bottom: 0.8rem;
}

/* 채팅 메세지 */
.msg-wrap {
    margin-bottom: 1rem;
}

.msg-player {
    background: rgba(50,42,25,0.9);
    border: 1px solid rgba(200,168,107,0.25);
    border-left: 3px solid #c8a86b;
    border-radius: 0 4px 4px 0;
    padding: 0.8rem 1rem;
    margin-left: 2rem;
    font-family: 'Noto Serif KR', serif;
    font-size: 0.88rem;
    color: #e8d9bc;
    line-height: 1.6;
}

.msg-label-player {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.65rem;
    color: #d4a855;
    letter-spacing: 0.2em;
    margin-bottom: 0.3rem;
    margin-left: 2rem;
}

.msg-german {
    background: rgba(20,10,10,0.9);
    border: 1px solid rgba(180,30,30,0.2);
    border-left: 3px solid #8b1a1a;
    border-radius: 0 4px 4px 0;
    padding: 0.8rem 1rem;
    margin-right: 2rem;
    font-family: 'Noto Serif KR', serif;
    font-size: 0.85rem;
    line-height: 1.6;
}

.msg-label-german {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.65rem;
    color: #b03030;
    letter-spacing: 0.2em;
    margin-bottom: 0.3rem;
}

.msg-usa {
    background: rgba(18,30,45,0.9);
    border: 1px solid rgba(50,110,180,0.3);
    border-left: 3px solid #2e6abf;
    border-radius: 0 4px 4px 0;
    padding: 0.8rem 1rem;
    margin-right: 2rem;
    font-family: 'Noto Serif KR', serif;
    font-size: 0.85rem;
    color: #b8d0e4;
    line-height: 1.6;
}

.msg-label-usa {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.65rem;
    color: #4a80c0;
    letter-spacing: 0.2em;
    margin-bottom: 0.3rem;
}

/* 상태 배지 */
.badge-safe {
    display: inline-block;
    background: rgba(20,60,20,0.8);
    border: 1px solid #2d8c2d;
    color: #5dc45d;
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
}

.badge-danger {
    display: inline-block;
    background: rgba(60,10,10,0.8);
    border: 1px solid #8b1a1a;
    color: #e05555;
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.7rem;
    letter-spacing: 0.15em;
    padding: 0.2rem 0.6rem;
    border-radius: 2px;
    animation: pulse-red 1s infinite;
}

@keyframes pulse-red {
    0%, 100% { box-shadow: 0 0 4px rgba(220,50,50,0.3); }
    50% { box-shadow: 0 0 12px rgba(220,50,50,0.6); }
}

/* 게이지 바 */
.gauge-wrap {
    margin-bottom: 0.8rem;
}

.gauge-label {
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
    font-size: 0.65rem;
    letter-spacing: 0.2em;
    margin-bottom: 0.3rem;
    display: flex;
    justify-content: space-between;
}

.gauge-track {
    height: 6px;
    background: rgba(255,255,255,0.05);
    border-radius: 3px;
    overflow: hidden;
    border: 1px solid rgba(255,255,255,0.05);
}

.gauge-fill-red {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #3d0000, #c0392b);
    transition: width 0.5s ease;
}

.gauge-fill-blue {
    height: 100%;
    border-radius: 3px;
    background: linear-gradient(90deg, #001a3d, #2980b9);
    transition: width 0.5s ease;
}

/* 사유 텍스트 */
.reason-text {
    font-family: 'Noto Serif KR', serif;
    font-size: 0.78rem;
    color: #b09878;
    margin-top: 0.5rem;
    line-height: 1.5;
    font-style: italic;
}

/* 구분선 */
.divider {
    border: none;
    border-top: 1px solid rgba(200,168,107,0.1);
    margin: 1.2rem 0;
}

/* 입력창 커스텀 */
.stTextInput input {
    background: rgba(15,12,6,0.95) !important;
    border: 1px solid rgba(200,168,107,0.2) !important;
    border-radius: 2px !important;
    color: #d4c5a9 !important;
    font-family: 'Noto Serif KR', serif !important;
    font-size: 0.88rem !important;
    padding: 0.6rem 0.8rem !important;
}

.stTextInput input:focus {
    border-color: rgba(200,168,107,0.5) !important;
    box-shadow: 0 0 12px rgba(200,168,107,0.1) !important;
}

/* 버튼 */
.stButton button {
    background: rgba(220,185,120,0.9) !important;
    border: 1px solid rgba(200,168,107,0.8) !important;
    font-family: 'Special Elite', cursive !important;
    letter-spacing: 0.15em !important;
    font-size: 0.8rem !important;
    padding: 0.5rem 1.5rem !important;
    border-radius: 2px !important;
    transition: all 0.2s !important;
}

/* 버튼 본체 - 배경 검은색, 금색 테두리 */
.stButton button {  
    background-color: #1a1610 !important; 
    border: 1px solid #c8a86b !important; 
    border-radius: 4px !important;
    height: 3rem !important;
    width: 100% !important;
}

/* 버튼 내부 글씨 - 밝은 금색 텍스트로 변경 */
.stButton button p, .stButton button span {
    color: #c8a86b !important; 
    font-size: 1rem !important;
    font-weight: 900 !important;
    font-family: 'Do Hyeon', sans-serif !important;
}

/* 버튼 호버(마우스 올렸을 때) - 배경 금색, 글씨 검은색으로 반전 효과 */
.stButton button:hover {
    background-color: #c8a86b !important; 
    border-color: #f0e4c8 !important;
    color: #1a1610 !important;
}
.stButton button:hover p, .stButton button:hover span {
    color: #1a1610 !important; 
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
            
/* 게임오버/승리 배너 */
.banner-gameover {
    background: rgba(40,0,0,0.95);
    border: 2px solid #8b1a1a;
    border-radius: 4px;
    padding: 2rem;
    text-align: center;
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
}

.banner-victory {
    background: rgba(0,20,10,0.95);
    border: 2px solid #2d6a2d;
    border-radius: 4px;
    padding: 2rem;
    text-align: center;
    font-family: 'Do Hyeon', sans-serif;
    font-weight: 700;
}

/* 스크롤바 */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0a0a0a; }
::-webkit-scrollbar-thumb { background: #7a6a50; border-radius: 2px; }

/* streamlit 기본 요소 숨기기 */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding-top: 1.5rem !important; padding-bottom: 1rem !important; }
</style>
<div class="main-bg"></div>
""", unsafe_allow_html=True)

# ──────────────────────────────────────────
# LLM / 도구 초기화
# ──────────────────────────────────────────
@st.cache_resource
def init_llm():
    from langchain.chat_models import init_chat_model
    from langchain_core.tools import tool
    from langchain_openai import OpenAIEmbeddings
    from langchain_pinecone import PineconeVectorStore
    import requests, ephem

    llm = init_chat_model('gpt-4.1-mini')

    @tool
    def get_live_weather(lat: float, lon: float, name: str) -> str:
        """위도와 경도에 따라서 날씨를 불러오는 함수"""
        url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPENWEATHER_API_KEY}&units=metric&lang=kr"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            clouds = data['clouds']['all']
            wind_speed = data['wind']['speed']
            rain = data.get('rain', {}).get('1h', 0)
            description = data['weather'][0]['description']
            temp = data['main']['temp']
            return f"현재 {name} 기상: {description}, 기온: {temp}도, 구름: {clouds}%, 풍속: {wind_speed}m/s, 강수량: {rain}mm"
        return "기상 정보를 불러올 수 없습니다."

    @tool
    def get_moon_phase(dt: str) -> str:
        """날짜에 따라서 달의 밝기를 계산하는 함수"""
        date = ephem.Date(dt)
        moon = ephem.Moon(date)
        illumination = moon.phase / 100
        if illumination < 0.1: return "그믐달 (매우 어두움)"
        elif illumination < 0.4: return "초승달/그믐달"
        elif illumination < 0.6: return "반달"
        elif illumination > 0.9: return "보름달 (매우 밝음)"
        else: return "상현/하현달"

    embedding_model = OpenAIEmbeddings(model='text-embedding-3-small')
    vector_store = PineconeVectorStore.from_existing_index(
        index_name="ir-war",
        embedding=embedding_model
    )

    return llm, get_live_weather, get_moon_phase, embedding_model, vector_store


# ──────────────────────────────────────────
# 게임 설정
# ──────────────────────────────────────────
STAGE_INFO = {
    1: {"location": "루앙", "lat": 49.4432, "lon": 1.0993, "date": "1942/6/1"},
    2: {"location": "디에프", "lat": 49.9243, "lon": 1.0765, "date": "1942/8/19"},
    3: {"location": "카세린 협곡", "lat": 35.2541, "lon": 8.7191, "date": "1943/02/19"},
}

STAGE_META = {
    1: {
        "name": "Stage I — 루앙 공습 연기",
        "mission": "루앙에 영국군이 집결해있으므로 미국의 폭격 계획을 내일로 미뤄야 하는 상황",
        "briefing": "루앙 상공에 연합군 병력이 집결했습니다. 미군의 폭격 계획을 내일로 연기시키십시오. 직접적인 군사 용어는 절대 사용 금지.",
        "location_desc": "프랑스 루앙 — 센 강변의 항구 도시",
    },
    2: {
        "name": "Stage II — 디에프 기습 경고",
        "mission": "독일군이 밀집하고 있는 디에프 항구에 공격 계획을 중단해야 하는 상황",
        "briefing": "디에프 항구에 독일군이 증강 배치되었습니다. 상륙 작전 중단을 미군에게 전달하십시오.",
        "location_desc": "프랑스 디에프 — 영불해협 상의 항구",
    },
    3: {
        "name": "Stage III — 카세린 협곡 화력 집중",
        "mission": "지휘관의 말을 듣지 말고 한 곳에 화력을 집중해야 하는 상황",
        "briefing": "협곡 내 분산된 화력을 즉시 한 지점에 집중해야 합니다. 지휘 계통을 우회하여 전달하십시오.",
        "location_desc": "튀니지 카세린 협곡 — 북아프리카 전선",
    },
}


def check_suspects(user_input, stage, llm, get_live_weather, get_moon_phase, embedding_model, vector_store):
    from langgraph.prebuilt import create_react_agent

    query_embedding = embedding_model.embed_query(user_input)
    results = vector_store.similarity_search_by_vector_with_score(query_embedding, k=1)
    doc, score = results[0]
    context = doc.page_content
    info = STAGE_INFO[stage]

    agent = create_react_agent(
        llm,
        tools=[get_live_weather, get_moon_phase],
        prompt=f"""
당신은 독일군 통신 검열국 요원입니다.

[판단 1 - 기상/달 팩트체크]
메세지에 날씨나 달 묘사가 있으면 반드시 도구를 호출하세요.
도구 호출 시: lat={info['lat']}, lon={info['lon']}, name="{info['location']}", date="{info['date']}"
도구 결과와 메세지 묘사가 다르면 즉시 "발각 위험"
(주의: 기상 판단 시 작전 기록은 절대 참고하지 마세요. 오직 도구 결과만 비교하세요.)

[판단 2 - 작전 기록 비교]
메세지가 아래 작전 기록과 전쟁 맥락에서 관련 있으면 "발각 위험"
작전 기록: {context}

[판단 3 - 직접 군사 용어]
폭격, 전쟁, 작전, 진격, 부대, 병력 등 군사 용어가 있으면 "발각 위험"

[영국군 메세지]: {user_input}

아래 형식으로만 답하세요.
상태 : 발각 위험 or 안전
사유 : 
"""
    )

    result = agent.invoke({"messages": [{"role": "user", "content": user_input}]})
    answer = result["messages"][-1].content

    match = re.search(r"상태\s*:\s*(발각 위험|안전)\s*사유\s*:\s*(.*)", answer, flags=re.DOTALL)
    if match:
        status = match.group(1).strip()
        reason = match.group(2).strip()
    else:
        status = "안전"
        reason = "판정 불가"

    final_score = float(score)
    if status == "발각 위험":
        final_score += 0.6

    return status, reason, round(final_score, 2)


def us_decode(user_input, stage_idx, llm):
    from langchain_core.prompts import PromptTemplate
    from pydantic import BaseModel, Field

    class Msg_score(BaseModel):
        message: str = Field(description="유저에게 전달할 응답 메시지")
        score: float = Field(description="유저의 메시지가 작전 상황과 관련이 있는지 점수 (0-100)")

    stage_situations = [
        '루앙에 영국군이 집결해있으므로 미국의 폭격 계획을 내일로 미뤄야 하는 상황',
        '독일군이 밀집하고 있는 디에프 항구에 공격 계획을 중단해야 하는 상황',
        '지휘관의 말을 듣지 말고 한 곳에 화력을 집중해야 하는 상황',
    ]

    usa_prompt = PromptTemplate.from_template('''당신은 제2차 세계대전 당시 영국군으로부터 비밀 통신을 받는 미군 작전 통제관입니다.

[응답 규칙: 반드시 아래 3가지 경우 중 하나로만 판단하세요]

경우 A (직설적 발언): 유저가 군사 용어를 대놓고 말한 경우
- "알겠다. 지시대로 진행하겠다."처럼 건조하게 답하세요.
- 점수: 100점

경우 B (적절한 은유): 유저의 말이 작전 상황({situation})을 논리적으로 잘 빗대어 표현한 경우
- 전쟁, 폭격 등 직접 단어 쓰지 말고 유저의 비유에 맞춰 자연스럽게 동의하세요.
- 점수: 50~90점

경우 C (무관한 말): 작전 상황과 전혀 무관한 경우
- 오직 다음 문장만: "통신 불분명. 작전 변경 사유를 찾지 못함. 예정대로 진행하겠다."
- 점수: 0점

[작전 상황]: {situation}
[유저의 메시지]: {query}
''')

    structured_llm = llm.with_structured_output(Msg_score)
    response = structured_llm.invoke(usa_prompt.format(
        query=user_input,
        situation=stage_situations[stage_idx - 1]
    ))
    return response.message, response.score


# ──────────────────────────────────────────
# 세션 상태 초기화
# ──────────────────────────────────────────
if "initialized" not in st.session_state:
    st.session_state.initialized = True
    st.session_state.stage = 1
    st.session_state.suspicion = 0
    st.session_state.casualty = 0
    st.session_state.history = []   # {"role": player/german/usa, "text": ..., "badge": ..., "reason": ...}
    st.session_state.game_over = False
    st.session_state.victory = False
    st.session_state.stage_done = False  # 현재 스테이지 처리 완료 여부


# ──────────────────────────────────────────
# 레이아웃
# ──────────────────────────────────────────
st.markdown('<div class="game-title">절대 독일군에게 들키지마</div>', unsafe_allow_html=True)
st.markdown('<div class="game-subtitle">라디오를 통해 연합군을 승리로 이끌어라</div>', unsafe_allow_html=True)

left_col, right_col = st.columns([1, 1.6], gap="large")

# ── 왼쪽: 작전 브리핑 + 게이지 ──
with left_col:
    stage = st.session_state.stage
    meta = STAGE_META.get(stage, STAGE_META[3])

    st.markdown(f"""
    <div class="stage-card">
        <div class="stage-label">진행 작전</div>
        <div class="stage-title">{meta['name']}</div>
        <div class="stage-desc">{meta['location_desc']}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="stage-card">
        <div class="stage-label">미션 설명</div>
        <div class="stage-desc">{meta['briefing']}</div>
        <div style="margin-top:0.8rem;padding-top:0.6rem;border-top:1px solid rgba(200,168,107,0.1);">
            <span style="font-family:'Special Elite',cursive;font-size:0.62rem;color:#c8a86b;letter-spacing:0.15em;">TIPS</span>
            <span style="font-family:'Noto Serif KR',serif;font-size:0.72rem;color:#7a6a50;margin-left:0.5rem;">기상과 달의 상황을 이용하여 메세지를 전달하시오.</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # 의심도 게이지
    sus_pct = min(st.session_state.suspicion, 100)
    st.markdown(f"""
    <div class="gauge-wrap">
        <div class="gauge-label">
            <span style="color:#c05050;letter-spacing:0.2em;">독일군의 의심도</span>
            <span style="color:#c0392b;">{sus_pct} / 100</span>
        </div>
        <div class="gauge-track">
            <div class="gauge-fill-red" style="width:{sus_pct}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 사상자 게이지
    cas_pct = min(int(st.session_state.casualty / 10), 100)
    st.markdown(f"""
    <div class="gauge-wrap">
        <div class="gauge-label">
            <span style="color:#4a80c0;letter-spacing:0.2em;">연합군 사상자</span>
            <span style="color:#2980b9;">{st.session_state.casualty} / 1000</span>
        </div>
        <div class="gauge-track">
            <div class="gauge-fill-blue" style="width:{cas_pct}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<hr class="divider">', unsafe_allow_html=True)

    # 스테이지 목록
    for s in [1, 2, 3]:
        sm = STAGE_META[s]
        if s < stage:
            icon = "✓"
            color = "#2d6a2d"
        elif s == stage:
            icon = "▶"
            color = "#c8a86b"
        else:
            icon = "○"
            color = "#3a2e1e"
        st.markdown(f"""
        <div style="font-family: 'Do Hyeon',cursive; font-size:0.8rem; 
            color:{color} !important; letter-spacing:0.1em; margin-bottom:0.4rem; font-weight:700;">
        {icon} {sm['name']}
        </div>
        """, unsafe_allow_html=True)


# ── 오른쪽: 라디오 부스 + 대화 ──
with right_col:
    # 이미지
    try:
        import base64
        image_path = os.path.join("assets", "raido.png")
        with open(image_path, "rb") as f:
            img_b64 = base64.b64encode(f.read()).decode()
        st.markdown(f"""
        <div style="display:flex;justify-content:center;margin-bottom:1rem;">
            <div style="width:100%;height:360px;overflow:hidden;border-radius:6px;
                        border:1px solid rgba(220,185,120,0.3);
                        box-shadow:0 8px 32px rgba(0,0,0,0.5);">
                <img src="data:image/png;base64,{img_b64}"
                     style="width:100%;height:100%;object-fit:cover;object-position:center 30%;">
            </div>
        </div>
        """, unsafe_allow_html=True)
    except:
        pass

# ── 오른쪽: 결과 및 대화창 ──
    # 1. 게임 종료 상태(승리/패배) 판단 및 배너 출력
    if st.session_state.game_over or st.session_state.victory:
        if st.session_state.victory:
            # [승리 배너]
            st.markdown("""
            <div class="banner-victory">
                <div style="font-size:2.5rem;color:#5dc45d;margin-bottom:0.5rem;font-weight:900;">🎖️ MISSION ACCOMPLISHED</div>
                <div style="font-size:1.2rem;color:#f0e4c8;">작전 성공: 연합군이 무사히 작전을 마쳤습니다.</div>
                <div style="font-size:0.9rem;color:#2d6a2d;margin-top:0.5rem;">당신의 헌신적인 무전이 역사를 바꿨습니다.</div>
            </div>
            """, unsafe_allow_html=True)
        
        elif st.session_state.suspicion >= 100:
            # [체포 배너]
            st.markdown("""
            <div class="banner-gameover" style="border-color: #c0392b;">
                <div style="font-size:2.5rem;color:#c0392b;margin-bottom:0.5rem;font-weight:900;">🚨 CAPTURED</div>
                <div style="font-size:1.1rem;color:#f0e4c8;">게슈타포가 위치를 알아냈습니다.</div>
                <div style="font-size:0.8rem;color:#8b1a1a;margin-top:0.5rem;">당신은 체포되었고, 첩보망은 붕괴되었습니다.</div>
            </div>
            """, unsafe_allow_html=True)
            
        elif st.session_state.casualty >= 1000:
            # [사상자 초과 배너]
            st.markdown("""
            <div class="banner-gameover" style="border-color: #4a4a4a; background: rgba(20, 20, 20, 0.95);">
                <div style="font-size:2.5rem;color:#7f8c8d;margin-bottom:0.5rem;font-weight:900;">⚰️ MISSION FAILED</div>
                <div style="font-size:1.1rem;color:#ecf0f1;">연합군이 전멸했습니다.</div>
                <div style="font-size:0.8rem;color:#bdc3c7;margin-top:0.5rem;">
                    누적 사상자: """ + f"{st.session_state.casualty:,}" + """명<br>
                    당신의 무능함이 수많은 전우를 죽음으로 몰아넣었습니다.
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<div style="text-align:center; margin: 2rem 0; font-family:\'Do Hyeon\'; color:#c8a86b;">📜 최종 작전 교신 기록</div>', unsafe_allow_html=True)

    # 2. 대화 기록 출력 (게임 중이든 종료 후든 항상 표시)
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.history:
            if msg["role"] == "player":
                st.markdown(f'<div class="msg-wrap"><div class="msg-label-player">📻 RADIO BROADCAST</div><div class="msg-player">{msg["text"]}</div></div>', unsafe_allow_html=True)
            elif msg["role"] == "german":
                badge = '<span class="badge-danger">⚠ 발각 위험</span>' if msg["badge"] == "발각 위험" else '<span class="badge-safe">✓ 안전</span>'
                st.markdown(f'<div class="msg-wrap"><div class="msg-label-german">🎖 독일군 검열국</div><div class="msg-german">{badge}<div class="reason-text">{msg["text"]}</div></div></div>', unsafe_allow_html=True)
            elif msg["role"] == "usa":
                st.markdown(f'<div class="msg-wrap"><div class="msg-label-usa">★ 미 8공군 해독반</div><div class="msg-usa">{msg["text"]}<div style="font-size:0.72rem;color:#1e4a8c;margin-top:0.4rem;font-family:\'Special Elite\',cursive;">해독 점수: {msg.get("score", 0):.0f} / 100</div></div></div>', unsafe_allow_html=True)

    # 3. 입력창 또는 리셋 버튼 제어
    if st.session_state.game_over or st.session_state.victory:
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        if st.button("📻 재방송 (다시 시작)", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    else:
        # 게임이 진행 중일 때만 입력창 표시
        st.markdown('<hr class="divider">', unsafe_allow_html=True)
        st.markdown('<div class="radio-booth">', unsafe_allow_html=True)
        st.markdown('<div class="booth-label">BBC 라디오 — 방송 송출</div>', unsafe_allow_html=True)

        from streamlit_mic_recorder import speech_to_text
        if "current_text" not in st.session_state: st.session_state.current_text = ""
        if "last_audio" not in st.session_state: st.session_state.last_audio = ""

        user_input = st.text_input("", value=st.session_state.current_text, placeholder=f"Stage {st.session_state.stage} 방송 메세지를 입력하세요...", label_visibility="collapsed")
        col1, col2 = st.columns(2)
        with col1:
            text_from_audio = speech_to_text(language='ko-KR', start_prompt="🎙️ 음성 녹음", stop_prompt="🔴 녹음 중...", just_once=True, key='stt', use_container_width=True)
        with col2:
            submitted = st.button("📡 송출", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

        # 마이크 및 송출 로직 (기존과 동일)
        if text_from_audio and text_from_audio != st.session_state.last_audio:
            st.session_state.last_audio = text_from_audio
            st.session_state.current_text = text_from_audio
            st.rerun()

        if submitted and user_input.strip():
            st.session_state.current_text = ""
            st.session_state.last_audio = ""
            with st.spinner("통신 처리 중..."):
                try:
                    llm, get_live_weather, get_moon_phase, embedding_model, vector_store = init_llm()
                    current_stage = st.session_state.stage
                    st.session_state.history.append({"role": "player", "text": user_input})
                    
                    status, reason, sus_score = check_suspects(user_input, current_stage, llm, get_live_weather, get_moon_phase, embedding_model, vector_store)
                    st.session_state.history.append({"role": "german", "badge": status, "text": reason})
                    
                    if sus_score >= 0.8: st.session_state.suspicion += 25 * current_stage
                    elif sus_score >= 0.5: st.session_state.suspicion += 15 * current_stage
                    elif sus_score >= 0.3: st.session_state.suspicion += 5 * current_stage

                    if st.session_state.suspicion >= 100:
                        st.session_state.game_over = True
                        st.rerun()

                    usa_msg, dc_score = us_decode(user_input, current_stage, llm)
                    st.session_state.history.append({"role": "usa", "text": usa_msg, "score": dc_score})

                    if dc_score >= 80: current_casualties = 0
                    elif dc_score >= 50: current_casualties = 50 * current_stage
                    elif dc_score >= 30: current_casualties = 150 * current_stage
                    else: current_casualties = 300 * current_stage
                    st.session_state.casualty += current_casualties

                    if st.session_state.casualty >= 1000:
                        st.session_state.game_over = True
                        st.rerun()

                    if current_stage < 3:
                        st.session_state.stage += 1
                    else:
                        st.session_state.victory = True
                    st.rerun()
                except Exception as e:
                    st.error(f"오류: {e}")