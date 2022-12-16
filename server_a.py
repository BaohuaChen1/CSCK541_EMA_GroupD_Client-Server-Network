import socket
from pathlib import Path
from cryptography.fernet import Fernet
import client_a
import pickle
import time
from functions import decrypt_file,deserialize,load_json,creat_file

def server_program():
    # get the hostname
    host = socket.gethostname()
    # initiate port number
    port = 5050
    #creat the socket isntance
    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
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

        # receive the task 1:
        rec_1 = connection.recv(1024)
        print("receive from task 1:", rec_1)

        # receive the task 2:
        rec_2 = connection.recv(1024)
        print("receive from task 2, the content is:", rec_2)
        option = input("task 2: please choose your option and input: print or file ")
        if option == "print":
           print(rec_2)
        #file in current directory
        if option == "file":
           check_file = Path('task_2_file.txt') 
        # will create a new file, if it exists will append text
           check_file.touch(exist_ok =True)
           with open(check_file,'a+') as creat_file:
              creat_file.write(str(rec_2))
              print("file created!, please check the file name: sever_received_infomation")
              creat_file.close()
        #  the task 3:

        while True:
            rec_msg = connection.recv(1024).decode(format)  ############### if the client send the file name ,then it wouldn't execute the following command
            if rec_msg =="exit":
               server_socket.close()
               break
            else:
               # receive the filename
               #rec_filename = connection.recv(1024).decode(format)
               rec_filename = rec_msg
               print(f"[RECV task 3] Received the filename, the filename is:", rec_filename)
               time.sleep(0.01)

               # receive the content after serialization
               seri_content = connection.recv(1024)
               print(f"[RECV task 3] the serialization by <<",rec_filename, ">> is:", seri_content)
               # to check if the file is encrypted, if yes, it would receive the following message
               encrypt_msg=connection.recv(1024)
               print(f"[RECV task 3] Received from client, :  ", encrypt_msg)

               # recive the file data
               file_data = connection.recv(1024)

               # decrypt the file 
               option_decrypt = input("Do you need to decrypt the file? please input yes or no ")
               # to check only the encrypted file needs to be decrypted
               if option_decrypt == "yes":
                    dec_data = decrypt_file(rec_filename)
                    print("decryption completed")  
                     #else:
                        #print("the file DOES NOT need to be decrypted!")  
               
               while True:
                     formats = ['binary', 'json', 'xml',"exit"]
                     deseri = input("task 3: please input the format of deserialization: binary,json, xml, or exit:")    
                     if deseri in formats:
                        break  
                     else:
                        print("plese input the correct formats:")
                     continue
               # to check if the file type is .pickle, then need to run pickle.load()
               if deseri == "binary":
                     file_data = deserialize(rec_filename)
                  #print("deserialize completed")

               if deseri == "json":
                     file_data = load_json(rec_filename) 
               
               if deseri== "xml":
                     if encrypt_msg ==b"encrypted":
                        file_data = dec_data

               # choose to print or save on a file
               option = input("task 3: please choose your option and input: print or file ")
               if option == "print":
                  print(f"[RECV task 3] after derialization by <<",rec_filename,">> is:", file_data)
               #file in current directory
               if option == "file":
                  check_file = Path('sever_received_infomation.txt') 
               # will create a new file, if it exists will append text
                  check_file.touch(exist_ok =True)
                  with open(check_file,'a+') as creat_file:
                     creat_file.write(str(file_data))
                     print("file created!, please check the file name: sever_received_infomation")
                     creat_file.close()
            continue
            
          


if __name__ == '__main__':
    server_program()
    
