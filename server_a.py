import socket
from pathlib import Path
from cryptography.fernet import Fernet
import client_a
import sys
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

    
   #Server has accepted the connection from the client, and print out the IP address
   connection, address = server_socket.accept()
   print("Got a connection from %s" % str(address))

   # receive content from the task 1:
   try :
      rec_1 = connection.recv(1024)
      print("receive from task 1:", rec_1)
   except socket.error:
      print("receiving data error %s" % socket.error)
      sys.exit(1)

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
         print("file created!, please check the file name: server_received_infomation")
         creat_file.close()
   #  the task 3:

   while True:
      rec_msg = connection.recv(1024).decode(format)  
      if rec_msg =="exit":
         print(rec_msg)
         break
         
      else:
         # receive the filename
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
         
         #!!!!!!!! if a file is encrypted firstly, it needs to be decrypted before running pickle.load(),or json.load()
         # decrypt the file
         option_decrypt = input("Do you need to decrypt the file? please input yes or no ")
         # to check only the encrypted file needs to be decrypted
         if option_decrypt == "yes":
               dec_data = decrypt_file(rec_filename)
               print("decryption completed")  
               #else:
                  #print("the file DOES NOT need to be decrypted!")  
         
         while True:
               formats = ['pickle', 'json', 'xml',"exit"]
               deseri = input("task 3: please input the format of deserialization: pickle,json, xml, or exit:")    
               if deseri in formats:
                  break  
               else:
                  print("plese input the correct formats:")
               continue
         
         # to check if the file type is .pickle, then need to run pickle.load()
         if deseri == "pickle":
               file_data = deserialize(rec_filename)
            #print("deserialize completed")
         # if the file type is .json, then need to run json.load()
         if deseri == "json":
               file_data = load_json(rec_filename) 
         
         if deseri== "xml":
               if encrypt_msg ==b"encrypted":  
                  file_data = dec_data # if the xml file is encrypted firstly, then return to the content after decryption.
                                       # if it's not encrypted ,the file_data is just the content received previously.
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
   connection.close()
            
          


if __name__ == '__main__':
    server_program()
    
