import streamlit as st
from tabs import politic_tab, economic_tab, local_tab, lifestyle_tab, it_science_tab, world_tab
from state import initialize_state

# 앱 초기화
initialize_state()

# 앱 제목
st.title("News Crawling Dashboard")

# 탭 생성
tabs = st.tabs(["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"])

# 각 탭 실행
with tabs[0]:
    politic_tab.render()

with tabs[1]:
    economic_tab.render()

with tabs[2]:
    local_tab.render()

with tabs[3]:
    lifestyle_tab.render()

with tabs[4]:
    it_science_tab.render()

with tabs[5]:
    world_tab.render()