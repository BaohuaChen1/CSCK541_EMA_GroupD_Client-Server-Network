from pathlib import Path
import pickle
import json
from dict2xml import dict2xml
from cryptography.fernet import Fernet

def creat_file(filename): #unittest passed
    #file in current directory
        check_file = Path(filename)  
    # will create a new file, if it exists will append text
        check_file.touch(exist_ok =True)
    # Append and Read (‘a+’),Write and Read (‘w+’)
        with open(check_file,'w+') as creat_file:
             creat_file.write('the task is to : Create a text file and send it to a server\n')
             creat_file.close()
        return creat_file

def creat_dictionary(fruit_names,item_prices): #unittest passed
        seri_content = {fruit:price for (fruit, price) in zip(fruit_names, item_prices)}
        print("dictionary content:   ", seri_content)
        return seri_content

def serialize(seri_content,seri_file):
    file_to_write = open(seri_file, "wb")
    pickle.dump(seri_content,file_to_write)
    file_to_write.close()

        
def deserialize(seri_content):
    file_to_read= open(seri_content,"rb")
    dictionary_deserialize = pickle.load(file_to_read)
    #print("deserialize completed", dictionary_deserialize)
    file_to_read.close()
    return dictionary_deserialize
    

def dump_json(seri_content,seri_file):
    file_to_write = open(seri_file, "w")
    json.dump(seri_content,file_to_write)
    file_to_write.close()

def load_json(seri_content):
    file_to_read= open(seri_content,"r")
    dictionary_load_json = json.load(file_to_read)
    file_to_read.close()
    return dictionary_load_json

def dict_2_xml(seri_content,seri_file):
    file_to_read= open(seri_file,"w") # with open('dico.xml', 'w') as f:
    dictionary_dict2xml = dict2xml(seri_content,seri_file)
    file_to_read.write(str(dictionary_dict2xml))
    file_to_read.close()
    
def send_text_to_server(text,socket_name,format_name):
        socket_name.sendall(text.encode(format_name))  #socket_client

def encrypt_file(filename):  #file_to_encrypt,file_encrypted
        #generating the keys:
        key = Fernet.generate_key() ##########
        # string the key in a file
        with open('filekey.key', 'wb') as filekey:
            filekey.write(key)
        # opening the key
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()  
        # using the generated key    
        fernet = Fernet(key)   ##########
        # opening the original file to encrypt
        with open(filename, 'rb') as file:
            original = file.read()
        # encrypting the file
        encrypted = fernet.encrypt(original)  ##########
        # opening the file in write mode and writing the encrypted data
        with open(filename,'wb') as encrypted_file:
            encrypted_file.write(encrypted)
       
def decrypt_file(filename):
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
            

def send_file_to_server(filename,socket_name,format_name):
        file = open(filename,"r")
        #using the if statement, to check whether the client want to encrypt the file
        config = input("please choose encryption or not, input yes or no:    ")
        if config =="yes":
             encrypt_file(filename)
             #messge ="the file is encrypted"
             #socket_client.send(message.encode(format))
             encrypt_msg =" the file has been encrypted!"
             socket_name.send(encrypt_msg.encode(format_name))
        if config =="no":
            pass
        #Sending the file data to the server
        data = file.read()
        socket_name.send(data.encode(format_name))
        message = socket_name.recv(1024).decode(format_name) 
        print(f"SERVER:{message}")    
        #file.close()

def send_to_server(filename,socket_name,format_name):
        file = open(filename,"r")
        #Sending the file data to the server
        data = file.read()
        socket_name.send(data.encode(format_name))
        #message = socket_name.recv(1024).decode(format_name) 
        #print(f"SERVER:{message}")    
        #file.close()







    

if __name__ == '__main__':

    creat_dictionary()
    encrypt_file()