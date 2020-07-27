import asyncio


async def one_more():
    await asyncio.sleep(1)
    print('in first')
    await asyncio.sleep(1)
    print('in first second time')
    return 'result1'


async def second_more():
    await asyncio.sleep(1)
    print('in second')
    return 'result2'


second_event_loop = asyncio.get_event_loop()
try:
    second_event_loop.create_task(one_more())
    second_event_loop.create_task(second_more())
    second_event_loop.run_forever()
finally:
    second_event_loop.close()