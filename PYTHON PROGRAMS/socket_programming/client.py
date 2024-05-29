import socket
def mpm():
 host = '127.0.0.1'
 port = 6000
 s = socket.socket() # socket pakage from socket method
 s.connect((host,port))
 while True:
    x = input('Enter New Message:')
    y = x.encode('ascii')
    s.send(y)
    data = s.recv(1024)
    d = data.decode('ascii')
    print('Server:',d)
mpm()
