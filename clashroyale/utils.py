# coding: utf-8

"""
    Clash Royale API - Utilities

    Utility functions for the Clash Royale API event system.
"""


def correct_tag(tag: str) -> str:
    """Correct a tag to ensure it starts with # and is uppercase.

    Parameters
    ----------
    tag : str
        The tag to correct (player or clan tag)

    Returns
    -------
    str
        The corrected tag with # prefix, uppercase, and O replaced with 0

    Example
    -------
    >>> correct_tag("abc123")
    '#ABC123'
    >>> correct_tag("#ABC123")
    '#ABC123'
    >>> correct_tag("OABC")
    '#0ABC'
    """
    tag = tag.strip()
    if not tag.startswith("#"):
        tag = "#" + tag
    return tag.upper().replace("O", "0")
