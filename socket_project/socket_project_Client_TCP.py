import socket #pip install sockets
import time

#serverName = '172.20.10.2'
serverName = socket.gethostbyname(socket.gethostname())
print(f"The server name of this pc is {serverName}")
serverPort = 12000
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET=IPV4 SOCK_STREAM=TCP
clientSocket.connect((serverName,serverPort))
message = input('SEND YOUR SERVER A MESSAGE:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
print(modifiedMessage. decode())
clientSocket.close()