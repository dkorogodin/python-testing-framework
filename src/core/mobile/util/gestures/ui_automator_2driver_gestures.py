from .mobile_gestures import MobileGestures
from .model.android.click_gesture import ClickGesture
from .model.android.drag_gesture import DragGesture
from .model.android.fling_gesture import FlingGesture
from .model.android.long_click_gesture import LongClickGesture
from .model.android.pinch_gesture import PinchGesture
from .model.android.swipe_gesture import SwipeGesture


class UIAutomator2DriverGestures(MobileGestures):
    """
    Android-specific gestures for UIAutomator2.
    """

    def click(self, gesture: ClickGesture): return self.execute("clickGesture", gesture)

    def double_click(self, gesture: ClickGesture): return self.execute("doubleClickGesture", gesture)

    def long_click(self, gesture: LongClickGesture): return self.execute("longClickGesture", gesture)

    def drag(self, gesture: DragGesture): return self.execute("dragGesture", gesture)

    def fling(self, gesture: FlingGesture): return self.execute("flingGesture", gesture)

    def pinch_open(self, gesture: PinchGesture): return self.execute("pinchOpenGesture", gesture)

    def pinch_close(self, gesture: PinchGesture): return self.execute("pinchCloseGesture", gesture)

    def swipe(self, gesture: SwipeGesture): return self.execute("swipeGesture", gesture)

    def can_scroll_more(self, gesture: SwipeGesture) -> bool:
        return bool(self.driver.execute_script("mobile: scrollGesture", gesture.get_supported_arguments()))
