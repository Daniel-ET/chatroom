# client should be able to send request to server
import socket

#local machine acting as both client and server
host='localhost'
port=8080

#create socket and connect with host and port number
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((host,port))

#client should be able to receive messages (and continuing receiving)
message = sock.recv(1024)

while message:
    print("Message:", message.decode())
    message=sock.recv(1024)

sock.close()
