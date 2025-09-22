#!/usr/bin/python3
"""Example using Abstract Base Classes and duck typing with shapes."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for all shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle shape."""

    def __init__(self, radius):
        """Initialize a circle with a given radius."""
        self.radius = radius

    def area(self):
        """Return the area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return the perimeter (circumference) of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape."""

    def __init__(self, width, height):
        """Initialize a rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return the area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return the perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print the area and perimeter of a shape (duck typing)."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
