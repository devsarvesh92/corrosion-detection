"""
Process image using open cv
"""

from pathlib import Path
from typing import Any

import cv2
import numpy as np

from core.detector.result import Result


class ImageProcessing:
    """
    Detect corrosion using image processing
    """

    def detect(self, *, image_path: Path) -> tuple[Result, Any]:
        """
        Detects corroded area using open cv
        """
        img = cv2.imread(str(image_path.absolute()))
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        lower_red = np.array([0, 50, 50])
        upper_red = np.array([11, 255, 255])
        lower_red2 = np.array([175, 50, 50])
        upper_red2 = np.array([179, 255, 255])
        mask1 = cv2.inRange(hsv, lower_red, upper_red)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        mask = mask1 + mask2
        corroded_area = cv2.bitwise_and(img, img, mask=mask)

        # this calculation needs to be corrected
        result = (
            Result.corroded
            if round(np.count_nonzero(mask) / np.size(mask) * 100, 1) < 2
            else Result.clean
        )

        return result, corroded_area
