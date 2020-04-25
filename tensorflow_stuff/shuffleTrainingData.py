#John Hughes
#Shuffling the data for use in training and testing

import os
import random
import shutil

def main():
    basePath = 'C:/Capstone Git/versiontest/NewImages'
    buildings = ['Blair','Hollenbeck','Koch','Krieg','Science','Synod','Zimmerman']
    for building in buildings:
        currPath = os.path.join(basePath, building)
        os.mkdir(os.path.join(currPath, 'train'))
        os.mkdir(os.path.join(currPath, 'test'))
        for i in range(175):
            curr = random.choice(os.listdir(currPath))
            while curr == 'test' or curr == 'train':
                curr = random.choice(os.listdir(currPath))
            shutil.move(os.path.join(currPath, curr),os.path.join(currPath, 'train'))
        for j in range(50):
            curr = random.choice(os.listdir(currPath))
            while curr == 'test' or curr == 'train':
                curr = random.choice(os.listdir(currPath))
            shutil.move(os.path.join(currPath, curr),os.path.join(currPath, 'test'))

main()
