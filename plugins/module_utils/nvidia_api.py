"""API client for NVIDIA NIM inference microservices."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module_utils: nvidia_api
short_description: REST API client for NVIDIA NIM inference microservices
description:
  - Provides a lightweight REST client for the NVIDIA API.
  - Handles authentication, request construction, and error handling.
author:
  - Steve Fulmer (@stevefulme1)
"""

import json
import time

try:
    import requests
    HAS_REQUESTS = True
except ImportError:
    HAS_REQUESTS = False


class NvidiaApiError(Exception):
    """Exception for NVIDIA API errors."""

    def __init__(self, status, message, response=None):
        self.status = status
        self.message = message
        self.response = response
        super().__init__(f"HTTP {status}: {message}")


class NvidiaApiClient:
    """REST client for NVIDIA NIM inference microservices."""

    def __init__(self, api_url, api_key=None, validate_certs=True, timeout=60):
        self.api_url = api_url.rstrip("/")
        self.api_key = api_key
        self.validate_certs = validate_certs
        self.timeout = timeout
        self.session = requests.Session()
        if api_key:
            self.session.headers["Authorization"] = f"Bearer {api_key}"
        self.session.headers["Content-Type"] = "application/json"
        self.session.headers["Accept"] = "application/json"

    def request(self, method, path, data=None, params=None):
        """Send an API request with retry logic."""
        url = f"{self.api_url}{path}"
        last_error = None
        for attempt in range(4):
            try:
                resp = self.session.request(
                    method=method,
                    url=url,
                    json=data,
                    params=params,
                    verify=self.validate_certs,
                    timeout=self.timeout,
                )
                if resp.status_code >= 400:
                    msg = resp.text
                    try:
                        msg = resp.json().get("message", resp.text)
                    except (ValueError, AttributeError):
                        pass
                    if resp.status_code in (429, 500, 503) and attempt < 3:
                        time.sleep(2 ** attempt)
                        continue
                    raise NvidiaApiError(resp.status_code, msg, resp)
                if resp.status_code == 204:
                    return None
                if resp.content:
                    return resp.json()
                return None
            except requests.ConnectionError as exc:
                last_error = exc
                if attempt < 3:
                    time.sleep(2 ** attempt)
                    continue
                raise
        raise last_error  # pragma: no cover

    def get(self, path, params=None):
        """Send GET request."""
        return self.request("GET", path, params=params)

    def post(self, path, data=None):
        """Send POST request."""
        return self.request("POST", path, data=data)

    def put(self, path, data=None):
        """Send PUT request."""
        return self.request("PUT", path, data=data)

    def patch(self, path, data=None):
        """Send PATCH request."""
        return self.request("PATCH", path, data=data)

    def delete(self, path):
        """Send DELETE request."""
        return self.request("DELETE", path)


def create_api_client(module):
    """Create an NvidiaApiClient from module params."""
    if not HAS_REQUESTS:
        module.fail_json(msg="The 'requests' Python library is required. Install with: pip install requests")
    return NvidiaApiClient(
        api_url=module.params["api_url"],
        api_key=module.params.get("api_key"),
        validate_certs=module.params.get("validate_certs", True),
        timeout=module.params.get("timeout", 60),
    )
