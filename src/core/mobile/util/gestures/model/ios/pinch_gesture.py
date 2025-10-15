from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class PinchGesture(Gesture):
    scale: float  # Pinch scale of type float. Use a scale between 0 and 1 to "pinch close" or zoom out and a scale greater than 1 to "pinch open" or zoom in
    velocity: float  # The velocity of the pinch in scale factor per second

    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["scale"] = self.scale
        data["velocity"] = self.velocity

        if self.element: data["elementId"] = self.element.id
        return data
