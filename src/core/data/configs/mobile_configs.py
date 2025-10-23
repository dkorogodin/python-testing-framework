from pathlib import Path

from src.core.mobile.data.enums.mobile_platform import MobilePlatform
from src.core.util.system.config_loader_util import ConfigLoader


class MobileConfigs:
    """
    Loads and provides mobile configuration properties for both local and cloud setups.

    Mirrors the Java MobileProperties class:
      - Loads platform, device, app, and cloud credentials
      - Supports both Android and iOS
      - Handles both local and cloud execution
    """
    # src/core/data/configs/mobile_configs.py
    APP_PATH = Path(__file__).resolve().parents[4] / "data/app"

    def __init__(self, loader: ConfigLoader):
        self.loader = loader

        # =============================
        # COMMON
        # =============================
        self.mobile_platform = MobilePlatform.from_property(self.loader.get("common.platform"))
        self.is_cloud = self.loader.get("common.isCloud")
        self.recordVideo = self.loader.get("common.recordVideo")

        self.app_name = None
        self.app_package_or_bundle_id = None
        self.device_platform_version = None
        self.device_name = None
        self.device_udid = None

        # =============================
        # IOS SPECIFIC CONFIGS
        # =============================
        self.xcode_org_id = None
        self.xcode_signing_id = None

        # =============================
        # APPIUM SERVICE
        # =============================
        self.appium_service_type = self.loader.get("local.appiumService.type")
        self.appium_service_url = None

        # =============================
        # CLOUD SPECIFIC CONFIGS
        # =============================
        self.cloud_username = None
        self.cloud_access_key = None
        self.cloud_session_name = None
        self.cloud_build_name = None

        if self.is_cloud:
            self._load_cloud_configs()
        else:
            self._load_local_configs()

    def set_appium_service_url(self, new_appium_service_url: str):
        """Update the appium_service_url value."""
        self.appium_service_url = new_appium_service_url

    def set_mobile_platform(self, new_mobile_platform: MobilePlatform):
        """Update the mobile_platform value."""
        self.mobile_platform = new_mobile_platform

    def _load_local_configs(self):
        if self.mobile_platform == MobilePlatform.ANDROID:
            self.app_name = str(self.APP_PATH / self.loader.get("local.android.app"))
            self.app_package_or_bundle_id = self.loader.get("local.android.appPackage")
            self.device_udid = self.loader.get("local.android.device.udid")
            self.device_platform_version = self.loader.get("local.android.device.platformVersion")
        else:
            self.app_name = str(self.APP_PATH / self.loader.get("local.ios.app"))
            self.app_package_or_bundle_id = self.loader.get("local.ios.bundleId")
            self.device_name = self.loader.get("local.ios.device.name")
            self.device_udid = self.loader.get("local.ios.device.udid")
            self.device_platform_version = self.loader.get("local.ios.device.platformVersion")
            self.xcode_org_id = self.loader.get("local.ios.xcodeOrgId")
            self.xcode_signing_id = self.loader.get("local.ios.xcodeSigningId")

    def _load_cloud_configs(self):
        self.appium_service_url = self.loader.get("cloud.appiumService.url")
        self.cloud_username = self.loader.get("cloud.credentials.username")
        self.cloud_access_key = self.loader.get("cloud.credentials.accessKey")

        if self.mobile_platform == MobilePlatform.ANDROID:
            self.app_name = self.loader.get("cloud.android.app")
            self.device_name = self.loader.get("cloud.android.device.name")
            self.device_platform_version = self.loader.get("cloud.android.device.platformVersion")
            self.cloud_session_name = self.loader.get("cloud.android.sessionName")
            self.cloud_build_name = self.loader.get("cloud.android.buildName")
        else:
            self.app_name = self.loader.get("cloud.ios.app")
            self.device_name = self.loader.get("cloud.ios.device.name")
            self.device_platform_version = self.loader.get("cloud.ios.device.platformVersion")
            self.cloud_session_name = self.loader.get("cloud.ios.sessionName")
            self.cloud_build_name = self.loader.get("cloud.ios.buildName")
