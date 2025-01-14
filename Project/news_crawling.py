# pip install streamlit-wordcloud
import streamlit as st
from modules.lda_wc_maker import make_lda_wc

if "page" not in st.session_state:
    st.session_state.page = "news_crawling"



def render_page(change_page):

    st.markdown("""
    <style>
        [data-testid="stHorizontalBlock"] img {
            transition: transform 0.3s ease;
        }

        [data-testid="stHorizontalBlock"] img:hover {
            transform: scale(1.5);
        }
    </style>
    """, unsafe_allow_html=True)

    # 뉴스 토픽 분석 및 워드클라우드
    section = st.selectbox("궁금하신 테마를 선택하세요.", ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"])

    if st.button("분석 시작"):
        with st.spinner('로딩중...'):
            # 여기서 로딩 작업 수행 (예: 시간이 걸리는 작업)
            news_data, images = make_lda_wc(section)  # images는 로컬 파일 경로 리스트
            col_widths = [1, 1, 1]  # 열 비율 설정 (1:1:1:1:1)
            cols = st.columns(col_widths)

            for idx, img in enumerate(images):
                with cols[idx]:
                    st.image(img, use_container_width=True)  # 로컬 파일 경로를 바로 사용

            st.header("최신 기사")
            for num in range(5):
                st.subheader(f'{news_data[num]["title"]}')
                st.text(f'{news_data[num]["body"]}')




    if __name__ == "__news_crawling__":
        render_page(change_page)


