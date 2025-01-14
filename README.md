# News_Crawling_Dashboard

# 데이터 소개
1. 코스피, 코스닥 데이터
최근 1년(2024-01-14 ~ 2025-01-14)간의 코스피, 코스닥 지수 데이터(csv) 다운로드
columns : 날짜, 종가, 시가, 고가, 저가, 거래량, 변동 %
- 코스피 : https://kr.investing.com/indices/kospi-historical-data
- 코스닥 : https://kr.investing.com/indices/kospi-historical-data
  
2. 네이버페이 증권 : https://m.stock.naver.com/domestic/capitalization/KOSPI
시가총액 1,2,3순위(삼성전자, SK 하이닉스, LG 에너지솔루션)의 주식 일별 크롤링 데이터
- 삼성 전자 : https://m.stock.naver.com/fchart/domestic/stock/005930
- SK 하이닉스 : https://m.stock.naver.com/fchart/domestic/stock/000660
- LG 에너지솔루션 : https://m.stock.naver.com/fchart/domestic/stock/373220
columns : localDate, openPrice, closePrice, highPrice, lowPrice, accumulatedTradingVolume, foreignRetentionRate



# 데이터 전처리
- 날짜를 datetime 형식으로 변환
- 종가를 float으로 데이터 변환
- 시가 총액 1,2,3순위의 json 파일을 데이터프레임 형태로 변환
- 
- 
