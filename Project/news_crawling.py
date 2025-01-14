import streamlit as st
from tabs import politic_tab, economic_tab, local_tab, lifestyle_tab, it_science_tab, world_tab

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "news_crawling"

# 탭 제목
st.title("News Crawling Dashboard")

# CSS 스타일 정의
st.markdown(
    """
    <style>
    .stTabs {
        width:100%;
    }
    </style>
    """,
    unsafe_allow_html=True
)

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