import cv2
from matplotlib import pyplot
import logging

logging.basicConfig(level=logging.INFO)

image = cv2.imread("lab/cropped2.png")
image = cv2.cvtColor(image, cv2.COLOR_BGR2YUV)
(R,G,B) = cv2.split(image)
logging.info(image.shape)
image = cv2.resize(image, (100, 100))
cv2.rectangle(image, (0, 0), (17, 17), (255), 2)
# image = cv2.circle(image, (20,20), radius=0, color=(0, 0, 255), thickness=5)
logging.info(image[20,20])
logging.info(R.shape)
figure, axis = pyplot.subplots(2, 2)
axis[0,0].imshow(R, cmap='gray')
axis[0,1].imshow(G, cmap='gray')
axis[1,0].imshow(B, cmap='gray')
axis[1,1].imshow(image)
# pyplot.imshow(image[0:200, 0:200])
pyplot.show()