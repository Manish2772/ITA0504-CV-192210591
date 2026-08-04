import cv2
import matplotlib.pyplot as plt
import os

# --------------------------------
# Load Image
# --------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "tree.png")

# Read color image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB for display
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(gray, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")

plt.tight_layout()
plt.show()

# --------------------------------
# Image Information
# --------------------------------

print("========== IMAGE DETAILS ==========")
print("Image Shape :", image.shape)
print("Height      :", image.shape[0])
print("Width       :", image.shape[1])
print("Channels    :", image.shape[2])

print("\nGrayscale Shape :", gray.shape)

print("\nImage converted successfully!")