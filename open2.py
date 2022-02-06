import cv2
from matplotlib import pyplot

image = cv2.imread("lab/cropped1.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
cropped_image = image[0:250, 0:250]
pyplot.imshow(cropped_image)
cv2.imwrite("lab/cropped2.png", cv2.cvtColor(cropped_image, cv2.COLOR_RGB2BGR))
pyplot.show()