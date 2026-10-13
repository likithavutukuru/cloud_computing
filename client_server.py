#server.py
import socket

server = socket.socket()

server.bind(("127.0.0.1", 5000))

server.listen(5)

print("Server waiting for client...")

client_socket, address = server.accept()

print("Connected to:", address)

data = client_socket.recv(1024).decode()
print("Received data:", data)

numbers = [int(x) for x in data.split()]

total = sum(numbers)
print("Calculated total:", total)

client_socket.send(str(total).encode())

client_socket.close()
server.close()

#client.py
import socket

client = socket.socket()

client.connect(("127.0.0.1", 5000))

numbers = input("Enter the numbers separated by space : ")

client.send(numbers.encode())

result = client.recv(1024).decode()

print(result)

client.close()