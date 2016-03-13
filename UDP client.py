__author__ = 'guoqingxiong'
import random
from socket import *
from datetime import *
import time

clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.connect(('127.0.0.1', 12000))
clientSocket.settimeout(1)
for x in range(1, 11):
    message = 'Ping ' + str(x) + ' ' + date.today().isoformat() + ' T '
    message += datetime.now().time().isoformat() + ' UTC'
    print 'Sending to Server: \'{0}\''.format(message)
    sent_time = int(round(time.time() * 1000))
    try:
        clientSocket.send(message)
        message2, address = clientSocket.recvfrom(1024)
        recv_time = int(round(time.time() * 1000))
        print 'Received from Server: \'{0}\''.format(message2)
        print 'RTT: {0}'.format(recv_time - sent_time)
    except timeout:
        print 'Request Timed Out\n'
clientSocket.close()
