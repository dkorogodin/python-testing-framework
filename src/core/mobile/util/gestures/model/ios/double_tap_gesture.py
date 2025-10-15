from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class DoubleTapGesture(Gesture):
    element: Optional[WebElement] = None  # Active app element will be used instead if this parameter is not provided
    x: Optional[int] = None  # Horizontal coordinate offset
    y: Optional[int] = None  # Vertical coordinate offset

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        if self.element: data["elementId"] = self.element.id
        if self.x is not None: data["x"] = self.x
        if self.y is not None: data["y"] = self.y
        return data
