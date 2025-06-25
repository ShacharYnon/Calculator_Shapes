class Shape:

    def __init__(self ,name):
        self.name = name

    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area()")

    def get_perimeter(self):
        raise NotImplementedError("Subclasses must implement get_perimeter()")

