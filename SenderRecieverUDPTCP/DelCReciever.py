# TCP Reciever
# Felix Cenusa and Mathilda Ronnqvist

from socket import *
recieverPort = 1200

#create UDP socket
recieverSocket = socket(AF_INET, SOCK_STREAM)
#bind socket to port
recieverSocket.bind(('', recieverPort))
recieverSocket.listen(1)
connectionSocket, addr = recieverSocket.accept()
expectedNr = 10001
print("You are ready to receive")

#make an dictionary to store the expectedNr of the messages and switch it to True when the message is received
messages = {}
nrLossed = 0
#populate the dictionary with the expectedNr from 10000 to 10000 + NrOfPackets
for i in range(10001, 10000 + 500):
    messages[i] = False


while True:
    message = connectionSocket.recv(1024).decode()
    ## dont print the message if its empty
    if not message:
        break
    # add the message to the dictionary
    try:
        messages[int(message[0:5])] = True
    except:
        print("Error in message")
    print("Received message:", message)

# check if all the messages were received
for key in messages:
    if messages[key] == False:
        print("Message", key, "was not received")
        nrLossed += 1
print("Number of lossed packets: " + str(nrLossed))
