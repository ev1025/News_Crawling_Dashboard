# pip install wordcloud
import streamlit as st
from modules.lda_wc_maker import make_lda_wc
import time
import datetime
import os

if "page" not in st.session_state:
    st.session_state.page = "news_crawling"



def render_page(change_page):

    st.markdown("""
    <style>
                
        /* 기사 더보기 */
        span.st-emotion-cache-pkbazv.e11k5jya0 > div[data-testid="stMarkdownContainer"] p {
        text-decoration: underline;
        }
                
        /* 토글 기사 제목 */ 
        span.st-emotion-cache-1dtefog.enj44ev2 div[data-testid="stMarkdownContainer"] p {
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
    

    image_path = os.path.join(os.path.dirname(__file__), "images", "nnews.png")
    st.image(image_path)
    st.header('최신 뉴스 토픽', ) 
    st.markdown(
        f"""
        <div style="text-align: right; font-size: 20px;">
            Today: {formatted_today}
        </div>
        """,
        unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        section = st.selectbox("테마", section_list)  # Section 선택

    with col2:
        topic_num = st.selectbox("토픽 수", [i for i in range(1, 6)])  # Topic 수 선택
    
    with col3:
        st.write('')
    
    with col4:
        st.write('')



    if st.button("분석 시작"):
        with st.spinner('로딩중...'):
            # 로딩 작업 수행
            news_data, images = make_lda_wc(section,topic_num)  # images는 로컬 파일 경로 리스트
            
            # 워드클라우드와 기사 표시
            for idx, (topic, img) in enumerate(zip(news_data.values(), images)):
                # 워드클라우드 표시
                st.image(img, use_container_width=True)

                # 기사 표시
                st.subheader(f'Topic {idx + 1} 관련기사')
                for j in range(5):
                    article = topic[j]
                    with st.expander(list(article.values())[0]['title']):
                        st.write(list(article.values())[0]['body'])

  
            a = st.success('완료')
            time.sleep(1)
            a.empty()
            
            st.page_link(f"https://news.naver.com/section/{section_dict[section]}", label=f"{section}기사 보러 가기", icon='📰')


    if __name__ == "__news_crawling__":
        render_page(change_page)