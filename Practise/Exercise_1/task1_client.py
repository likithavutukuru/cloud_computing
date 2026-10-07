import socket

client = socket.socket()

client.connect(("127.0.0.1", 5000))

numbers = input("Enter the numbers separated by space : ")

client.send(numbers.encode())

result = client.recv(1024).decode()

print(result)

client.close()