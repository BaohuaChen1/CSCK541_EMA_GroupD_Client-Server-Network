import socket

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
    # receive data stream. it won't accept data packet greater than 1024 bytes
        #data = connection.recv(1024).decode()
        #Server has accepted the connection from the client.
        connection, address = server_socket.accept()
        print("Got a connection from %s" % str(address))
        #Receiving the filename from the client.
        filename = connection.recv(1024).decode(format)
        print(f"[RECV] Receiving the filename.")
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
