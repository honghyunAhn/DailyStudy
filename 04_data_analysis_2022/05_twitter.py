import tweepy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")


# 발급 완료된 키를 {your_key} 대신 입력합니다.
CONSUMER_KEY = "GjHiCcHz8h439twifLIDmgbSj"
CONSUMER_SECRET = "Sb8hCHeRiEnu1vEryv1anedsKiQNZyLVCjMw1DIhOUbeA0WwAI"
ACCESS_TOKEN_KEY = "1491344148519354372-oANvjTcI4SFXrZa5hWv8uRGJaUBEO3"
ACCESS_TOKEN_SECRET = "ZJjdZw87ISr6hZ38g7SB1fdj8elH86AZoy30YdP3eOOFl"

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
