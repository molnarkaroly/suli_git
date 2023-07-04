import subprocess

message = input("Enter:...")

link_url = message[1]
result = subprocess.run(["cmd","/c" f"start {link_url} "], capture_output=True)
print(result.stdout)

'''
import socket
import os
import subprocess
import webbrowser


server_socket = socket.socket()
server_socket.bind(('192.168.1.12', 12345))
server_socket.listen(1)

client_socket, client_address = server_socket.accept()

while True:
    data = client_socket.recv(1024)
    if not data:
        break
    print(f"Received: {data.decode()}")
    
    message = data.decode()

    if message == "web_link":
        client_socket.sendall("írd a linket:".encode())
        data = client_socket.recv(1024)
        link = data.decode()
        webbrowser.open(link)

    
    client_socket.sendall(data)

client_socket.close()
server_socket.close()


'''