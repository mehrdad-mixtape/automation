import socket, sys, login_form
from hashlib import sha256

class Client():
    def __init__(self):
        self.HEADER_LENGTH = 10
        self.Report = True

    def Receive_Message(self, receiver_socket):  # internal function
        try:
            message_header = receiver_socket.recv(self.HEADER_LENGTH)  # try to get first message from clients with 10 bytes.
            if not len(message_header):  # if message_header was empty we can close the connection.
                return False

            message_length = int(message_header.decode("utf-8").strip())  # yes my message received XD, I should decode received message to utf-8 and calculate length.
            return receiver_socket.recv(message_length).decode('utf-8')
        except:
            return False

    def Send_Message(self, sender_socket, message):
        msg = message.encode('utf-8')
        msg_header = f"{len(msg):<{self.HEADER_LENGTH}}".encode("utf-8")
        sender_socket.send(msg_header + msg)

    def Connect_and_authenticate_to_server(self, server_ip, server_port, username, password):
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket, socket.SOCK_STREAM = this socket work with TCP-IP.
            client_socket.connect((server_ip, server_port)) # I ready my socket for connect to server.
            client_socket.setblocking(False) # disable blocking operation socket.

            user_pass = username + "ε" + self.Hash(password)
            user_pass = user_pass.encode('utf-8')
            user_pass_header = f"{len(user_pass):<{self.HEADER_LENGTH}}".encode('utf-8')

            client_socket.send(user_pass_header + user_pass)
            while True:
                receive_message = self.Receive_Message(client_socket)
                if receive_message != False:
                    if receive_message == 'authentication failed':
                        self.Report = False
                        return self.Report
                    else:
                        while True:
                            send_message = input(f"{username} > ") # now I can write my message and send it to server.
                            if send_message:
                                self.Send_Message(client_socket, send_message)

                            while True:
                                receive_message = self.Receive_Message(client_socket)
                                if receive_message == 'Connection closed from you': # if I send 'exit' server send me this message.
                                    self.Report = receive_message
                                    return self.Report
                                # elif receive_message == 'Server shutdown':
                                #     self.Report = receive_message
                                #     return self.Report
                                else:
                                    print(receive_message)
                                    break

        except Exception: # If anything happens to the server this exception can handle it.
            self.Report = False
            return self.Report

    def Hash(self, input):
        return str(sha256(input.encode('utf-8')).hexdigest())

# if __name__ == "__main__":
#     client = Client()
#     client.Connect_and_authenticate_to_server('127.0.0.1', 4444, 'mixtape', '123')