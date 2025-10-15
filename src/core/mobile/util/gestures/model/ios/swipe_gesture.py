from typing import Optional, Dict, Any

from appium.webdriver import WebElement

from src.core.mobile.data.enums.mobile_gesture_direction import MobileGestureDirection
from src.core.mobile.util.gestures.model.gesture import Gesture


class SwipeGesture(Gesture):
    direction: MobileGestureDirection  # The direction in which to swipe. Either 'up', 'down', 'left' or 'right'

    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided
    # The value is measured in pixels per second and same values could behave differently on different devices depending on their display density. Higher values make swipe gesture faster (which usually scrolls larger areas if we apply it to a list) and lower values slow it down. Only values greater than zero have effect
    velocity: Optional[int] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["direction"] = self.direction.value

        if self.element: data["elementId"] = self.element.id
        if self.name: data["velocity"] = self.velocity
        return data
