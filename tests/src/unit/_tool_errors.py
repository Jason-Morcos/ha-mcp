"""Reads the error object out of a raised ToolError."""

from __future__ import annotations

import json
from collections.abc import Awaitable
from typing import Any

import pytest

from ha_mcp._vendor.fastmcp.exceptions import ToolError


def _error(exc_info: pytest.ExceptionInfo[ToolError]) -> dict[str, Any]:
    error: dict[str, Any] = json.loads(str(exc_info.value))["error"]
    return error


async def _tool_error(call: Awaitable[Any]) -> dict[str, Any]:
    """The error payload of a tool call that must fail."""
    with pytest.raises(ToolError) as excinfo:
        _ = await call
    error: dict[str, Any] = json.loads(str(excinfo.value))
    return error
