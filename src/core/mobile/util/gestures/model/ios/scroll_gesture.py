from typing import Optional, Dict, Any

from appium.webdriver import WebElement

from src.core.mobile.data.enums.mobile_gesture_direction import MobileGestureDirection
from src.core.mobile.util.gestures.model.gesture import Gesture


class ScrollGesture(Gesture):
    direction: MobileGestureDirection  # The main difference from swipe call with the same argument is that scroll will try to move the current viewport exactly to the next/previous page (the term "page" means the content, which fits into a single device screen). Either 'up', 'down', 'left' or 'right'

    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided
    # The accessibility id of the child element, to which scrolling is performed. The same result can be achieved by setting predicateString argument to 'name == accessibilityId'. Has no effect if elementId is not a container
    name: Optional[str] = None
    # The NSPredicate locator of the child element, to which the scrolling should be performed. Has no effect if elementId is not a container. Example: label == "foo"
    predicate_string: Optional[str] = None
    # If set to true then asks to scroll to the first visible elementId in the parent container. Has no effect if elementId is not set
    to_visible: Optional[bool] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["direction"] = self.direction.value

        if self.element: data["elementId"] = self.element.id
        if self.name: data["name"] = self.name
        if self.predicate_string: data["predicateString"] = self.predicate_string
        if self.to_visible is not None: data["toVisible"] = self.to_visible
        return data
