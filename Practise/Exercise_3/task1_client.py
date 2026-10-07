import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket()

client.connect((HOST, PORT))

print("Connected to server.")

while True:

    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client.send(message.encode())

    response = client.recv(1024).decode()

    print("Server:", response)

client.close()