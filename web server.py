<html>
  <head>
    <meta http-equiv="Content-Style-Type" content="text/css" /> 
    <title>server.py</title>
    <link href="/library/skin/tool_base.css" type="text/css" rel="stylesheet" media="all" />
    <link href="/library/skin/new-york-u/tool.css" type="text/css" rel="stylesheet" media="all" />
    <script type="text/javascript" language="JavaScript" src="/library/js/headscripts.js"></script>
    <style>body { padding: 5px !important; }</style>
  </head>
  <body>
#import socket module
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)

#Prepare a sever socket
serverSocket.bind(('127.0.0.1', 6789))#Fill in start
serverSocket.listen(5)#Fill in end

while True:
    #Establish the connection
    print 'Ready to serve...'
    connectionSocket, addr = serverSocket.accept()#Accepts a TCP client connection, waiting until connection arrives
    print 'Required connection', addr
    try:

        message = connectionSocket.recv(1024)#Fill in start #Fill in end
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()#Fill in start #Fill in end

        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.0 200 OK\r\n\r\n")#Fill in start


        #Send the content of the requested file to the client

        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.send("\r\n")
        
        connectionSocket.close() 

    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
        connectionSocket.send("<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n")#Fill in start
        #Fill in end

        #Close client socket
        connectionSocket.close()#Fill in start
        serverSocket.close()#Fill in end

  </body>
</html>
