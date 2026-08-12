import cv2
import numpy as np

# Create a blank image
height = 400
width = 700

image = np.zeros((height, width, 3), dtype=np.uint8)

# Shades of blue in BGR format
shades = [
    (255, 0, 0),      # Blue
    (220, 0, 0),      # Dark Blue
    (180, 0, 0),
    (140, 0, 0),
    (100, 0, 0),
    (60, 0, 0),
    (30, 0, 0)
]

# Width of each stripe
stripe_width = width // len(shades)

# Create blue stripes
for i, color in enumerate(shades):
    x1 = i * stripe_width
    x2 = (i + 1) * stripe_width
    image[:, x1:x2] = color

# Display
cv2.imshow("Shades of Blue", image)

cv2.waitKey(0)
cv2.destroyAllWindows()