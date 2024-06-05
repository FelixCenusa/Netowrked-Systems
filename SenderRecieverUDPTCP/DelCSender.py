# Del C Sender
# Felix Cenusa and Mathilda Ronnqvist
from socket import *
import time
# receiverIp
receiverIp = '193.11.184.229'
receiverPort = 1200

# create TCP socket
senderSocket = socket(AF_INET, SOCK_STREAM)

# connect to receiver
senderSocket.connect((receiverIp, receiverPort))

# send messages
nrOfPackets = 1000
messageNr = 10000
delayInSeconds = 0.02  # adjust the delay as needed

for i in range(nrOfPackets):
    # create message
    messageNr = messageNr + 1
    message = str(messageNr)
    for j in range(1480):
        message = message + 'C'
    message = message + '####'
    print(messageNr)

    # send to socket
    senderSocket.send(message.encode())
    
    # delay before sending the next packet
    time.sleep(delayInSeconds)

senderSocket.close()

