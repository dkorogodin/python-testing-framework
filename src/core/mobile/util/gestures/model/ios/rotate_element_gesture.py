from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class RotateElementGesture(Gesture):
    rotation: float  # Mandatory argument. The rotation of the gesture in radians. Example: Math.PI
    velocity: float  # Mandatory argument. The velocity of the rotation gesture in radians per second. Example: Math.PI / 4

    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["rotation"] = self.rotation
        data["velocity"] = self.velocity

        if self.element: data["elementId"] = self.element.id
        return data
