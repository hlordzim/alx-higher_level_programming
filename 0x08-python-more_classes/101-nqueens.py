#!/usr/bin/python3
"""Defines a Rectangle class."""


class Rectangle:
    """Represent a rectangle."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        Rectangle.number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get/set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_dimension(value, "width")
        self.__width = value

    @property
    def height(self):
        """Get/set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_dimension(value, "height")
        self.__height = value

    def validate_dimension(self, value, dimension):
        """Validate a dimension (width or height)."""
        if not isinstance(value, int):
            raise TypeError(f"{dimension} must be an integer")
        if value < 0:
            raise ValueError(f"{dimension} must be >= 0")

    def area(self):
        """Return the area of the Rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Return the perimeter of the Rectangle."""
        return 0 if self.__width == 0 or self.__height == 0 else (self.__width * 2) + (self.__height * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Return the Rectangle with the greater area."""
        if not all(isinstance(rect, Rectangle) for rect in (rect_1, rect_2)):
            raise TypeError("Both rect_1 and rect_2 must be instances of Rectangle")
        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    def __str__(self):
        """Return the printable representation of the Rectangle."""
        return "" if self.__width == 0 or self.__height == 0 else (
            (str(self.print_symbol) * self.__width + "\n") * self.__height
        )

    def __repr__(self):
        """Return the string representation of the Rectangle."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print a message for every deletion of a Rectangle."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
