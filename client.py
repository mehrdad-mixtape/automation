import socket
import select
import errno

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 4444))

msg = s.recv(1024)
print(msg.decode("utf-8"))

# HEADER_LENGTH = 10
#
# IP = "127.0.0.1"
# PORT = "4444"
#
# my_username = input("Username: ")
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((IP, PORT))
# client_socket.setblocking(False)