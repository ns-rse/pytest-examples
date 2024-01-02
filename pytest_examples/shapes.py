"""Summarise Shapes."""
import numpy.typing as npt
from skimage import measure


def summarise_shape(shape: npt.NDArray) -> list:
    """
    Summarise the region properties of a 2D numpy array using Scikit-Image.

    Parameters
    ----------
    shape : npt.NDArray
        2D binary array of a shape.

    Returns
    -------
    list
        List of Region Properties each item describing one labelled region.
    """
    return measure.regionprops(shape)
