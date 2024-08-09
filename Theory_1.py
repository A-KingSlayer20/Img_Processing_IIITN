# Image conversion to grayscale and B+W


import cv2 as cv

img=cv.imread("D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg")
cv.imshow("Img",img)

grey_img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# def rescaleFrame(frame,scale=0.75) :
#     width=int(frame.shape[1]*scale)
#     height=int(frame.shape[0]*scale)

#     dimensions=(width,height)

#     return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)

cv.waitKey(0)