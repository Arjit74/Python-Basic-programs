#echo _server:
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1235))
s.listen(1)
print('waiting for connection')
while 1:
    c1,address=s.accept()
    #c1.send(b'welcome to gla local server)
    data=c1.recv(1024)
    print('Client :- ',data.decode())
    data=input('Server:- ').encode()
    c1.send(data)
c1.close()