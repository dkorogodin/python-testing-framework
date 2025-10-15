from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class ForcePressGesture(Gesture):
    # It is expected that both x and y are provided if this argument is omitted. If the element identifier is provided without coordinates then the actual element's touch point will be calculated automatically by WebDriverAgent
    element: Optional[WebElement] = None
    # x coordinate of the gesture. It is calculated relatively to the given element (if provided). Otherwise, the gesture destination point is calculated relatively to the active application
    x: Optional[int] = None
    # y coordinate of the gesture. It is calculated relatively to the given element (if provided). Otherwise, the gesture destination point is calculated relatively to the active application
    y: Optional[int] = None
    # Number of seconds the force press action would take. If duration is provided then it is also expected that a custom pressure value is provided as well. 0.5 by default
    duration: Optional[float] = None
    # Number defining how much pressure to apply. If pressure is provided then it is also expected that a custom duration value is provided as well. 1.0 by default
    pressure: Optional[float] = None

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)

        if self.element: data["elementId"] = self.element.id
        if self.x is not None: data["x"] = self.x
        if self.y is not None: data["y"] = self.y
        if self.duration is not None: data["duration"] = self.duration
        if self.pressure is not None: data["pressure"] = self.pressure
        return data
