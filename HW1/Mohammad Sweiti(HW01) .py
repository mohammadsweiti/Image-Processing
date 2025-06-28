#name : mohammad Omar Sweiti
#ID# : 211098

import cv2 as cv

img = cv.imread("./gray.png", cv.IMREAD_GRAYSCALE)
size = img.shape

firstThreshold = int(input("enter  first threshold which is between 0 and 255): "))
secondThreshold = int(input("enter  second threshold which is between 0 and 255): "))

outputImage = img.copy()


for i in range(size[0]):
    for j in range(size[1]):
        pixelValue = img[i, j]
        if firstThreshold <= pixelValue <= secondThreshold:
            outputImage[i, j] = pixelValue
        else:
            outputImage[i, j] = 0

cv.imshow("input_image", img)
cv.imshow("output_image", outputImage)
cv.imwrite("output_image.png", outputImage)


cv.waitKey(0)   