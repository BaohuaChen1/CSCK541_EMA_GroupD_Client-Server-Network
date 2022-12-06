import socket
from pathlib import Path

def server_program():
    # get the hostname
    host = socket.gethostname()
    # initiate port number
    port = 5050
    #creat the socket isntance
    server_socket = socket.socket() 
    #bind the ip address and the port together
    server_socket.bind((host, port)) 
    # configure how many client the server can listen simultaneously
    server_socket.listen(5)
    format = 'utf-8'

    while True:
        #data = connection.recv(1024).decode()
        #Server has accepted the connection from the client.
        connection, address = server_socket.accept()
        print("Got a connection from %s" % str(address))

    # TASK NUMBER ONE
    # the task is to input a message from the client and send to the server
    # and the server should have an option to choose from print and to creat a file
        # receive the message from the client side and print on the screen
        msg = connection.recv(1024)
        option = input("please choose your option and input: print or file ")
        if option == "print":
           print('Received:' + msg.decode())
        #file in current directory
        if option == "file":
           check_file = Path('mytext.txt') 
        # will create a new file, if it exists will append text
           check_file.touch(exist_ok =True)
           with open(check_file,'a+') as creat_file:
              creat_file.write(msg.decode())
              print("file created!")
              creat_file.close()
        #if option != "print" or "file":
           # print("please input the choice of print or file only !")

    # TASK NUMBER TWO
    # the task is to creat a text file from the client and send to the server
        #Receiving the filename from the client.
        filename = connection.recv(1024).decode(format)
        #print(f"[RECV] Receiving the filename.")
        file= open(filename,"w")
        connection.send("Filename received.".encode(format))
        #Receiving the file data from the client.
        data = connection.recv(1024).decode(format)
        print(f"[RECV] Receiving the file data.")
        file.write(data)
        connection.send("File data received".encode(format))
        #Closing the file
        file.close()
        #Closing the connection from the client.
        connection.close()
        print(f"[DISCONNECTED] {address} disconnected.")

if __name__ == '__main__':
    server_program()
