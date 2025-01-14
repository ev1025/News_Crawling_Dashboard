import streamlit as st
import pandas as pd

def render():
    """정치 탭을 렌더링합니다."""
    st.header("정치")
    st.write("여기에 최신 뉴스 기사가 표시됩니다.")
    
    # 예시 뉴스 데이터
    news_data = {
        "제목": ["뉴스 1", "뉴스 2", "뉴스 3"],
        "내용": ["내용 1", "내용 2", "내용 3"]
    }
    news_df = pd.DataFrame(news_data)
    
    for index, row in news_df.iterrows():
        st.subheader(row['제목'])
        st.write(row['내용'])
        st.write("---")