#!/usr/bin/env python3
"""
A coroutine that takes no arguments
"""

import asyncio
import random


async def async_generator() -> Generator[int, None, Nome]:
    """
    Yields 10 random numbers between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
