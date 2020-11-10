import socket
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 4444

def Connect_to_Server(ip, port):
    try:
        my_username = input("Username: ")
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket |||| socket.SOCK_STREAM = this socket work with TCP-IP.
        client_socket.connect((ip, port)) # I ready my socket for connect to server.
        client_socket.setblocking(False) # disable blocking operation socket.

        username = my_username.encode("utf-8") # encode username to uft-8 for send first message to server.
        username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8") # calculate username length and + with Header_length.
        client_socket.send(username_header + username) # I send my username to server for first message.

        while True:
            message = input(f"{my_username} > ") # now I can write my message and send it to server.

            if (message == "exit"):
                print(f"Connection Closed Dear user: {my_username}")
                sys.exit()

            if message:
                message = message.encode("utf-8") # encode message to utf-8.
                message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8") # calculate message_length for header and send it to server for check my header.
                client_socket.send(message_header + message)

    except Exception:
        print(" Sorry server is down :( ",'\n'," Connection refused, please try again")
        sys.exit()

def Start_Client():
    Connect_to_Server(IP,PORT)
#---------------------------------------------------------------------------------------------------------------------#
Start_Client()