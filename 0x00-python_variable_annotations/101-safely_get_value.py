#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary.
"""


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, Any], key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary. If the key exists in the dictionary,
    returns its value. Otherwise, returns the default value.
    """

    if key in dct:
        return dct[key]
    else:
        return default
