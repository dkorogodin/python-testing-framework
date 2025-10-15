from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class ClickGesture(Gesture):
    element: Optional[WebElement] = None  # If element is missing then both click offset coordinates must be provided
    x: Optional[int] = None  # x-offset coordinate
    y: Optional[int] = None  # y-offset coordinate

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        if self.element: data["elementId"] = self.element.id
        if self.x is not None: data["x"] = self.x
        if self.y is not None: data["y"] = self.y
        return data
