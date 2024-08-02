#!/usr/bin/env python3
"""
Module for safely getting a value from a dictionary.
"""


from typing import Any, Mapping, TypeVar, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, Any],
        key: Any,
        default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Safely gets a value from a dictionary.

    This function takes a dictionary `dct` and a key `key`. It returns the
    value associated with the key from the dictionary if the key exists in the
    dictionary. If the key does not exist in the dictionary, it returns the
    default value provided.

    Args:
        dct (Mapping[Any, Any]): The dictionary from which to get the value.
        key (Any): The key to get the value for.
        default (Union[T, None], optional): The default value to return if the
            key is not in the dictionary. Defaults to None.

    Returns:
        Union[Any, T]: The value from the dictionary if the key exists,
            otherwise the default value.
    """

    # Check if the key exists in the dictionary
    if key in dct:
        # Return the value associated with the key
        return dct[key]
    else:
        # Return the default value
        return default
