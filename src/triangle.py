import math
from src.figure import Figure


class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")
        if (side_a + side_b <= side_c) or (side_a + side_c <= side_b) or (side_b + side_c <= side_a):
            raise ValueError("нельзя создать треугольник")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return math.sqrt(self.side_a + self.side_b + self.side_c) / 2

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_b