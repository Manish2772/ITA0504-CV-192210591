import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# --------------------------------
# Read Image
# --------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "image.jpg")

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# --------------------------------
# Translate Image
# --------------------------------

height, width = image.shape[:2]

# Translation distances
tx = 100      # Move Right
ty = 80       # Move Down

# Translation Matrix
translation_matrix = np.float32([
    [1, 0, tx],
    [0, 1, ty]
])

# Apply Translation
translated = cv2.warpAffine(
    image_rgb,
    translation_matrix,
    (width, height)
)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(translated)
plt.title("Translated Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# --------------------------------
# Image Information
# --------------------------------

print("========== IMAGE DETAILS ==========")
print("Original Size :", width, "x", height)
print("Moved Right by :", tx, "pixels")
print("Moved Down by  :", ty, "pixels")

print("\nImage Translation Completed Successfully!")