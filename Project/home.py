import streamlit as st

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "home"

def render_page(change_page):
    st.title("홈 페이지 :smile:")
    if st.button("news crawling페이지로 이동"):
        change_page("news_crawling")