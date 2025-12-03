import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

input_image = cv.imread('image.jpeg')

gray_image = cv.cvtColor(input_image, cv.COLOR_BGR2GRAY)