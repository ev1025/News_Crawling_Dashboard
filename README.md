# 네이버 뉴스와 수치형 데이터 시각화를 활용한 Streamlit 대시보드
#### 프로젝트 설명
사용자가 네이버 뉴스를 크롤링하여 특정 카테고리의 토픽을 분석하고 이를 워드 클라우드 형태로 시각화하는 동시에 수치형 데이터를 활용한 시각화를 통해 직관적이고 효율적인 데이터 분석 경험을 제공하는 Streamlit 기반 대시보드 애플리케이션을 제작하는 것을 목표로 함

## 데이터 소개
#### 1. 네이버 뉴스
url : https://news.naver.com/section/100
#### 1. 코스피, 코스닥
최근 1년(2024-01-14 ~ 2025-01-14)간의 코스피, 코스닥 지수 데이터(csv) 다운로드

columns : 날짜, 종가, 시가, 고가, 저가, 거래량, 변동 %
- 코스피 : https://kr.investing.com/indices/kospi-historical-data
- 코스닥 : https://kr.investing.com/indices/kospi-historical-data
  
#### 2. 네이버페이 증권
url : https://m.stock.naver.com/domestic/capitalization/KOSPI
시가총액 1,2,3순위(삼성전자, SK 하이닉스, LG 에너지솔루션)의 주가 크롤링 데이터(json)
- 삼성 전자 : https://m.stock.naver.com/fchart/domestic/stock/005930
- SK 하이닉스 : https://m.stock.naver.com/fchart/domestic/stock/000660
- LG 에너지솔루션 : https://m.stock.naver.com/fchart/domestic/stock/373220
columns : localDate, openPrice, closePrice, highPrice, lowPrice, accumulatedTradingVolume, foreignRetentionRate

## 데이터 전처리
- 날짜를 datetime 형식으로 변환
- 종가를 float으로 데이터 변환
- 시가 총액 1,2,3순위의 json 파일을 데이터프레임 형태로 변환
- 

### 3. 기술 스택
- Frontend : Streamlit
- Backend : Pyhton(BeautifulSoup, pandas, matplotlib, seaborn, requests)
  - 데이터 분석 : pandas, nltk, genism의 LDA
  - 데이터 시각화 : Word Cloud, Matplotlib, Plotly, seaborn, 


## 데이터 분석
### 1. 데이터 분석
1) 네이버 뉴스 크롤링 및 토픽 모델링
- 사용자가 정치, 경제, 사회, 생활/문화, 과학, 세계 카테고리 중 하나를 선택하면 해당 카테고리의 최신 기사를 BeautifulSoup로 크롤링
- 불용어 처리 : RegexpTokenizer를 사용하여 텍스트 정제 및 불용어 처리
- genism의 LDA 모델을 활용하여 토픽 모델링을 수행
- 토픽 모델링 결과를 wordcloud로 시각화
2) 수치형 데이터 크롤링 및 시각화
- 삼성전자, SK 하이닉스, LG 에너지 솔루션의 최신 1년의 주가 데이터 크롤링
- 
### 2. Streamlit


