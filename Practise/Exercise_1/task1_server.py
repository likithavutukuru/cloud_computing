import socket

server = socket.socket()

server.bind(("127.0.0.1", 5000))

server.listen(5)

print("Server waiting for client...")

client_socket, address = server.accept()

print("Connected to:", address)

data = client_socket.recv(1024).decode()

numbers = [int(x) for x in data.split()]

total = sum(numbers)

client_socket.send(str(total).encode())

client_socket.close()
server.close()