import streamlit as st
import pandas as pd
import numpy as np
# 주식 받은 파일 라이브러리
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import matplotlib as mpl
import matplotlib.dates as mdates
from plotly.subplots import make_subplots

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

    # CSV 파일 불러오기
    df = pd.read_csv('./csv/pop_stock_change.csv') 

    # 1순위부터 100순위까지 데이터 선택
    top_100_stocks = df.head(100)

    # 종목명 선택 셀렉트 박스 추가
    stock_names = top_100_stocks['종목명'].tolist() 
    selected_stock = st.selectbox("종목을 선택하세요:", stock_names)

    # 선택한 종목의 데이터 필터링
    selected_row = top_100_stocks[top_100_stocks['종목명'] == selected_stock]

    # 선택된 종목의 데이터가 있을 경우 표시
    if not selected_row.empty:
        row = selected_row.iloc[0]  # 첫 번째 행 선택
        
        # 컬럼으로 영역을 나누어 표기
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.metric(label="현재가", value=f"{row['현재가']}원", delta=row['전일비'])  # delta는 전일비로 수정
        col2.metric(label="전일비", value=row['전일비'], delta=row['전일비'])  # delta는 전일비 변화로 수정
        col3.metric(label="등락률", value=row['등락률'], delta=row['등락률'])  # delta는 등락률 변화로 수정
        col4.metric(label="거래량", value=row['거래량'], delta=row['거래량'])  # delta는 거래량 변화로 수정
        col5.metric(label="시가", value=f"{row['시가']}원", delta=row['시가'])  # delta는 시가 변화로 수정

    # 구분선 생성
    st.divider()

    # data extraction title
    kospi = pd.read_csv('./csv/kospi.csv')
    kosdaq = pd.read_csv('./csv/kosdaq.csv')


    kospi['날짜'] = pd.to_datetime(kospi['날짜'])

    def num(x):
        return float(x.replace(',',''))
    kospi['종가'] = [num(i) for i in kospi['종가']]
    kospi['시가'] = [num(i) for i in kospi['시가']]
    kospi['고가'] = [num(i) for i in kospi['고가']]
    kospi['저가'] = [num(i) for i in kospi['저가']]


    # 컨테이너 : 화면의 일정 영역 -> 웹 브라우저 화면을 컨테이너로 사용
    # st.dataframe(kospi, use_container_width=False)
    # st.dataframe(kosdaq, use_container_width=False)

    # 4. Plotly 이중 축 그래프 객체 생성
    fig = make_subplots(specs=[[{"secondary_y": True}]])

   # selectbox 사용 (수평 선택 가능)
    chart_type = st.selectbox("Select Chart Type", ("Candle_Stick", "Line"))

    # 선택된 차트 타입에 따라 다른 내용을 표시
    if chart_type == "Candle_Stick":
        st.write("Candle Stick 차트를 선택했습니다.")
        # 여기에 Candle Stick 차트 관련 코드 추가
    else:
        st.write("Line 차트를 선택했습니다.")
    # 여기에 Line 차트 관련 코드 추가
    
    # 4. Plotly 이중 축 그래프 객체 생성
    fig = make_subplots(specs=[[{"secondary_y": True}]])

    if chart_type == "Candle_Stick":
        # Kospi 캔들스틱 추가
        fig.add_trace(go.Candlestick(
            x=pd.to_datetime(kospi['날짜']),
            open=kospi["시가"],
            high=kospi["고가"],
            low=kospi["저가"],
            close=kospi["종가"],
            name='Kospi',
            increasing_line_color='#EA6F76',  # 상승 색상
            decreasing_line_color='#EA6F76'  # 하락 색상
        ))

        # Kosdaq 캔들스틱 추가 (이중 축)
        fig.add_trace(go.Candlestick(
            x=pd.to_datetime(kosdaq['날짜']),
            open=kosdaq["시가"],
            high=kosdaq["고가"],
            low=kosdaq["저가"],
            close=kosdaq["종가"],
            name='Kosdaq',
            increasing_line_color='#6F96EA',  # 상승 색상
            decreasing_line_color='#6F96EA'  # 하락 색상
        ), secondary_y=True)
        # 6. 레이아웃 설정
        fig.update_layout(
            title="Kospi / Kosdaq",
            title_font_size=18,
            xaxis_title="Date",
            yaxis_title="Kospi Price",
            yaxis2_title="Kosdaq Price",  # 이중 축의 제목 설정
            template="plotly_white",  # Plotly 스타일 설정
            height=800,  # 그래프 높이
            width=1400,  # 그래프 폭
            title_font_family="맑은고딕"
        )

        # 축 범위 및 기타 설정
        fig.update_yaxes(title_text="Kospi Price", secondary_y=False)  # 기본 y축
        fig.update_yaxes(title_text="Kosdaq Price", secondary_y=True)  # 이중 y축

    else:  # Line Chart 선택 시
        # 1. Plotly 이중 축 그래프 객체 생성
        fig = make_subplots(specs=[[{"secondary_y": True}]])

        # Kospi 라인 차트 추가
        fig.add_trace(go.Scatter(
            x=pd.to_datetime(kospi['날짜']),
            y=kospi['종가'],
            mode='lines',
            name='Kospi',
            line=dict(color='#EA6F76')
        ), secondary_y=False)

        # Kosdaq 라인 차트 추가 (이중 축)
        fig.add_trace(go.Scatter(
            x=pd.to_datetime(kosdaq['날짜']),
            y=kosdaq['종가'],
            mode='lines',
            name='Kosdaq',
            line=dict(color='#6F96EA')
        ), secondary_y=True)

        # 레이아웃 설정
        fig.update_layout(
            title="Kospi / Kosdaq Line Chart",
            title_font_size=18,
            xaxis_title="Date",
            yaxis_title="Kospi Price",
            yaxis2_title="Kosdaq Price",  # 이중 축의 제목 설정
            template="plotly_white",
            height=800,
            width=1400,
            title_font_family="맑은고딕"
        )

        # 축 범위 및 기타 설정
        fig.update_yaxes(title_text="Kospi Price", secondary_y=False)  # 기본 y축
        fig.update_yaxes(title_text="Kosdaq Price", secondary_y=True)  # 이중 y축


    # Streamlit에서 그래프 표시
    st.title("Kospi and Kosdaq Chart")
    st.plotly_chart(fig, use_container_width=True)

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