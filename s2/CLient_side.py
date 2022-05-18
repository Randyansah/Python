import socket #pip install sockets
import time
import hashlib

#serverName = '172.20.10.2'
serverName = socket.gethostbyname(socket.gethostname())
print(f"The server name of this pc is {serverName}")
serverPort = 12000
time.sleep(3)
print(f"The server port used for this communication is: {serverPort}")

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET=IPV4 SOCK_STREAM=TCP
clientSocket.connect((serverName,serverPort)) #Takes only one input
message = input('SEND YOUR SERVER A MESSAGE:')
clientSocket.sendto(message.encode(),(serverName,serverPort))
modifiedMessage,serverAddress = clientSocket.recvfrom(1024)
message_ENCRPT=modifiedMessage.decode()
hased=hashlib.md5(message_ENCRPT.encode())
print(hased.hexdigest())
clientSocket.close()