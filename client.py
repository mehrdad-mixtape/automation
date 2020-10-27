import socket
import errno # handle errors
import sys

HEADER_LENGTH = 10

IP = "127.0.0.1"
PORT = 4444

my_username = input("Username: ")
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket |||| socket.SOCK_STREAM = this socket work with TCP-IP.
client_socket.connect((IP, PORT)) # I ready my socket for connect to server.
client_socket.setblocking(False) # disable blocking operation socket.

username = my_username.encode("utf-8") # encode username to uft-8 for send first message to server.
username_header = f"{len(username):<{HEADER_LENGTH}}".encode("utf-8") # calculate username length and + with Header_length.
client_socket.send(username_header + username) # I send my username to server for first message.

while True:
    message = input(f"{my_username} > ") # now I can write my message and send it to server.

    if message:
        message = message.encode("utf-8") # encode message to utf-8.
        message_header = f"{len(message):<{HEADER_LENGTH}}".encode("utf-8") # calculate message_length for header and send it to server for check my header.
        client_socket.send(message_header + message)

    try:
        while True:
            #################### I receive username's clients from server.####################
            username_header = client_socket.recv(HEADER_LENGTH) # when I connect to server , if send message or not, server don't close my connection and just send my my username and empty data & message
            if not len(username_header): # if server shutdown when clients are in the server, I do this work
                print("Sorry ! Connection closed by server :(")
                sys.exit()
            username_length = int(username_header.decode("utf-8").strip()) # I catch my username from server and calculate length.
            username = client_socket.recv(username_length).decode("utf-8")

            #################### I receive message's client from server.####################
            message_header = client_socket.recv(HEADER_LENGTH)
            message_length = int(message_header.decode("utf-8").strip())
            message = client_socket.recv(message_length).decode("uft-8")

            print(f"{username} > {message}")

    except IOError as e:
        if e.errno != errno.EAGAIN and e.errno != errno.EWOULDBLOCK:
            print('Reading error', str(e))
            sys.exit()
        continue

    except Exception as e:
        print('General error', str(e))
        sys.exit()