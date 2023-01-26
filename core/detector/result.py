from enum import Enum
from typing import Final


class Result(str, Enum):

    corroded: Final[str] = "Surface is corroded"
    clean: Final[str] = "Surface is clean"
