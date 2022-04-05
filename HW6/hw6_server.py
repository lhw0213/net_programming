from socket import *
from collections import defaultdict

BUFFSIZE = 1024
port = 7777
s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))

dict = defaultdict(list)

while True:
    data, addr = s_sock.recvfrom(BUFFSIZE)
    data = data.decode()
    
    check = data.split(' ')
    print(data)
    if check[0] == 'send':
        msg = ' '.join(check[2:])
        dict[check[1]].append(msg)
        print(dict)
        s_sock.sendto("OK".encode(), addr)
    elif check[0] == 'receive':
        print(dict)
        if check[1] in dict:
            if not dict[check[1]]:
                print("not")
                s_sock.sendto("No message".encode(), addr)
            else:
                mail = dict[check[1]].pop(0)
                print(dict)
                s_sock.sendto(mail.encode(), addr)
        else:
            s_sock.sendto("No message".encode(), addr)
    if data == 'quit':
        break