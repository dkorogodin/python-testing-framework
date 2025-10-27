import base64
import datetime
import os
from pathlib import Path
from typing import Optional


class VideoUtil:
    """
    Handles start/stop video recording for Appium (mobile) and saves the video if a test fails.
    """

    _recording_active = False

    @staticmethod
    def start_recording(driver):
        """Starts video recording on Appium driver if supported."""
        if hasattr(driver, "start_recording_screen"):
            print("[INFO] Starting video recording...")
            driver.start_recording_screen()
            VideoUtil._recording_active = True
        else:
            print("[WARN] This driver does not support screen recording.")

    @staticmethod
    def stop_recording(driver) -> Optional[str]:
        """Stops recording and returns Base64 video data (if supported)."""
        if not VideoUtil._recording_active:
            return None

        if hasattr(driver, "stop_recording_screen"):
            print("[INFO] Stopping video recording...")
            try:
                return driver.stop_recording_screen()
            finally:
                VideoUtil._recording_active = False
        return None

    @staticmethod
    def save_video_if_test_failed(driver, test_name: str, base64_data: Optional[str]):
        """Saves the Base64 video only if test failed."""
        if not base64_data:
            return

        # Example structure: target/videos/20251016/ANDROID_14_OS/test_name_20251016_1422.mp4
        date_str = datetime.datetime.now().strftime("%Y%m%d")
        time_str = datetime.datetime.now().strftime("%H%M%S")
        platform = str(driver.capabilities.get("platformName", "UNKNOWN")).upper()
        version = driver.capabilities.get("appium:platformVersion", "")
        env_dir = f"{platform}_{version}_OS" if version else platform

        video_dir = Path("target/videos") / date_str / env_dir
        os.makedirs(video_dir, exist_ok=True)

        filename = f"{test_name}_{time_str}.mp4"
        file_path = video_dir / filename

        with open(file_path, "wb") as video_file:
            video_file.write(base64.b64decode(base64_data))
        print(f"[INFO] Video saved: {file_path}")
