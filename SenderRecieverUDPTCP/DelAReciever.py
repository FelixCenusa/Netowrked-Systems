# UDP Reciever
# Felix Cenusa and Mathilda Ronnqvist

from socket import *
recieverPort = 1200

#create UDP socket
recieverSocket = socket(AF_INET, SOCK_DGRAM)
#bind socket to port
recieverSocket.bind(('', recieverPort))

print("You are ready to recieve")

expectedNr = 10001
nrLossed = 0

while True:
    message, senderAddress = recieverSocket.recvfrom(2048)

    if int(message.decode()[0:5]) != expectedNr:
        print ("Oordning: " + (message.decode()[0:5]))
        nrLossed += (int(message.decode()[0:5]) - expectedNr)
        expectedNr = int(message.decode()[0:5])
        print("Number of lossed packets: " + str(nrLossed)) 

    else:
        print (message.decode()[0:5])
    expectedNr += 1