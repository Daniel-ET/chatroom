# tkinter for client side GUI
# socket to establish connection between server and client
import tkinter as tk
import socket
from tkinter import *
from threading import Thread

def receive():
    while True: #as long as clients exchanging messages
        try:
            msg = s.recv(1024).decode('utf8') #socket recv and decode
            msg_list.insert(tkinter.END, msg) #put latest message at end of message list
        except:
            print('There is an error receiving the message')

def send():
    msg = my_msg.get() #get value of variable my_msg and store in msg
    my_msg.set('') #set entry field to empty after each message
    s.send(bytes(msg,'utf8')) #send message to server in encoded form to broadcast
    if msg == '#quit': #close connection and window if client quits
        s.close()
        window.close()

def on_closing():
    my_msg.set('#quit') #quit button equivalent to client typing #quit
    send()

window = Tk()
window.title("Chat Room App") #change window title
window.configure(bg="black") #change background color

message_frame = Frame(window, height = 25, width = 50, bg ='blue') #create message frame
message_frame.pack()  #put frame inside window

my_msg=StringVar()
my_msg.set("") #text field will initially be empty

#create scrollbar and put messages in the form of a list
scroll_bar = Scrollbar(message_frame)
msg_list = Listbox(message_frame, height=25, width=50, bg='blue', yscrollcommand=scroll_bar.set)
scroll_bar.pack(side=RIGHT, fill=Y) #inside window
msg_list.pack(side=LEFT, fill=BOTH) #inside window
msg_list.pack()

#create label to ask for user entry
label = Label(window, text='enter your message',fg='red', font='arial', bg='black')
label.pack()

#create entry field for client to input message
entry_field = Entry(window, textvariable=my_msg,fg='red', width=50)
entry_field.pack()

#create send button
send_button = Button(window, text='Send', font='arial', fg='white', command=send) #invoke send func
send_button.pack()

#create quit button
quit_button = Button(window, text='Quit', font='arial', fg='white', command=on_closing) #invoke on_cls func
quit_button.pack()

host='localhost'
port=8080

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

#thread to receive the messages that the client will exchange
receive_Thread = Thread(target=receive) #target recieve func
receive_Thread.start()

mainloop()
