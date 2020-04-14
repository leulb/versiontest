#John Hughes
#Attempting to learn how to create and train my own tensorflow neural net using keras and tensorflow.py


from __future__ import absolute_import, division, print_function, unicode_literals

import os
import matplotlib.pyplot as plt
import pathlib
import numpy as np
from PIL import Image

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D

def getPrediction(model, img_path):
    img = image.load_img(img_path, target_size = (224, 224))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    arr = model.predict_classes(img)
    prdNum = arr[0][0]
    if prdNum == 0:
        return "Hollenbeck"
    else:
        return "Science"

def main():
    data_dir = pathlib.Path("D:/Senior Capstone Stuff/git/versiontest/Images")

    train_dir = os.path.join(data_dir, "train")
    test_dir = os.path.join(data_dir, "test")
    total_train = len(os.listdir(os.path.join(train_dir,"Hollenbeck")))\
                  +len(os.listdir(os.path.join(train_dir,"Science")))
    total_test = len(os.listdir(os.path.join(test_dir,"Hollenbeck")))\
                 +len(os.listdir(os.path.join(test_dir,"Science")))

    BATCH_SIZE = 30
    IMG_HEIGHT = 224
    IMG_WIDTH = 224
    EPOCHS = 10
    
    train_image_generator = ImageDataGenerator(rescale=1./255)
    test_image_generator = ImageDataGenerator(rescale=1./255)

    train_data_gen = train_image_generator.flow_from_directory(batch_size=BATCH_SIZE,
                                                               directory=train_dir,
                                                               shuffle=True,
                                                               target_size=(IMG_HEIGHT,IMG_WIDTH),
                                                               class_mode='binary')
    test_data_gen = test_image_generator.flow_from_directory(batch_size=10,
                                                             directory=test_dir,
                                                             target_size=(IMG_HEIGHT, IMG_WIDTH),
                                                             class_mode='binary')
    
    model = Sequential([
        Conv2D(16, 3, padding='same', activation='relu', input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),
        MaxPooling2D(),
        Conv2D(32, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Conv2D(64, 3, padding='same', activation='relu'),
        MaxPooling2D(),
        Flatten(),
        Dense(512, activation = 'relu'),
        Dense(1)
        ])

    model.compile(optimizer='adam',
                  loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
                  metrics=['accuracy'])

    history = model.fit_generator(
        train_data_gen,
        steps_per_epoch=total_train // BATCH_SIZE,
        epochs = EPOCHS,
        validation_data=test_data_gen,
        validation_steps=total_test // 10)

    return model, history
        
m,h = main()
