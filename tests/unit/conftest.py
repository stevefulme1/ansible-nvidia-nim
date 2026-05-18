"""Shared pytest fixtures for nvidia_nim collection unit tests."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import sys
import types
from unittest.mock import MagicMock

import pytest

_collection_root = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
_namespace_root = os.path.abspath(os.path.join(_collection_root, os.pardir, os.pardir))
if os.path.isdir(os.path.join(_namespace_root, "ansible_collections")) and _namespace_root not in sys.path:
    sys.path.insert(0, _namespace_root)

try:
    import ansible_collections.stevefulme1.nvidia_nim  # noqa: F401
except (ImportError, ModuleNotFoundError):
    for _pkg_name in ("ansible_collections", "ansible_collections.stevefulme1"):
        if _pkg_name not in sys.modules:
            _pkg = types.ModuleType(_pkg_name)
            _pkg.__path__ = []
            _pkg.__package__ = _pkg_name
            sys.modules[_pkg_name] = _pkg

    _coll_mod = types.ModuleType("ansible_collections.stevefulme1.nvidia_nim")
    _coll_mod.__path__ = [_collection_root]
    _coll_mod.__package__ = "ansible_collections.stevefulme1.nvidia_nim"
    sys.modules["ansible_collections.stevefulme1.nvidia_nim"] = _coll_mod

    sys.modules["ansible_collections"].stevefulme1 = sys.modules["ansible_collections.stevefulme1"]
    sys.modules["ansible_collections.stevefulme1"].nvidia_nim = _coll_mod


@pytest.fixture
def module_args():
    """Return a base dict of common module arguments."""
    return {
        "api_url": "https://api.nim.nvidia.com",
        "api_key": "test-api-key",
        "validate_certs": True,
        "timeout": 60,
        "wait": True,
        "wait_timeout": 1200,
        "wait_interval": 30,
        "state": "present",
    }


@pytest.fixture
def mock_api_client():
    """Factory fixture that returns a MagicMock configured as an API client."""
    def _factory(client_name: str = "GenericClient") -> MagicMock:
        client = MagicMock(name=client_name)
        return client
    return _factory
