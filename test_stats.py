import pytest

from stats import letter_grade, mean, median, pass_rate


def test_mean_basic():
    assert mean([1, 2, 3]) == 2.0


def test_mean_empty_raises():
    with pytest.raises(ValueError):
        mean([])


def test_median_odd():
    assert median([3, 1, 2]) == 2


def test_median_even():
    assert median([1, 2, 3, 4]) == 2.5


def test_median_empty_raises():
    with pytest.raises(ValueError):
        median([])


def test_pass_rate_normal():
    assert pass_rate([50, 60, 70, 80]) == 0.75


def test_pass_rate_custom_threshold():
    assert pass_rate([50, 60, 70, 80], threshold=70) == 0.5


def test_pass_rate_empty_raises():
    with pytest.raises(ValueError):
        pass_rate([])


def test_letter_grade_all_bands():
    assert letter_grade(95) == "A"
    assert letter_grade(85) == "B"
    assert letter_grade(75) == "C"
    assert letter_grade(65) == "D"
    assert letter_grade(30) == "F"
