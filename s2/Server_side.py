from socket import*
import time
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(( '', serverPort))
serverSocket.listen(1)
print("The server is ready to receive")
time.sleep(6)
print("Go Live Now.........")

while True:
    connectionSocket,addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024 ).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()
