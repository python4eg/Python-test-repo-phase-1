import socket
import datetime

IP = '127.0.0.1'
PORT = 65432
msg = f'Time: {datetime.datetime.now().isoformat()}, from Zimbabwe! asd asdd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd asd aswdw asd asd asd asd asd asd asd asd asd as das das das das das das das das das das das das das daasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasdadaasdasdsadasdasda sd asd asd asd asd sas d'

socket1 = socket.socket()
socket1.connect((IP, PORT))
while True:
    socket1.sendall(bytes(msg, encoding='utf-8'))
    data = socket1.recv(256)
    print(f'Received {data}')
socket1.close()
