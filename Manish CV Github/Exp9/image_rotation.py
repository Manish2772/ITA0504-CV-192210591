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
# Rotate Image
# --------------------------------

# 90° Clockwise
clockwise = cv2.rotate(image_rgb, cv2.ROTATE_90_CLOCKWISE)

# 90° Counter-Clockwise
counter_clockwise = cv2.rotate(image_rgb, cv2.ROTATE_90_COUNTERCLOCKWISE)

# --------------------------------
# Display Images
# --------------------------------

plt.figure(figsize=(15,5))

plt.subplot(1,3,1)
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")

plt.subplot(1,3,2)
plt.imshow(clockwise)
plt.title("Clockwise Rotation")
plt.axis("off")

plt.subplot(1,3,3)
plt.imshow(counter_clockwise)
plt.title("Counter-Clockwise Rotation")
plt.axis("off")

plt.tight_layout()
plt.show()

# --------------------------------
# Image Information
# --------------------------------

print("========== IMAGE DETAILS ==========")
print("Original Shape :", image.shape)
print("Clockwise Shape :", clockwise.shape)
print("Counter-Clockwise Shape :", counter_clockwise.shape)

print("\nImage Rotation Completed Successfully!")