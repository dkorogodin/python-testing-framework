from typing import Optional, Set

from src import logger


class ContextActions:
    """
    Provides methods to manage and switch between contexts in a mobile application.

    Supports switching between native app context and webview context.
    """

    def __init__(self, driver):
        self.driver = driver

    # ------------------------------------------------
    # Context getters
    # ------------------------------------------------
    def get_current_context(self) -> str:
        """Returns the current context of the mobile driver."""
        try:
            logger.info("Getting current context...")
            return self.driver.context
        except Exception as e:
            logger.warning(f"Could not get current context: {e}")
            return ""

    def get_all_contexts(self) -> Optional[Set[str]]:
        """Returns all available contexts of the mobile driver."""
        try:
            logger.info("Getting all mobile contexts...")
            return set(self.driver.contexts)
        except Exception as e:
            logger.warning(f"Could not get contexts: {e}")
            return None

    # ------------------------------------------------
    # Context names
    # ------------------------------------------------
    def get_webview_name(self) -> str:
        """Returns the name of the WebView context, or empty string if none exists."""
        contexts = self.get_all_contexts()
        if not contexts or len(contexts) < 2:
            logger.warning("No WebView context available.")
            return ""

        for context in contexts:
            if "webview" in context.lower():
                return context
        return ""

    def get_native_view_name(self) -> str:
        """Returns the name of the Native app context."""
        contexts = self.get_all_contexts()
        if not contexts:
            logger.warning("No contexts found.")
            return ""
        return list(contexts)[0]

    # ------------------------------------------------
    # Switch operations
    # ------------------------------------------------
    def switch_to_context(self, context_name: str):
        """
        Switches the driver to a specified context.
        Returns the driver in the new context, or None if switch failed.
        """
        try:
            logger.info(f"Switching to '{context_name}' context...")
            self.driver.switch_to.context(context_name)
            return self.driver
        except Exception as e:
            logger.warning(f"Could not switch to context '{context_name}': {e}")
            return None

    def switch_to_webview_app(self):
        """Switches the driver to the WebView context."""
        return self.switch_to_context(self.get_webview_name())

    def switch_to_native_app(self):
        """Switches the driver to the Native app context."""
        return self.switch_to_context(self.get_native_view_name())
