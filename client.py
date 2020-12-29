import socket, pickle
from hashlib import sha256

class Client():
    def __init__(self):
        self.HEADER_LENGTH = 10
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # socket.AF_INET = create a ipv4 socket, socket.SOCK_STREAM = this socket work with TCP-IP.

    def Receive_Message(self, receiver_socket):  # internal function to receive messages.
        try:
            message_header = receiver_socket.recv(self.HEADER_LENGTH)  # try to get first message from clients with 10 bytes.
            if not len(message_header):  # if message_header was empty, client with to server send it
                return False
            message_length = int(message_header.decode("utf-8").strip()) # yes my message received XD, I should decode received message to utf-8 and calculate length.
            return receiver_socket.recv(message_length).decode('utf-8') # we can receive message from server with new header_length size.
        except Exception:
            return False

    def Receive_Big_Message(self, receiver_socket):
        try:
            message_header = receiver_socket.recv(self.HEADER_LENGTH)  # try to get first message from clients with 10 bytes.
            if not len(message_header):  # if message_header was empty, client with to server send it
                return False
            message_length = int(message_header.decode("utf-8").strip()) # yes my message received XD, I should decode received message to utf-8 and calculate length.
            return pickle.loads(receiver_socket.recv(message_length)) # we can receive message from server with new header_length size.
        except Exception as e:
            # print(e)
            return False

    def Send_Message(self, sender_socket, message):
        try:
            msg = message.encode('utf-8')
            msg_header = f"{len(msg):<{self.HEADER_LENGTH}}".encode("utf-8")
            sender_socket.send(msg_header + msg)
        except Exception:
            return False

    def Hash(self, input):
        return str(sha256(input.encode('utf-8')).hexdigest())

    def Connect_to_server(self, server_ip, server_port):
        try:  # for first time client try authentication with server than send user/pass to server.
            self.client_socket.connect((server_ip, server_port)) # my socket can connect to server.
            self.client_socket.setblocking(False) # disable blocking operation socket.

        except Exception: # If anything happens to the server this exception can handle it.
            return 'C_F' # Connection_Failed

    def Authenticate_to_server(self, username, password, key):
        try:
            user_pass = username + "ε" + self.Hash(password) + "ε" + key
            user_pass = user_pass.encode('utf-8')
            user_pass_header = f"{len(user_pass):<{self.HEADER_LENGTH}}".encode('utf-8')

            self.client_socket.send(user_pass_header + user_pass)

            while True:  # I try receive authentication message from server.
                receive_message = self.Receive_Message(self.client_socket)
                if receive_message != False:
                    if receive_message == 'authentication failed':
                        return 'A_F' # Authentication Failed
                    else:
                        return 'A_S' # Authentication Successful
                        #
                        # while True:
                        #     send_message = self.Get_msg()
                        #
                        #     if send_message:
                        #         self.Send_Message(client_socket, send_message)
                        #
                        #     while True: # client wait to server send message.
                        #         receive_message = self.Receive_Message(client_socket)
                        #
                        #         if receive_message == 'Connection closed': # if I send 'exit' server send me this message.
                        #             return receive_message
                        #
                        #         elif receive_message != False:
                        #             print(receive_message)
                        #             break
                        #
                        #         else: # if I don't send message to server and push "enter_button", server don't send me message too and I can get out from this loop.
                        #             break
        except Exception:
            return 'A_F' # Authentication Failed