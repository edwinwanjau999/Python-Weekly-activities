import math
from abc import ABC, abstractmethod

#Create an abstract class named Shape
class Shape(ABC):
    
    #Define an abstract method named area()
    @abstractmethod
    def area(self):
        """Abstract method that must be implemented by all subclasses."""
        pass


#Create a class named Circle that inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    #Implement area() in Circle using: Area = π × radius²
    def area(self):
        return math.pi * (self.radius ** 2)


#Create a class named Rectangle that inherits from Shape
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    #Implement area() in Rectangle using: Area = Length × Width
    def area(self):
        return self.length * self.width


if __name__ == "__main__":
    # vii. Create one circle object and one rectangle object
    my_circle = Circle(radius=7.0)
    my_rectangle = Rectangle(length=12.5, width=4.0)

    circle_area = my_circle.area()
    rectangle_area = my_rectangle.area()

    print("--- Engineering Shape Area Calculation ---")
    print(f"Circle (Radius: {my_circle.radius})     : Area = {circle_area:,.2f}")
    print(f"Rectangle (L: {my_rectangle.length}, W: {my_rectangle.width}): Area = {rectangle_area:,.2f}")

    print("\n--- Polymorphic Behavior Across Mixed Shapes ---")
    shape_collection = [Circle(5.0), Rectangle(8.0, 3.0), Circle(10.0)]
    
    for shape in shape_collection:
        print(f"Shape: {type(shape).__name__:<10} | Area: {shape.area():,.2f}")
