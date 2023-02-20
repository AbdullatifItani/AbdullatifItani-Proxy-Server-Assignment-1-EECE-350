#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 19:17:37 2023

@author: abdellatifitani
"""

#Name: Abdullatif Itani
#ID: 202203750
import socket
import time
import re, uuid

#We Take Google As An Example And Ping Google In The Terminal To Get Current IP Address
#Current Google IP Address(142.250.200.238)
#Take IP Address As Input
websiteIP = input("Enter your website IP: ")

#The Port We Connect To Is 2003
serverPort=2003

#The Buffer Size Is 4096
receive_buffer_size = 4096

#127.0.0.1 Is The Local Host We Work On
proxyIP = "127.0.0.1"

#Form Request
request = "GET / HTTP/1.1\nHost: "+websiteIP+"\n\n"

#Create Client Sockket And Connect To Proxy Server
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientSocket.connect((proxyIP,serverPort))

#Send Request To Proxy Server
t1=time.time()
clientSocket.send(request.encode())

#Print Request Details And Time It Was Sent
print("The IP of the request was",websiteIP,"and the request was sent at:",time.ctime())

#Recieve Reply From Proxy Servor And Display It With The Time It Was Recieved
response = clientSocket.recv(receive_buffer_size).decode()
t2=time.time()
print("The response was:")
print(response)
print("The response was recieved from the server at:",time.ctime())

#Total Round-Trip Time And MAC Address(60:30:d4:81:11:28)
print("The total round trip time is:",t2-t1,"seconds")
#MAC Address Code Is From Googgle
print ("My MAC address is: ", end="")
print (':'.join(re.findall('..', '%012x' % uuid.getnode())))