import socket
import threading

def handle_client(client_socket, address):
    print("Client Connected: ",address)
    while True:
        data = client_socket.recv(1024)

        if not data or data.lower().strip() == 'exit':
            print(f"Client {address} disconnected..")
            break

        message = data.decode()
        print("Message from",address,":",message)
        # print(address, ":", data.decode())

        response = input(f"Enter message to client {address}: ")
        client_socket.send(response.encode())

    print("Client disconnected:",address)
    client_socket.close()
    
server = socket.socket()

server.bind(("127.0.0.1", 5000))

server.listen()

print("Server is listening...")

while True:
    client_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )

    thread.start()