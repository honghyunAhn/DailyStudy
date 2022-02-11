import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np

X = tf.placeholder(tf.float32, shape=[None, 10])
Y = tf.placeholder(tf.float32, shape=[None, 1])
W = tf.Variable(tf.random_normal([10,1]), name="weight")
b = tf.Variable(tf.random_normal([1]), name="bias")

hypothesis = tf.matmul(X,W) + b

saver = tf.train.Saver()
model = tf.global_variables_initializer()

emotion = float(input("정서: "))
autonomous = float(input("자율: "))
motivation = float(input("학습동기: "))
time_management = float(input("시간관리: "))
concentration = float(input("집중력: "))
reading = float(input("독서능력: "))
memorize = float(input("암기능력: "))
test_management = float(input("시험관리: "))
taking_note = float(input("노트필기: "))
focus = float(input("수업집중: "))

with tf.Session() as sess:
    sess.run(model)
    
    save_path = "./saved_eduvil_predict.cpkt"
    saver.restore(sess, save_path)
    
    data = ((emotion, autonomous, motivation, time_management, concentration, reading, memorize, test_management, taking_note, focus),)
    arr = np.array(data, dtype=np.float32)
    
    x_data = arr[0:10]
    dict = sess.run(hypothesis, feed_dict={X: x_data})
    print(dict[0])