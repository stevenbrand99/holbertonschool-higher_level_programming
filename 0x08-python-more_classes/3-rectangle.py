#!/usr/bin/python3
"""This module defines the class Rectangle"""


class Rectangle:
    """Class that builds a rectangle"""

    def __init__(self, width=0, height=0):
        """
        Initializes instance of the rectangle
        Args:
            width: width for __width attribute
            height: height for __height atributte
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """
        Getter function of height
        Returns:
            The height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter function of height
        Args:
            value: value for __height attribute
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """
        Getter function of width
        Returns:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter function of width
        Args:
            value: value for __width attribute
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """
        Funtion that returns the area of a rectangle instance
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Function that returns the perimeter of a rectangle instance
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
        Return the rectangle in a string representation
        """

        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        for row in range(self.__height):
            for _ in range(self.__width):
                string += "#"
            if row < self.__height - 1:
                string += "\n"
        return string
