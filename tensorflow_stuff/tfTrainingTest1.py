#John Hughes
#Attempting to learn how to create and train my own tensorflow neural net using keras and tensorflow.py


from __future__ import absolute_import, division, print_function, unicode_literals

import os
import matplotlib.pyplot as plt
import pathlib
import numpy as np

import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, Flatten, Dropout, MaxPooling2D

def main():
    hoTrainDir = "C:/Users/John Hughes/git/versiontest/Images/Hollenbeck/train"
    hoValDir = "C:/Users/John Hughes/git/versiontest/Images/Hollenbeck/test"
    sciTrainDir = "C:/Users/John Hughes/git/versiontest/Images/Science/train"
    sciValDir = "C:/Users/John Hughes/git/versiontest/Images/Science/test"
    
    
    
main()
