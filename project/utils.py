"""Utility functions for basic mathematics."""

from typing import Iterable


def mean(values: Iterable[float]) -> float:
    """Calculate the arithmetic mean of ``values``.

    Parameters
    ----------
    values:
        A non-empty iterable of numbers.

    Returns
    -------
    float
        The average of the provided values.

    Raises
    ------
    ValueError
        If ``values`` is empty.
    """
    values = list(values)
    if not values:
        raise ValueError("values must not be empty")

    return sum(values) / len(values)
