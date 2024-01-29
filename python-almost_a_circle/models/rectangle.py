#!/usr/bin/python3
"""
This module defines a class named Rectangle that inherits from Base
"""
from models.base import Base


class Rectangle(Base):
    """This is a class Rectnagle that inherits from Base"""
    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        """This method creates new instances of Rectangle"""
        super().__init__(id)

        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.height = height

        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.x = x

        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.y = y

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
        if value < 0:
            raise ValueError("x must be >= 0")
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
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """This method calculates the area of Rectangle"""
        return self.__width * self.__height

    def display(self):
        """This method prints the rectangle using '#'"""
        for _ in range(self.y):
            print()
        for i in range(self.height):
            print(" " * self.x + str(self.print_symbol) * self.width)

    def __str__(self):
        """This method overrides the printing"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """This method assigns attrs to args"""
        args_len = len(args)

        if args_len >= 1:
            self.id = args[0]
        if args_len >= 2:
            self.width = args[1]
        if args_len >= 3:
            self.height = args[2]
        if args_len >= 4:
            self.x = args[3]
        if args_len >= 5:
            self.y = args[4]

        for key, value in kwargs.items():
            setattr(self, key, value)

    def to_dictionary(self):
        """This method returns the dictionary representation of a Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y,
        }
