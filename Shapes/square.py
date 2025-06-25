from shape import *
import math

class Square(Shape):

    def __init__(self ,name :str, side:float):
        super().__init__(name)
        self.side = side

    def get_area(self):
        return self.side * self.side

    def get_perimeter(self):
        return self.side * 4

    def __str__(self):
        return  f"name shape: {self.name} ,area: {self.get_area():.2f} ,perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return f"Square(name={self.name}, side={self.side})"
