import socket
import os
from pathlib import Path

def creat_file():
    #file in current directory
    check_file = Path('mytext.txt')  
    # will create a new file, if it exists will append text
    check_file.touch(exist_ok =True)
    # Append and Read (‘a+’),Write and Read (‘w+’)
    with open(check_file,'a+') as creat_file:
       creat_file.write('This is the last line\n')
    creat_file.close()


def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5050  # socket server port number
    #Staring a TCP socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    # connecting to the server
    client_socket.connect((host, port))  # connect to the server
    format = "utf-8"
    

    #message = input(" -> ")  # take input

   # while message.lower().strip() != 'bye':
        #if message.lower().strip() == 'send file':
           # Opening and reading the file data. 
    file = open("mytext.txt", "r")
    data = file.read()
    #Sending the filename to the server       
    client_socket.send("mytext.txt".encode(format))
    message = client_socket.recv(1024).decode(format)
    print(f"SERVER:{message}")
    #Sending the file data to the server
    client_socket.send(data.encode(format))
    message = client_socket.recv(1024).decode(format)
    print(f"SERVER:{message}")
            
    file.close()
    print ("sent finished")
        #else:
            #client_socket.send(message.encode())  # send message
            #data = client_socket.recv(1024).decode()  # receive response

            #print('Received message from server: ' + data)  # show in terminal

            #message = input(" input the message-> ")  # again take input

    client_socket.close()  # close the connection


if __name__ == '__main__':
    creat_file()
    client_program()