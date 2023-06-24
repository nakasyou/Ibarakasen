import requests
import asyncio

async def request_from_async(*args):
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(None, requests.get, *args)