# BUILDING A SERVER NETWORK


## Table of Contents

- [BUILDING A SERVER NETWORK](#building-a-server-network)
  - [Table of Contents](#table-of-contents)
  - [Description](#description)
  - [Technologies](#technologies)
  - [Installation](#installation)
  - [Project](#project)
  - [Author](#author)


## Description

A simple client-network server in Python has been developed adding different functionalities as message sending, creation of text files, serializing and deserializing dictionaries according to different formats (JSON, XML, or binary) and encrypting and decrypting some content. Additionally, some unit tests have been created to validate the adequate performance of the different functions.

## Technologies

A list of technologies used within the project:
* [Python](https://www.python.org/downloads/): Version 3.11.0 
* [Visual Studio Code](https://visualstudio.microsoft.com/es/): Version: 1.73.v 
* [Anaconda](https://www.anaconda.com/products/distribution): Version: 4.12.0 

## Installation
```bash
pip install dict2xml
```
```bash
pip install cryptography
```
```bash
pip install pickle
```
```bash
pip install paramiko
```
```bash
pip install json
```
```bash
pip install socket
```
```bash
pip install pathlib 
```
```bash
pip install sys
```


## Project
This project consists of 4 different Modules(server_a.py client_a.py unittest.py functions.py).

The modules server_a.py client_a.py and functions.py interact althogether to perform the following tasks

1. Send Message to the server.
2. Create a Text File
3. Create a dictionary, populate it, serialize it. [1]
4. Encryption and Decryption of files [2]

The unittest.py module is used for. comparing the results of the functions as expected.

5. Create a reports including Readme.md and requirements.txt

Condition:

[1] Choose format: binary, JSON or XML.
[2] Need to have the option to encrypt and decrypt .
* The server should have a configurable option to print the contents of the sent items to the screen and or to a file.
* The server need to be able to handle encrypted contents.
* Written in PEP standard.


## Author
* Luis Ricardo Atristain [Github](https://github.com/SoftDevGroupD)
* Baohua Chen [Github](https://github.com/stevenchan88)
* Kentaro Fujita [Github](https://github.com/Ken-juuli)

