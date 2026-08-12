import cv2
import numpy as np

# Create a blank image
height = 500
width = 700

image = np.zeros((height, width, 3), dtype=np.uint8)

# Define colors in BGR format
colors = [
    (0, 0, 255),      # Red
    (0, 165, 255),    # Orange
    (0, 255, 255),    # Yellow
    (0, 255, 0),      # Green
    (255, 0, 0),      # Blue
    (130, 0, 75),     # Indigo
    (211, 0, 148)     # Violet
]

# Width of each stripe
stripe_width = width // len(colors)

# Create vertical stripes
for i, color in enumerate(colors):
    x1 = i * stripe_width
    x2 = (i + 1) * stripe_width
    image[:, x1:x2] = color

# Display the image
cv2.imshow("Color Stripes", image)

# Wait for a key press
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()