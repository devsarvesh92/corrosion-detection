from pathlib import Path

import cv2

from core.detector.corrosion_detector import CorrosionDetector
from core.utils import get_message_configuration
from core.detector.image_processing import ImageProcessing

corrosion_detectors: dict[str, type[CorrosionDetector]] = {
    "image_procession": ImageProcessing,
    "deep_learning": lambda: print("Deep learning is not supported yet"),
}

if __name__ == "__main__":
    # display original image
    for image_path in [
        Path("./data/clean_image.png"),
        Path("./data/rust_image.jpg"),
    ]:

        img = cv2.imread(str(image_path.absolute()))
        cv2.imshow("frame", img)

        if cv2.waitKey() == ord("p"):
            result, coroded_area = corrosion_detectors["image_procession"]().detect(
                image_path=image_path
            )

            message_configuration = get_message_configuration(is_corroded=result)

            cv2.putText(
                coroded_area,
                result.value,
                message_configuration.bottomLeftCornerOfText,
                message_configuration.font,
                message_configuration.fontScale,
                message_configuration.fontColor,
                message_configuration.thickness,
                message_configuration.lineType,
            )
            # display result
            cv2.imshow("frame", coroded_area)

            if cv2.waitKey() == ord("q"):
                continue
