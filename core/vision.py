"""
Process image using open cv
"""

from pathlib import Path

import cv2
import numpy as np



def detect_corrosion(*, image_src: Path):
    """
    Detects corroded area using open cv
    """
    img = cv2.imread(str(image_src.absolute()))
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lower_red = np.array([0,50,50])
    upper_red = np.array([11,255,255])
    lower_red2 = np.array([175,50,50])
    upper_red2 = np.array([179,255,255]) 
    mask1 = cv2.inRange(hsv, lower_red, upper_red)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
    mask=mask1+mask2 

    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow('frame', result)

    