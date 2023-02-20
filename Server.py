#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:17:35 2023

@author: abdellatifitani
"""

#Name: Abdullatif Itani
#ID: 202203750
import socket
import time

#The Port We Listen On Is 2003
serverPort=2003

#The Buffer Size Is 4096
receive_buffer_size = 4096

#127.0.0.1 Is The Local Host We Work On
proxyIP = "127.0.0.1"

#Create Socket And Bind It To My Loacal IP Adsress
proxySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
proxySocket.bind((proxyIP,serverPort))
                   
#Listen On Port Of Your Own Choice
proxySocket.listen(2)
print("The server is ready to recieve")
    
while True:
    try:
        #Accept Connection And Create A Socket For The Connection
        clientSocket,addr = proxySocket.accept()
        
        #Recieve The Request And Parse It To Get IP
        request = clientSocket.recv(receive_buffer_size).decode()
        requestsplit=request.split()
        serverIP=requestsplit[4]
        
        #Print Request And Server IP With The Exact Time Of The Request
        print("The IP of the request is:",serverIP,"and the request was recieved at:",time.ctime())
        
        #Create Website Socket And Connect To It
        websiteSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        websiteSocket.connect((serverIP,80))
        print("We are connected to website")
        
        #Send Clients Request To Destination Server
        websiteSocket.send(request.encode())
        
        #Print Time The Request Was Send To Destination Server
        print("The request to the destination server was sent at:",time.ctime())
        
        #Recieve Response From Destination Server
        response = websiteSocket.recv(receive_buffer_size).decode()
        
        #Print Message That Response Was Recieved And The Time It Was Recieved
        print("The response from the destination server was:",response)
        print("The response was recieved from the destination server at: ",time.ctime())
        
        #Send Response To Client
        clientSocket.send(response.encode())
        
        #Print Message That Response Was Sent To Client And The Time It Was Sent
        print("The response was sent to the client at:",time.ctime())
        
        #Close Sockets
        websiteSocket.close()
        clientSocket.close()
        proxySocket.close()
        break
        
        
    except:
        #Send Error Message To Client
        errorMessage="There was an error!"
        clientSocket.send(errorMessage.encode())
        #Display Error Message
        print(errorMessage)
        
        #Close Sockets
        websiteSocket.close()
        clientSocket.close()
        proxySocket.close()
        break