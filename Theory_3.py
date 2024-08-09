#Image conversion to only R , G and B color scale

import cv2 as cv

import numpy as np

img = cv.imread('D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg')

# Split the image into its Blue, Green, and Red channels
b, g, r = cv.split(img)

# Create images with only one color channel
# Blue scale
blue_scale = cv.merge([b, np.zeros_like(b), np.zeros_like(b)])

# Green scale
green_scale = cv.merge([np.zeros_like(g), g, np.zeros_like(g)])

# Red scale
red_scale = cv.merge([np.zeros_like(r), np.zeros_like(r), r])

# Display the images
cv.imshow('Original Image', img)
cv.imshow('Blue Channel', blue_scale)
cv.imshow('Green Channel', green_scale)
cv.imshow('Red Channel', red_scale)

cv.waitKey(0)
cv.destroyAllWindows()
