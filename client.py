import socket
import sys

class Client():
    def __init__(self, HEADER_LENGTH, IP, PORT):
        self.HEADER_LENGTH = HEADER_LENGTH
        self.IP = IP
        self.PORT = PORT

    def Connect_to_Server(self, username):
        try:
            my_username = str(username)
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket |||| socket.SOCK_STREAM = this socket work with TCP-IP.
            client_socket.connect((self.IP, self.PORT)) # I ready my socket for connect to server.
            client_socket.setblocking(False) # disable blocking operation socket.

            encode_username = my_username.encode("utf-8") # encode username to uft-8 for send first message to server.
            username_header = f"{len(encode_username):<{self.HEADER_LENGTH}}".encode("utf-8") # calculate username length and + with Header_length.
            client_socket.send(username_header + encode_username) # I send my username to server for first message.

            while True:
                message = input(f"{my_username} > ") # now I can write my message and send it to server.

                if (message == "exit"):
                    print(f"Connection Closed Dear user: {my_username}")
                    sys.exit()

                if message:
                    message = message.encode("utf-8") # encode message to utf-8.
                    message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode("utf-8") # calculate message_length for header and send it to server for check my header.
                    client_socket.send(message_header + message)

        except Exception:
            print(" Sorry server is down :( ",'\n'," Connection refused, please try again")
            sys.exit()