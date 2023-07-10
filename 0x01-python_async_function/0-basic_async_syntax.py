#!/usr/bin/env python3

"""import modules for the task"""
import asyncio
import random


async def wait_random(max_delay=10):
    time = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time