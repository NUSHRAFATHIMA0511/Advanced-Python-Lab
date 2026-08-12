import cv2

# Start webcam
cap = cv2.VideoCapture(0)

# Store drawing points
points = []

drawing = False


# Mouse function
def draw(event, x, y, flags, param):
    global drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        points.append((x, y))

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        points.append((x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False


# Create window
cv2.namedWindow("Live Drawing")
cv2.setMouseCallback("Live Drawing", draw)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Draw lines between stored points
    for i in range(1, len(points)):
        cv2.line(frame, points[i - 1], points[i], (0, 0, 255), 3)

    cv2.imshow("Live Drawing", frame)

    # Press C to clear drawing
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        points.clear()

    # Press Q to quit
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()