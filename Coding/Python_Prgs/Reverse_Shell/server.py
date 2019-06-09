import socket
import sys


# Creating the Socket( allows two computers to connect )
def create_socket():
    try:
        global host
        global port
        global s
        host = ''
        port = 9999
        s = socket.socket()
    except socket.error as e:
        print("Socket Creation error: " + str(e))


# Binding socket to port and wait for connection from the client
def bind_socket():
    try:
        global host
        global port
        global s
        print("Binding socket to port : " + str(port))
        s.bind((host, port))
        s.listen(5) # allow server to accept incoming connections
    except socket.error as e:
        print("Socket Binding Error : " + str(e) + "\n" + "Retyring...")
        bind_socket()


# Establishing a connection with client (socket must be listening for them)
def socket_accept():
    conn, addr = s.accept() # accepts a new connection
    print("Connection has been Established | " + "IP " + addr[0] + " | Port " + str(addr[1]))
    send_commands(conn)
    conn.close()


# # Send Commands to Client
def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024), "utf-8")
            print(client_response, end="")


if __name__ == "__main__":
    create_socket()
    bind_socket()
    socket_accept()