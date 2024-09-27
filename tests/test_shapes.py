"""Test the shapes module."""

import pytest

from pytestexamples import shapes


@pytest.mark.parametrize(
    ("shape", "area", "feret_diameter_max", "centroid"),
    [
        pytest.param("square", 24, 9.219544457292887, (4, 4), id="summary of square"),
        pytest.param("circle", 12, 5.385164807134504, (4, 4), id="summary of circle"),
    ],
)
def test_summarise_shape_get_fixture_value(
    shape: str, area: float, feret_diameter_max: float, centroid: tuple[int, int], request
) -> None:
    """Test the summarisation of shapes."""
    shape_summary = shapes.summarise_shape(request.getfixturevalue(shape))
    assert shape_summary[0]["area"] == area
    assert shape_summary[0]["feret_diameter_max"] == feret_diameter_max
    assert shape_summary[0]["centroid"] == centroid
