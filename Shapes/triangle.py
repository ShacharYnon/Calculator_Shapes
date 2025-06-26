from .rectangle import Rectangle
import math


class RightTriangle(Rectangle):

    def __init__(self, length: float, width: float ):
        super().__init__(length, width)
        self.name = "Right Triangle"

    def get_area(self):
        return super().get_area() / 2

    def get_perimeter(self):
        hypotenuse =  math.hypot(self.length ,self.width)
        return self.length + self.width +hypotenuse

    def __str__(self):
        return  f"name shape: {self.name} ,area: {self.get_area():.2f} ,perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return f"IsoscelesTriangle(name={self.name}, length={self.length} ,width={self.width} ,hypotenuse={math.hypot(self.length ,self.width)})"