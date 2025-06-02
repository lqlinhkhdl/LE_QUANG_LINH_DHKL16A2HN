import socket
import time
import random

HOST = 'localhost'
PORT = 12345
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))
for i in range(10):
    temp = round(random.uniform(25.0, 35.0), 2)
    message = f'nhiệt độ: {temp} C'
    client_socket.sendall(message.encode())
    print(f'[CLIENT]: {message}')
    time.sleep(2)
client_socket.close()