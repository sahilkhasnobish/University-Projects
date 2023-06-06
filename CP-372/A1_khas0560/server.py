'''
Sahil Khasnobish
CP-372 A1
190990560
'''
# Import socket module
from socket import * 
import struct
import sys # In order to terminate the program
from random import randint

# Assign a port number
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Bind the socket to server address and server port
serverSocket.bind(("", serverPort))


    
while True:

    print('The server is ready to receive')
    
    
    packet, clientAddress = serverSocket.recvfrom(1024)
    message_length, pcode, entity, message = struct.unpack('!IHH14s2x', packet)
    #verify packet 
    if(message_length%4 == 0):
        serverSocket.close()
        
    #create new packet to send back to client
    repeat = randint(5, 20)
    udp_port = randint(20000,30000)
    length = randint(50,100)
    codeA  = randint(100,400)
    entity = 2
    
    new_packet = struct.pack('!IHHIIHH', message_length, pcode, entity, repeat, udp_port, length, codeA)
    serverSocket.sendto(new_packet, clientAddress)
    

serverSocket.close()  
sys.exit()#Terminate the program after sending the corresponding data
