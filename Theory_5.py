#Huffman Coding

import cv2
import numpy as np
import heapq
from collections import defaultdict, Counter

# Node for Huffman Tree
class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    # Comparing nodes based on frequency
    def __lt__(self, other):
        return self.freq < other.freq

# Create Huffman Tree
def build_huffman_tree(symbols):
    heap = [Node(symbol, freq) for symbol, freq in symbols.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2
        heapq.heappush(heap, merged)
    
    return heap[0]

# Generate Huffman Codes
def generate_codes(root, code="", codes={}):
    if root is not None:
        if root.symbol is not None:
            codes[root.symbol] = code
        generate_codes(root.left, code + "0", codes)
        generate_codes(root.right, code + "1", codes)
    return codes

# Compress Image
def huffman_compress(image):
    flat_image = image.flatten()
    frequencies = Counter(flat_image)
    
    # Build Huffman Tree
    huffman_tree_root = build_huffman_tree(frequencies)
    
    # Generate Huffman Codes
    huffman_codes = generate_codes(huffman_tree_root)
    
    # Encode the image
    encoded_image = ''.join(huffman_codes[pixel] for pixel in flat_image)
    
    return encoded_image, huffman_codes

# Decompress Image
def huffman_decompress(encoded_image, huffman_codes, shape):
    reverse_codes = {v: k for k, v in huffman_codes.items()}
    
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

# Compress the image using Huffman coding
compressed_image, huffman_codes = huffman_compress(image)
print("Compression done!")

# Decompress the image
decompressed_image = huffman_decompress(compressed_image, huffman_codes, image.shape)
print("Decompression done!")

# Calculate sizes
original_size_bits = image.size * 8  # Each pixel is 8 bits in grayscale
compressed_size_bits = len(compressed_image)  # Length of the encoded bit string
compression_ratio = original_size_bits / compressed_size_bits

print(f"Original Size: {original_size_bits} bits")
print(f"Compressed Size: {compressed_size_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}")


# Display the original and decompressed images
cv2.imshow("Original Image", image)
cv2.imshow("Decompressed Image", decompressed_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
