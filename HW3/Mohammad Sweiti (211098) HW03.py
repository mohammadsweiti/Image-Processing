#name : Mohammad Omar Ahmad Sweiti  
#ID : 211098
#HW03

import cv2
import numpy as np

def threshold_channel(channel, low, high):
    height, width = channel.shape
    mask = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            if low <= channel[i, j] <= high:
                mask[i, j] = 1
    return mask

def red_highlighting(image, mask):
    result = image.copy()
    for i in range(mask.shape[0]):
        for j in range(mask.shape[1]):
            if mask[i, j]:
                result[i, j] = [0, 0, 255]  
    return result


#######################################################
#Reading the image
image = cv2.imread('./1.jpg', cv2.IMREAD_COLOR)

#read it as HSV model
hsv_img = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

#using h and s channels only to detect the football field
h_channel ,s_channel,_ = cv2.split(hsv_img)

#thresholding value for each channel
hl, hh = 35, 90   
#range for s channel which is very saturated
sl, sh = 80, 255  

#making the mask for each channel
h_mask = threshold_channel(h_channel, hl, hh)
#the opencv library uses 0-255 for the s channel, so we need to convert it to 1 to 255
cv2.imshow("h_mask", h_mask*255)
s_mask = threshold_channel(s_channel, sl, sh)
cv2.imshow("s_mask", s_mask*255)
# combine the result
combined_mask = np.logical_and(h_mask, s_mask).astype(np.uint8)
cv2.imshow("combine the result mask", combined_mask*255)


#highlight the football field in red in the original image
output_image = red_highlighting(image, combined_mask)

# Save the result
cv2.imwrite("oup.jpg", output_image)
cv2.imshow("output image", output_image)

cv2.waitKey(0)
cv2.destroyAllWindows()


