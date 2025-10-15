from typing import Dict, Any

from appium.webdriver import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class ScrollToElementGesture(Gesture):
    element: WebElement  # The destination element must be located in a scrollable container and must be hittable. If the element is already present in the current viewport then no action is performed.

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["elementId"] = self.element.id
        return data
