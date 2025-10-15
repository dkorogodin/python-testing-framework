from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class LongClickGesture(Gesture):
    element: Optional[WebElement] = None  # If element is missing then both click offset coordinates must be provided
    x: Optional[int] = None  # x-offset coordinate
    y: Optional[int] = None  # y-offset coordinate
    duration: Optional[int] = None  # Click duration in milliseconds. 500 by default. The value must not be negative

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        if self.element: data["elementId"] = self.element.id
        if self.x is not None: data["x"] = self.x
        if self.y is not None: data["y"] = self.y
        if self.duration is not None: data["duration"] = self.duration
        return data
