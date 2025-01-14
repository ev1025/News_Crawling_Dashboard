import requests
from bs4 import BeautifulSoup
import re

'''
start_crawling를 import하여
start_crawling('원하는 토픽')을 입력하면 크롤링 됩니다.

크롤링 순서 : 각 페이지별로 next(다음 페이지의 커서 값)이 존재합니다. 
해당 next값을 모두 수집 후 페이지별 next값을 페이지번호와 매칭시키면 
해당 페이지의 정보를 얻을 수 있습니다.

토픽 종류 : '정치','경제', '사회','생활/문화','IT/과학','세계'

'''


# 넥스트값 추출
def next_get(sid, base_url, headers, page_num):
    # 첫 넥스트 값 받기
    response = requests.get(base_url, headers=headers)
    data = response.json()['renderedComponent']['SECTION_ARTICLE_LIST']
    soup = BeautifulSoup(data, 'html.parser')
    page = soup.select_one('div.section_latest_article._CONTENT_LIST._PERSIST_META')
    next = page['data-cursor']
    next_list = []
    next_list.append(next)
    
    # 나머지 값 받기
    for i in range(1,page_num):
        next_url = f'https://news.naver.com/section/template/SECTION_ARTICLE_LIST?sid={sid}&sid2=&cluid=&pageNo={i}&date=&next={next}&_='
        next_response = requests.get(next_url, headers=headers)
        next_data = next_response.json()['renderedComponent']['SECTION_ARTICLE_LIST']
        next_soup = BeautifulSoup(next_data, 'html.parser')
        next_page = next_soup.select_one('div.section_latest_article._CONTENT_LIST._PERSIST_META')

        # 넥스트 수집
        next = next_page['data-cursor']
        next_list.append(next)

    return page, next_list


# 사이트값 추출
def get_site(sid, page, next_list, headers, page_num):
    site_list = []
    site_list.extend([ j.get('href') for j in page.select('a.sa_thumb_link')])

    for num in range(1,page_num):
        data_url = f'https://news.naver.com/section/template/SECTION_ARTICLE_LIST?sid={sid}&sid2=&cluid=&pageNo={num}&date=&next={next_list[num]}&_='
        response = requests.get(data_url, headers=headers)
        data = response.json()['renderedComponent']['SECTION_ARTICLE_LIST']
        soup = BeautifulSoup(data, 'html.parser')
        site_page = soup.select_one('div.section_latest_article._CONTENT_LIST._PERSIST_META')
        
        site_list.extend([ j.get('href') for j in site_page.select('a.sa_thumb_link')])

    return site_list


# 제목, 본문 뽑기
def get_title_body(news):
    title = news.select_one('div.media_end_head_title h2#title_area')
    #title = title.text.strip() if title else "제목 없음"
    #print(title.text)
    body = news.select_one('article#dic_area')
    #print(body)
    # 사진 설명 모두 제거
    for caption in body.find_all('span.end_photo_org'): # table.nbd_table
        caption.decompose()
    for caption in body.find_all('em'):
        caption.decompose()
    for caption in body.find_all('td'):
        caption.decompose()
    # 본문 텍스트 추출
    body = body.get_text().strip()
    body = re.sub(r"\s+(?!\S)", "", body)  # 연속된 공백은 제거하되, 공백 자체는 남겨둠
    news_dict = { 'title':title.text, 'body':body}
    return news_dict


# 제목, 본문 딕트에 받기
def get_body(site_list, headers, body_list):

    for site in site_list:
        response_body = requests.get(site, headers)
        soup_body = BeautifulSoup(response_body.text, 'html.parser')
        body = get_title_body(soup_body)
        body_list.append(body)


def start_crawling(topic):
    sid_list = [100,101,102,103,104,105]
    section_list = ['정치','경제', '사회','생활/문화','IT/과학','세계']
    section_dict = dict(zip(section_list, sid_list))

    page_num = 2

    # 제목, 본문 리스트
    body_list = []

    # '정치'에 select된 값 넣으면 됨
    sid = section_dict[topic]

    base_url = f'https://news.naver.com/section/template/SECTION_ARTICLE_LIST?sid={sid}&sid2=&cluid=&pageNo=0&date=&next=&_='
    headers = {'User-Agent': 
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}

    # 각 함수 불러오기
    page, next_list = next_get(sid, base_url, headers, page_num)
    site_list = get_site( sid, page, next_list, headers, page_num)
    get_body(site_list, headers, body_list)

    return body_list

