"""Test the shapes module."""
import pytest

from pytest_examples.shapes import summarise_shape


@pytest.mark.parametrize(
    ("shape", "area", "feret_diameter_max", "centroid"),
    [
        pytest.param("square", 11, 7.810249675906654, (1.3636363636363635, 1.3636363636363635), id="summary of square"),
        pytest.param("circle", 12, 5.385164807134504, (4, 4), id="summary of circle"),
    ],
)
def test_summarise_shape_get_fixture_value(
    shape: str, area: float, feret_diameter_max: float, centroid: tuple, request
) -> None:
    """Test the summarisation of shapes."""
    shape_summary = summarise_shape(request.getfixturevalue(shape))
    assert shape_summary[0]["area"] == area
    assert shape_summary[0]["feret_diameter_max"] == feret_diameter_max
    assert shape_summary[0]["centroid"] == centroid


@pytest.mark.parametrize(
    ("shape", "area", "feret_diameter_max", "centroid"),
    [
        pytest.param(
            pytest.lazy_fixture("square"),
            11,
            7.810249675906654,
            (1.3636363636363635, 1.3636363636363635),
            id="summary of square",
        ),
        pytest.param(pytest.lazy_fixture("circle"), 12, 5.385164807134504, (4, 4), id="summary of circle"),
    ],
)
def test_summarise_shape_lazy_fixture(shape: str, area: float, feret_diameter_max: float, centroid: tuple) -> None:
    """Test the summarisation of shapes."""
    shape_summary = summarise_shape(shape)
    assert shape_summary[0]["area"] == area
    assert shape_summary[0]["feret_diameter_max"] == feret_diameter_max
    assert shape_summary[0]["centroid"] == centroid
