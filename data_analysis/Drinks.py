import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = './data/drinks.csv'
drinks = pd.read_csv(file_path)  # read_csv 함수로 데이터를 Dataframe 형태로 불러옵니다.

print(drinks.info())

drinks.head(10)

drinks.describe()
