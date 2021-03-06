"""Exceptions for Dingz API client."""


class DingzError(Exception):
    """General Dingz exception occurred."""

    pass


class DingzConnectionError(DingzError):
    """When a connection error is encountered."""

    pass


class DingzNoDataAvailable(DingzError):
    """When no data is available."""

    pass
