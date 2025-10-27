from .mobile_gestures import MobileGestures
from .model.ios.double_tap_gesture import DoubleTapGesture
from .model.ios.drag_from_to_for_duration_gesture import DragFromToForDurationGesture
from .model.ios.drag_from_to_with_velocity_gesture import DragFromToWithVelocity
from .model.ios.force_press_gesture import ForcePressGesture
from .model.ios.pinch_gesture import PinchGesture
from .model.ios.rotate_element_gesture import RotateElementGesture
from .model.ios.scroll_gesture import ScrollGesture
from .model.ios.scroll_to_element_gesture import ScrollToElementGesture
from .model.ios.select_picker_wheel_value_gesture import SelectPickerWheelValueGesture
from .model.ios.swipe_gesture import SwipeGesture
from .model.ios.tap_gesture import TapGesture
from .model.ios.tap_with_number_of_taps_gesture import TapWithNumberOfTapsGesture
from .model.ios.touch_and_hold_gesture import TouchAndHoldGesture
from .model.ios.two_finger_tap_gesture import TwoFingerTapGesture


class XCUITestDriverGestures(MobileGestures):
    """
    iOS-specific gestures for XCUITest.
    """

    def tap(self, gesture: TapGesture) -> "XCUITestDriverGestures":
        return self.execute("tap", gesture)

    def double_tap(self, gesture: DoubleTapGesture) -> "XCUITestDriverGestures":
        return self.execute("doubleTap", gesture)

    def touch_and_hold(self, gesture: TouchAndHoldGesture) -> "XCUITestDriverGestures":
        return self.execute("touchAndHold", gesture)

    def two_finger_tap(self, gesture: TwoFingerTapGesture) -> "XCUITestDriverGestures":
        return self.execute("twoFingerTap", gesture)

    def drag_from_to_for_duration(self, gesture: DragFromToForDurationGesture) -> "XCUITestDriverGestures":
        return self.execute("dragFromToForDuration", gesture)

    def drag_from_to_with_velocity(self, gesture: DragFromToWithVelocity) -> "XCUITestDriverGestures":
        return self.execute("dragFromToWithVelocity", gesture)

    def rotate_element(self, gesture: RotateElementGesture) -> "XCUITestDriverGestures":
        return self.execute("rotateElement", gesture)

    def tap_with_number_of_taps(self, gesture: TapWithNumberOfTapsGesture) -> "XCUITestDriverGestures":
        return self.execute("tapWithNumberOfTaps", gesture)

    def force_press(self, gesture: ForcePressGesture) -> "XCUITestDriverGestures":
        return self.execute("forcePress", gesture)

    def scroll_to_element(self, gesture: ScrollToElementGesture) -> "XCUITestDriverGestures":
        return self.execute("scrollToElement", gesture)

    def swipe(self, gesture: SwipeGesture) -> "XCUITestDriverGestures":
        return self.execute("swipe", gesture)

    def scroll(self, gesture: ScrollGesture) -> "XCUITestDriverGestures":
        return self.execute("scroll", gesture)

    def select_picker_wheel_value(self, gesture: SelectPickerWheelValueGesture) -> "XCUITestDriverGestures":
        return self.execute("selectPickerWheelValue", gesture)

    def pinch(self, gesture: PinchGesture) -> "XCUITestDriverGestures":
        return self.execute("pinch", gesture)
