from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class DragFromToForDurationGesture(Gesture):
    duration: float  # Mandatory argument. number of seconds in range [0.5, 60]. How long the tap gesture at starting drag point should be before to start dragging
    from_x: int  # Mandatory argument. The x coordinate of starting drag point
    from_y: int  # Mandatory argument. The y coordinate of starting drag point
    to_x: int  # Mandatory argument. The x coordinate of ending drag point
    to_y: int  # Mandatory argument. The y coordinate of ending drag point

    element: Optional[WebElement] = None  # Absolute screen coordinates are expected if this argument is not set

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["duration"] = self.duration
        data["fromX"] = self.from_x
        data["fromY"] = self.from_y
        data["toX"] = self.to_x
        data["toY"] = self.to_y

        if self.element: data["elementId"] = self.element.id
        return data
