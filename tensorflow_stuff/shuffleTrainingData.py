#John Hughes
#Shuffling the data for use in training and testing

import os
import random
import shutil

def main():
    hoPath = 'C:/Users/John Hughes/git/versiontest/Images/Hollenbeck'
    sciPath = 'C:/Users/John Hughes/git/versiontest/Images/Science'
    for i in range(80):
        curr = random.choice(os.listdir(hoPath))
        while curr == 'test' or curr == 'train':
            curr = random.choice(os.listdir(hoPath))
        shutil.move(os.path.join(hoPath,curr),os.path.join(hoPath, 'train'))
    for j in range(20):
        curr = random.choice(os.listdir(hoPath))
        while curr == 'test' or curr == 'train':
            curr = random.choice(os.listdir(hoPath))
        shutil.move(os.path.join(hoPath,curr),os.path.join(hoPath, 'test'))
    for k in range(80):
        curr = random.choice(os.listdir(sciPath))
        while curr == 'test' or curr == 'train':
            curr = random.choice(os.listdir(sciPath))
        shutil.move(os.path.join(sciPath,curr),os.path.join(sciPath, 'train'))
    for l in range(20):
        curr = random.choice(os.listdir(sciPath))
        while curr == 'test' or curr == 'train':
            curr = random.choice(os.listdir(sciPath))
        shutil.move(os.path.join(sciPath,curr),os.path.join(sciPath, 'test'))

main()