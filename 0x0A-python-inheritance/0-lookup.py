#!/usr/bin/python3
"""Defines an object attributes lookup functions"""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
