import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

# xData = [73.6, 85.4, 77.9, 68.4, 60.7, 66] # 3D평균
# yData = [2.5, 5.25, 1.75, 4.38, 3, 2] # 학종 내신
xData = [1,2,3,4,5,6,7]
yData = [25000,55000,75000,110000,128000,155000,180000]

W = tf.Variable(tf.random_uniform([1], -100, 100))
b = tf.Variable(tf.random_uniform([1], -100, 100))
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

H = W * X + b

cost = tf.reduce_mean(tf.square(H - Y))
a = tf.Variable(0.01)
optimizer = tf.train.GradientDescentOptimizer(a)
train = optimizer.minimize(cost)
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)
for i in range(5001):
    sess.run(train, feed_dict={X: xData, Y: yData})
    if i % 500 == 0:
        print(i, sess.run(cost, feed_dict={X: xData, Y: yData}), sess.run(W), sess.run(b))
result = sess.run(H, feed_dict={X: 8})
print(result)