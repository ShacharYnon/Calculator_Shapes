from shape import *
import math

class Hexagon(Shape):
    def __init__(self ,side_length):
        super().__init__(self)
        self.side_length = side_length

    def get_area(self):
        return (3 * math.sqrt(3) / 2) * (self.side_length ** 2)

    def get_primer(self):
        return self.side_length * 6

    def __str__(self):
        return  f"name shape: {self.name} ,area: {self.get_area():.2f} ,perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return f"Hexagon(name={self.name}, rib_length={self.side_length})"