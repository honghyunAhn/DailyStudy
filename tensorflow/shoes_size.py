import tensorflow as tf

heigt = 170
shoes = 260

a = tf.Variable(0.1) 
b = tf.Variable(0.2) #초기값은 아무렇게 정의

def 손실함수():
    예측값 = heigt * a + b
    return tf.square(260 - 예측값) #손실값 = (실제값 - 예측값)^2

opt = tf.keras.optimizers.Adam(learning_rate=0.1) #경사하강법을 도와줌 ()를 비우면 자동으로 지정 ()안에 수동으로 지정도 가능

#opt.minimize(손실함수, var_list=[a,b]) #경사하강 1번 해줌 == a,b를 1번 수정해줌

#반복할 수록 좋은 값이 도출된다
for i in range(300):
    opt.minimize(손실함수, var_list=[a,b])
    print(a.numpy(),b.numpy()) #numpy()를 붙이면 변수에 담긴 숫자만 출력
    
print("완료") #결과를 보면 예측한 신발사이즈 = 키 *1.52 + 1.62