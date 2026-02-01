import pytest

from app.main import get_human_age


@pytest.mark.parametrize(
    "cat_age, dog_age, expected",
    [
        (0, 0, [0, 0]),
        (-1, -1, [0, 0]),
        (14, 14, [0, 0]),
        (15, 15, [1, 1]),
        (23, 23, [1, 1]),
        (24, 24, [2, 2]),
        (100, 100, [21, 17])
    ],
    ids=[
        "test_returns_zero_when_age_is_zero",
        "test_returns_zero_when_age_is_negative",
        "test_returns_zero_when_age_below_first_threshold_15_years",
        "test_returns_one_when_age_equals_first_threshold_15_years",
        "test_returns_one_when_age_between_thresholds_15_and_24_years",
        "test_returns_two_when_age_equals_24_years",
        "test_returns_expected_values_for_extreme_ages",
    ]
)
def test_get_human_age(cat_age: int, dog_age: int, expected: str) -> None:
    assert get_human_age(cat_age, dog_age) == expected
