#!/usr/bin/python3
"""
This module defines a class named Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """This is a class Rectnagle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method creates new instances of Rectangle"""
        super().__init__(id)

        self.__width = width
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        
        self.__height = height
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        
        self.__x = x
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x <= 0:
            raise ValueError("x must be > 0")

        self.__y = y
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y <= 0:
            raise ValueError("y must be > 0")

    @property
    def width(self):
        """Width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X property"""
        return self.__x

    @x.setter
    def x(self, value):
        """X setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__x = value

    @property
    def y(self):
        """Y property"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value
