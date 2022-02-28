from collections import Counter
from konlpy.tag import Okt
import re
import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")


# 발급 완료된 키를 {your_key} 대신 입력합니다.
CONSUMER_KEY = "#"
CONSUMER_SECRET = "#"
ACCESS_TOKEN_KEY = "#"
ACCESS_TOKEN_SECRET = "#"

# 개인정보 인증을 요청하는 Handler입니다.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

# 인증 요청을 수행합니다.
auth.set_access_token(ACCESS_TOKEN_KEY, ACCESS_TOKEN_SECRET)

# twitter API를 사용하기 위한 준비입니다.
api = tweepy.API(auth)

keyword = "베이징"
tweets = api.search_tweets(keyword)
for tweet in tweets:
    print(tweet.text)
    print(tweet.entities['user_mentions'])
    print(tweet.entities['hashtags'])
    print(tweet.created_at)

# 크롤링된 데이터를 저장할 데이터 프레임입니다.
columns = ['created', 'tweet_text']
df = pd.DataFrame(columns=columns)

# 크롤링을 수행할 갯수를 입력하고,Cursor 객체를 사용하여 크롤링을 수행합니다.
max_tweets = 1000
searched_tweets = [status for status in tweepy.Cursor(
    api.search_tweets, q=keyword).items(max_tweets)]

# '베이징'이 포함된 1000개의 트윗들에서, 'text', 'created_at' 정보를 데이터 프레임으로 저장합니다.
for tweet in searched_tweets:
    tweet_json = tweet._json
    tweet_text = tweet_json['text']
    created = tweet_json['created_at']
    row = [created, tweet_text]
    series = pd.Series(row, index=df.columns)
    df = df.append(series, ignore_index=True)
df.to_csv("tweet_temp.csv", index=False)

df = pd.read_csv("tweet_temp.csv")
df.head()


# 텍스트 정제 함수 : 한글 이외의 문자는 전부 제거합니다.

def text_cleaning(text):
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')  # 한글의 정규표현식을 나타냅니다.
    result = hangul.sub('', text)
    return result


# 'tweet_text' 피처에 이를 적용합니다.
df['ko_text'] = df['tweet_text'].apply(lambda x: text_cleaning(x))
df.head()


# 한국어 약식 불용어 사전 예시 파일입니다. 출처 - (https://www.ranks.nl/stopwords/korean)
korean_stopwords_path = "./data/korean_stopwords.txt"
with open(korean_stopwords_path, encoding='utf8') as f:
    stopwords = f.readlines()
stopwords = [x.strip() for x in stopwords]


def get_nouns(x):
    nouns_tagger = Okt()
    nouns = nouns_tagger.nouns(x)

    # 한글자 키워드를 제가합니다.
    nouns = [noun for noun in nouns if len(noun) > 1]

    # 불용어를 제거합니다.
    nouns = [noun for noun in nouns if noun not in stopwords]

    return nouns


# 'ko_text' 피처에 이를 적용합니다.
df['nouns'] = df['ko_text'].apply(lambda x: get_nouns(x))
print(df.shape)
df.head()
