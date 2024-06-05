# Del A Sender
# Felix Cenusa and Mathilda Ronnqvist

from socket import *
import time
# recieverIp
recieverIp = '192.168.139.231'

recieverPort = 1200

# create UDP socket
senderSocket = socket(AF_INET, SOCK_DGRAM)


# send messages
nrOfPackets = 10000
messageNr = 10000
for i in range(nrOfPackets):
    # create message
    messageNr = messageNr + 1
    message = str(messageNr)
    for j in range(1460):
        message = message + 'B'
    message = message + '####'
    print(messageNr)

    # send to socket
    time.sleep(0)
    senderSocket.sendto(message.encode(),(recieverIp, recieverPort))


senderSocket.close()