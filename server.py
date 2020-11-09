import socket # use for socket.
import select # use for many client.

HEADER_LENGTH = 10 # size packets.

IP = "127.0.0.1"
PORT = 4444

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket |||| socket.SOCK_STREAM = this socket work with TCP-IP.
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # initial socket.

server_socket.bind((IP, PORT)) # bind ip and port on socket.
server_socket.listen() # socket should be lister on IP:PORT because I am server :D.

sockets_list = [server_socket] # list of sockets : server and other client.
clients = {} # {socket:data}.

def receive_message(client_socket):
    try:
        message_header = client_socket.recv(HEADER_LENGTH) # try to get first message from clients with 10 bytes.
        if not len(message_header): # if message_header was empty we can close the connection.
            return False

        message_length = int(message_header.decode("utf-8").strip()) # yes my message received XD, I should decode received message to utf-8 and calculate length.
        return {"header": message_header, "data": client_socket.recv(message_length)} # we can receive message from each client with new header_length size.

    except:
        return False


while True:
    read_sockets, _, exception_sockets = select.select(sockets_list, [], sockets_list) # manage more client sockets, I give it my socket_list, [] empty, my socket_list for what?
    # first: read all sockets from list, second: write sockets to [], third: ?, each time I read socket list if new client connect to my server and check it.

    for notified_socket in read_sockets: # search in read_sockets.

        ################################ for first time we check server socket for client that connect.################################
        if notified_socket == server_socket: # server socket is always first socket that give me notify because client connect to my server.

            client_socket, client_address = server_socket.accept() # when client connect to my server I accept it and get IP:PORT from it. I get client_socket and client address=[IP, PORT]
            user = receive_message(client_socket) # I call my def to receive message from client. this def return a dictionary that contain message_header and data, data for first time is username of client.
            if user is False: # if user don't send message I continue other lines(disconnect client) :).
               continue
            # else:
            sockets_list.append(client_socket)
            clients[client_socket] = user # I create dictionary keys=client_socket : value= a dictionary that I recevied from client.

            print(f"Accepted new connection from {client_address[0]}:{client_address[1]} username:{user['data'].decode('utf-8')}") # yes you connected ! and your first message is your username.

        ################################ for second time we check client that send message.################################
        else:
            message = receive_message(notified_socket) # my notify socket is client_socket.

            if message is False:
                print(f"Closed connection from {clients[notified_socket]['data'].decode('utf-8')}") # clients={client_socket:{"header": message_header, "data": client_socket.recv(message_length)}, ...}
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

            user = clients[notified_socket] # I access to {"header": message_header, "data": client_socket.recv(message_length)}
            print(f"message from >>> {user['data'].decode('utf-8')} <<<: {message['data'].decode('utf-8')}")
            print(len(message['data'].decode('utf-8')))

            if (message['data'].decode('utf-8') == "exit"):
                sockets_list.remove(notified_socket)
                del clients[notified_socket]
                continue

    for notified_socket in exception_sockets:
        sockets_list.remove(notified_socket)
        del clients[notified_socket]