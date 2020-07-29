import asyncio
import json

clients = []

msg = []

async def server_handler(reader, writer):
    data = await reader.read(100)
    message_data = data.decode()
    message_json = json.loads(message_data)
    addr = writer.get_extra_info('peername')
    clients.append(writer)
    print(f"Get {message_json['message']} from {message_json['sender']}")
    msg.append(data)
    print(f"Send to all clients: {message_json['message']}")
    for client in clients:
        if client == writer:
            for m in msg:
                client.write(m)
                client.write('\n'.encode())
        else:
            client.write(data)
        await client.drain()



async def main():
    server = await asyncio.start_server(server_handler, '127.0.0.1', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())