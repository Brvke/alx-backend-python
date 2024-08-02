#!/usr/bin/env python3
"""
Module for safely getting the first element of a sequence.
"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Returns the first element of the list if it exists, if not returns None.

    :param lst: Sequence of elements
    :return: The first element of the sequence or None
    """
    if lst:
        return lst[0]
    else:
        return None
