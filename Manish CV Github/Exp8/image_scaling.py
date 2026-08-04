import cv2
import matplotlib.pyplot as plt
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
# Scale Image
# --------------------------------

height, width = image.shape[:2]

# Enlarge Image (2x)
bigger = cv2.resize(
    image_rgb,
    (width * 2, height * 2),
    interpolation=cv2.INTER_CUBIC
)

# Shrink Image (Half Size)
smaller = cv2.resize(
    image_rgb,
    (width // 2, height // 2),
    interpolation=cv2.INTER_AREA
)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(bigger)
plt.title("Scaled Bigger (2x)")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(smaller)
plt.title("Scaled Smaller (0.5x)")
plt.axis("off")

plt.tight_layout()
plt.show()

# --------------------------------
# Image Information
# --------------------------------

print("========== IMAGE DETAILS ==========")
print("Original Size :", width, "x", height)
print("Bigger Size   :", bigger.shape[1], "x", bigger.shape[0])
print("Smaller Size  :", smaller.shape[1], "x", smaller.shape[0])

print("\nImage Scaling Completed Successfully!")