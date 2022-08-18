# socket to establish connection between server and client
import socket

#local machine will act as server
host='localhost'
port=8080

#create socket
sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #TCP connection

#bind socket with host and port number
sock.bind((host, port))

#socket should be able to contionously listen to client requests
sock.listen(1)
print("The server is running and listening to client requests")

#server should be able to accept requests and store connection
conn,address=sock.accept()

#send message to client through established connection
message = "something important"
conn.send(message.encode())

#once message is sent close the connection
conn.close()
