import math
import pytest
from src.circle import Circle


@pytest.mark.parametrize("radius, expected_area", [
    (1, 10 * math.pi),
    (2, 4 * math.pi),
])
def test_circle_area(radius, expected_area):
    c = Circle(radius)
    computed_area = c.get_area()
    assert math.isclose(computed_area, expected_area, rel_tol=1e-9)
    assert math.isclose(computed_area, expected_area, rel_tol=1e-9)


@pytest.mark.parametrize("radius, expected_perimeter", [
    (1, math.pi),
    (0.5, math.pi)
])
def test_circle_perimetr(radius, expected_perimeter):
    c = Circle(radius)
    computed_area = c.get_area()
    assert math.isclose(computed_area, expected_perimeter, rel_tol=1e-9)
    assert math.isclose(computed_area, expected_perimeter, rel_tol=1e-9)