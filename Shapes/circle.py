from shape import *
import math

class Circle(Shape):

    def __init__(self ,name :str,radius :float):
        super().__init__(name)
        self.radius = radius

    pi = math.pi

    def get_area(self):
        return self.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * self.pi *  self.radius

    def __str__(self):
        return  f"name shape: {self.name} ,area: {self.get_area():.2f} ,perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return f"Circle(name={self.name}, radius={self.radius})"

