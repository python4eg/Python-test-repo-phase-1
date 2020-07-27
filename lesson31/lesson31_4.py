import asyncio
from aiohttp_requests import requests
import time
import random

async def one_more(id=1, delay=3000):
    print(f'w{id} request')
    t1 = time.time()
    resp = await requests.get(f'http://slowwly.robertomurray.co.uk/delay/{delay}/url/http://www.google.co.uk')
    print(f'w{id} resp')
    data = await resp.text()
    print(f'time: {time.time() - t1}')
    print(f'w{id} return')
    return data


second_event_loop = asyncio.get_event_loop()
try:
    for i in range(10):
        second_event_loop.create_task(one_more(i, random.random()*2000))
    second_event_loop.run_forever()
finally:
    second_event_loop.close()
