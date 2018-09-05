#!/usr/bin/python
from socket import *
serverName = '127.0.0.1'
import sys
import datetime
import time
serverPort = int(sys.argv[1])
sentence = sys.argv[2]
clientSocket = socket(AF_INET, SOCK_STREAM) 
clientSocket.connect((serverName,serverPort))
text_file = open("echo_response_1.txt", "w")
ts = time.time()
st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
text_file.write(st)
text_file.write("\n") 
#sentence = raw_input('Input sentence:') 
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
text_file.write(modifiedSentence)
text_file.close() 
print 'From Server:', modifiedSentence 
clientSocket.close()


