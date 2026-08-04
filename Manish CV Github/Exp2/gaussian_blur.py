import cv2
import matplotlib.pyplot as plt
import os

# --------------------------------
# Read Image
# --------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "scenery.png")

image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB for displaying
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# --------------------------------
# Apply Gaussian Blur
# --------------------------------

blur = cv2.GaussianBlur(image_rgb, (11, 11), 0)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(blur)
plt.title("Gaussian Blur")
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

print("\nGaussian Blur Applied Successfully!")