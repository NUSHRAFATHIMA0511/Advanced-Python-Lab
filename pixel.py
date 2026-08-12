import cv2

# Read the image
image = cv2.imread("image.jpg")

# Check if image is loaded
if image is None:
    print("Image not found")
else:
    # Get image dimensions
    height, width, channels = image.shape

    print("Image Resolution:", width, "x", height)
    print("Width:", width, "pixels")
    print("Height:", height, "pixels")
    print("Number of Channels:", channels)

    # Total number of pixels
    total_pixels = width * height
    print("Total Pixels:", total_pixels)

    # Display image
    cv2.imshow("Image", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()