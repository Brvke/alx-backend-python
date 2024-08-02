#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary.
"""

from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary. If the key exists in the dictionary,
    returns its value. Otherwise, returns the default value.

    :param dct: Dictionary or mapping from which to get the value
    :param key: Key to look up in the dictionary
    :param default: Default value to return if key is not found
    :return: The value from the dictionary or the default value
    """
    if key in dct:
        return dct[key]
    else:
        return default
