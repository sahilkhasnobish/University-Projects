'''
Sahil Khasnobish
CP-372 A1
190990560
'''
# Import socket module
from socket import * 
import struct
import sys # In order to terminate the program

serverName = 'localhost'
# Assign a port number
serverPort = 12000

# Bind the socket to server address and server port
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = "hello world!!!\0\0"
message_length = len(message)
pcode = 0
entity = 1 
packet = struct.pack('!IHH14s2x', message_length, pcode, entity, message.encode('utf-8'))


#clientSocket.connect((serverName, serverPort))
clientSocket.sendto(packet, (serverName, serverPort))
modifiedSentence, serverAddress = clientSocket.recvfrom(2048)

print('From server: ', modifiedSentence.decode())
clientSocket.close()