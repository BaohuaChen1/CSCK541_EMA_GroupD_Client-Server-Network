import socket
from pathlib import Path
from cryptography.fernet import Fernet
import client_a
import pickle

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
        filename = connection.recv(1024).decode(format)
        print(f"[RECV] Received the filename, the filename is:  ", filename)
        # to check if the file is encrypted
        encrypt_msg=connection.recv(1024)
        print(f"[RECV] Received from client, :  ", encrypt_msg)
        # recive the information 
        msg = connection.recv(1024)

        # decrypt the information
        if encrypt_msg == "encrypted":
            with open('filekey.key', 'rb') as filekey:
               key = filekey.read()
        # using the key
            fernet = Fernet(key)
        # opening the encrypted file
            with open(filename , 'rb') as enc_file:
               encrypted = enc_file.read()
        # decrypting the file
            decrypted = fernet.decrypt(encrypted) 
        # opening the file in write mode and writing the decrypted data
            with open(filename, 'wb') as dec_file:
               dec_file.write(decrypted)
               msg = dec_file.read()
            print("decryption completed")
        # to check if the file type is .pickle, then need to run pickle.load()
        #if filename == "dictionary.pickle":
            file_to_read_binary= open("dictionary.pickle" ,"rb")
            dictionary_to_read_binary = pickle.load(file_to_read_binary)
            msg = file_to_read_binary.read()
            print(f"This is file_to_read_binary:\n{dictionary_to_read_binary}\n")
        # choose to print or save on a file
        option = input("please choose your option and input: print or file ")
        if option == "print":
           print('Received from the client:' + msg.decode())#######????
        #file in current directory
        if option == "file":
           check_file = Path('sever_received_infomation.txt') 
        # will create a new file, if it exists will append text
           check_file.touch(exist_ok =True)
           with open(check_file,'a+') as creat_file:
              creat_file.write(msg.decode())
              print("file created!, please check the file  name:sever_received_infomation")
              creat_file.close()


if __name__ == '__main__':
    server_program()
