#!/usr/bin/env python3
"""
Duck Typing Exercise with Abstract Base Classes

This module demonstrates:
1. Abstract Base Classes (ABC) to define a blueprint for shapes
2. Duck typing to handle objects uniformly based on their behavior
3. Polymorphism through method implementation in concrete classes
"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for all shapes.
    
    This class defines the interface that all shapes must implement,
    ensuring that concrete shape classes provide area() and perimeter() methods.
    """
    
    @abstractmethod
    def area(self):
        """Calculate and return the area of the shape."""
        pass
    
    @abstractmethod
    def perimeter(self):
        """Calculate and return the perimeter of the shape."""
        pass


class Circle(Shape):
    """
    A concrete implementation of Shape for circles.
    
    Attributes:
        radius (float): The radius of the circle
    """
    
    def __init__(self, radius):
        """
        Initialize a Circle with the given radius.
        
        Args:
            radius (float): The radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """
        Calculate the area of the circle.
        
        Returns:
            float: The area of the circle (π * r²)
        """
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.
        
        Returns:
            float: The perimeter of the circle (2 * π * r)
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    A concrete implementation of Shape for rectangles.
    
    Attributes:
        width (float): The width of the rectangle
        height (float): The height of the rectangle
    """
    
    def __init__(self, width, height):
        """
        Initialize a Rectangle with the given dimensions.
        
        Args:
            width (float): The width of the rectangle
            height (float): The height of the rectangle
        """
        self.width = width
        self.height = height
    
    def area(self):
        """
        Calculate the area of the rectangle.
        
        Returns:
            float: The area of the rectangle (width * height)
        """
        return self.width * self.height
    
    def perimeter(self):
        """
        Calculate the perimeter of the rectangle.
        
        Returns:
            float: The perimeter of the rectangle (2 * (width + height))
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    Print the area and perimeter of any shape-like object.
    
    This function demonstrates duck typing - it doesn't check the type
    of the object, but simply assumes it has area() and perimeter() methods.
    If the object "walks like a duck and quacks like a duck", it's treated
    as a duck (or in this case, as a Shape).
    
    Args:
        shape: Any object that implements area() and perimeter() methods
    """
    # Duck typing in action: we don't check isinstance(shape, Shape)
    # We just trust that the object has the methods we need
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")



if __name__ == "__main__":
    # Test with Circle and Rectangle (inherit from Shape)
    circle = Circle(radius=5)
    rectangle = Rectangle(width=4, height=7)
    
    print("=== Testing with Shape subclasses ===")
    print("Circle:")
    shape_info(circle)
    print("\nRectangle:")
    shape_info(rectangle)
    
    print("\n=== Demonstrating polymorphism ===")
    shapes = [circle, rectangle]
    for i, shape in enumerate(shapes, 1):
        print(f"Shape {i}:")
        shape_info(shape)
        print()