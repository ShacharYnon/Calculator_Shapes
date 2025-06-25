from shape import *
from rectangle import *



class RightTriangle(Rectangle ):

    def __init__(self ,name:str ,length:float ,width:float):
        Shape.__init__(name ,length ,width)
        # self.radius = radius

    def get_area(self):
        return

    def get_perimeter(self):
        return

    def __str__(self):
        return  f"name shape: {self.name} ,area: {self.get_area():.2f} ,perimeter: {self.get_perimeter():.2f}"

    def __repr__(self):
        return f"IsoscelesTriangle(name={self.name}, radius={self.radius})"