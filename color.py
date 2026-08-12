import cv2
import numpy as np

# Create a blank grayscale image
height = 400
width = 600

image = np.zeros((height, width), dtype=np.uint8)

# Shades of black/gray
shades = [0, 40, 80, 120, 160, 200, 240]

# Width of each stripe
stripe_width = width // len(shades)

# Create vertical stripes
for i, shade in enumerate(shades):
    x1 = i * stripe_width
    x2 = (i + 1) * stripe_width
    
    image[:, x1:x2] = shade

# Display image
cv2.imshow("Shades of Black", image)

cv2.waitKey(0)
cv2.destroyAllWindows()