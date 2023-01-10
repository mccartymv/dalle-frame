import numpy as np
import cv2

# Load the image from a file
image = cv2.imread("wheat-stalks.png")

# Get image dimensions
h, w = image.shape[:2]

# Create a mask with a transparent-to-black radial gradient
mask = np.zeros((h, w), dtype=np.uint8)
center = (w//2, h//2)
radius = min(w, h) // 1.5  # Make the radius smaller to create a more pronounced iris effect
for y in range(h):
    for x in range(w):
        r = np.sqrt((x - center[0])**2 + (y - center[1])**2)
        if r < radius:
            mask[y, x] = int(255 * (radius - r) / radius)  # Invert the gradient to go from transparent to black

# Apply the mask to the image
image[:,:,0] = image[:,:,0] * (mask / 255)
image[:,:,1] = image[:,:,1] * (mask / 255)
image[:,:,2] = image[:,:,2] * (mask / 255)

# Save the image to a file
cv2.imwrite("output.png", image)
