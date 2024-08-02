#!/usr/bin/env python3
"""
Module for zooming in on elements of a tuple.
"""


from typing import List, Tuple


def zoom_array(lst: Tuple[int, ...], factor: int = 2) -> List[int]:
    """
    Zoom in on elements of a tuple by a given factor.

    Parameters:
        lst (Tuple[int, ...]): A tuple of integers.
        factor (int, optional): The factor by which to zoom in on the elements.
            Defaults to 2.

    Returns:
        List[int]: A list with elements repeated according to the factor.
    """

    # Create a list by repeating each element in the tuple 'factor' times.
    zoomed_in = [item for item in lst for _ in range(factor)]

    return zoomed_in


array = (12, 72, 91)  # Convert the list to a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
