import matplotlib as mpl
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings("ignore")

picher_file_path = './data/picher_stats_2017.csv'
batter_file_path = './data/batter_stats_2017.csv'
picher = pd.read_csv(picher_file_path)
batter = pd.read_csv(batter_file_path)

picher.columns

picher.head()

print(picher.shape)

# 현재 OS 내에 설치된 폰트를 확인합니다.
set(sorted([f.name for f in mpl.font_manager.fontManager.ttflist]))

# 자신의 OS에 존재하는 한글 폰트를 선택합니다. 없는경우, 위의 링크에서 한글폰트 설치 후 실행합니다.
mpl.rc('font', family='NanumGothicOTF')

picher['연봉(2018)'].describe()
picher['연봉(2018)'].hist(bins=100)  # 2018년 연봉 분포를 출력합니다.

picher.boxplot(column=['연봉(2018)'])  # 연봉의 Boxplot을 출력합니다.