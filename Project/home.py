import streamlit as st
import numpy as np
import os


# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "home"

def render_page(change_page):
    st.title("News & Stock Crawling")
    # 세션 상태에 'show_image' 키가 없으면 초기화
   
    if 'show_image' not in st.session_state:
        st.session_state.show_image = False
    
    # 풍선 애니메이션 표시
    st.balloons() 

    # 이미지 URL 또는 경로
    image_path = os.path.join(os.path.dirname(__file__), "images", "jamie-street-Zqy-x7K5Qcg-unsplash.jpg")


    # 이미지를 계속 보여주기
    st.image(image_path)

    st.markdown("<h2 style='font-size: 30px;background:#e3f2e3;padding:5px 10px;margin:8px 0 10px 0; color:black;'>데이터 소개</h2>", unsafe_allow_html=True)
    # 네이버 뉴스
    st.markdown("<h3 style='font-size: 24px;padding:15px 10px;'>1. 네이버 뉴스</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **URL**: [네이버 뉴스](https://news.naver.com/section/100)
    """)
    st.markdown("<h4 style='font-size: 20px;padding:10px;'>설명</h4>", unsafe_allow_html=True)
    st.markdown("""
    - 네이버 뉴스의 실시간 뉴스 토픽을 알려드립니다.
    - 궁금하신 테마를 선택하시면 AI가 해당 테마의 3가지 토픽과 최신 기사 5개를 확인해보세요.
    """)

    # 코스피, 코스닥 데이터 소개
    st.markdown("<h3 style='font-size: 24px;padding:15px 10px;'>2. 코스피, 코스닥 지수</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **URL**: [코스피 지수 데이터](https://kr.investing.com/indices/kospi-historical-data)
    - **URL**: [코스닥 지수 데이터](https://kr.investing.com/indices/kospi-historical-data)
    - 최근 1년(2024-01-14 ~ 2025-01-14)간의 코스피, 코스닥 지수 데이터
    """)
    st.markdown("<h4 style='font-size: 20px;padding:10px;'>설명</h4>", unsafe_allow_html=True)
    st.markdown("""
     - **columns**: 날짜, 종가, 시가, 고가, 저가, 거래량, 변동 %
    - **주식 시장의 변동을 추적하고 분석
    """)

    # 네이버페이 증권 데이터 소개
    st.markdown("<h3 style='font-size: 24px;padding:15px 10px;'>3. 네이버페이 증권</h3>", unsafe_allow_html=True)
    st.markdown("""
    - **삼성전자**: [삼성전자 주가](https://m.stock.naver.com/fchart/domestic/stock/005930)
    - **SK 하이닉스**: [SK 하이닉스 주가](https://m.stock.naver.com/fchart/domestic/stock/000660)
    - **LG 에너지솔루션**: [LG 에너지솔루션 주가](https://m.stock.naver.com/fchart/domestic/stock/373220)
    - 시가총액 1, 2, 3위(삼성전자, SK 하이닉스, LG 에너지솔루션)의 주가 크롤링 데이터 
    """)
    st.markdown("<h4 style='font-size: 20px;padding:10px;'>설명</h4>", unsafe_allow_html=True)
    st.markdown("""
    - **columns**: localDate, openPrice, closePrice, highPrice, lowPrice, accumulatedTradingVolume, foreignRetentionRate
    - 시가총액 상위 기업들의 주가 추이를 분석하고 시각화
    """)

    # 2개의 컬럼 생성
    col1, col2 = st.columns(2)

    # 첫 번째 컬럼: 데이터 전처리
    with col1:
        st.markdown("<h2 style='font-size: 30px;background:#fff9c7;padding:5px 10px;margin:30px 0 10px 0; color:black;'>데이터 전처리 과정</h2>", unsafe_allow_html=True)
        st.markdown("""
        - **날짜**: 모든 날짜를 `datetime` 형식으로 변환합니다.
        - **종가**: 종가는 `float` 형식으로 변환하여 분석에 적합하게 만듭니다.
        - **주가 데이터**: 시가총액 상위 기업들의 JSON 데이터를 데이터프레임 형태로 변환하여 분석합니다.
        """)

    # 두 번째 컬럼: 기술 스택
    with col2:
        st.markdown("<h2 style='font-size: 30px;background:#fff9c7;padding:5px 10px;margin:30px 0 10px 0; color:black;'>기술 스택</h2>", unsafe_allow_html=True)
        st.markdown("""
        - **Frontend**: Streamlit
        - **Backend**: Python
        - **웹 크롤링**: BeautifulSoup
        - **데이터 분석**: Pandas
        - **데이터 시각화**: Word Cloud, Matplotlib, Seaborn, Plotly
        """)
        
    
    if __name__ == "__home__":
        render_page(change_page)