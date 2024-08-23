#Arithmetic coding

import cv2
import numpy as np
from collections import Counter
from decimal import Decimal, getcontext

# Set the precision high enough to avoid numerical issues
getcontext().prec = 50

def arithmetic_encode(symbols, probabilities):
    low = Decimal(0)
    high = Decimal(1)
    for symbol in symbols:
        range_ = high - low
        high = low + range_ * Decimal(probabilities[symbol][1])
        low = low + range_ * Decimal(probabilities[symbol][0])
    return low

def arithmetic_decode(encoded_value, probabilities, total_symbols):
    low = Decimal(0)
    high = Decimal(1)
    decoded_symbols = []
    for _ in range(total_symbols):
        range_ = high - low
        code = (encoded_value - low) / range_
        for symbol, (low_prob, high_prob) in probabilities.items():
            if low_prob <= code < high_prob:
                decoded_symbols.append(symbol)
                high = low + range_ * Decimal(high_prob)
                low = low + range_ * Decimal(low_prob)
                break
    return decoded_symbols

def calculate_probabilities(symbols):
    total_count = sum(symbols.values())
    cumulative_prob = Decimal(0)
    probabilities = {}
    for symbol, count in sorted(symbols.items()):
        prob = Decimal(count) / Decimal(total_count)
        probabilities[symbol] = (cumulative_prob, cumulative_prob + prob)
        cumulative_prob += prob
    return probabilities

def arithmetic_compress(image):
    flat_image = image.flatten()
    frequencies = Counter(flat_image)
    
    # Calculate cumulative probabilities
    probabilities = calculate_probabilities(frequencies)
    
    # Encode the image using arithmetic coding
    encoded_value = arithmetic_encode(flat_image, probabilities)
    
    return encoded_value, probabilities, len(flat_image)

def arithmetic_decompress(encoded_value, probabilities, total_symbols, shape):
    decoded_image = arithmetic_decode(encoded_value, probabilities, total_symbols)
    return np.array(decoded_image).reshape(shape)

# Load Image
image_path = 'D:\ThirdYear_Books\Img_Processing_IIITN\Photos\park.jpg'
image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Compress the image using Arithmetic coding
encoded_value, probabilities, total_symbols = arithmetic_compress(image)

# Calculate sizes
original_size_bits = image.size * 8  # Each pixel is 8 bits in grayscale
compressed_size_bits = len(bin(int(encoded_value * (2 ** 32)))) - 2  # Convert encoded value to binary
compression_ratio = original_size_bits / compressed_size_bits

print(f"Original Size: {original_size_bits} bits")
print(f"Compressed Size: {compressed_size_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}")

# Decompress the image
decompressed_image = arithmetic_decompress(encoded_value, probabilities, total_symbols, image.shape)

# Display the original and decompressed images
cv2.imshow("Original Image", image)
cv2.imshow("Decompressed Image", decompressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

