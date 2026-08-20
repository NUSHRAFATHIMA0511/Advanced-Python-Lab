import cv2

# Open the input video
cap = cv2.VideoCapture("input.mp4")

# Set output video width and height
width = 640
height = 480

# Get FPS of input video
fps = cap.get(cv2.CAP_PROP_FPS)

# If FPS cannot be detected, use 30 FPS
if fps == 0:
    fps = 30

# Create output video
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter(
    "flipped_video.mp4",
    fourcc,
    fps,
    (width, height)
)

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Resize video frame to 640 x 480
    frame = cv2.resize(frame, (width, height))

    # Flip horizontally
    flipped = cv2.flip(frame, 1)

    # Save flipped frame
    out.write(flipped)

    # Display video
    cv2.imshow("Flipped Video", flipped)

    # Press Q to stop
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
out.release()
cv2.destroyAllWindows()

print("Video flipped successfully!")