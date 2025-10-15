from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class TapWithNumberOfTapsGesture(Gesture):
    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided
    number_of_taps: Optional[int] = None  # The number of taps. 1 by default
    number_of_touches: Optional[int] = None  # The number of touch points. 1 finger by default

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)

        if self.element: data["elementId"] = self.element.id
        if self.element: data["numberOfTaps"] = self.number_of_taps
        if self.element: data["numberOfTouches"] = self.number_of_touches
        return data
