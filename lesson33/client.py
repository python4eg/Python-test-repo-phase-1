import asyncio
import json
from sys import stdout

class Client(asyncio.Protocol):
    def __init__(self, loop, user):
        self.user = user
        self.is_open = False
        self.loop = loop
        self.output_callback = None

    def set_output_callback(self, output):
        self.output_callback = output

    def connection_made(self, transport):
        self.transport = transport
        self.is_open = True
        self.send(self.user, 'user_name')

    def connection_lost(self, exc):
        self.is_open = False
        self.loop.stop()

    def print_data(self, json_data):
        message = f'[{json_data["time"]}] {json_data["sender"]}: {json_data["message"]}'
        if self.output_callback is None:
            stdout.write(message)
        else:
            self.output_callback(message)

    def data_received(self, data):
        if data:
            decoded_data = data.decode()
            print(decoded_data)
            json_data = json.loads(decoded_data)
            if isinstance(json_data, list):
                for item in json_data:
                    self.print_data(item)
            elif isinstance(json_data, dict):
                self.print_data(json_data)
            else:
                print(f'Unexpected data received')

    def send(self, message, message_type='message'):
        data = json.dumps({'type': message_type, 'message': message})
        self.transport.write(data.encode())
