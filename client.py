import socket
import os
from pathlib import Path
import pickle
import json
from dicttoxml import dicttoxml

def creat_file():
    #file in current directory
    check_file = Path('mytext.txt')  
    # will create a new file, if it exists will append text
    check_file.touch(exist_ok =True)
    # Append and Read (‘a+’),Write and Read (‘w+’)
    with open(check_file,'a+') as creat_file:
       creat_file.write('This is the last line\n')
    creat_file.close()

def creat_dictionary():
    fruits = ["apple", "banana", "cherry", "pear", "avocado"]
    prices = [100, 50, 150, 80, 120]
    dictionary_fruits_price = {fruit:price for (fruit, price) in zip(fruits, prices)}
    #print(dictionary_fruits_price)
    # Serialize the dictionary
    my_pickled_object = pickle.dumps(dictionary_fruits_price)  # Pickling the object
    print(f"This is my pickled object:\n{my_pickled_object}\n")
    # Deserialize the dictionary
    my_unpickled_object = pickle.loads(my_pickled_object)  # Unpickling the object
    print(f"This is a_dict of the unpickled object:\n{my_unpickled_object}\n")
    # write binary
  
    file_to_write_binary = open("dictionary.pickle", "wb")
    pickle.dump(dictionary_fruits_price,file_to_write_binary)
    file_to_write_binary.close()
    # read binary
    file_to_read_binary= open("dictionary.pickle","rb")
    dictionary_to_read_binary = pickle.load(file_to_read_binary)
    file_to_read_binary.close()
    print(f"This is file_to_read_binary:\n{dictionary_to_read_binary}\n")


    my_json_object = json.dumps(dictionary_fruits_price)  
    print(f"This is my json object:\n{my_json_object}\n")

    my_unjson_object = json.loads(my_json_object)  
    print(f"This is a_dict of the unjson object:\n{my_unjson_object}\n")

    # write json
  
    file_to_write_json = open("dictionary.json", "w")
    json.dump(dictionary_fruits_price,file_to_write_json)
    file_to_write_json.close()
    # read json
    file_to_read_json= open("dictionary.json","r")
    dictionary_to_read_json = json.load(file_to_read_json)
    file_to_read_json.close()
    print(f"This is file_to_read_json:\n{dictionary_to_read_json}\n")

    # Serialize Python dictionary to XML
    dictionary_xml = dicttoxml(dictionary_fruits_price)  
    print(f"Serialize Python dictionary to XML:\n{dictionary_xml}\n")

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5050  # socket server port number
    #Staring a TCP socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # instantiate
    # connecting to the server
    client_socket.connect((host, port))  # connect to the server
    format = "utf-8"
    

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

    client_socket.close()  # close the connection


if __name__ == '__main__':
    creat_file()
    client_program()