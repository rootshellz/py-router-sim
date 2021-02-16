import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.bind((socket.gethostname(), 8000))
connection.listen(5)

while True:
    connected_socket, address = connection.accept()
    print(f"Connection from {address} established")
    connected_socket.send(bytes("First message", "utf-8"))
