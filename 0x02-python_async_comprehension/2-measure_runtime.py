#!/usr/bin/env python3
""" a module for the function measure_runtime """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Measures the total runtime of executing async_comprehension
    four times in parallel.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension())
    total_time = time.perf_counter() - start
    return total_time
