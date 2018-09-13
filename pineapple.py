# -*- coding:utf-8 -*-
__author__ = 'Microcosm'
 
import cv2
import numpy as np
from matplotlib import pyplot as plt
from pymouse import PyMouse
import time
from PIL import ImageGrab
import os
from calculate import *

cur_dir = os.path.dirname(__file__)
imgAll = ImageGrab.grab(bbox=(680,518,1300,920))#设置窗口大小
imgAll.save(os.path.join(cur_dir, "asd.png"))
# pathDir = os.listdir("./cards")
# print pathDir
# for file in pathDir:
img = cv2.imread("asd.png",0)
img2 = img.copy()
cardList = [[0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
cardPercent = [[0,0,0], [0,0,0,0,0], [0,0,0,0,0]]
for i in range(1, 53):
    template = cv2.imread("./cards/" + str(i) + "_put.png",0)
    w,h = template.shape[::-1]

    # # 6 中匹配效果对比算法
    # methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
    #            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
    # for meth in methods:
    meth = 'cv2.TM_CCORR_NORMED'
    img = img2.copy()

    method = eval(meth)

    res = cv2.matchTemplate(img,template,method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    if max_val > 0.99:
        position = getPosition(top_left)
        if position is None:
            continue
        print top_left, position
        if max_val > cardPercent[position[0]][position[1]]:
            cardPercent[position[0]][position[1]] = max_val
            cardList[position[0]][position[1]] = i
    # print i, min_val, max_val, min_loc, max_loc
    # m = PyMouse()
    # m.move(top_left[0], top_left[1])

    # print meth
print cardList
# plt.subplot(221), plt.imshow(img2)
# plt.title('Original Image'), plt.xticks([]),plt.yticks([])
# plt.subplot(222), plt.imshow(template)
# plt.title('template Image'),plt.xticks([]),plt.yticks([])
# plt.subplot(223), plt.imshow(res)
# plt.title('Matching Result'), plt.xticks([]),plt.yticks([])
# plt.subplot(224), plt.imshow(img)
# plt.title('Detected Point'),plt.xticks([]),plt.yticks([])
# plt.show()


# m = PyMouse()
# m.move(853, 853)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
# for i in range(1, 120):
#     m.move(853, 853 - 1 * i)
#     time.sleep(0.01)
# win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
