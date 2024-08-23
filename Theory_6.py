#Shannon fano Algorithm

import cv2
import numpy as np
from collections import Counter

def shannon_fano(freq_table):
    # Sort the frequency table by descending frequency
    sorted_freq = sorted(freq_table.items(), key=lambda item: item[1], reverse=True)
    
    def shannon_fano_recursive(symbols):
        if len(symbols) == 1:
            return {symbols[0][0]: ""}
        
        # Find the partition point
        total = sum(freq for _, freq in symbols)
        cumulative = 0
        partition = 0
        for i, (_, freq) in enumerate(symbols):
            cumulative += freq
            if cumulative >= total / 2:
                partition = i + 1
                break
        
        # Recursively generate codes
        left_codes = shannon_fano_recursive(symbols[:partition])
        right_codes = shannon_fano_recursive(symbols[partition:])
        
        # Assign '0' to the left partition and '1' to the right partition
        codes = {}
        for symbol, code in left_codes.items():
            codes[symbol] = '0' + code
        for symbol, code in right_codes.items():
            codes[symbol] = '1' + code
        
        return codes
    
    return shannon_fano_recursive(sorted_freq)

def shannon_fano_compress(image):
    flat_image = image.flatten()
    frequencies = Counter(flat_image)
    
    # Generate Shannon-Fano codes
    shannon_fano_codes = shannon_fano(frequencies)
    
    # Encode the image
    encoded_image = ''.join(shannon_fano_codes[pixel] for pixel in flat_image)
    
    return encoded_image, shannon_fano_codes

def shannon_fano_decompress(encoded_image, shannon_fano_codes, shape):
    reverse_codes = {v: k for k, v in shannon_fano_codes.items()}
    
    decoded_image = []
    current_code = ""
    
    for bit in encoded_image:
        current_code += bit
        if current_code in reverse_codes:
            decoded_image.append(reverse_codes[current_code])
            current_code = ""
    
    return np.array(decoded_image).reshape(shape)

# Load Image
image_path = 'D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Compress the image using Shannon-Fano coding
compressed_image, shannon_fano_codes = shannon_fano_compress(image)

# Calculate sizes
original_size_bits = image.size * 8  # Each pixel is 8 bits in grayscale
compressed_size_bits = len(compressed_image)  # Length of the encoded bit string
compression_ratio = original_size_bits / compressed_size_bits

print(f"Original Size: {original_size_bits} bits")
print(f"Compressed Size: {compressed_size_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}")

# Decompress the image
decompressed_image = shannon_fano_decompress(compressed_image, shannon_fano_codes, image.shape)

# Display the original and decompressed images
cv2.imshow("Original Image", image)
cv2.imshow("Decompressed Image", decompressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
