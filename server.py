#socket to establish connection between server and client
#thread to handle multiple tasks/request simultaneously
import socket
from threading import Thread

#local machine will act as server
host='localhost'
port=8080
clients = {}
addresses = {}

#create pocket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP connection

#bind socket with host and port number
sock.bind((host, port))

def handle_clients(conn, address):
    name = conn.recv(1024).decode() #1024 bytes max length
    welcome = "welcome "+name+". you can type #quit if you ever want to leave the Chat Room"
    conn.send(bytes(welcome, "utf8")) # encode
    msg = name + "has recently joined the chat room" # message to be sent to all other clients in chatrooom
    broadcast(bytes(msg,"utf8")) #encode
    clients[conn]=name #store name in client dict

    while True: #as long as clients exchanging messages
        msg = conn.recv(1024)
        if msg!=bytes('#quit', 'utf8'):
            broadcast(msg,name+":")
        else:
            conn.send(bytes('#quit','utf8'))
            conn.close() #close connection
            del clients[conn] # delete client
            broadcast(bytes(name+" has left the chatroom",'utf8'))

def accept_client_connections(): #as long as clients connecting
    while True:
       client_conn, client_address= sock.accept()
       print(client_address,' has connected')
       client_conn.send("Welcome to the chatroom, please type your name to continue".encode('utf8'))
       addresses[client_conn]=client_address # store connection address in dict

       Thread(target=handle_clients, args=(client_conn, client_address)).start()

def broadcast(msg, prefix=""):
    for x in clients:
        x.send(bytes(prefix,"utf8")+msg)

#socket should be able to listen to multiple client request simultaneously
if __name__=="__main__":

    sock.listen(5)
    print("The server is running and is listening to clients requests")

    t1 = Thread(target=accept_client_connections)
    t1.start()
    t1.join()
