import socket

server_socket = socket.socket()
server_socket.bind(('192.168.1.11', 12345))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")
    client_socket.sendall(data)

client_socket.close()
server_socket.close()

