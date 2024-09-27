"""Example code for pytest-mpl exposition."""

import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt


def scatter(
    n_obs: int,
    figsize: tuple[int, int],
    title: str | None = None,
    cmap: str = "green",
    seed: int = 3513387,
) -> tuple:
    """Generate a scatter plot of x v y with histograms of each on the border.

    This example is taken from the `Scatter Histogram Example
    <https://matplotlib.org/stable/gallery/lines_bars_and_markers/scatter_hist.html>`_.

    Parameters
    ----------
    n_obs : int
        Number of random observations to generate.
    figsize : tuple[int, int]
        Shape to plot.
    cmap : str
        Colour to use for plotting.
    seed : int
        Seed for pseudo-random number generation.

    Returns
    -------
    tuple(fig, ax)

    """
    # Generate two random sets of numbers
    x = np.random.randn(n_obs)
    y = np.random.randn(n_obs)
    # Create the figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot()
    ax.scatter(x, y)

    return (fig, ax)
