import cv2
import numpy as np

img = cv2.imread('6ZKQoVeY.png', cv2.IMREAD_COLOR)
gammas = [0.1, 0.2, 0.8, 1.5, 3, 5]

cv2.imshow('Image', img)

cv2.waitKey(0)


def adjust_gamma(img, gamma = 1.0):
    # invGamma = 1.0 / gamma
    table = np.array([((i / 255.0) ** gamma) * 255
                     for i in np.arange(0, 256)]).astype('uint8')
    return cv2.LUT(img, table)


for gamma in gammas:
    img = adjust_gamma(img, gamma)
    cv2.imshow(f'Image with gamma {gamma}', img)
    cv2.waitKey(0)                       