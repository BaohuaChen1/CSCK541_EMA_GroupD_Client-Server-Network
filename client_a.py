import socket
import os
from pathlib import Path
import pickle
import json
from dicttoxml import dicttoxml

class Function():



    def creat_file(self,filename):
    #file in current directory
        check_file = Path(filename)  
    # will create a new file, if it exists will append text
        check_file.touch(exist_ok =True)
    # Append and Read (‘a+’),Write and Read (‘w+’)
        with open(check_file,'a+') as creat_file:
             creat_file.write('the task is to : Create a text file and send it to a server\n')
             creat_file.close()

    def send_file_to_server(self,filename):
        file = open(filename,"r")
        data = file.read()

    #Sending the file data to the server
        socket_client.send(data.encode(format))
        message = socket_client.recv(1024).decode(format)
        print(f"SERVER:{message}")    
    #file.close()


    def creat_dictionary(self):
        fruits = ["apple", "banana", "cherry", "pear", "avocado"]
        prices = [100, 50, 150, 80, 120]
        self.dictionary_fruits_price = {fruit:price for (fruit, price) in zip(fruits, prices)}
        print(self.dictionary_fruits_price)
    
    

    def write_binary(self,filename):
        file_to_write_binary = open(filename, "wb")
        dictionary_to_write_binary=pickle.dump(self.dictionary_fruits_price,file_to_write_binary)
        file_to_write_binary.close()
        print(f"This is file_to_write_binary:\n{dictionary_to_write_binary}\n")
    
    def write_json(self,filename):
  
        file_to_write_json = open(filename, "w")
        dictionary_to_write_json=json.dump(self.dictionary_fruits_price,file_to_write_json)
        file_to_write_json.close()
        print(f"This is file_to_write_json:\n{dictionary_to_write_json}\n")

    def write_xml(self,filename):
        file_to_write_xml = open(filename, "w")
        dictionary_to_write_xml = dicttoxml(self.dictionary_fruits_price,file_to_write_xml)  
        file_to_write_xml.close()
        print(f"This is file_to_write_XML:\n{dictionary_to_write_xml}\n")

def Deserialize_the_dictionary():
    my_unpickled_object = pickle.loads(Serialize_the_dictionary.my_pickled_object)  # Unpickling the object
    print(f"This is a_dict of the unpickled object:\n{my_unpickled_object}\n")
    
def Serialize_the_dictionary(self):
        my_pickled_object = pickle.dumps(self.dictionary_fruits_price)  # Pickling the object
        print(f"This is my pickled object:\n{my_pickled_object}\n")
    
def read_binary():
    file_to_read_binary= open("dictionary.pickle","rb")
    dictionary_to_read_binary = pickle.load(file_to_read_binary)
    file_to_read_binary.close()
    print(f"This is file_to_read_binary:\n{dictionary_to_read_binary}\n")

'''
    my_json_object = json.dumps(dictionary_fruits_price)  
    print(f"This is my json object:\n{my_json_object}\n")

    my_unjson_object = json.loads(my_json_object)  
    print(f"This is a_dict of the unjson object:\n{my_unjson_object}\n")


    # read json
    file_to_read_json= open("dictionary.json","r")
    dictionary_to_read_json = json.load(file_to_read_json)
    file_to_read_json.close()
    print(f"This is file_to_read_json:\n{dictionary_to_read_json}\n")



def pickle_function(content, file_name):
    file__binary = open(file_name, 'wb')
    file_to_write_binary=pickle.dump(content, file__binary)
    file__binary.close()
    print(f"This is file_to_write_binary:\n{file_to_write_binary}\n")

#def send_file_to_server(file_name, socket):
    #file = open(file_name, "r")
    #data = file.read()
'''   


    

 

    #send_file_to_server.data= creat_file()
    #send_file_to_server()
    




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
    function = Function()

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
    function.creat_dictionary()
    if config =="binary":
       filename ="dictionary.pickle"
       
       function.write_binary(filename)

    if config =="json":
       filename ="dictionary.json"

       function.write_json(filename)

    if config =="xml":
       filename ="dictionary.xml"

       function.write_xml(filename)
    function.send_file_to_server(filename)