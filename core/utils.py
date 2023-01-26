from collections import namedtuple

import cv2

from core.detector.result import Result

message_configuration = namedtuple(
    "message_coniguration",
    field_names=[
        "font",
        "bottomLeftCornerOfText",
        "fontScale",
        "fontColor",
        "thickness",
        "lineType",
    ],
)


def get_message_configuration(is_corroded: Result) -> namedtuple:

    match is_corroded:
        case Result.corroded:
            return message_configuration(
                font=cv2.FONT_HERSHEY_SIMPLEX,
                bottomLeftCornerOfText=(10, 70),
                fontScale=4,
                fontColor=(0, 0, 255),
                thickness=4,
                lineType=2,
            )

        case Result.clean:
            return message_configuration(
                font=cv2.FONT_HERSHEY_SIMPLEX,
                bottomLeftCornerOfText=(10, 70),
                fontScale=1,
                fontColor=(0, 255, 0),
                thickness=1,
                lineType=2,
            )
