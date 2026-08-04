import cv2

# --------------------------------
# Open Webcam
# --------------------------------

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Cannot access webcam.")
    exit()

print("====================================")
print("WEBCAM VIDEO PROCESSING")
print("====================================")
print("Press N : Normal Speed")
print("Press S : Slow Motion")
print("Press F : Fast Motion")
print("Press Q : Quit")
print("====================================")

# Default Speed (Normal)
delay = 30

while True:

    ret, frame = cap.read()

    if not ret:
        print("Failed to capture frame.")
        break

    # Display video
    cv2.imshow("Webcam Video", frame)

    key = cv2.waitKey(delay) & 0xFF

    # Quit
    if key == ord('q'):
        break

    # Normal Speed
    elif key == ord('n'):
        delay = 30
        print("Normal Speed")

    # Slow Motion
    elif key == ord('s'):
        delay = 100
        print("Slow Motion")

    # Fast Motion
    elif key == ord('f'):
        delay = 5
        print("Fast Motion")

cap.release()
cv2.destroyAllWindows()