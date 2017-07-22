# -- coding: utf-8 --

import cv2
import numpy as np 


# 单通道的直方图
def calcAndDrawHist(image, color):
	hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
	minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
	histImg = np.zeros([256, 256, 3], np.uint8)
	hpt = int(0.9 * 256)

	for h in range(256):
		intensity= int(hist[h]*hpt/maxVal)
		cv2.line(histImg, (h, 256), (h, 256-intensity), color)

	return histImg

if __name__ == '__main__':
	img = cv2.imread("test0.png")
	bgr_b, bgr_g, bgr_r = cv2.split(img)

	equ_b = cv2.equalizeHist(bgr_b)  
	equ_g = cv2.equalizeHist(bgr_g)  
	equ_r = cv2.equalizeHist(bgr_r) 

	merged_bgr = cv2.merge([equ_b, equ_g, equ_r])

# ----------------------------------------------------------
	 histImgB = calcAndDrawHist(bgr_b, [255, 0, 0])
	 histImgG = calcAndDrawHist(bgr_g, [0, 255, 0])
	 histImgR = calcAndDrawHist(bgr_r, [0, 0, 255])

	 cv2.imshow("histImgB", histImgB)
	 cv2.imshow("histImgG", histImgG)
	 cv2.imshow("histImgR", histImgR)
#----------------------------------------------------------

	cv2.imshow("Img", img)
	cv2.imshow('merged_bgr', merged_bgr)
	cv2.waitKey(0)
	cv2.destroyAllWindows()
