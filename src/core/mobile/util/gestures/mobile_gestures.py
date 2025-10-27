from src import logger
from src.core.mobile.util.gestures.model.gesture import Gesture


class MobileGestures:
    def __init__(self, driver):
        self.driver = driver

    def execute(self, gesture_name: str, gesture: Gesture) -> "MobileGestures":
        try:
            logger.info(f"Executing '{gesture_name}' gesture: {gesture}")
            self.driver.execute_script(f"mobile: {gesture_name}", gesture.get_supported_arguments())
        except Exception as e:
            logger.error(f"Failed to execute gesture '{gesture_name}': {e}")
        return self
