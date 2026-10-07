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