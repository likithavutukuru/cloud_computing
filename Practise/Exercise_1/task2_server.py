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

serialized = client_socket.recv(4096)

data = pickle.loads(serialized)

print("Name:", data.name)
print("Values:", data.values)

total = sum(data.values)

client_socket.send(str(total).encode())

client_socket.close()
server.close()