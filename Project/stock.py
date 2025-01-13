import streamlit as st

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "stock"

def render_page(change_page):
    st.title("주식")
    if st.button("홈으로 이동"):
        change_page("home")