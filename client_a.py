import socket
from pathlib import Path
from dict2xml import dict2xml
from cryptography.fernet import Fernet
from functions import creat_dictionary,serialize,dump_json,dict_2_xml,send_text_to_server,send_file_to_server,creat_file,send_to_server


if __name__ == '__main__':

    host = socket.gethostname()  # as both code is running on same pc
    port = 5050  # socket server port number
    #Staring a TCP socket
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    # connecting to the server
    socket_client.connect((host, port))  # connect to the server
    format = "utf-8"

    # TASK NUMBER ONE
    # the task is to input a message from the client and send to the server
    # and the server should have an option to choose from print and to creat a file
    message = input("task 1: please input the content you want to send to ther server>>> ")
    socket_client.send(message.encode(format))

    # TASK NUMBER TWO
    # the task is to creat a text file from the client and send to the server
    message = input("task 2: creat a text file from the client and send to the server, input input the file name you want:>>> ")
    creat_file_name = message
    creat_file(creat_file_name)
    send_to_server(creat_file_name,socket_client,format)


    # TASK NUMBER THREE
    #Create a dictionary, populate it, serialize it and send it to a server,
    #With the dictionary, the user should be able to set the pickling format 
    #to one of the following: binary, JSON and XML.
 
    # creat a new dictionary
    key_item  = ["name", "subject", "project"]
    value_item = ['TeamD', 'SoftwareDevelopment', "client server network"]
    dic = creat_dictionary(key_item, value_item)

    print('This dictionary is for demonstration purpose:', dic)

   
    while True:

         formats = ['binary', 'json', 'xml',"exit"]
    
         while True:
               config = input("task 3: please input the method of serialization: binary,json, xml, or exit:")    
               if config in formats:
                  break  
               else:
                  print("plese input the correct formats:")
               continue

         if config =="binary":
            file_name ="dictionary_binary.pickle"  #define the file name
            send_text_to_server(file_name,socket_client,format) #send the fileanme to the server
            serialize(seri_file=file_name, seri_content=dic) # serialize the file with pickle
            send_file_to_server(file_name,socket_client,format)  # send the file to the server
         if config =="json":
            file_name ="dictionary_json.json"
            send_text_to_server(file_name,socket_client,format) #send the fileanme to the server
            dump_json(seri_file=file_name,seri_content=dic) # serialize the file with json
            send_file_to_server(file_name,socket_client,format)
         if config =="xml":
            file_name ="dictionary_xml.xml"
            send_text_to_server(file_name,socket_client,format)#send the fileanme to the server
            dict_2_xml(seri_file=file_name,seri_content=dic)  # serialize the file with xml
            send_file_to_server(file_name,socket_client,format)
         if config == "exit":
            send_text_to_server("exit",socket_client,format)#send the text of "exit" to the server
            socket_client.close()
            break
         continue   # to input the format of serialization


    