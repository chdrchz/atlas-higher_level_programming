#!/usr/bin/python3
"""
This module defines a class named Rectangle that inherits from Base
"""
from base import Base


class Rectangle(Base):
    """This is a class Rectnagle that inherits from Base"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """This method creates new instances of Rectangle"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        self.__width = value

    @property
    def height(self):
        """Height property"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """Height setter"""
        self.__height = value
    
    @property
    def x(self):
        """X property"""
        return self.__x
    
    @x.setter
    def x(self, value):
        """X setter"""
        self.__x = x
    
    @property
    def y(self):
        """Y property"""
        return self.__y
    
    @y.setter
    def y(self, value):
        """Y setter"""
        return self.__y
