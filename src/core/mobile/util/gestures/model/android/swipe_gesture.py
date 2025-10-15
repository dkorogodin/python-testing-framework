from typing import Optional, Dict, Any

from appium.webdriver import WebElement

from src.core.mobile.data.enums.mobile_gesture_direction import MobileGestureDirection
from src.core.mobile.util.gestures.model.gesture import Gesture


class SwipeGesture(Gesture):
    direction: MobileGestureDirection  # Mandatory value. Swipe direction
    percent: float  # Mandatory value. The size of the swipe as a percentage of the swipe area size. Valid values must be float numbers in range 0..1, where 1.0 is 100%

    element: Optional[WebElement] = None  # If element id is missing then pinch bounding area must be provided
    left: Optional[int] = None  # left coordinate of the swipe bounding area
    top: Optional[int] = None  # top coordinate of the swipe bounding area
    width: Optional[int] = None  # width of the swipe bounding area
    height: Optional[int] = None  # height of the swipe bounding area
    # The speed at which to perform this gesture in pixels per second. The value must not be negative. The default value is 5000 * displayDensity
    speed: Optional[int] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["direction"] = self.direction.value
        data["percent"] = self.percent

        if self.element: data["elementId"] = self.element.id

        for field in ["left", "top", "width", "height", "speed"]:
            value = getattr(self, field)
            if value is not None:
                data[field] = value
        return data
