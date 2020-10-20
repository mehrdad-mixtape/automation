import socket
import select
import errno

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 4444))

full_msg = ''
while True:
    msg = s.recv(8) # receive data from server with 1024 byte buffer
    if msg.decode("utf-8"):
        break
    else:
        full_msg += msg.decode("utf-8")

print(full_msg)

# HEADER_LENGTH = 10
#
# IP = "127.0.0.1"
# PORT = "4444"
#
# my_username = input("Username: ")
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect((IP, PORT))
# client_socket.setblocking(False)