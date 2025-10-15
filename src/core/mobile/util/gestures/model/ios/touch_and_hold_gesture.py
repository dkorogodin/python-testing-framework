from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class TouchAndHoldGesture(Gesture):
    duration: int  # The float duration of press action in seconds

    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided
    x: Optional[int] = None  # Horizontal coordinate offset
    y: Optional[int] = None  # Vertical coordinate offset

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["duration"] = self.duration

        if self.element: data["elementId"] = self.element.id
        if self.element: data["x"] = self.x
        if self.element: data["y"] = self.y
        return data
