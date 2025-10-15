from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class PinchGesture(Gesture):
    percent: float  # Mandatory value. The size of the pinch as a percentage of the pinch area size. Valid values must be float numbers in range 0..1, where 1.0 is 100%

    element: Optional[WebElement] = None  # If element id is missing then pinch bounding area must be provided
    left: Optional[int] = None  # left coordinate of the fling bounding area
    top: Optional[int] = None  # top coordinate of the fling bounding area
    width: Optional[int] = None  # width of the fling bounding area
    height: Optional[int] = None  # height of the fling bounding area
    # The speed at which to perform this gesture in pixels per second. The value must be greater than the minimum fling velocity for the given view (50 by default). The default value is 7500 * displayDensity.
    speed: Optional[int] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["percent"] = self.percent

        if self.element: data["elementId"] = self.element.id
        if self.left is not None: data["left"] = self.x
        if self.top is not None: data["top"] = self.y
        if self.width is not None: data["width"] = self.y
        if self.height is not None: data["height"] = self.y
        if self.speed is not None: data["speed"] = self.y
        return data
