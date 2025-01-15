# pip install wordcloud
import streamlit as st
from modules.lda_wc_maker import make_lda_wc
import time
import datetime
if "page" not in st.session_state:
    st.session_state.page = "news_crawling"



def render_page(change_page):

    st.markdown("""
    <style>
        /* 워드클라우드 호버 */
        [data-testid="stHorizontalBlock"] img {
        transition: transform 0.3s ease;
        }
        [data-testid="stHorizontalBlock"] img:hover {
        transform: scale(1.8);
        position: relative;
        z-index: 9999;
        }
                
        /* 기사 더보기 */
        span.st-emotion-cache-pkbazv.e11k5jya0 > div[data-testid="stMarkdownContainer"] p {
        text-decoration: underline;
        }
                
        /* 토글 기사 제목 */ 
        .st-emotion-cache-1wmy9hl.e1f1d6gn1 .st-emotion-cache-1puwf6r.e1nzilvr5 p {
        font-size: 18px;
        font-weight: bold;  
        } 
                
        .stElementContainer.element-container.st-emotion-cache-3w7kxl.e1f1d6gn4 {
        margin: 0px;
        padding : 0px
        }
</style>
    """, unsafe_allow_html=True)

    section_list = ["정치", "경제", "사회", "생활/문화", "IT/과학", "세계"]
    section_num = [i for i in range(100,106)]
    section_dict = dict(zip(section_list, section_num))

    # 오늘 날짜 가져오기
    today = datetime.date.today()
    formatted_today = today.strftime("%Y-%m-%d")
    
    st.image("images/nnews.png")
    st.header('최신 뉴스 토픽', ) 
    st.write("Today:", formatted_today)
    
    section = st.selectbox("궁금하신 테마를 선택하세요.", section_list)

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
                with st.expander(f'{news_data[num]["title"]}'):
                    st.write(f'{news_data[num]["body"]}')
            a = st.success('완료')
            time.sleep(1)
            a.empty()
            
            st.page_link(f"https://news.naver.com/section/{section_dict[section]}", label=f"{section}기사 보러 가기", icon='📰')


    if __name__ == "__news_crawling__":
        render_page(change_page)