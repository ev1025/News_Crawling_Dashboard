import streamlit as st
from importlib import import_module

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "Home"

# 페이지 이동 함수
def change_page(page_name):
    st.session_state.page = page_name
    st.rerun()

# 페이지별 모듈 매핑
pages = {
    "Home": "home",
    "news_crawling": "news_crawling",
    "stock": "stock",
}

# 사이드바에서 페이지 선택
st.sidebar.title("MENU")
for page_name in pages.keys():
    if st.sidebar.button(page_name):
        change_page(page_name)

# 현재 페이지 실행
current_page = pages[st.session_state.page]
module = import_module(current_page)  # 동적으로 모듈 가져오기
st.write('현재 실행중인 파일 : ',module.__name__)
module.render_page(change_page)       # 각 페이지의 render_page 함수 호출