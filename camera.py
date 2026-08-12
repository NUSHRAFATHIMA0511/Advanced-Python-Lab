import cv2
from datetime import datetime

# Initialize the default web camera
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Camera opened successfully with live time. Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame. Exiting ...")
        break

    # Get the current date and time
    now = datetime.now()
    # Format the time string (e.g., "2026-06-06 14:30:15")
    time_string = now.strftime("%Y-%m-%d %H:%M:%S")

    # Put the time text on the video frame
    # Parameters: frame, text, origin (bottom-left corner of text), font, scale, color (BGR), thickness, linetype
    cv2.putText(
        img=frame,
        text=time_string,
        org=(30, 50),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=1,
        color=(0, 255, 0),  # Green color in BGR
        thickness=2,
        lineType=cv2.LINE_AA
    )

    # Display the resulting frame
    cv2.imshow('Webcam Feed with Time', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()