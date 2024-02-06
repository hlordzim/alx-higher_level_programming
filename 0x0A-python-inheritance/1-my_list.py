#!/usr/bin/python3
"""Defines an inherited list Mylist"""


class MyList(list):
    """Inherits from list and provides additional method print_sorted."""

    def print_sorted(self):
        """Print the list in sorted order (ascending)."""
        sorted_list = sorted(self)
        print(sorted_list)
