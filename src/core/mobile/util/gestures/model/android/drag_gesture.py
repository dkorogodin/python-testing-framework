from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class DragGesture(Gesture):
    end_x: int  # Mandatory argument. x-end coordinate
    end_y: int  # Mandatory argument. y-end coordinate

    element: Optional[WebElement] = None  # If element is missing then both click offset coordinates must be provided
    start_x: Optional[int] = None  # x-start coordinate
    start_y: Optional[int] = None  # y-start coordinate
    # The speed at which to perform this gesture in pixels per second. The value must not be negative. The default value is 2500 * displayDensity
    speed: Optional[int] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["endX"] = self.end_x
        data["endY"] = self.end_y

        if self.element: data["elementId"] = self.element.id
        if self.start_x is not None: data["startX"] = self.start_x
        if self.start_y is not None: data["startY"] = self.start_y
        if self.speed is not None: data["speed"] = self.speed
        return data
