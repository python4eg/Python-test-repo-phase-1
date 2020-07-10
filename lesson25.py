import socket

IP = '127.0.0.1'
PORT = 65432


socket1 = socket.socket()
socket1.bind((IP, PORT))
socket1.listen()

while True:
    connection, addr = socket1.accept()
    print(f'Connected with: {addr}')
    data = connection.recv(256)
    if not data:
        continue
    print(f'Recv {data}')
    connection.send(b'Thanks YOU!')
connection.close()
socket1.close()
