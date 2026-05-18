"""Common argument specs and constants for NVIDIA NIM inference microservices."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = r"""
---
module_utils: nvidia_common
short_description: Shared argument specs and constants for NVIDIA NIM inference microservices
description:
  - Defines NVIDIA_COMMON_ARGS, the common argument spec shared by all modules.
  - Provides lifecycle state constants and helper functions.
author:
  - Steve Fulmer (@stevefulme1)
"""


NVIDIA_COMMON_ARGS = dict(
    api_url=dict(type="str", default="https://api.nim.nvidia.com"),
    api_key=dict(type="str", no_log=True),
    validate_certs=dict(type="bool", default=True),
    timeout=dict(type="int", default=60),
    wait=dict(type="bool", default=True),
    wait_timeout=dict(type="int", default=1200),
    wait_interval=dict(type="int", default=30),
)

STATE_ACTIVE = "ACTIVE"
STATE_READY = "READY"
STATE_RUNNING = "RUNNING"
STATE_CREATING = "CREATING"
STATE_DELETED = "DELETED"
STATE_DELETING = "DELETING"
STATE_FAILED = "FAILED"
STATE_STOPPED = "STOPPED"
STATE_COMPLETED = "COMPLETED"

READY_STATES = frozenset({
    STATE_ACTIVE,
    STATE_READY,
    STATE_RUNNING,
    STATE_COMPLETED,
})

DEAD_STATES = frozenset({
    STATE_DELETED,
})

WAIT_STATES = frozenset({
    STATE_CREATING,
    STATE_DELETING,
})


def to_dict(resource):
    """Convert a resource object or dict to a plain dictionary."""
    if resource is None:
        return {}
    if isinstance(resource, dict):
        return resource
    if hasattr(resource, "__dict__"):
        result = {}
        for key, value in resource.__dict__.items():
            if key.startswith("_"):
                continue
            if isinstance(value, list):
                result[key] = [to_dict(i) if hasattr(i, "__dict__") else i for i in value]
            elif hasattr(value, "__dict__") and not isinstance(value, (str, int, float, bool, dict)):
                result[key] = to_dict(value)
            else:
                result[key] = value
        return result
    return resource
