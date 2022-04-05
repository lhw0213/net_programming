from socket import *
import random

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 8888))
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
            Heartbeat = str(random.randrange(40, 141))
            Steps = str(random.randrange(2000, 6001))
            Cal = str(random.randrange(1000, 4001))
            Total = Heartbeat + ' ' + Steps + ' ' + Cal
            print(Total)
            conn.send(Total.encode())
        elif Data == 'quit':
            break
    if Data == 'quit':
        break

    conn.close()