#!/usr/bin/env python3
"""
A module containing the `element_length` function.

"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Generate a list of tuples
    """
    return [(i, len(i)) for i in lst]
