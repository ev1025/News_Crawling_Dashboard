# 네이버 뉴스와 수치형 데이터 시각화를 활용한 Streamlit 대시보드
#### 프로젝트 소개
사용자가 네이버 뉴스를 크롤링하여 특정 카테고리의 토픽을 분석하고 이를 워드 클라우드 형태로 시각화하는 동시에 수치형 데이터를 활용한 시각화를 통해 직관적이고 효율적인 데이터 분석 경험을 제공하는 Streamlit 기반 대시보드 애플리케이션을 제작
### 폴더 구조
```
│  .DS_Store
│  .gitignore
│  README.md
│  requirements.txt
│  
└─Project
    │  app.py
    │  home.py
    │  news_crawling.py
    │  stock.py
    │  
    ├─csv
    │      kosdaq.csv
    │      kospi.csv
    │      merged.csv
    │      pop_stock.csv
    │      sample1.csv
    │      
    ├─Fonts
    │      NanumGothicBold.ttf
    │      
    ├─images
    │      nnews.png
    │      stock_img.jpg
    │      jamie-street-Zqy-x7K5Qcg-unsplash.jpg
    │      
    ├─modules
    │  │  crawler.py
    │  │  lda_wc_maker.py
    │  │  
    │  └─__pycache__
    │          crawler.cpython-38.pyc
    │          lda_wc_maker.cpython-38.pyc
    │          lda_wc_maker.cpython-39.pyc
    │          st_wordcloud.cpython-38.pyc
    │          
    ├─text
       └─ stopwords.txt
 
```

## 데이터 소개
#### 1. 네이버 뉴스
url : https://news.naver.com/section/100
#### 2. 코스피, 코스닥
최근 1년(2024-01-14 ~ 2025-01-14)간의 코스피, 코스닥 지수 데이터(csv)

columns : 날짜, 종가, 시가, 고가, 저가, 거래량, 변동 %
- 코스피 : https://kr.investing.com/indices/kospi-historical-data
- 코스닥 : https://kr.investing.com/indices/kospi-historical-data
  
#### 3. 네이버페이 증권
url : https://m.stock.naver.com/domestic/capitalization/KOSPI

시가총액 1,2,3순위(삼성전자, SK 하이닉스, LG 에너지솔루션)의 주가 크롤링 데이터(json)
- 삼성 전자 : https://m.stock.naver.com/fchart/domestic/stock/005930
- SK 하이닉스 : https://m.stock.naver.com/fchart/domestic/stock/000660
- LG 에너지솔루션 : https://m.stock.naver.com/fchart/domestic/stock/373220
  
columns : localDate, openPrice, closePrice, highPrice, lowPrice, accumulatedTradingVolume, foreignRetentionRate

## 기술 스택
- Frontend : Streamlit
- Backend : Pyhton(BeautifulSoup, pandas, matplotlib, seaborn, requests)
  - 데이터 분석 : pandas, nltk, genism - LDA
  - 데이터 시각화 : Word Cloud, Matplotlib, Plotly, seaborn, 

## 주요 기능
1. 네이버 뉴스 크롤링 및 토픽 모델링
네이버 뉴스 크롤링 및 토픽 모델링
- 사용자가 정치, 경제, 사회, 생활/문화, 과학, 세계 카테고리 중 하나를 선택하면 해당 카테고리의 최신 기사를 BeautifulSoup로 크롤링
- 불용어 처리 : RegexpTokenizer를 사용하여 텍스트 정제 및 불용어 처리
- genism의 LDA 모델을 활용하여 토픽 모델링을 수행
- 토픽 모델링 결과를 wordcloud로 시각화
2. 수치형 데이터 시각화
- 삼성전자, SK 하이닉스, LG 에너지 솔루션의 최신 1년의 주식 데이터를 크롤링하여 시각화를 진행하고 유의미한 정보 제공
- 코스피/코스닥 지수 데이터를 사용하여 시각화를 진행하고 유의미한 정보 제공
- 시각화 자료로 3사의 종가 데이터 비교 및 최신 주가 데이터의 변동을 확인할 수 있음
3. Streamlit 대시보드
- 사용자 친화적인 인터페이스 제공
- Candlestick Chart와 line plot을 통한 데이터 시각화
- Candlestick Chart로 날짜를 조절하여 원하는 기간동안의 데이터만 확인 가능

## 데이터 전처리
- 날짜를 datetime 형식으로 변환
- 종가를 float으로 데이터 변환
- 시가 총액 1,2,3순위의 json 파일을 데이터프레임 형태로 변환
  

## Streamlit
사이드 바로 페이지 선택 가능
1) 홈 화면
   - 사진 추가
2) 뉴스 크롤링 화면
   - select box로 정치, 경제, 사회, 생활/문화, 과학, 세계 카테고리 중 하나를 선택
   - 선택된 카테고리의 뉴스 크롤링 데이터를 활용하여 WordCloud 시각화 자료 생성
     -> 각 카테고리 별로 자주 언급되는 단어를 확인할 수 있음
     
     <img width="485" alt="image" src="https://github.com/user-attachments/assets/a5e0302f-db79-4a10-ab04-a0016414e6f6" />

   - 선택된 카테고리의 최신 뉴스를 예시로 5개 보여줌
     
     ![image](https://github.com/user-attachments/assets/0aa58720-2897-4347-856d-f8ff87fe68a0)

   - 워드 클라우드에 호버 기능 추가

3) 수치 데이터 시각화 화면
  - 주식 & 수익률 차트
    - 라디오 버튼으로 3사 중 하나를 선택하여 종가 데이터의 Candlestick Chart와 line plot을 선택하여 볼 수 있음(시작/종료 날짜 선택 가능)
    - 3사의 데이터 프레임 내용(종가/시가/고가/저가 등) 확인 가능
    - 수익률 탭에서 시가와 종가의 차이를 데이터 프레임 형태로 확인할 수 있음
      -> 3사의 종가 데이터 비교 및 최신 주가 데이터의 변동을 확인할 수 있음
  <img width="539" alt="image" src="https://github.com/user-attachments/assets/67cfe0f5-0121-496b-a849-a1d9b0271b12" />

  - 코스피 / 코스닥 지수 차트
    - 라디오 버튼으로 코스피/코스닥 지수 데이터 Candlestick Chart와 line plot을 선택하여 볼 수 있음
    - 코스피 지수와 코스닥 지수 비교 가능
    - Candlestick Chart로 날짜를 조절하여 원하는 기간동안의 데이터만 확인 가능
      ![newplot](https://github.com/user-attachments/assets/8814d0db-fc64-4340-90b9-96f352550ed9)

