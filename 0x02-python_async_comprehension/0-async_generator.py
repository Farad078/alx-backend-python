#!/usr/bin/env python3

"""import necessary modules for async generator"""
import asyncio
import random


async def async_generator():
    """The coroutine will loop 10 times when called, and
    each time it waits asynchronously for 1 second,
    then yield a random number between 0 and 10"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
