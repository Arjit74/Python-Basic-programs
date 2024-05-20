import socket  # Import the socket module

# Create a socket object using the AF_INET address family (IPv4) and the SOCK_STREAM socket type (TCP)
client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# Connect to the server at 'localhost' on port 7512
client_socket.connect(('localhost',7512))

# Receive data from the server, here 1024 is the buffer size to take the data it is the maximum size
# data = client_socket.recv(1024)



message = "Hello this is echo message from the client".encode() # encode changes it to byte 

print("Dtata sent form the client",message)

print('Client:',message)
client_socket.send(message)

data = client_socket.recv(1024)
print('Server', data)


# Print the data received from the server
# print('Server: ',data.decode())

# Close the client socket
client_socket.close()


#----------------------------------------------
