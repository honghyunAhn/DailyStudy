import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Pandas의 Dataframe을 생성합니다.
names = ['Bob', 'jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]
custom = [1, 5, 25, 13, 23232]

BabyDataSet = list(zip(names, births))  # list가 여러개로 나눠져 있을때 list를 세로로 묶어준다
df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

df.head()  # 정의한 df를 출력합니다.

# 데이터 프레임의 열 타입 정보를 출력합니다.
print(df.dtypes)
print("-----------------------")

# 데이터프레임의 형태 정보입니다.
print(df.index)
print("-----------------------")

# 데이터프레임의 열 정보입니다.
print(df.columns)

df['Names']  # 데이터프레임의 하나의 열을 선택합니다.

df[0:3]  # 0-3 번째 인덱스를 선택합니다.

df[df['Births'] > 100].head(2)  # Births 열이 100보다 큰 데이터를 선택합니다. 상위 2개만 봅니다.

df.mean()  # 데이터프레임에서의 평균값을 계산합니다.

df.describe()  # 통계정보를 요약해서 출력


arr1 = np.arange(15).reshape(3, 5)  # 15개의 값을 3행 5열로 만듦.
print(arr1)

np.arange(10)

arr1.shape  # arr1의 차원을 출력합니다.

arr3 = np.zeros((3, 4))  # 0을 출력
print(arr3)
print("---------------")
arr4 = np.ones((3, 4))  # 1을 출력
print(arr4)

arr5 = np.array([
    [1, 2, 3],
    [4, 5, 6]
], dtype=np.float64)

arr6 = np.array([
    [7, 8, 9],
    [10, 11, 12]
], dtype=np.float64)

# 사칙연산을 출력합니다.
print("arr5 + arr6 = ")
print(arr5 + arr6, "\n")
print("arr5 - arr6 = ")
print(arr5 - arr6, "\n")
print("arr5 * arr6 = ")
print(arr5 * arr6, "\n")
print("arr5 / arr6 = ")
print(arr5 / arr6, "\n")

y = df['Births']
x = df['Names']

print(x)
print(y)

# bar plot을 출력합니다.
plt.bar(x, y)  # --> 막대그래프 객체 생성
plt.xlabel('Names')  # --> x축 제목
plt.ylabel('Births')  # --> y축 제목
plt.title('Bar plot')  # --> 그래프 제목
plt.show()  # --> 그래프 출력

# 랜덤 추출 시드를 고정합니다.
np.random.seed(19920613)

# scatter plot 데이터를 생성합니다.
x = np.arange(0.0, 100.0, 5.0)
y = (x * 1.5) + np.random.rand(20) * 50

# scatter plot을 출력합니다.
plt.scatter(x, y, c="b", alpha=0.5, label="scatter point")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(loc='upper left')
plt.title('Scatter plot')
plt.show()
