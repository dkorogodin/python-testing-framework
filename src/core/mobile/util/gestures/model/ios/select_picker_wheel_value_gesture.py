from typing import Optional, Dict, Any

from appium.webdriver import WebElement

from src.core.mobile.data.enums.mobile_gesture_order import MobileGestureOrder
from src.core.mobile.util.gestures.model.gesture import Gesture


class SelectPickerWheelValueGesture(Gesture):
    element: WebElement  # The element must be of type XCUIElementTypePickerWheel
    order: MobileGestureOrder  # Either next to select the value next to the current one from the target picker wheel or previous to select the previous one

    # The value in range [0.01, 0.5]. It defines how far from picker wheel's center the click should happen. The actual distance is calculated by multiplying this value to the actual picker wheel height. Too small offset value may not change the picker wheel value and too high value may cause the wheel to switch two or more values at once. Usually the optimal value is located in range [0.15, 0.3]. 0.2 by default
    offset: Optional[float] = None
    # If provided WDA will try to automatically scroll in the given direction until the actual picker value reaches the expected one or the amount of scrolling attempts is exceeded
    value: Optional[str] = None
    # The maximum number of scrolling attempts to reach value before an error will be thrown. Only makes sense in combination with value. 25 by default
    max_attempts: Optional[int] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["elementId"] = self.element.id
        data["order"] = self.order.value

        if self.name: data["offset"] = self.offset
        if self.name: data["value"] = self.value
        if self.name: data["maxAttempts"] = self.max_attempts
        return data
