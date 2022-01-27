import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = './data/drinks.csv'
drinks = pd.read_csv(file_path)  # read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.

print(drinks.info())

drinks.head(10)

drinks.describe()

# 'beer_servings', 'wine_servings' 두 피처간의 상관계수를 계산합니다.
# pearson은 상관계수를 구하는 계산 방법 중 하나를 의미하며, 가장 널리 쓰이는 방법입니다.
corr = drinks[['beer_servings', 'wine_servings']].corr(method='pearson')
print(corr)

# 피처간의 상관계수 행렬을 구합니다.
cols = ['beer_servings', 'spirit_servings',
        'wine_servings', 'total_litres_of_pure_alcohol']
corr = drinks[cols].corr(method='pearson')
print(corr)
