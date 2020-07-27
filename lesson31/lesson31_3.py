import asyncio
import random

q = asyncio.Queue(10)
event_loop = asyncio.get_event_loop()


async def produce():
    while True:
        if q.full():
            await asyncio.sleep(0.5 + random.random())
            print('is full')
            continue
        await q.put(random.random() * 10)


async def consume(index):
    while True:
        if q.empty():
            await asyncio.sleep(0.5 + random.random())
            print('is empty')
            continue
        value = await q.get()
        print(f'Consumer {index}: consumed {value}')
        await asyncio.sleep(random.random())

event_loop.create_task(produce())
event_loop.create_task(consume(1))
event_loop.create_task(consume(2))
event_loop.run_forever()