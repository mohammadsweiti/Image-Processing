'''
Name : Mohammad Sweiti
Id# : 211098 
HW02
comments is added in the code for explanation
'''

#libraries needed
import cv2 as cv 

# This function transforms the kernel to make the convolution 
def transfomKernel(kernel):
    flipped_kernel = []
    for row in reversed(kernel):
        new_row = []
        for value in reversed(row):
            new_row.append(value)
        flipped_kernel.append(new_row)
    return flipped_kernel

#this is the covolution function which is required from us 
def  convolution(image , kernel):
    size = image.shape

    #this for the size of the image and the size of teh kernel
    imageW = size[0]
    imageH = size[1]
    kernelW = len(kernel)
    kernelH = len(kernel[0])

    #this is the transforming of the kernel
    transfomKernel(kernel)

    #I used the Border repalicate to put the border of the image as the original
    outputimage = image.copy()

    #two for loops to iterate over the image
    for i in range(1,imageW-1):
        for j in range(1,imageH-1):
            sum = 0
            #two for loop to iterate over the kernel
            for k in range(0,kernelW):
                for l in range(0,kernelH):     
                    #here for ensuring that the kernel is not out of the image size
                    if i+k-1 < imageW and j+l-1 < imageH:
                        sum += int(image[i+k-1][j+l-1])*kernel[k][l] 
            if sum > 255:
                sum = 255
            if sum < 0:
                sum = 0
            outputimage[i][j] = sum
    return outputimage


#this function is making sobel edge detection
def sobel(image):
    image2 = image.copy()
    #gradient in x directoin kernel
    kernel_gx =[
        [-1, 0, 1],
        [-2, 0, 2],
        [-1, 0, 1]
    ]
    #gradient in y direction kerne;
    kernel_gy = [
        [-1, -2, -1],
        [ 0,  0,  0],
        [ 1,  2,  1]
    ]
    #making the convolution for the image and the kernel
    gx = convolution(image, kernel_gx)
    gy = convolution(image2, kernel_gy)
    
    #this is the gradient magnitude image
    magnitude = image.copy()
    #this two loop for making the gradient magnitude 
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # Compute the gradient magnitude
            mag = min(abs(int(gx[i][j])) + abs(int(gy[i][j])), 255)
            if mag > 255:
                mag = 255
            magnitude[i][j] = mag
            
    return magnitude

#ٌ   1) Reading the Grayscale image
img = cv.imread('00.png', cv.IMREAD_GRAYSCALE)


#   2) Sobel Edge Detection (convolution with Sobel kernel)
img2 = sobel(img)

threshold = 30

#  3) Thresholding the Sobel image
img3 = img2.copy()
for i in range(img3.shape[0]):
        for j in range(img3.shape[1]):
            if img3[i,j] >= threshold:
                mag = 0
            elif img3[i,j] < threshold:
                mag = 255
            img3[i][j] = mag


# Smoothing the image using a 5x5 averaging filter
smoothing = [
    [2/159, 4/159, 5/159, 4/159, 2/159],
    [4/159, 9/159, 12/159, 9/159, 4/159],
    [5/159, 12/159, 15/159, 12/159, 5/159],
    [4/159, 9/159, 12/159, 9/159, 4/159],
    [2/159, 4/159, 5/159, 4/159, 2/159],
]

#smoothing the original imaage with the filter
img4 = convolution(img, smoothing)

#sobel after the averaging 
img5 = sobel(img4)

#applying the threshold
for i in range(img5.shape[0]):
        for j in range(img5.shape[1]):
            if img5[i,j] >= threshold:
                mag = 0
            elif img5[i,j] < threshold:
                mag = 255
            img5[i][j] = mag
    
            
#showing the images
cv.imshow('original image ', img)
cv.imshow('sobel edge detection', img2)
cv.imshow(' sobel with thresholding', img3)
cv.imshow('avg  img', img4)
cv.imshow(' avd solbel  img ', img5)

# Save the images to files
cv.imwrite('sobel.png', img2)
cv.imwrite('sobel_with_thresholding.png', img3)
cv.imwrite('avg_img.png', img4)
cv.imwrite('avg_sobel_img.png', img5)



cv.waitKey(0)
cv.destroyAllWindows()