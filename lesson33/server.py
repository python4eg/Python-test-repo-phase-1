import asyncio
import json

from datetime import datetime


class EchoServerProtocol(asyncio.Protocol):
    def __init__(self, transports, messages):
        self.transports = transports
        self.messages = messages
        self.username = 'Unknown user'

    def connection_made(self, transport):
        self.peername = transport.get_extra_info('peername')
        print(f'Connection from {self.peername!r}')

        self.transport = transport
        messages = [{'message': 'Welcome to out chat!'}]
        messages.extend(self.messages[-5:])
        if self.messages:
            messages.append({'message': '_'*10 + f'Last {len(self.messages[-5:])} messages' + '_'*10})
        self.transport.write(json.dumps(messages).encode())
        self.transports.append(self.transport)

    def data_received(self, data):
        decoded_data = data.decode()
        json_data = json.loads(decoded_data)
        if json_data.get('type') == 'user_name':
            self.username = json_data.get('message', self.username)
        elif json_data.get('type') == 'message':
            print(f'Data received: {json_data!r}')
            message = self.get_message(json_data.get('message', ''))
            for transport in self.transports:
                transport.write(json.dumps(message).encode())
            self.messages.append(message)

    def connection_lost(self, exc):
        error_message = str(exc)
        if isinstance(exc, ConnectionResetError):
            self.transports.remove(self.transport)
            error_message = exc.strerror

        message = f'User disconnected. Reason: {error_message!r}'
        message_data = self.get_message(message)
        for transport in self.transports:
            transport.write(json.dumps(message_data).encode())

    def get_message(self, message):
        return {
            'message': message,
            'sender': self.username,
            'time': datetime.utcnow().strftime('%m/%d/%Y, %H:%M:%S')
        }


async def main():
    loop = asyncio.get_running_loop()
    transports = []
    messages = []
    server = await loop.create_server(lambda: EchoServerProtocol(transports, messages),
                                      '127.0.0.1',
                                      8888)

    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(main())