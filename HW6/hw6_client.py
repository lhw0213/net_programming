from socket import *

BUFFSIZE = 1024
port = 7777

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect(('localhost', port))

while True:
    msg = input('Enter the message("send mboxId message" or "receive mboxId"):')
    msglist = msg.split(' ')

    if msglist[0] == 'send':
        c_sock.sendto(msg.encode(), ('localhost', port))
        data, addr = c_sock.recvfrom(BUFFSIZE)
        print(data.decode())
    elif msglist[0] == 'receive':
        c_sock.sendto(msg.encode(), ('localhost', port))
        data, addr = c_sock.recvfrom(BUFFSIZE)
        print(data.decode())
    else:
        c_sock.sendto('quit'.encode(), ('localhost', port))
    if msg == 'quit':
        c_sock.sendto(msg.encode(), ('localhost', port))
        break