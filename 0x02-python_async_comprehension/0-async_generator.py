#!/usr/bin/env python3
""" a module housing the function async_generator """
import random
import asyncio
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Asynchronous generator that yields a random number between 0 and 10,
    10 times, each time after a 1 second delay.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
