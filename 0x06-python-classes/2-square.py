#!/usr/bin/python3
class Square:
    """
    Square class represents a square.

    Attributes:
        size (int): Size of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            size (int, optional): Size of the square. Defaults to 0.
        """
        self.__size = size
        self.__validate_size()

    def __validate_size(self):
        """
        Validates the size attribute.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        elif self.__size < 0:
            raise ValueError("size must be >= 0")
