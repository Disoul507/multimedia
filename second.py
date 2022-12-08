import math
import cv2
import numpy as np


def gauss_blurr():
    #начало функции gauss_blur
    img1 = cv2.imread('E:/new/photo/d.jpg')
    gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    newGray = cv2.imread('E:/new/photo/d.jpg')
    newGray = cv2.cvtColor(newGray, cv2.COLOR_BGR2GRAY)
    h, w = newGray.shape[:2]
    n = 5
    new_value=0
    start = n // 2
    gauss_matrix = [[0] * n for i in range(n)]
    print(gauss_matrix)
    for k in range(n):
        for l in range(n):
            gauss_matrix[k][l] = (1 / (2 * math.pi)) * np.exp(-((k - start) ** 2 + (l - start) ** 2) / 2)


    sum = 0
    for k in range(0, n):
        for l in range(0, n):
            sum += gauss_matrix[k][l]
    print(sum)
    print(gauss_matrix)
    new_sum=0
    for k in range(0, n):
        for l in range(0, n):
            gauss_matrix[k][l] /= sum
            new_sum += gauss_matrix[k][l]
    print(new_sum)
    print(gauss_matrix)

    finishh = h - start
    finishw = w - start
    print(h, w, start)

    for i in range(start, finishh):
        for j in range(start, finishw):
            new_value=0
            for k in range(0, n):
                for l in range(0, n):
                    new_value = new_value + gauss_matrix[k][l] * gray[i - start + k][j - start + l]
            newGray[i][j] = new_value

    cv2.namedWindow('old', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('old', gray)
    cv2.namedWindow('new', cv2.WINDOW_AUTOSIZE)
    cv2.imshow('new', newGray)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    #конец функции gauss_blur

gauss_blurr()