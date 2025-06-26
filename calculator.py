# from circle import Circle
# from rectangle import Rectangle
# from square import Square
# from triangle import Triangle
# from hexagon import Hexagon
from Shapes import *


def get_circle():
    radius = float(input("Enter the radius of the circle: "))
    circle = Circle(radius)
    print(f"\n🔵 Circle Info:\n{circle}")

def get_hexagon():
    side_length = float(input("Enter the side length of the hexagon: "))
    hexagon = Hexagon(side_length)
    print(f"\n⬡ Hexagon Info:\n{hexagon}")

def get_rectangle():
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    rectangle = Rectangle(length ,width)
    print(f"\n📏 Rectangle Info:\n{rectangle}")

def get_square():
    side = float(input("Enter the side of the square: "))
    square = Square(side)
    print(f"\n⬛ Square Info:\n{square}")

def get_right_triangle():
    length = float(input("Enter the length of the Right_Triangle: "))
    width = float(input("Enter the width of the Right_Triangle: "))
    right_triangle = RightTriangle(length ,width)
    print(f"\n🔺 RightTriangle Info:\n{right_triangle}")









