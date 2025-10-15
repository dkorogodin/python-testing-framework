from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class TapGesture(Gesture):
    x: int  # Mandatory argument. Horizontal coordinate offset
    y: int  # Mandatory argument. Vertical coordinate offset

    element: Optional[WebElement] = None  # If element is missing then calculated relatively to active app element

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["x"] = self.x
        data["y"] = self.y

        if self.element: data["elementId"] = self.element.id
        return data
