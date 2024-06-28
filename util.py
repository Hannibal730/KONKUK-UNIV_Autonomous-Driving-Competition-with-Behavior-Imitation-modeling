#util

import time

import os

import cv2



# fps 계산용

def calc_fps(last_time):

    t_current = time.time()

    fps = round(1/(t_current-last_time + 10e-8),1)

    return fps



# 이미지 저장 폴더 생성

def makeImgDir():

    if not os.path.exists('image'):

        os.makedirs('image')

        os.makedirs('image' + os.sep + 'go')

        os.makedirs('image' + os.sep + 'left')

        os.makedirs('image' + os.sep + 'right')

        os.makedirs('image' + os.sep + 'brake')

        os.makedirs('image' + os.sep + 'parking')

        os.makedirs('image' + os.sep + 'other')







if __name__ == '__main__':

    makeImgDir()

