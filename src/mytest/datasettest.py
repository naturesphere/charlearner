import tensorflow as tf

# dataset1 = tf.data.Dataset.from_tensor_slices(tf.random_uniform([4,10]))
# print(dataset1.output_types)
# print(dataset1.output_shapes)

# dataset2 = tf.data.Dataset.from_tensor_slices((tf.random_uniform([4]),
# tf.random_uniform([4,100],maxval=100,dtype=tf.int32)))
# print(dataset2.output_types)
# print(dataset2.output_shapes)

# dataset3 = tf.data.Dataset.zip((dataset1,dataset2))
# print(dataset3.output_types)
# print(dataset3.output_shapes)

# dataset4 = tf.data.Dataset.from_tensor_slices(
# {
#     "a":tf.random_uniform([4]),
#     "b":tf.random_uniform([4,100], maxval=100, dtype=tf.int32)
# })
# print(dataset4.output_types)
# print(dataset4.output_shapes)


# dataset = tf.data.Dataset.range(100)
# iterator = dataset.make_one_shot_iterator()
# next_element = iterator.get_next()

# with tf.Session() as sess:
#     for i in range(100):
#         value = sess.run(next_element)
#         assert i==value
# print("over")


# max_value = tf.placeholder(tf.int64, shape=[])
# dataset = tf.data.Dataset.range(max_value)
# iterator = dataset.make_initializable_iterator()
# next_element = iterator.get_next()
# sess = tf.Session()
# sess.run(iterator.initializer, feed_dict={max_value:10})
# for i in range(10):
#     value = sess.run(next_element)
#     assert i == value
# print("m1")
# sess.run(iterator.initializer, feed_dict={max_value:100})
# for i in range(100):
#     value = sess.run(next_element)
#     assert i==value
# print("m2")
dataset = tf.data.Dataset.range(5)
iterator = dataset.make_initializable_iterator()
next_element = iterator.get_next()
result = tf.add(next_element, next_element)

sess = tf.Session()
sess.run(iterator.initializer)
while True:
    try:
        print(sess.run(result))
    except tf.errors.OutOfRangeError:
        print("End of dataset")
        break
