import socket
import time

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket()

client.connect((HOST, PORT))

print("Connected to coordinator.")

client.send("REQUEST".encode())

response = client.recv(1024).decode()

if response == "GRANT":

    print("Permission granted.")

    print("Entering Critical Section...")

    time.sleep(3)

    print("Leaving Critical Section.")

    client.send("RELEASE".encode())

client.close()