#!/usr/bin/env python3
"""
Module for zooming in on elements of a tuple.
"""

from typing import List, Tuple, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Zoom in on elements of a tuple by a given factor.

    :param lst: Tuple of elements
    :param factor: Factor by which to zoom in on the elements
    :return: A list with elements repeated according to the factor
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Convert the list to a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
