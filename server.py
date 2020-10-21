import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket.AF_INET = create a ipv4 socket |||| socket.SOCK_STREAM = this socket work with TCP-IP
s.bind((socket.gethostname(), 4444)) # socket.gethostname() = get hostname from client on port number
s.listen(5) # this socket listen on 4444

while True: # each client want to connect to the server, this part catch requests,
    client_socket, address = s.accept() # client_socket is obj for client.
    print(f"Connection from {address} has been established :D")
    # print("Connection form ",address," has been established :D")
    client_socket.send(bytes("Welcome to the automation_server :)", "utf-8")) # server said to client welcome.
    client_socket.close() # when I send data to client I close this socket
    break