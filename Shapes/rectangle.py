from .shape import Shape



class Rectangle(Shape):

    def __init__(self ,length:float ,width:float ,name:str = 'Rectangle' ):
        super().__init__(name)
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return (self.length * 2) + (self.width * 2)

def __str__(self):
    return  f"name shape: {self.name} ,area: {self.get_area():.2f} ,perimeter: {self.get_perimeter():.2f}"

def __repr__(self):
    return f"Rectangle(name={self.name}, length={self.length} ,width={self.width})"