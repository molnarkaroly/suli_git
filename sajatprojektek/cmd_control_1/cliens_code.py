import socket

client_socket = socket.socket()
client_socket.connect(('192.168.1.12', 12345))

while True:
    message = input("Enter message: ")
    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print(f"Received: {data.decode()}")
    
client_socket.close()

