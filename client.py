import socket, sys, pickle

class Client():
    def __init__(self):
        self.HEADER_LENGTH = 10
        self.Report = True

    def Connect_and_authenticate_to_server(self, server_ip, server_port, username, password):
        try:
            '''
            d = {1: "Hey", 2: "There"}
            msg = pickle.dumps(d)
            msg = bytes(f'{len(msg):<{HEADER_SIZE}}', "utf-8") + msg
            client_socket.send(msg) # server said to client welcome.
            '''
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket, socket.SOCK_STREAM = this socket work with TCP-IP.
            client_socket.connect((server_ip, server_port)) # I ready my socket for connect to server.
            client_socket.setblocking(False) # disable blocking operation socket.

            user_pass = pickle.dump({1 : username, 2 : password})
            user_pass = bytes(f"{len(user_pass):<{self.HEADER_LENGTH}}", 'utf-8') + user_pass

            # my_username = username.encode('utf-8') # encode username to uft-8 for send first message to server.
            # my_password = password.encode('utf-8') # encode password to uft-8 for send first message to server.
            # username_header = f"{len(my_username):<{self.HEADER_LENGTH}}".encode('utf-8') # calculate username length and + with Header_length.
            # password_header = f"{len(my_password):<{self.HEADER_LENGTH}}".encode('utf-8') # calculate password length and + with Header_length.

            client_socket.send(user_pass) # I send my username to server for first message.

            while True:
                message = input(f"{username} > ") # now I can write my message and send it to server.

                if (message == "exit"):
                    print("Connection closed")
                    sys.exit()

                if message:
                    message = message.encode("utf-8") # encode message to utf-8.
                    message_header = f"{len(message):<{self.HEADER_LENGTH}}".encode("utf-8") # calculate message_length for header and send it to server for check my header.
                    client_socket.send(message_header + message)

        except Exception:
            #print("Sorry server is down :(",'\n',"Connection refused, please try again")
            self.Report = False
            return self.Report
            #sys.exit()