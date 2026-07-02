import pytest

from clock_logic import calculate_acute_angle


@pytest.mark.parametrize(
    ("hours", "minutes", "expected"),
    [
        (3, 0, 90),
        (6, 0, 180),
        (2, 30, 105),
        (12, 15, 82.5),
        (13, 0, 30),
    ],
)
def test_calculate_acute_angle(hours, minutes, expected):
    assert calculate_acute_angle(hours, minutes) == pytest.approx(expected)
