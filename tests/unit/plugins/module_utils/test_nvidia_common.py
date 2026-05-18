"""Unit tests for nvidia_common module_utils."""

from __future__ import absolute_import, division, print_function
__metaclass__ = type

from ansible_collections.stevefulme1.nvidia_nim.plugins.module_utils.nvidia_common import (
    NVIDIA_COMMON_ARGS,
    READY_STATES,
    DEAD_STATES,
    to_dict,
)


class TestNvidiaCommon:
    """Tests for nvidia_common module_utils."""

    def test_common_args_has_api_url(self):
        assert "api_url" in NVIDIA_COMMON_ARGS

    def test_common_args_has_api_key(self):
        assert "api_key" in NVIDIA_COMMON_ARGS

    def test_ready_states_contains_active(self):
        assert "ACTIVE" in READY_STATES

    def test_dead_states_contains_deleted(self):
        assert "DELETED" in DEAD_STATES

    def test_to_dict_none(self):
        assert to_dict(None) == {}

    def test_to_dict_dict(self):
        d = {"key": "value"}
        assert to_dict(d) == d

    def test_to_dict_object(self):
        class Obj:
            def __init__(self):
                self.name = "test"
                self._private = "hidden"
        result = to_dict(Obj())
        assert result["name"] == "test"
        assert "_private" not in result
