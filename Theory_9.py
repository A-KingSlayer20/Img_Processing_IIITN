# Code for LBP
import cv2
import numpy as np
import matplotlib.pyplot as plt

def lbp_image(image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get the dimensions of the image
    rows, cols = gray_image.shape

    # Create an output image to store LBP result
    lbp = np.zeros((rows, cols), dtype=np.uint8)

    # LBP operator
    for i in range(1, rows-1):
        for j in range(1, cols-1):
            center = gray_image[i, j]
            binary_string = ''
            binary_string += '1' if gray_image[i-1, j-1] >= center else '0'
            binary_string += '1' if gray_image[i-1, j] >= center else '0'
            binary_string += '1' if gray_image[i-1, j+1] >= center else '0'
            binary_string += '1' if gray_image[i, j+1] >= center else '0'
            binary_string += '1' if gray_image[i+1, j+1] >= center else '0'
            binary_string += '1' if gray_image[i+1, j] >= center else '0'
            binary_string += '1' if gray_image[i+1, j-1] >= center else '0'
            binary_string += '1' if gray_image[i, j-1] >= center else '0'
            
            # Convert binary string to integer
            lbp_value = int(binary_string, 2)
            lbp[i, j] = lbp_value

    return lbp

# Load image
image = cv2.imread('D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg')

# Compute LBP
lbp_result = lbp_image(image)

# Display LBP image
plt.figure(figsize=(10, 10))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(lbp_result, cmap='gray')
plt.title('LBP Image')
plt.axis('off')

plt.show()
