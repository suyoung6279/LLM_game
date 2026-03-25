import streamlit as st
import folium
from folium.features import DivIcon
from streamlit_folium import st_folium
import os
import ephem
from dotenv import load_dotenv

load_dotenv()

st.set_page_config(layout="wide")
st.title("📡 제2차 세계대전 연합군 기상 통제 시스템")

# 1. API 키 설정
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")

# ---------------------------------------------------------
# [추가] 스테이지 데이터 정의
# ---------------------------------------------------------
stage_info = {
    "1단계: 루앙 공중 폭격 작전": {"lat": 49.4432, "lon": 1.0993, "date": "1942/06/01", "loc_name": "Rouen"},
    "2단계: 디에프 항구 상륙 작전": {"lat": 49.9243, "lon": 1.0765, "date": "1942/08/19", "loc_name": "Dieppe"},
    "3단계: 카세린 협곡 공습 작전": {"lat": 35.2541, "lon": 8.7191, "date": "1943/02/19", "loc_name": "Kasserine Pass"},
}

# --- 달의 위상 계산 함수 ---
def get_moon_status(dt_str):
    try:
        date = ephem.Date(dt_str)
        moon = ephem.Moon(date)
        illumination = moon.phase / 100 
        
        if illumination < 0.1: phase_name, icon = "그믐달 (매우 어두움)", "🌑"
        elif illumination < 0.4: phase_name, icon = "초승달/그믐달", "🌙"
        elif illumination < 0.6: phase_name, icon = "반달", "🌓"
        elif illumination > 0.9: phase_name, icon = "보름달 (매우 밝음)", "🌕"
        else: phase_name, icon = "상현/하현달", "🌗"
            
        return phase_name, icon, illumination
    except:
        return "데이터 없음", "❓", 0

# --- 사이드바 구현 ---
with st.sidebar:
    st.header("📂 작전 스테이지 선택")
    # 사용자가 여기서 스테이지를 선택하면 날짜가 자동으로 결정됩니다.
    selected_stage_name = st.selectbox("진행 단계를 선택하세요", list(stage_info.keys()))
    current_data = stage_info[selected_stage_name]
    
    st.divider()
    
    st.header("🌙 작전 기상 보고")
    
    # 선택된 스테이지의 날짜를 사용
    phase_name, icon, illumi = get_moon_status(current_data['date'])
    
    st.markdown(f"""
        <div style="background-color: #1e1e1e; padding: 20px; border-radius: 10px; border: 1px solid #333; text-align: center;">
            <div style="font-size: 50px; margin-bottom: 10px;">{icon}</div>
            <div style="font-size: 18px; font-weight: bold; color: #ffcc00;">{phase_name}</div>
            <div style="font-size: 14px; color: #888; margin-top: 5px;">밝기: {illumi*100:.1f}%</div>
        </div>
    """, unsafe_allow_html=True)
    
    st.caption(f"작전 예정일: {current_data['date']}")
    
    st.divider()
    
    st.header("🌦️ 기상 데이터 가이드")
    # ... (구름/강수량 범례 코드는 동일) ...
    st.subheader("구름 두께 (Cloudiness)")
    st.markdown("""
        <div style="background: linear-gradient(to right, rgba(255,255,255,0.1), rgba(255,255,255,0.9)); 
                    height: 20px; width: 100%; border-radius: 5px; border: 1px solid #555;"></div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-top: 5px;">
            <span>옅음 (Clear)</span><span>두꺼움 (Cloudy)</span>
        </div>
    """, unsafe_allow_html=True)
    
    st.subheader("강수량 (Precipitation)")
    st.markdown("""
        <div style="background: linear-gradient(to right, #4b96ff, #4eff4e, #ffff4e, #ff4e4e); 
                    height: 20px; width: 100%; border-radius: 5px; border: 1px solid #555;"></div>
        <div style="display: flex; justify-content: space-between; font-size: 12px; margin-top: 5px;">
            <span>가랑비</span><span>보통</span><span>폭우</span>
        </div>
    """, unsafe_allow_html=True)

# 3. 레이어 URL 설정
cloud_url = f"https://tile.openweathermap.org/map/clouds_new/{{z}}/{{x}}/{{y}}.png?appid={OPENWEATHER_API_KEY}"
precip_url = f"https://tile.openweathermap.org/map/precipitation_new/{{z}}/{{x}}/{{y}}.png?appid={OPENWEATHER_API_KEY}"

# 4. 지도 생성 (선택된 스테이지의 좌표로 자동 이동)
m = folium.Map(location=[current_data['lat'], current_data['lon']], zoom_start=6)

# 5. 날씨 레이어 추가
folium.TileLayer(tiles=cloud_url, attr='Clouds', name='구름(Clouds)', overlay=True, opacity=0.9).add_to(m)
folium.TileLayer(tiles=precip_url, attr='Precipitation', name='강수량(Precipitation)', overlay=True, opacity=0.8).add_to(m)

# 6. 마커 함수 및 추가
def add_mission_marker(map_obj, lat, lon, name):
    folium.Marker([lat, lon], icon=folium.Icon(color='red')).add_to(map_obj)
    folium.Marker(
        [lat, lon],
        icon=DivIcon(
            icon_anchor=(-15, 10),
            html=f'<div style="font-size: 14pt; color: white; font-weight: bold; text-shadow: 2px 2px 2px black;">{name}</div>'
        )
    ).add_to(map_obj)

# 현재 선택된 스테이지에만 강조 마커 표시
add_mission_marker(m, current_data['lat'], current_data['lon'], current_data['loc_name'])

folium.LayerControl().add_to(m)

# 7. 지도 출력 (key 값을 할당해야 스테이지 변경 시 지도가 갱신됩니다)
st_folium(
    m,
    height=700,
    use_container_width=True,
    key=f"map_{selected_stage_name}"
)
st.markdown("""
<style>
/* 전체 배경 */
.stApp {
    background: #1a1610;
    color: #f0e4c8;
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