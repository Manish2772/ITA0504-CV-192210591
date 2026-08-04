import cv2
import matplotlib.pyplot as plt
import numpy as np
import os

# --------------------------------
# Read Image
# --------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "mickey.png")

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# --------------------------------
# Erode Image
# --------------------------------

# Create a 5x5 kernel
kernel = np.ones((5,5), np.uint8)

# Apply Erosion
eroded = cv2.erode(image_rgb, kernel, iterations=1)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(eroded)
plt.title("Eroded Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# --------------------------------
# Image Details
# --------------------------------

print("========== IMAGE DETAILS ==========")
print("Image Shape :", image.shape)
print("Height      :", image.shape[0])
print("Width       :", image.shape[1])
print("Channels    :", image.shape[2])

print("\nErosion Applied Successfully!")