from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class TwoFingerTapGesture(Gesture):
    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        if self.element: data["elementId"] = self.element.id
        return data
