'''
maek_lda_wc('섹션')을 입력하면
최신 180개의 기사를 크롤링(crwler.py 모듈 활용)하여
5개의 토픽으로 lda한 뒤, 각 워드 클라우드를 생성하는 코드입니다.
최신 기사의 뉴스 제목과 본문을 리턴합니다.

'''
from nltk.tokenize import RegexpTokenizer
from gensim import corpora, models
from wordcloud import WordCloud
from .crawler import start_crawling
import matplotlib.pyplot as plt
from io import BytesIO
from wordcloud import WordCloud
import matplotlib.pyplot as plt


# section : '정치','경제', '사회','생활/문화','IT/과학','세계'

# LDA 함수
def lda_func(section, num_topics):
    # 뉴스 크롤링
    news_data = start_crawling(section)

    # 불용어 리스트를 파일에서 읽기
    with open('./text/stopwords.txt', 'r', encoding='utf-8') as file:
        stop_words = set(file.read().splitlines())  # 한 줄씩 읽어서 불용어 목록에 저장

    # 텍스트 토크나이저 정의 (한글만 추출하는 정규식)
    tokenizer = RegexpTokenizer(r'[가-힣]+')

    # 전처리 함수
    def preprocess_korean_text(text):
        # 형태소 분석 및 명사 추출
        tokens = tokenizer.tokenize(text)  # 한글만 추출
        # 불용어 제거 및 길이가 1 이하인 단어 제외
        tokens = [word for word in tokens if word not in stop_words and len(word) > 1]
        return tokens

    # 본문 데이터 전처리
    texts = [preprocess_korean_text(article['title'] + " " + article['body']) for article in news_data]

    # 사전(Dictionary) 생성 - 단어와 ID 매핑
    dictionary = corpora.Dictionary(texts) # 각 단어에 id부여 {'단어1': 0(단어1 id), '단어2':1(단어2 id) ....} dictionary.token2id로 확인

    # BOW (Bag of Words) 코퍼스 생성 - 백터화
    corpus = [dictionary.doc2bow(text) for text in texts] # 각 기사별 단어의 빈도수[(단어 id, 빈도수 ), (단어 id, 빈도수)...]

    # LDA 모델 학습
    lda_model = models.LdaModel(corpus,                
                                num_topics=num_topics, # 모델이 학습할 주제 수(뉴스는 10~20개 적절)
                                id2word=dictionary,    # 말뭉치의 단어 id를 실제 단어와 매칭
                                passes=10,             # 학습 횟수
                                random_state=42)
    return lda_model, corpus, news_data


def get_topic__articles(lda_model, corpus, news_data, num_topics):
    topic_articles = {i: [] for i in range(num_topics)}

    # 가장 관련성 높은 토픽 dict에 (토픽관련성 : 기사내용)형식으로 삽입
    for idx, doc in enumerate(corpus):
        topic_distribution = lda_model[doc]
        dominant_topic = max(topic_distribution, key=lambda x: x[1])  # 관련이 높은 토픽과 관련도(토픽id, 관련도)
        topic_articles[dominant_topic[0]].append({dominant_topic[1] : news_data[idx]})
    
    # 관련도 순으로 정렬
    for topic in range(num_topics):
        topic_articles[topic] = sorted(topic_articles[topic], key = lambda x: list(x.keys()), reverse=True)

    return topic_articles


## 전체 데이터 넣고 싶다면 
# all_text = ' '.join([' '.join(text) for text in texts])

# WC 함수
def make_wc(section, num_topics, lda_model):

    plt.rcParams['font.family'] = 'NanumGothicBold'
    plt.rcParams['axes.unicode_minus'] = False

    images = []
    
    for topic_id in range(num_topics):
        topic_terms = lda_model.show_topic(topic_id, topn=20)
        word_weights = {word: weight for word, weight in topic_terms}
        wordcloud = WordCloud(font_path="./Fonts/NanumGothicBold.ttf", 
                              width=800, height=400,
                              colormap='coolwarm', max_words=50, 
                              background_color='white').generate_from_frequencies(word_weights)
        plt.figure(figsize=(10, 6))
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")

        # Save to buffer
        buf = BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        images.append(buf)
        plt.close()
    return images
    

# LDA + 워드클라우드 실행 함수

def make_lda_wc(section, num_topics):
    
    # LDA
    lda_model, corpus, news_data = lda_func(section, num_topics)

    # 워드클라우드 이미지
    images = make_wc(section, num_topics, lda_model)

    # 토픽별 관련도 높은 기사
    topic_articles = get_topic__articles(lda_model, corpus, news_data, num_topics)

    return topic_articles, images