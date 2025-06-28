# Name: Mohammad Sweity
# ID: 211098

#---------importing libraries---------------------
import cv2 as cv
import numpy as np

#---------------------function definitions---------------------

#this function applies a threshold to the image
def thresholding(img, threshold_value):
    result = img.copy()
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i, j] > threshold_value:
                result[i, j] = 0
            else:
                result[i, j] = 255
    return result

#this function applies an erosion to the image
def erosion(img, kernel):
    img_h, img_w = img.shape
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2
    padded_img = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    eroded = np.zeros_like(img)
    for i in range(img_h):
        for j in range(img_w):
            region = padded_img[i:i+k_h, j:j+k_w]
            if np.all(region[kernel == 1] == 255):
                eroded[i, j] = 255
    return eroded

#this function applies a dilation to the image
def dilation(img, kernel):
    img_h, img_w = img.shape
    k_h, k_w = kernel.shape
    pad_h = k_h // 2
    pad_w = k_w // 2

    padded_img = np.pad(img, ((pad_h, pad_h), (pad_w, pad_w)), mode='constant', constant_values=0)
    dilated = np.zeros_like(img)
    for i in range(img_h):
        for j in range(img_w):
            region = padded_img[i:i+k_h, j:j+k_w]
            if np.any(region[kernel == 1] == 255):
                dilated[i, j] = 255
    return dilated
    
#this function applies an  opening to the image
def opening(img, kernel):
    return dilation(erosion(img, kernel), kernel)

#this function applies a closing to the image
def closing(img, kernel):
    return erosion(dilation(img, kernel), kernel)

#---------------------end of function definitions---------------------

#---------------------main program starts here---------------------
# Load the image
inputImage = cv.imread('c1.jpg') 

# convert it to greyscale
grayImage = cv.cvtColor(inputImage, cv.COLOR_BGR2GRAY)

#thresholding to generate an initial segmentation
thresholdValue = 236

thresh = thresholding(grayImage, thresholdValue)

dilationKernel = np.ones((3,3), dtype=np.uint8)
openKernel = np.ones((5,5), dtype=np.uint8)
closingKernel = np.ones((3,3), dtype=np.uint8)

opened = opening(thresh, openKernel)
dilationed1 = dilation(opened, dilationKernel)
dilationed2 = dilation(dilationed1, dilationKernel)
closed = closing(dilationed2, closingKernel)

dilationKernel = np.ones((5,5), dtype=np.uint8)
dilationed3 = dilation(closed, dilationKernel)

white_bg = np.ones_like(inputImage) * 255
mask = dilationed3.astype(np.uint8)
finalResult = white_bg.copy()
finalResult[mask == 255] = inputImage[mask == 255]

cv.imshow("Original", inputImage)
cv.imshow("grayImage", grayImage)
cv.imshow("Threshold", thresh)
cv.imshow("opening", opened)
cv.imshow("dilation 1", dilationed1)
cv.imshow("dilation 2", dilationed2)
cv.imshow("closing", closed)
cv.imshow("dilation 3", dilationed3)
cv.imshow("Restored Image", finalResult)

cv.waitKey(0)
cv.destroyAllWindows()
#---------------------end of main program  here---------------------