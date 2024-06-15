import pytest
from src.square import Square


@pytest.mark.parametrize("side_a", [3, 5])
def test_square(side_a):
    s = Square(side_a)
    assert s.get_area == side_a * side_a
    assert s.get_perimeter == 4 * side_a


@pytest.mark.parametrize(
    "side_a", [0, -1],
    ids=["zero value", "negative value"]
)
def test_square_negative(side_a):
    with pytest.raises(ValueError, match="нельзя создать квадрат"):
        Square(side_a)

    with pytest.raises(ValueError, match="нельзя создать квадрат"):
        Square(side_a)
