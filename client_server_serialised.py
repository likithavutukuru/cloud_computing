#server.py
import socket
import pickle

class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values

server = socket.socket()
server.bind(("127.0.0.1", 5000))
server.listen(5)

print("Server waiting...")

client_socket, address = server.accept()
print("Connected by:", address)

serialized = client_socket.recv(4096)

data = pickle.loads(serialized)

print("Name:", data.name)
print("Values:", data.values)

total = sum(data.values)
print("Calculated total:", total)

client_socket.send(str(total).encode())

client_socket.close()
server.close()

#client.py
import socket
import pickle

class DataObject:
    def __init__(self, name, values):
        self.name = name
        self.values = values

client = socket.socket()
client.connect(("127.0.0.1", 5000))

data = DataObject("Numbers", [10, 20, 30])

serialized = pickle.dumps(data)

client.send(serialized)

result = client.recv(1024).decode()

print("Sum:", result)

client.close()