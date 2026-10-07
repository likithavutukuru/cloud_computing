import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

cs_busy = False
waiting_queue = []

lock = threading.Lock()


def handle_process(client_socket, address):

    global cs_busy

    while True:

        data = client_socket.recv(1024)

        if not data:
            break

        message = data.decode()

        print("Message from", address, ":", message)

        if message == "REQUEST":

            with lock:

                if not cs_busy:

                    cs_busy = True

                    client_socket.send("GRANT".encode())

                    print("GRANT sent to", address)

                else:

                    waiting_queue.append(client_socket)

                    print("Process added to waiting queue:", address)

        elif message == "RELEASE":

            with lock:

                cs_busy = False

                print("CS released by", address)

                if waiting_queue:

                    next_client = waiting_queue.pop(0)

                    cs_busy = True

                    next_client.send("GRANT".encode())

    client_socket.close()


server = socket.socket()

server.bind((HOST, PORT))

server.listen()

print("Coordinator is running...")

while True:

    client_socket, address = server.accept()

    thread = threading.Thread(
        target=handle_process,
        args=(client_socket, address)
    )

    thread.start()