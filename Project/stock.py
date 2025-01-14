import streamlit as st
import pandas as pd
import numpy as np

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "stock"

# stock title
st.title("Stock Dashboard")

# 컬럼으로 영역을 나누어 표기한 경우
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric(label="현재량", value="54,000원", delta="-120원")
col2.metric(label="전일비", value="-100", delta="-7.44원")
col3.metric(label="등락률", value="-0.18%", delta="11.44원")
col4.metric(label="거래량", value="6,219,363", delta="11.44")
col5.metric(label="시가", value="54,200원", delta="11.44원")

# 구분선 생성
st.divider()

# data extraction title
st.title("Data Extraction")

# 주식 data
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# detalied data view title
st.title("Detalied Data View")

# 주식 data 로드
# CSV 파일을 데이터프레임으로 읽기
ddv_df = pd.read_csv("./sample1.csv")
# 데이터프레임을 화면에 표시
st.dataframe(ddv_df)