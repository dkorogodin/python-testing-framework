from typing import Optional, Dict, Any, Tuple
import requests
from src import logger


class HttpClient:
    """
    A lightweight HTTP client wrapper around `requests` for API testing.
    Supports Basic Authentication, logging, and JSON-friendly defaults.
    """

    def __init__(
        self,
        base_url: str,
        timeout: int = 10,
        basic_auth: Optional[Tuple[str, str]] = None
    ):
        self.base_url = base_url.rstrip("/")  # avoid double slashes
        self.timeout = timeout
        self.basic_auth = basic_auth  # (username, password)
        logger.info(
            f"Initialized RequestClient with base_url: {self.base_url}, "
            f"timeout: {self.timeout}s, basic_auth={'set' if self.basic_auth else 'not set'}"
        )

    def get(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: dict = None) -> requests.Response:
        return self._request("GET", endpoint, headers=headers, params=params)

    def post(self, endpoint: str, headers: Optional[Dict[str, str]] = None, json: dict = None) -> requests.Response:
        return self._request("POST", endpoint, headers=headers, json=json)

    def put(self, endpoint: str, headers: Optional[Dict[str, str]] = None, json: dict = None) -> requests.Response:
        return self._request("PUT", endpoint, headers=headers, json=json)

    def patch(self, endpoint: str, headers: Optional[Dict[str, str]] = None, json: dict = None) -> requests.Response:
        return self._request("PATCH", endpoint, headers=headers, json=json)

    def delete(self, endpoint: str, headers: Optional[Dict[str, str]] = None, params: dict = None) -> requests.Response:
        return self._request("DELETE", endpoint, headers=headers, params=params)

    def _request(
        self,
        method: str,
        endpoint: str,
        headers: Optional[Dict[str, str]] = None,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> requests.Response:
        url = self._build_url(endpoint)

        logger.info(f"[{method.upper()}] Sending request to {url}")
        if params:
            logger.info(f"Query Params: {params}")
        if json:
            logger.info(f"Request Body: {json}")
        if headers:
            logger.info(f"Headers: {headers}")
        if self.basic_auth:
            logger.info(f"auth: {self.basic_auth}")


        try:
            response = requests.request(
                method=method.upper(),
                url=url,
                headers=headers or {},
                params=params,
                json=json,
                auth=self.basic_auth,  # ✅ Basic Auth handled automatically
                timeout=self.timeout,
            )
            logger.info(f"[{method.upper()}] Response received: {response.status_code}")
            logger.info(f"Response Body: {response.text}")
            return response
        except requests.exceptions.RequestException as e:
            logger.error(f"[{method.upper()}] HTTP request failed: {e}")
            raise

    def _build_url(self, endpoint: str) -> str:
        full_url = f"{self.base_url}/{endpoint.lstrip('/')}"
        logger.info(f"Built URL: {full_url}")
        return full_url
