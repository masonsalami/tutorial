import pytest

from project.utils import mean


def test_mean_returns_float():
    assert mean([1, 2]) == 1.5


def test_mean_empty_values():
    with pytest.raises(ValueError):
        mean([])
