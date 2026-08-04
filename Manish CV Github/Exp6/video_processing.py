import cv2
import os

# --------------------------------
# Read Video
# --------------------------------

current_dir = os.path.dirname(os.path.abspath(__file__))
video_path = os.path.join(current_dir, "captured_video.mp4")

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Unable to open video.")
    exit()

print("Press:")
print("n - Normal Speed")
print("s - Slow Motion")
print("f - Fast Motion")
print("q - Quit")

# Default speed (Normal)
delay = 30

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Video Processing", frame)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('q'):
        break

    elif key == ord('n'):
        delay = 30
        print("Normal Speed")

    elif key == ord('s'):
        delay = 100
        print("Slow Motion")

    elif key == ord('f'):
        delay = 5
        print("Fast Motion")

cap.release()
cv2.destroyAllWindows()