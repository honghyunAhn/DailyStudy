import matplotlib.pyplot as plt

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
