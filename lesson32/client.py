import asyncio
import json

async def client():
    while True:
        reader, writer = await asyncio.open_connection('127.0.0.1', 8888)
        message = input()
        print(f'Send to server: {message}')
        data = json.dumps({'sender': 'First', 'message': message})
        writer.write(data.encode())
        data = await reader.read(100)
        if data:
            print(f'Received: {data.decode()}')
            await asyncio.sleep(1)

asyncio.run(client())
