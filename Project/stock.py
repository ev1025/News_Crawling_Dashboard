import streamlit as st
import pandas as pd
import numpy as np
# 주식 받은 파일 라이브러리
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates

# 시스템 기본 한글 폰트 설정
mpl.rcParams['font.family'] = 'AppleGothic'
mpl.rcParams['axes.unicode_minus'] = False  # 음수 기호가 깨지지 않도록 설정

# 세션 상태로 현재 페이지 저장
if "page" not in st.session_state:
    st.session_state.page = "stock"

# 랜더 오류
def render_page(change_page):
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
    ddv_df = pd.read_csv("./csv/merged.csv")
    # 데이터프레임을 화면에 표시
    st.dataframe(ddv_df)
    
    # 주식 & 수익률차트 탭
    st.title("주식 & 수익률차트")
    # 탭 생성
    tab1, tab2 = st.tabs(["주식 차트", "수익률 차트"])

    # 파일 읽기
    try:
        df = pd.read_csv("./csv/merged.csv")
    except ValueError as e:
        st.error(f"파일을 읽는 중 오류가 발생했습니다: {e}")
        return  # 오류 발생 시 함수 종료
    except FileNotFoundError:
        st.error("지정한 경로에 파일이 존재하지 않습니다.")
        return  # 오류 발생 시 함수 종료

    # 'localDate' 열을 datetime 형식으로 변환
    df['localDate'] = pd.to_datetime(df['localDate'], errors='coerce')

    # 탭 1: 주식 차트
    with tab1:
        # 회사 선택 및 날짜 입력
        st.title("Stock Chart")
        company = st.selectbox("Select Company", ["Samsung", "SK hynix", "LG ensol"], key="stock_company")
        ticker = {"Samsung": "Samsung", "SK hynix": "SK hynix", "LG ensol": "LG ensol"}[company]
        st.markdown('^마크다운^')
        start_date = st.date_input("시작 날짜: ", value=pd.to_datetime("2023-01-01"), key="stock_start_date")
        end_date = st.date_input("종료 날짜: ", value=pd.to_datetime("2025-01-01"), key="stock_end_date")
        
        # 선택한 회사에 해당하는 데이터만 필터링
        company_df = df[df['Company'] == ticker]

        if company_df.empty:
            st.warning(f"{company}에 대한 데이터가 없습니다.")
            return

        st.dataframe(company_df, use_container_width=True)  # 선택한 회사의 데이터 출력

        # 날짜 부분만 추출하여 새로운 열에 저장
        company_df['localDate'] = company_df['localDate'].dt.date
        
        # 'localDate'를 'YYYY-MM' 형식으로 변환
        monthly_data = company_df.copy()  # monthly_data를 초기화
        monthly_data['localDate'] = pd.to_datetime(monthly_data['localDate'])
        monthly_data['localDate'] = monthly_data['localDate'].dt.strftime('%Y-%m')
        
        # Line Chart, Candle Stick 선택형으로 만들기
        chart_type = st.radio("Select Chart Type", ("Candle_Stick", "Line"), key="stock_chart_type")
        candlestick = go.Candlestick(x=company_df['localDate'], open=company_df['openPrice'], high=company_df['highPrice'], low=company_df['lowPrice'], close=company_df['closePrice'])
        line = go.Scatter(x=company_df['localDate'], y=company_df['closePrice'], mode='lines', name='Close')

        if chart_type == "Candle_Stick":
            fig = go.Figure(candlestick)
        elif chart_type == "Line":
            fig = go.Figure(line)
        else:
            st.error("error")

        fig.update_layout(title=f"{company} {chart_type} Chart", xaxis_title="Date", yaxis_title="Price")
        st.plotly_chart(fig)

    # 탭 2: 수익률 차트
    with tab2:
        # 회사 선택 및 날짜 입력
        st.title("Return Chart")
        company = st.selectbox("Select Company", ["Samsung", "SK hynix", "LG ensol"], key="return_company")
        ticker = {"Samsung": "Samsung", "SK hynix": "SK hynix", "LG ensol": "LG ensol"}[company]
        
        # 선택한 회사에 해당하는 데이터만 필터링
        company_df = df[df['Company'] == ticker]  

        # 월별 첫 날과 마지막 날의 데이터 추출
        company_df.set_index('localDate', inplace=True)
        monthly_data = company_df.resample('M').agg({'openPrice': 'first', 'closePrice': 'last', 'highPrice': 'max', 'lowPrice': 'min'}).reset_index()

        # 수익률 계산
        monthly_data['Return'] = ((monthly_data['closePrice'] - monthly_data['openPrice']) / monthly_data['openPrice'] * 100).round(2).astype(str) + '%'
        monthly_data['Return_Value'] = ((monthly_data['closePrice'] - monthly_data['openPrice']) / monthly_data['openPrice'] * 100).round(2)  # 수익률 값만 저장

        # 'localDate'를 'YYYY-MM' 형식으로 변환
        monthly_data['localDate'] = monthly_data['localDate'].dt.strftime('%Y-%m')
        
        # 데이터프레임 출력
        st.dataframe(monthly_data[['openPrice', 'closePrice', 'Return']], use_container_width=True)

        # Line Chart, Candle Stick 선택형으로 만들기
        chart_type = st.radio("Select Chart Type", ("Candle_Stick", "Line"), key="return_chart_type")
        
        # 수익률을 y축으로 사용하는 차트 생성
        if chart_type == "Candle_Stick":
            candlestick = go.Candlestick(
                x=monthly_data['localDate'],
                open=monthly_data['openPrice'],
                high=monthly_data['highPrice'],  # 고가
                low=monthly_data['lowPrice'],     # 저가
                close=monthly_data['closePrice']
            )
            fig = go.Figure(candlestick)
        elif chart_type == "Line":
            line = go.Scatter(x=monthly_data['localDate'], y=monthly_data['Return_Value'], mode='lines', name='Return')
            fig = go.Figure(line)
        else:
            st.error("error")

        fig.update_layout(title=f"{company} {chart_type} Chart", xaxis_title="Date", yaxis_title="Return (%)")
        st.plotly_chart(fig)

    # 주식차트 
    if __name__ == "__stock__":
        render_page(change_page)
