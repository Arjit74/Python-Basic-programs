import socket  # Import the socket module

# Create a socket object using the AF_INET address family (IPv4) and the SOCK_STREAM socket type (TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address ('localhost') and port (7512) or we can use only 0 - 1024 and available port number are 0 - 35565 (2^16) we can also use socket.gethostbyname instead of 
server_socket.bind(('localhost', 7512))

# Start listening for incoming connections with a backlog of 1
server_socket.listen(1)

print('Waiting for connection')
while 1:
    # Accept a connection from a client
    client, address = server_socket.accept()

    # Send a welcome message to the client
    # client.send('Welcome to GLA Local Server'.encode())
    data = client.rec(1024)
    print('Client',data.decode())
    print('Response Sent!')
    client.send(data)



    # Close the server socket
    client.close()
