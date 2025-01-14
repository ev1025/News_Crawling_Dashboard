import streamlit as st
import numpy as np

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "home"

def render_page(change_page):
    st.title("홈 페이지 :smile:")
    # 세션 상태에 'show_image' 키가 없으면 초기화
    if 'show_image' not in st.session_state:
        st.session_state.show_image = False
    # 이미지 URL 또는 경로
    image_path = "./images/stock_img.jpg"
    # 이미지를 계속 보여주기
    st.image(image_path)
    if __name__ == "__home__":
        render_page(change_page)