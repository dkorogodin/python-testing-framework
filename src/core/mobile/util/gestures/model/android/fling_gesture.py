from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.data.enums.mobile_gesture_direction import MobileGestureDirection
from src.core.mobile.util.gestures.model.gesture import Gesture


class FlingGesture(Gesture):
    direction: MobileGestureDirection  # Mandatory value. Direction of the fling

    element: Optional[WebElement] = None  # If the element id is missing then fling bounding area must be provided
    left: Optional[int] = None  # left coordinate of the fling bounding area
    top: Optional[int] = None  # top coordinate of the fling bounding area
    width: Optional[int] = None  # width of the fling bounding area
    height: Optional[int] = None  # height of the fling bounding area
    # The speed at which to perform this gesture in pixels per second. The value must be greater than the minimum fling velocity for the given view (50 by default). The default value is 7500 * displayDensity.
    speed: Optional[int] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["direction"] = self.direction.value

        if self.element: data["elementId"] = self.element.id
        if self.left is not None: data["left"] = self.x
        if self.top is not None: data["top"] = self.y
        if self.width is not None: data["width"] = self.y
        if self.height is not None: data["height"] = self.y
        if self.speed is not None: data["speed"] = self.y
        return data
