#Bit - slicing

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Function to extract and display bit planes
def display_bit_planes(image_path):
    # Load the image in grayscale
    image = cv2.imread("D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg", cv2.IMREAD_GRAYSCALE)

    if image is None:
        raise ValueError("Image not found or path is incorrect.")

    # Number of bit planes
    num_bits = 8

    # Prepare the subplot grid
    fig, axes = plt.subplots(1, num_bits + 1, figsize=(20, 5))
    axes = axes.flatten()

    # Display original image
    axes[0].imshow(image, cmap='gray')
    axes[0].set_title('Original Image')
    axes[0].axis('off')

    # Iterate over each bit plane
    for bit in range(num_bits):
        # Create a bit plane mask
        bit_plane = (image >> bit) & 1
        bit_plane *= 255  # Scale the bit plane to 0-255 for display

        axes[bit + 1].imshow(bit_plane, cmap='gray')
        axes[bit + 1].set_title(f'Bit Plane {bit}')
        axes[bit + 1].axis('off')

    plt.tight_layout()
    plt.show()

# Provide the path to your image
image_path = 'path_to_your_image.jpg'

# Display the bit planes
display_bit_planes(image_path)
