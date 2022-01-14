from pickletools import optimize
import pandas as pd

data = pd.read_csv('gpascore.csv') #csv 파일을 읽는다.

#print(data.isnull().sum()) #빈칸의 수를 알려준다.
data = data.dropna() #dropna()는 NaN/빈값있는 행을 제거해줌
#data = data.fillna(100) #빈칸에 100을 채워 넣음

#print(data['gpa'].min()) #gpa열의 최저 값을 찾아줌
#print(data['gpa'].count()) #gpa열이 몇개인지 알려줌

y = data['admit'].values
x = []

for i, rows in data.iterrows(): #data라는 데이터프레일을 가로 한줄씩 출력
    #print(rows['gre']) #gre 세로 열에 있는 데이터 출력
    x.append([rows['gre'], rows['gpa'], rows['rank']])

import numpy as np
import tensorflow as tf

model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'), #activation function 넣는법(자주 사용되는 함수 : sigmoid, tanh, relu, softmax, leakyRelu)
    tf.keras.layers.Dense(128, activation='tanh'), #레이어 만드는 법 ()안의 숫자는 node의 갯수, 레이어 갯수 / 노드 갯수는 결과가 잘 나올 때까지 실험으로 파악해야함.
    tf.keras.layers.Dense(1, activation='sigmoid') #결과물이 하나라는 말, sigmoid는 0~1사이의 확률만 압축해서 예측결과 출력
]) #딥러닝 모델 만드는 법

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.fit(np.array(x), np.array(y),epochs=3000) #epochs는 몇번을 학습시킬지 정해준다.

#기복적으로 사용되는 optimizer : adam, adagrad,adaelta, rmsprop, sgd 등

#예측
predict = model.predict([[750, 3.70, 3], [400, 2.2, 1]])
print(predict)