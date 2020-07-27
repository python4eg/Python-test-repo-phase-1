import asyncio

async def callback():
    print('waiting for first')
    result1 = await first()
    print('waiting for second')
    result2 = await second(result1)
    return result1, result2


async def first():
    await asyncio.sleep(1)
    print('in first')
    await asyncio.sleep(1)
    return 'result1'


async def second(arg):
    print('in second')
    return 'Received from first: {}'.format(arg)


event_loop = asyncio.get_event_loop()
try:
    return_value = event_loop.run_until_complete(callback())
    print('{}'.format(return_value))
finally:
    event_loop.close()
