import cv2
import numpy as np

# image import part
image_path = "image_operations\image.png"
image = cv2.imread(image_path)

# image resizing part
resized_img = cv2.resize(image, (250,250))

# grayscale the image
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# histogram sync
equalized_img = cv2.equalizeHist(gray_img)

# adding Gaussian Noise
mean = 0 
sddev = 20 # standart deviation
gaussian_noise = np.random.normal(mean, sddev, image.shape).astype(np.uint8)
noisy_image = cv2.add(image, gaussian_noise)

cv2.imshow("Original Image", image)
cv2.imshow("Resized Image", resized_img)
cv2.imshow("Gray Image", gray_img)
cv2.imshow("Histogram Synced Image", equalized_img)
cv2.imshow("Noised Image", noisy_image)

# screens close so fast that we cant even see the images.
# so i set the program that wait for closing till the one key down.
cv2.waitKey(0)
cv2.destroyAllWindows()