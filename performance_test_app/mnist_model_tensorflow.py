from __future__ import print_function
import tensorflow as tf
from tensorflow import keras

import matplotlib.pyplot  as plt

mnist = keras.datasets.mnist


img_rows, img_cols = 28, 28

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print(x_train.shape)
plt.subplot(221)
plt.imshow(x_train[0], cmap=plt.get_cmap('gray'))
plt.subplot(222)
plt.imshow(x_train[1], cmap=plt.get_cmap('gray'))
plt.subplot(223)
plt.imshow(x_train[2], cmap=plt.get_cmap('gray'))
plt.subplot(224)
plt.imshow(x_train[3], cmap=plt.get_cmap('gray'))
# show the plot
plt.show()


x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)
x_train = x_train.astype('float32')
x_test = x_test.astype('float32')
x_train /= 255
x_test /= 255
print(x_train.shape[0], 'train samples')
print(x_test.shape[0], 'test samples')

print("Y train sample = ",y_train[0])
# convert class vectors to binary class matrices
y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)
print("Y train sample with one-hot = ",y_train[0])


from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout

model = Sequential()
model.add(Dense(512, activation='sigmoid', input_shape=(784,)))
model.add(Dropout(0.2))
model.add(Dense(512, activation='sigmoid'))
model.add(Dropout(0.2))
model.add(Dense(10, activation='softmax'))

model.summary()
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(x_train,y_train,batch_size=100,epochs=10,validation_data=(x_test,y_test))

score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])

plt.figure(figsize=(9,6))
plt.plot(model.history.history['accuracy'], label='Train accuracy')
plt.plot(model.history.history['val_accuracy'], label='Validation accuracy')
plt.ylabel('Value')
plt.xlabel('No. epoch')
plt.legend()
plt.show()



########## Predict ##########


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage import util 
from PIL import Image
import numpy as np
size=(28,28)
# imgplot = plt.imshow(img)
img = Image.open('/home/jovyan/number2.jpg').convert("L")
img = img.resize(size)
img = np.resize(img, (28,28))
im2arr = np.array(img)
im2arr = im2arr.reshape(1,28,28,1)

img = img / 255.0
img = 1-img
# plt.imshow(x_test[image_index].reshape(28, 28),cmap='Greys')
plt.imshow(img ,cmap=plt.get_cmap('gray'))
img = img.reshape(1, 784)

pred = model.predict(img)

print("Prediction probability array is:")

count = 0

for i in pred.squeeze():
    print(count, ":", round(i,4))
    count += 1

print("From which the max choice is:", pred.argmax())