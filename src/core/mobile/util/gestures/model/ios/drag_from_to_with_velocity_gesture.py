from typing import Optional, Dict, Any

from selenium.webdriver.remote.webelement import WebElement

from src.core.mobile.util.gestures.model.gesture import Gesture


class DragFromToWithVelocity(Gesture):
    press_duration: float  # Mandatory argument. Number of seconds in range [0, 60]. How long the tap gesture at starting drag point should be before to start dragging
    hold_duration: float  # Mandatory argument. Number of seconds in range [0, 60]. The duration for which to hold over the other coordinate or the given element after dragging
    velocity: int  # Mandatory argument. The speed at which to move from the initial press position to the other element or coordinate, expressed in pixels per second

    from_element: Optional[WebElement] = None  # Absolute screen coordinates are expected if this argument is not set
    to_elementId: Optional[WebElement] = None  # This parameter is mandatory if fromElementId is provided
    from_x: Optional[int] = None  # x coordinate of starting drag point. Must be provided if fromElementId not defined
    from_y: Optional[int] = None  # y coordinate of starting drag point. Must be provided if fromElementId not defined
    to_x: Optional[int] = None  # x coordinate of ending drag point. Must be provided if fromElementId is not defined
    to_y: Optional[int] = None  # y coordinate of ending drag point. Must be provided if fromElementId is not defined

    def get_supported_arguments(self) -> Dict[str, Any]:
        data = self.model_dump(exclude_none=True)
        data["pressDuration"] = self.press_duration
        data["holdDuration"] = self.hold_duration
        data["velocity"] = self.velocity

        if self.from_element: data["fromElementId"] = self.from_element.id
        if self.to_elementId: data["toElementId"] = self.to_elementId.id
        if self.from_x: data["fromX"] = self.from_x
        if self.from_y: data["fromY"] = self.from_y
        if self.to_x: data["toX"] = self.to_x
        if self.to_y: data["toY"] = self.to_y
        return data
