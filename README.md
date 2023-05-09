# Overview:

This Python code snippet utilizes the OpenCV and NumPy libraries to overlay a radial gradient onto an image, creating a unique "keyhole" or "iris" visual effect. This effect can be used to draw focus to the center of an image, or to create artistic photographic modifications.

# Key Concepts:

The script first imports necessary libraries - NumPy for numerical computation and OpenCV for image processing. It then reads an image file "wheat-stalks.png" into an array. The script then captures the dimensions of the image to create a mask of the same size.

The mask, initially filled with zeros (representing black), is then filled with a radial gradient. The center of the gradient is calculated as the center of the image, and the radius is calculated as the smaller of the image's width and height divided by 1.5. This size was chosen to create a more pronounced iris effect, but it can be adjusted as needed.

Each pixel in the mask is then updated based on its distance from the center. Pixels within the radius are set to a value ranging from 255 (white) at the center to 0 (black) at the edge of the radius. This creates a smooth gradient from transparent at the center to black at the radius.

Next, the mask is applied to each color channel (Blue, Green, Red) of the image separately. This involves multiplying the color intensity at each pixel by the mask's intensity at the corresponding pixel. The division by 255 is necessary as the mask's intensity is in the range 0-255, while color intensity is in the range 0-1.

Finally, the modified image is saved to the file "output.png".
