"""Simple division function with exceptions."""

from __future__ import annotations

import sys

from loguru import logger

logger.remove()
logger.add(
    sys.stdout,
    level="INFO",
    format="<g>{time:YYYY-MM-DD HH:mm:ss.SSS}</g> | <level>{level:<8}</level> | <level>{message}</level>",
)
logger.add(
    sys.stdout,
    level="WARNING",
    format="<y>{time:YYYY-MM-DD HH:mm:ss.SSS}</y> | <level>{level:<8}</level> | <level>{message}</level>",
)
logger.add(
    sys.stderr,
    level="ERROR",
    format="<r>{time:YYYY-MM-DD HH:mm:ss.SSS}</r> | <level>{level:<8}</level> | <level>{message}</level>",
)


def divide(a: float | int, b: float | int) -> float:
    """
    Divide a by b.

    Parameters
    ----------
    a : float | int
        Number to be divided.
    b : float | int
        Number to divide by.

    Returns
    -------
    float
        Returns a divided by b.
    """
    try:
        return a / b
    except TypeError as e:
        if not isinstance(a, (int | float)):
            raise TypeError(f"Error 'a' should be int or float, not {type(a)}") from e
        raise TypeError(f"Error 'b' should be int or float, not {type(b)}") from e
    except ZeroDivisionError as e:
        raise ZeroDivisionError(f"Can not divide by {b}, choose another number.") from e
