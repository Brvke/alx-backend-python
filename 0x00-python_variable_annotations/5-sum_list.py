#!/usr/bin/env python3
""" a module holding the function sum_list """

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of all elements in the input list.

    Args:
        input_list (List[float]): A list of floats.

    Returns:
        float: The sum of all elements in the input list.
    """
    # Initialize the accumulator variable to 0.
    i: float = 0

    # Iterate over each element in the input list.
    for j in input_list:
        # Add the current element to the accumulator.
        i += j

    # Return the accumulated sum.
    return i
