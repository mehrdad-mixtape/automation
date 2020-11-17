import socket, select, datetime # use for socket.

class Server():
    def __init__(self):
        self.HEADER_LENGTH = 10 # size packets.
        self.IP = "127.0.0.1"
        self.PORT = 8888
        self.sockets_list = [] # list of sockets : server and other client.
        self.clients = {} # {socket:data}.

    def Instraction_Handler(self, cmd, owner_cmd): # use for check messages
        if (cmd == "exit"):
            self.sockets_list.remove(owner_cmd)
            del self.clients[owner_cmd]

    def Server_time(self):
        return datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

    def Receive_Message(self, client_socket): # internal function
        try:
            message_header = client_socket.recv(self.HEADER_LENGTH) # try to get first message from clients with 10 bytes.
            if not len(message_header): # if message_header was empty we can close the connection.
                return False

            message_length = int(message_header.decode("utf-8").strip()) # yes my message received XD, I should decode received message to utf-8 and calculate length.
            message_data = client_socket.recv(message_length).decode('utf-8').split(" ") # "username password".split(" ")
            return {"header": message_header, "data": message_data[0]} # we can receive message from each client with new header_length size.
        except:
            return False

    def Run_Server(self):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket, socket.SOCK_STREAM = this socket work with TCP-IP.
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # initial socket.
        server_socket.bind((self.IP, self.PORT)) # bind ip and port on socket.
        server_socket.listen() # socket should be lister on IP:PORT because I am server :D.
        self.sockets_list.append(server_socket)

        while True:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list) # manage more client sockets, I give it my socket_list, [] empty, my socket_list for what?
            # first: read all sockets from list, second: write sockets to [], third: ?, each time I read socket list if new client connect to my server and check it.

            for notified_socket in read_sockets: # search in read_sockets.

                ################################ for first time we check server socket for client that connect.################################
                if notified_socket == server_socket: # server socket is always first socket that give me notify because client connect to my server.

                    client_socket, client_address = server_socket.accept() # when client connect to my server I accept it and get IP:PORT from it. I get client_socket and client address=[IP, PORT]
                    user = self.Receive_Message(client_socket) # I call my def to receive message from client. this def return a dictionary that contain message_header and data, data for first time is username of client.
                    if user is False: # user can press enter with out message
                        continue
                    # else:
                    self.sockets_list.append(client_socket)
                    self.clients[client_socket] = user # I create dictionary keys=client_socket : value= a dictionary that I received from client.

                    print(f"{self.Server_time()} '{user['data']}' with {client_address[0]}:{client_address[1]} login to server") # yes you connected ! and your first message is your username.

                ################################ for second time we check client that send message.################################
                else:
                    message = self.Receive_Message(notified_socket) # my notify socket is client_socket.

                    if message is False:
                        print(f"Closed connection from {self.clients[notified_socket]['data']}") # clients={client_socket:{"header": message_header, "data": client_socket.recv(message_length)}, ...}
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue

                    user = self.clients[notified_socket] # I access to {"header": message_header, "data": client_socket.recv(message_length)}
                    print(f"{self.Server_time()} message from {user['data']}: {message['data']}")

                    self.Instraction_Handler(message['data'], notified_socket)

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

server = Server()
server.Run_Server()