"""Waiter utilities for NVIDIA NIM inference microservices."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module_utils: nvidia_wait
short_description: Waiter utilities for NVIDIA NIM inference microservices
description:
  - Provides wait_for_state to poll a resource until it reaches a target state.
author:
  - Steve Fulmer (@stevefulme1)
"""

import time

from ansible_collections.stevefulme1.nvidia_nim.plugins.module_utils.nvidia_api import (
    NvidiaApiError,
)


def wait_for_state(module, client, path, target_states, failure_states=None):
    """Poll a resource until it reaches a target state."""
    wait = module.params.get("wait", True)
    if not wait:
        try:
            return client.get(path)
        except NvidiaApiError:
            return None

    timeout = module.params.get("wait_timeout", 1200)
    interval = module.params.get("wait_interval", 30)

    if failure_states is None:
        failure_states = frozenset({"FAILED"})

    start = time.monotonic()
    while True:
        try:
            resource = client.get(path)
        except NvidiaApiError as exc:
            if exc.status == 404 and "DELETED" in target_states:
                return None
            raise

        state = resource.get("status") or resource.get("state", "")
        if state.upper() in target_states:
            return resource
        if state.upper() in failure_states:
            module.fail_json(
                msg=f"Resource entered failure state: {state}",
            )

        elapsed = time.monotonic() - start
        if elapsed >= timeout:
            module.fail_json(
                msg=f"Timed out waiting for resource. Current state: {state}",
            )
        time.sleep(min(interval, timeout - elapsed))
