# UDP Server
from socket import *
def prime_checker(num):
  try:
    num =int(num)
  except:
    prime_flag= -1
    return str(prime_flag)
  if num>1:
    prime_flag=1
    for i in range(2, num):
      if (num%i) ==0:
        prime_flag=0
        break
  else:
    prime_flag=0
  return str(prime_flag)
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print("Server ready  to receive")
while 1:
  message, clientAddress = serverSocket.recvfrom(2048)
  print("Datagram from:", clientAddress)
  message = message.decode ('utf-8')
  isprime= prime_checker(message)
  serverSocket.sendto (isprime.encode('utf-8'), clientAddress)
