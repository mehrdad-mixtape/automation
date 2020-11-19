import socket, select, datetime, hashlib, sys# use for socket.
import manage_db

class Server():
    def __init__(self):
        self.HEADER_LENGTH = 10 # size packets.
        self.IP = "127.0.0.1"
        self.PORT = 4444
        self.sockets_list = [] # list of sockets : server and other client.
        self.clients = {} # {socket:data}.

    def Instraction_Handler(self, cmd, client_socket): # use for check messages
        if (cmd == "exit"):
            self.Send_Message(client_socket, 'Connection closed from you')
            # self.sockets_list.remove(client_socket)
            # del self.clients[client_socket]

    def Receive_Message(self, receiver_socket): # internal function
        try:
            message_header = receiver_socket.recv(self.HEADER_LENGTH) # try to get first message from clients with 10 bytes.
            if not len(message_header): # if message_header was empty we can close the connection.
                return False

            message_length = int(message_header.decode("utf-8").strip()) # yes my message received XD, I should decode received message to utf-8 and calculate length.
            message_data = receiver_socket.recv(message_length).decode('utf-8').split("ε") # "username password".split("ε") for an other messages don't split.
            return {"header": message_header, "data": message_data} # we can receive message from each client with new header_length size.
        except:
            return False

    def Send_Message(self, sender_socket, message):
        msg = message.encode('utf-8')
        msg_header = f"{len(msg):<{self.HEADER_LENGTH}}".encode("utf-8")
        sender_socket.send(msg_header + msg)

    def Authenticate(self, usr, passwd):
        data = db.Get_attrib_admin(usr)
        if data == False:
            return False

        elif data[0] == usr and data[1] == passwd:
            return True

    def Run_Server(self):

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # socket.AF_INET = create a ipv4 socket, socket.SOCK_STREAM = this socket work with TCP-IP.
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # initial socket.
        server_socket.bind((self.IP, self.PORT))  # bind ip and port on socket.
        server_socket.listen()  # socket should be lister on IP:PORT because I am server :D.
        self.sockets_list.append(server_socket)

        while True:
            read_sockets, _, exception_sockets = select.select(self.sockets_list, [], self.sockets_list) # manage more client sockets, I give it my socket_list, [] empty, my socket_list for what?
            # first: read all sockets from list, second: write sockets to [], third: ?, each time I read socket list if new client connect to my server and check it.

            for notified_socket in read_sockets: # search in read_sockets.

                ################################ for first time we check server socket for client that connect and authenticate.################################
                if notified_socket == server_socket: # server socket is always first socket that give me notify because client connect to my server.

                    client_socket, client_address = server_socket.accept() # when client connect to my server I accept it and get IP:PORT from it. I get client_socket and client address=[IP, PORT]
                    user_pass = self.Receive_Message(client_socket) # I call my def to receive message from client. this def return a dictionary that contain message_header and data, data for first time is username of client.
                    if user_pass is False: # user can press enter with out message
                        continue

                    else:
                        if self.Authenticate(user_pass['data'][0], user_pass['data'][1]) == True:
                            self.sockets_list.append(client_socket)
                            self.clients[client_socket] = user_pass['data'][0] # clients={client_socket:{"header": message_header, "data": client_socket.recv(message_length)}, ...}
                            self.Send_Message(client_socket, 'authentication complete')
                            print(f"{self.Server_time()} authentication complete from '{user_pass['data'][0]}' with {client_address[0]}:{client_address[1]} to server") # log
                        else:
                            self.Send_Message(client_socket, 'authentication failed')
                            print(f"{self.Server_time()} authentication fail from '{user_pass['data'][0]}' with {client_address[0]}:{client_address[1]} to server") # log

                ################################ for second time we check client that send message to server and  client want to receive acknowledge from server.################################
                else:
                    message = self.Receive_Message(notified_socket) # my notify socket is client_socket.

                    if message is False:
                        print(f"{self.Server_time()}Connection closed from '{self.clients[notified_socket]['data'][0]}'") # log
                        self.sockets_list.remove(notified_socket)
                        del self.clients[notified_socket]
                        continue

                    user = self.clients[notified_socket] # I access to {"header": message_header, "data": client_socket.recv(message_length)}
                    self.Instraction_Handler(message['data'][0], notified_socket)
                    self.Send_Message(notified_socket, 'ack')
                    print(f"{self.Server_time()} message from '{user['data'][0]}':  {message['data']}")  # log

            for notified_socket in exception_sockets:
                self.sockets_list.remove(notified_socket)
                del self.clients[notified_socket]

    def Server_time(self):
        return datetime.datetime.now().strftime("%y-%m-%d %H:%M:%S")

if __name__ == "__main__":
    db = manage_db.Automation_BD()
    # db.Insert_admin('mixtape', str(hashlib.sha256('123'.encode('utf-8')).hexdigest()), 'mehrdad', 'arman', 'mehrdad1998a@gmail.com', '09369798295')
    # db.Delete_admin("5fb52fc768fdd8977be33228")
    # db.Update_admin("5fb427cb2584ac9a1dd9f933", 'sname', 'mixtape')
    # print(db.Get_attrib_admin('mixtape'))
    server = Server()
    server.Run_Server()