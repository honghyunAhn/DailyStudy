import tensorflow as tf

tensor = tf.constant(3) #정수만 입력가능

tensor1 = tf.constant( [3.0,4,5] ) #list로 만들 수 있음 3.0으로 정의하면 float형이 된다
tensor2 = tf.constant( [6,7,8], tf.float32) #강제로 float형으로 형변환

print(tensor1 + tensor2) #텐서끼리 한번에 더하기 가능

tensor3 = tf.constant( [ [3,4], 
                        [2,1] ]  ) #텐서로 행렬 표현 가능
tensor4 = tf.constant( [ [1,5], 
                        [3,7] ]  )

print("행렬의 더하기")
print(tf.add(tensor1, tensor2)) #tensorflow의 더하기 함수

print("행렬의 곱")
print(tf.matmul(tensor3, tensor4))

tensor5 = tf.zeros([4,2,3]) #데이터를 많이 담고 싶지만 아직 어떤 데이터를 넣을지 모를때 사용 0만 담긴 텐서를 만들어줌
print(tensor5) #3열 2행인 행렬을 4개 만들어준다

print("\ntensor5의 차원")
print(tensor5.shape)

w = tf.Variable(1.0) #딥러닝의 weight 정의(변수) / tf.constant() -> 상수
print(w)
w.assign(2) #w변수의 값을 2로 변경
print(w)
