# coding: utf-8

"""
    Clash Royale API - Custom Errors

    Custom exceptions for the Clash Royale API event system.
"""

from clashroyale.exceptions import ApiException


class Maintenance(ApiException):
    """Exception raised when the API is under maintenance (503 status code).

    This exception is used by the EventsClient to detect maintenance windows
    and pause polling until the API is available again.
    """
    pass


class NotFound(ApiException):
    """Exception raised when a resource is not found (404 status code).

    This is typically raised when a player or clan tag doesn't exist.
    """
    pass


class InvalidTag(ApiException):
    """Exception raised when an invalid tag format is provided."""
    pass


class PrivateWarLog(ApiException):
    """Exception raised when trying to access a private war log."""
    pass
