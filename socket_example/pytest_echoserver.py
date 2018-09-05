#!/usr/bin/python
from socket import *
import sys
import datetime
import time
#st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
#print st
print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)
serverPort = int(sys.argv[1])
print "The port number is: ", serverPort
serverSocket = socket(AF_INET,SOCK_STREAM) 
serverSocket.bind(('',serverPort)) 
serverSocket.listen(1)
print 'The server is ready to receive' 
while 1:
	connectionSocket, addr = serverSocket.accept()
	print addr 
	sentence = connectionSocket.recv(1024)
	print sentence 
	#capitalizedSentence = sentence.upper() 
	connectionSocket.send(sentence)
	text_file = open("echo_message_1.txt", "w")
	text_file.write(addr[0])
	text_file.write(" ")
	text_file.write(str(addr[1]))
	text_file.write("\n")
	text_file.write(sentence)
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
	text_file.write(st)
	text_file.close() 
	connectionSocket.close()

        
