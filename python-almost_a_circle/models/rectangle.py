#!/usr/bin/python3
"""
This module defines a class named Rectangle that inherits from Base
"""
from base import Base


class Rectangle(Base):
    """This is a class Rectnagle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method creates new instances of Rectangle"""
        super().__init__(self, id=None)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value)
        self.__height = value
    
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        self.__x = x
    
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value)
        return self.__y
