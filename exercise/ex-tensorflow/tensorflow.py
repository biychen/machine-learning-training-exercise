import tensorflow as tf
import random
import matplotlib.pyplot as plt

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)

# training data
K = random.randint(-10, 10)
Y0 = random.randint(-10, 10)
x_train = [i for i in range(10)]
y_train = [K * x + Y0 + random.normalvariate(mu=0, sigma=1) for x in x_train]

# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong
for i in range(1000):
  sess.run(train, {x: x_train, y: y_train})

# evaluate training accuracy
curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
print("K: %s Y0: %s" % (K, Y0))
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
print(x_train)
print(y_train)

fig=plt.figure(figsize=(10, 10), dpi=80, facecolor='w', edgecolor='k')
plt.plot(x_train, y_train, "o", alpha=0.75)
x0, xn = min(x_train), max(x_train)
y0, yn = map(lambda x: K * x + Y0, (x0, xn))
yy0, yyn = map(lambda x: curr_W[0] * x + curr_b[0], (x0, xn))
plt.plot([x0, xn], [y0, yn], 'g--')
plt.plot([x0, xn], [yy0, yyn], 'k--')
plt.show()