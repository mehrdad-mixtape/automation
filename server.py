import socket, select, datetime, sys# use for socket.
import manage_db
from hashlib import sha256

class Server():
    def __init__(self, ip, port):
        self.HEADER_LENGTH = 10 # size packets.
        self.IP = ip
        self.PORT = port
        self.sockets_list = [] # list of sockets : server and other client.
        self.clients = {} # {socket:data}.
        self.db = manage_db.Automation_BD()

    def Server_time(self): # internal function to return live time for logs.
        return datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

    def Instruction_Handler(self, cmd, client_socket): # internal function to check contain of messages that have keyword.
        if (cmd == "exit"):
            self.Send_Message(client_socket, 'Connection closed')
            self.db.Record_action_log(f"action # {cmd} # from {self.clients[client_socket][0]}", self.clients[client_socket][0])
            self.db.Record_login_log(f"Logout from server", self.clients[client_socket][0]) # record log on db.

            print(f"{self.Server_time()} connection closed from '{self.clients[client_socket][0]}'") # log
            client_socket.close()
            self.sockets_list.remove(client_socket)
            del self.clients[client_socket]

    def Authenticate(self, usr, passwd, key): # internal function to authenticate users that want login to server.
        if key == 'admin':  # I want to login with admin
            data = self.db.Get_attrib_admin(usr, passwd)
            if data == False:
                return False
            elif data[1] == usr and data[2] == passwd:
                return True

        elif key == 'normal_user': # I want to login with normal_user
            data = self.db.Get_attrib_user(usr, passwd)
            if data == False:
                return False
            elif data[1] == usr and data[2] == passwd:
                return True

    def Receive_Message(self, receiver_socket): # internal function to receive messages.
        try:
            message_header = receiver_socket.recv(self.HEADER_LENGTH) # try to get first message from clients with 10byte buffer.
            if not len(message_header): # if message_header was empty we can close the connection.
                return False
            message_length = int(message_header.decode("utf-8").strip()) # server should decode received message to utf-8 and calculate length to can receive message_data.
            message_data = receiver_socket.recv(message_length).decode('utf-8').split("ε") # "username password".split("ε") for an other messages don't split.
            return {"header": message_header, "data": message_data} # we can receive message from each client with new header_length size.
        except:
            return False

    def Send_Message(self, sender_socket, message): # internal function to send messages.
        try:
            msg = message.encode('utf-8') # server encode message.
            msg_header = f"{len(msg):<{self.HEADER_LENGTH}}".encode("utf-8") # server calculate length of message to allocated it for sending.
            sender_socket.send(msg_header + msg)
            return 'ack'
        except:
            return False

    def Run_Server(self):
        try:
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET = create a ipv4 socket, socket.SOCK_STREAM = this socket work with TCP-IP.
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # initial socket.
            server_socket.bind((self.IP, self.PORT))  # bind ip and port on socket.
            server_socket.listen()  # socket should be lister on IP:PORT because I am server :D.
            self.sockets_list.append(server_socket)
        except Exception:
            return "internal error" # if ip/port cannot bind to server, server return "internal error" to Start_server on admin.py.

        while True:
            try: # when server start to work, try to accept requests from clients, authenticate them and add client_sockets to lists.
                read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list) # manage multi client sockets, server give it socket_list, [] empty, socket_list, for what?
                # first: read all sockets from list, second: write sockets to [], third: write exception_sockets to this list, each time I read socket list if new client connect to my server and check it.

                for notified_socket in read_sockets: # search in read_sockets.

                    ################################ for first time we check server socket for client that connect and authenticate.################################
                    if notified_socket == server_socket: # server socket is always first socket that give me notify because client connect to my server.

                        client_socket, client_address = server_socket.accept() # when client connect to my server I accept it and get IP:PORT from it. I get client_socket and client address=[IP, PORT]
                        user_pass = self.Receive_Message(client_socket) # I call my def to receive message from client. this def return a dictionary that contain message_header and data, data for first time is username of client.
                        if user_pass is False:
                            continue

                        else:
                            if self.Authenticate(user_pass['data'][0], user_pass['data'][1], user_pass['data'][2]) == True: # user_pass = {'header' : message_header, 'data' : ['username', 'hash', key]}.
                                # Server check user/pass and if this user/pass exist on db, return True.
                                self.Send_Message(client_socket, 'authentication complete')
                                # If Authentication() return True, server send a message to client with client_socket.
                                self.db.Record_login_log(f"authentication complete from {client_address[0]}:{client_address[1]} to server", user_pass['data'][0]) # record log on db.
                                print(f"{self.Server_time()} authentication complete from '{user_pass['data'][0]}' with {client_address[0]}:{client_address[1]} to server")  # log

                                self.sockets_list.append(client_socket) # After authentication I add client socket to socket_list.
                                self.clients[client_socket] = user_pass['data'] # clients={client_socket: username}, ...}.
                                # And client_socket add to dictionary that server can recognize client_socket with client_message.

                            else:
                                self.Send_Message(client_socket, 'authentication failed')
                                # If Authentication() return False, server send message to client with client_socket.
                                self.db.Record_login_log(f"authentication failed from {client_address[0]}:{client_address[1]} to server", user_pass['data'][0]) # record log on db.
                                print(f"{self.Server_time()} authentication failed from '{user_pass['data'][0]}' with {client_address[0]}:{client_address[1]} to server") # log

                    ################################ for second time we check client that send message to server and  client want to receive acknowledge from server.################################
                    else:
                        message = self.Receive_Message(notified_socket) # my notify_socket is client_socket.
                        # Server receive messages from clients.

                        if message is False: # if client disconnect or send 'exit' message, server remove that client_socket from socket_list[] & clients{}
                            pass
                            # self.db.Record_login_log(f"Logout from server", self.clients[notified_socket][0]) # record log on db.
                            # print(f"{self.Server_time()} connection closed from '{self.clients[notified_socket][0]}'") # log
                            # notified_socket.close()
                            # self.sockets_list.remove(notified_socket)
                            # del self.clients[notified_socket]
                            # continue
                        else:
                            user = self.clients[notified_socket] # I access to {"header": message_header, "data": client_socket.recv(message_length)}.
                            # I get username that saved with socket in clients{}.
                            self.Instruction_Handler(message['data'][0], notified_socket) # Can check messages if client send keyword to server, this function can handle it.
                            self.Send_Message(notified_socket, 'ack') # When server receive message and check it with Instruction_Handler(), send 'ack' with client_socket to client, it's mean : yes I receive your message.
                            print(f"{self.Server_time()} message from '{user[0]}':  {message['data'][0]}")  # log

                for notified_socket in exception_sockets: # if each client_socket exist on exception_socket, server remove it.
                    notified_socket.close()
                    self.sockets_list.remove(notified_socket)
                    del self.clients[notified_socket]

            except Exception: # if server cannot service to clients, send a message to clients and disconnect all clients.
                for notified_socket in self.sockets_list:
                    self.sockets_list.remove(notified_socket)
                    del self.clients[notified_socket]

if __name__ == "__main__":
    S = Server('127.0.0.1', 4444)
    S.Run_Server()