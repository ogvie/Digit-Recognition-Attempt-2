import os
import cv2 #load and process images
import numpy as np
import matplotlib.pyplot as plt #used to generate and visualise the numbers we will predict
import tensorflow as tf #machine learning part

#mnist = tf.keras.datasets.mnist
#split data into training data and testing data for the model
#(x_train, y_train), (x_test, y_test) = mnist.load_data()#x data is image of number and y is the correspnding number

#x_train = tf.keras.utils.normalize(x_train, axis=1) #normalise photo into greyscale so each pixel
#x_test = tf.keras.utils.normalize(x_test, axis=1) #is either 1 or 0

#model = tf.keras.models.Sequential()
#model.add(tf.keras.layers.Flatten(input_shape=(28, 28)))
#model.add(tf.keras.layers.Dense(128, activation="relu"))#relu rectify linear unit, activation funtion
#model.add(tf.keras.layers.Dense(10, activation="softmax")) #i have 10 digits, so 10 neurons in my network, will be used for predicting accuracy

#model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])

#train model here
#model.fit(x_train, y_train, epochs=5) #epochs is how many times we go through the same data

#model.save("digitrecogniser.model") 

model = tf.keras.models.load_model("digitrecogniser.model") 

#loss, accuracy = model.evaluate(x_test, y_test)
#print(loss)
#print(accuracy)

image_number = 1
#while os.path.isfile(f"digits/digit{image_number}.png"):
#    try:
#        for x in range(5):
#            img = cv2.imread(f"digits/digit{image_number}.png")[:,:,0]
#            img = np.invert(np.array([img]))
#            prediction = model.predict(img)
#            print(f"The digit is probably a {np.argmax(prediction)}")
#            plt.imshow(img[0], cmap=plt.cm.binary)
#            plt.show()
#    except:
#        print("Error...")
#    finally:
#        image_number +=1

for x in range(5):
            img = cv2.imread(f"digits/digit{image_number}.png")[:,:,0]
            img = np.invert(np.array([img]))
            prediction = model.predict(img)
            print(f"The digit is probably a {np.argmax(prediction)}")
            plt.imshow(img[0], cmap=plt.cm.binary)
            plt.show()