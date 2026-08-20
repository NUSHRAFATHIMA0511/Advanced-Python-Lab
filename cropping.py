import cv2
import numpy as np

# Create a sky-blue background
image = np.zeros((400, 400, 3), dtype=np.uint8)
image[:] = (255, 200, 100)

# Draw a white circle
cv2.circle(image, (200, 200), 100, (255, 255, 255), -1)

# Display the image
cv2.imshow("Sky Blue Background with Circle", image)

cv2.waitKey(0)
cv2.destroyAllWindows()