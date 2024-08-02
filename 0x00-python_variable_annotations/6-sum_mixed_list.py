#!/usr/bin/env python3
""" a module contating the function sum_mixed_type """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculates the sum of a list of mixed integers and floats.

    Args:
        mxd_lst (List[Union[int, float]]): A list of integers and/or floats.

    Returns:
        float: The sum of the list elements.
    """
    # Initialize the sum to 0.0
    i: float = 0.0

    # Iterate over each element in the list
    for j in mxd_lst:
        # Add the element to the sum
        i += j

    # Return the sum
    return i
