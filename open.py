import cv2
import matplotlib.pyplot as plt

image = cv2.imread("lab/vlc.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cropped_image = image[140:140+700, 0:0+2000]

cv2.imwrite("lab/cropped.png", cv2.cvtColor(cropped_image, cv2.COLOR_RGB2BGR))

# plt.imshow(image)
plt.imshow(cropped_image)
plt.show()