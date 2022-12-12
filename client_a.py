import socket
from pathlib import Path
import pickle
import json
from dict2xml import dict2xml
from cryptography.fernet import Fernet
from functions import creat_dictionary,serialize,dump_json,dict_2_xml,send_text_to_server,send_file_to_server


if __name__ == '__main__':

    host = socket.gethostname()  # as both code is running on same pc
    port = 5050  # socket server port number
    #Staring a TCP socket
    socket_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    # connecting to the server
    socket_client.connect((host, port))  # connect to the server
    format = "utf-8"
    #creat_file()

    #creat_dictionary()
    #Serialize_the_dictionary()
    #creat_dictionary()


    # TASK NUMBER ONE
    # the task is to input a message from the client and send to the server
    # and the server should have an option to choose from print and to creat a file
    #message = input("please the content you want to send to ther server>>> ")
    #socket_client.send(message.encode(format))

    # TASK NUMBER TWO
    # the task is to creat a text file from the client and send to the server
    #filename = "TASK NUMBER TWO:creat a text file"
    #print("filename is", filename)
    #function.creat_file(filename)
    #function.send_file_to_server(filename)


    # TASK NUMBER THREE
    #Create a dictionary, populate it, serialize it and send it to a server,
    #With the dictionary, the user should be able to set the pickling format 
    #to one of the following: binary, JSON and XML.
 


    config = input("please input the method of serialization: binary, json, xml    ")
    # creat a new dictionary
    fruit_names = ["apple", "banana", "cherry", "pear", "avocado"]
    item_prices = [100, 50, 150, 80, 120]
    dic = creat_dictionary(fruit_names,item_prices)

    if config =="binary":
       file_name ="dictionary_binary.pickle"  ###############?????
       send_text_to_server(file_name,socket_client,format) #send the fileanme to the server
       serialize(seri_file=file_name, seri_content=dic)

    if config =="json":
       file_name ="dictionary_json.json"
       send_text_to_server(file_name,socket_client,format) #send the fileanme to the server
       dump_json(seri_file=file_name,seri_content=dic)

    if config =="xml":
       file_name ="dictionary_xml.xml"
       send_text_to_server(file_name,socket_client,format)#send the fileanme to the server
       dict_2_xml(seri_file=file_name,seri_content=dic)
    
    send_file_to_server(file_name,socket_client,format) # sometimes, filename is not defined