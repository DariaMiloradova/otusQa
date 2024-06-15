import math
import pytest
from src.triangle import Triangle


@pytest.mark.parametrize("side_a, side_b, side_c", [
    (2, 4, 5),
    (5, 5, 5),
    (1.9, 100, 2.5),
])
def test_triangle(side_a, side_b, side_c):
    t = Triangle(side_a, side_b, side_c)
    perimeter = (side_a + side_b + side_c) / 2
    expected_area = math.sqrt(perimeter * (perimeter - side_a) *
                              (perimeter - side_b) * (perimeter - side_c))
    assert t.get_area() == expected_area
    assert t.get_perimeter() == perimeter

@pytest.mark.parametrize("side_a, side_b, side_c", [
    (1, 1, 3),
])
def test_triangle_invalid_side(side_a, side_b, side_c):
    with pytest.raises(ValueError, match="нельзя создать треугольник"):
        Triangle(side_a, side_b, side_c)
