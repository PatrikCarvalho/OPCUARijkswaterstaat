from opcua import Server
from random import randint
import time

server = Server()

# Define the ip adres and the port number of the Server
url = "opc.tcp://192.168.43.21:62654"     # use command "netstat" in the windows command prompt to see available ports
server.set_endpoint(url)

# Define an adres space
name = "OPCUA_SIMULATION_SERVER"
addspace = server.register_namespace(name)

# Define our root node
node = server.get_objects_node()

# Add a sub node where we assign the parameters to the addresspace
Param = node.add_object(addspace, "Parameters")

# Define variables
Temp = Param.add_variable(addspace, "Temperature", 0)
Pres = Param.add_variable(addspace, "Pressure", 0)
## and so on ....


# Make the variables writable
Temp.set_writable()
Pres.set_writable()


# start the server and display message
server.start()
print("Server has started at {}".format(url))


while(True):

    # Define random values
    Temperature = randint(10, 50)
    Pressure = randint(100, 500)

    print(Temperature, Pressure)

    # Set the values into the parameters defined in the sub node
    Temp.set_value(Temperature)
    Pres.set_value(Pressure)

    # Add a delay in seconds
    time.sleep(2)


