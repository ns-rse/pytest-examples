"""Tests of the mpl_example module."""

import numpy as np
import numpy.typing as npt
import pytest
from pytest_examples import mpl_example

np.random.seed(324985)


@pytest.mark.mpl_image_compare(baseline_dir="resources/img")
@pytest.mark.parametrize(
    ("n_obs", "figsize", "title", "cmap", "seed"),
    [
        pytest.param(300, (6, 6), None, "green", 3513387, id="300 points; 6x6; no title; green"),
        pytest.param(3000, (6, 6), "Lots of points!", "green", 3513387, id="3000 points; 6x6; Lots of points; blue"),
    ],
)
def test_scatter_hist(n_obs: int, figsize: tuple[int, int], title: str, cmap: str, seed: int) -> None:
    """Test of the scatter_hist() function."""
    fig = mpl_example.scatter(n_obs, figsize, title, cmap, seed)
    return fig
