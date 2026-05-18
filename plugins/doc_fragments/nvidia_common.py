# -*- coding: utf-8 -*-
# Copyright (c) 2024, Steve Fulmer
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""Documentation fragment for NVIDIA NIM inference microservices."""

from __future__ import absolute_import, division, print_function

__metaclass__ = type


class ModuleDocFragment:
    """Documentation fragment for NVIDIA common options."""

    DOCUMENTATION = r"""
options:
    api_url:
        description:
            - The URL of the NVIDIA API endpoint.
        type: str
        default: "https://api.nim.nvidia.com"
    api_key:
        description:
            - The API key for authentication.
        type: str
    validate_certs:
        description:
            - Whether to validate SSL certificates.
        type: bool
        default: true
    timeout:
        description:
            - Request timeout in seconds.
        type: int
        default: 60
    wait:
        description:
            - Whether to wait for the resource to reach the desired state.
        type: bool
        default: true
    wait_timeout:
        description:
            - Maximum time in seconds to wait.
        type: int
        default: 1200
    wait_interval:
        description:
            - Interval in seconds between state checks.
        type: int
        default: 30
"""
