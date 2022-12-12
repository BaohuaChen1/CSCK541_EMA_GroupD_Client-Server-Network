import socket
from pathlib import Path
from cryptography.fernet import Fernet
import client_a
import pickle
from functions import decrypt_file,deserialize

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


        # receive the filename
        rec_filename = connection.recv(1024).decode(format)
        print(f"[RECV] Received the filename, the filename is:", rec_filename)

        # to check if the file is encrypted, if yes, it would receive the following message
        encrypt_msg=connection.recv(1024)
        print(f"[RECV] Received from client, :  ", encrypt_msg)

        # recive the file data
        file_data = connection.recv(1024)

        # decrypt the information #### convert to importing using the def function.
        ############################
        ############################
        ##########################
        #######################
        if encrypt_msg == b' the file has been encrypted!':
            decrypt_file(rec_filename)
            print("decryption completed")
           
        # to check if the file type is .pickle, then need to run pickle.load()

        if rec_filename == "dictionary_binary.pickle":
           file_data = deserialize(rec_filename)
           #print("deserialize completed")
           
 
        # choose to print or save on a file
        option = input("please choose your option and input: print or file ")
        if option == "print":
           print(file_data)
        #file in current directory
        if option == "file":
           check_file = Path('sever_received_infomation.txt') 
        # will create a new file, if it exists will append text
           check_file.touch(exist_ok =True)
           with open(check_file,'a+') as creat_file:
              creat_file.write(str(file_data))
              print("file created!, please check the file name: sever_received_infomation")
              creat_file.close()


if __name__ == '__main__':
    server_program()
    