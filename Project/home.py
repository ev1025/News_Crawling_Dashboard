import streamlit as st

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "home"

st.title("홈 페이지")
st.write("이곳은 홈입니다.")