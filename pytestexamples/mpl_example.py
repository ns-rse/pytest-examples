"""Example code for pytest-mpl exposition."""

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure


def scatter(
    n_obs: int,
    figsize: tuple[int, int],
    title: str | None = None,
    seed: int = 3513387,
) -> tuple[Figure, Axes]:
    """
    Generate a scatter plot of 'x' v 'y' with histograms of each on the border.

    Parameters
    ----------
    n_obs : int
        Number of random observations to generate.
    figsize : tuple[int, int]
        Shape to plot.
    title : str | None
        Title to add to the plot.
    seed : int
        Seed for pseudo-random number generation.

    Returns
    -------
    tuple(fig, ax)
        Returns a Matplotlib figure and axis.
    """
    # Generate two random sets of numbers
    rng = np.random.default_rng(seed)
    x = rng.random(n_obs)
    y = rng.random(n_obs)
    # Create the figure
    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot()
    ax.scatter(x, y)
    plt.title(title)

    return (fig, ax)
