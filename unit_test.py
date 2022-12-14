
import os
from pathlib import Path
import pickle
import json
from dict2xml import dict2xml
from cryptography.fernet import Fernet
from functions import creat_file,creat_dictionary,encrypt_file,decrypt_file,serialize,deserialize
import pickle
import unittest
import socket


class Test(unittest.TestCase):
    # test: creating a new file
    def test_creat_file(self):
        """Test File Creation"""
        filename = "Test File Creation"
        # to check if the file exits?
        self.assertTrue(creat_file(filename))
        print("unittest: test_creat_file, passed")

     # test: creating a new dictionary
    def test_creat_dictionary(self):
        fruit_names = ["apple", "banana", "cherry"]
        item_prices = [100, 50, 150]
         # test the function of creat_dictionary
        data_str = creat_dictionary(fruit_names,item_prices)
        actual = data_str
        expected = {'apple': 100, 'banana': 50, 'cherry': 150}
        # to test if the expected output equals the actual output:
        self.assertEqual(actual, expected) 
        print("unittest: test_creat_dictionary, passed")

        # test the outcome of serialization and deserialization
    def test_serialization_deserialization(self):    
        mock_dict = {'name': "steven", 'sex': "male"}
        seri_file = "test_dictionary.pickle"
        # to serialize the mock dictionary first
        serialize(mock_dict, seri_file)
        # to check if files exists
        self.assertTrue(os.path.exists(seri_file))  
        
        with open("test_dictionary.pickle","rb") as f:
             print("the mock dictionary after serialization is:",f.read())
        # to deserialize the dictionary
        # to test if the deserialized dictionary equals the mock dictionary                 
        self.assertEqual(deserialize(seri_file),mock_dict)
        print ('unittest: serialization and deserialization, passed')

    def test_encryption_decryption(self):
        # creat a mock file and intput some texts
        mock_file = "test encryption"
        with open(mock_file, 'w+') as file:
            file.write('this is a test')
        with open(mock_file,'rb') as file:
        # return the orignal texts in the mock file, and print it out
            original = file.read()
            print("the original content of the mock file is:",original)
        # to encrypt the mock file
        encrypt_file(mock_file)
        with open(mock_file,'rb') as encrypted_file:
            # to check if the encrypted file exits
            self.assertTrue(encrypted_file)
            print("the content after encryption is:", encrypted_file.read()) 
        # to decrpyt the mock file
        decrypt_file(mock_file)
        with open(mock_file,'rb') as dec_file:
             output = dec_file.read()
             # to check if the decrypted file exits
             self.assertTrue(dec_file)
             print("the content after decryption is:",output)  
        # to check if the content of file after decryption equals the orignial file
        self.assertEqual(output,original)
        print('unittest: encryption and decryption, passed')
    



if __name__ == '__main__':
    unittest.main()

