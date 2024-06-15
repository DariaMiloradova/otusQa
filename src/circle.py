import math
from src.figure import Figure


class Circle(Figure):
    def __init__(self, radius):
        super().__init__(name="Circle")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius
