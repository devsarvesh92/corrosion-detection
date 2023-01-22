

from pathlib import Path

import cv2
from core import vision

if __name__ == '__main__':
    while True:
        image_src = Path('./data/reference_image.jpg')
        vision.detect_corrosion(image_src= image_src)
        if cv2.waitKey(1) == ord('q'):
            break