from opcua import Client
import time

# Define url of the server
url =  "opc.tcp://192.168.43.21:62654"

# Define client to server url
client = Client(url)

# connect client to server
client.connect()
print("Client connected to server")

# Get the value of the parameters from the server For this we need the node ID which is available in UAExpert software
while(True):
    Temp = client.get_node("ns=2;i=2")
    Temperature = Temp.get_value()
    print(Temperature)

    Pres = client.get_node("ns=2;i=3")
    Pressure = Pres.get_value()
    print(Pressure)

    time.sleep(1)
