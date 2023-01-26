from pathlib import Path
from typing import Any, Protocol

from core.detector.result import Result


class CorrosionDetector(Protocol):
    """
    Corrosion detector protocol
    """

    def detect(self, image_path: Path) -> tuple[Result, Any]:
        """
        Detects corrosion
        """
