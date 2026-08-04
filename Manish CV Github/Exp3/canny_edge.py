import cv2
import matplotlib.pyplot as plt
import os

# --------------------------------
# Read Image
# --------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(current_dir, "scenery.png")

# Read the image
image = cv2.imread(image_path)

if image is None:
    print("Image not found!")
    exit()

# Convert BGR to RGB for displaying
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# --------------------------------
# Apply Canny Edge Detection
# --------------------------------

edges = cv2.Canny(gray, 100, 200)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,2,2)
plt.imshow(edges, cmap="gray")
plt.title("Canny Edge Detection")
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

print("\nCanny Edge Detection Applied Successfully!")