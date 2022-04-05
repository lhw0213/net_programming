from socket import *
import random

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 7777))
sock.listen(5)
print('Waiting..')

while True:
    conn, addr = sock.accept()
    print('Connection from ', addr)
    while True:
        Data = conn.recv(1024)
        if not Data:
            break
        Data = Data.decode()
        print(Data)
        if Data == 'Request':
            Temp = str(random.randrange(0, 41))
            Humid = str(random.randrange(0, 101))
            Illum = str(random.randrange(70, 151))
            Total = Temp + ' ' + Humid + ' ' + Illum
            print(Total)
            conn.send(Total.encode())
        elif Data == 'quit':
            break
    if Data == 'quit':
        break

    conn.close()