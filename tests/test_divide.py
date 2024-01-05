"""Example pytests showing parameterisation and testing of failures."""
from __future__ import annotations

import pytest

from pytest_examples.divide import divide


def test_divide_unparameterised() -> None:
    """Test the divide function."""
    assert divide(10, 5) == 2


@pytest.mark.parametrize(
    ("a", "b", "expected"),
    [
        pytest.param(10, 5, 2, id="ten divided by five"),
        pytest.param(9, 3, 3, id="nine divided by three"),
        pytest.param(5, 2, 2.5, id="five divided by two"),
        pytest.param(0, 100, 0, id="zero divided by one hundred"),
        pytest.param(10, 0, ZeroDivisionError, id="zero division error", marks=pytest.mark.xfail),
    ],
)
def test_divide(a: float | int, b: float | int, expected: float) -> None:
    """Test the divide function."""
    assert divide(a, b) == expected


@pytest.mark.parametrize(
    ("a", "b", "exception"),
    [
        pytest.param("a", 5, TypeError, id="a is string"),
        pytest.param(9, "b", TypeError, id="b is string"),
        pytest.param([1], 2, TypeError, id="a is list"),
        pytest.param(10, [2], TypeError, id="b is list"),
    ],
)
def test_divide_type_errors(a: float | int, b: float | int, exception: TypeError) -> None:
    """Test that TypeError is raised when objects other than int or float are passed as a and b."""
    with pytest.raises(exception):
        divide(a, b)


@pytest.mark.parametrize(
    ("a", "b", "exception"),
    [
        pytest.param(10, 0, ZeroDivisionError, id="b is zero"),
    ],
)
def test_divide_zero_division_error(a: float | int, b: float | int, exception: ZeroDivisionError) -> None:
    """Test that ZeroDivsionError is raised when attempting to divide by zero."""
    with pytest.raises(exception):
        divide(a, b)
