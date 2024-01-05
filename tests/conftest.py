"""Fixtures for tests."""
import numpy as np
import numpy.typing as npt
import pytest
from skimage import draw


@pytest.fixture()
def square() -> npt.NDArray:
    """Return a 2D numpy array of a square."""
    square_array = np.zeros((9, 9), dtype=np.uint8)
    start = (2, 2)
    end = (6, 6)
    rr, cc = draw.rectangle_perimeter(start, end)
    square_array[rr, cc] = 1
    return square_array


@pytest.fixture()
def circle() -> npt.NDArray:
    """Return a 2D numpy array of a circle."""
    circle_array = np.zeros((7, 7), dtype=np.uint8)
    rr, cc = draw.circle_perimeter(r=4, c=4, radius=2, shape=circle_array.shape)
    circle_array[rr, cc] = 1
    return circle_array
