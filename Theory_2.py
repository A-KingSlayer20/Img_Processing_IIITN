import cv2 as cv
import matplotlib.pyplot as plt

# Read the image
img = cv.imread('D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg')
cv.imshow("Original Image", img)

# Split the image into its Blue, Green, and Red channels
colors = ('b', 'g', 'r')
channels = cv.split(img)

# Create a figure for displaying histograms
plt.figure(figsize=(12, 6))

# Plot the original histogram
plt.subplot(2, 2, 1)
plt.title("Original Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for channel, color in zip(channels, colors):
    hist = cv.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

# Apply histogram equalization to each channel
equalized_channels = [cv.equalizeHist(channel) for channel in channels]

# Merge the equalized channels back into a BGR image
equalized_img = cv.merge(equalized_channels)
cv.imshow("Equalized Image", equalized_img)

# Plot the equalized histogram
plt.subplot(2, 2, 2)
plt.title("Equalized Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of Pixels")
for channel, color in zip(equalized_channels, colors):
    hist = cv.calcHist([channel], [0], None, [256], [0, 256])
    plt.plot(hist, color=color)
    plt.xlim([0, 256])

plt.tight_layout()
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()
