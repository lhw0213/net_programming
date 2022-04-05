from socket import *
import os
import time

sock1 = socket(AF_INET, SOCK_STREAM)
sock1.connect(('localhost', 7777))
sock2 = socket(AF_INET, SOCK_STREAM)
sock2.connect(('localhost', 8888))

f = open('.data.txt', 'a')

while True:
    msg = input('Enter the device number ')
    if msg == 'quit':
        sock1.send(b'quit')
        sock2.send(b'quit')
        break
    elif msg == '1':
        sock1.send(b'Request')
        rsp = sock1.recv(1024).decode()
        Data = rsp.split(' ')
        Temp = Data[0]
        Humid = Data[1]
        Illum = Data[2]
        t = time.asctime()
        d = t + ':' + ' ' + 'Device1: ' + '온도= ' + Temp + ', 습도= ' + Humid + ', 조도= ' + Illum + '\n'
        print(d)
        f.write(d)
    elif msg == '2':
        sock2.send(b'Request')
        rsp  = sock2.recv(1024).decode()
        Data = rsp.split(' ')
        Heartbeat = Data[0] 
        Steps = Data[1]
        Cal = Data[2]
        t = time.asctime()
        d = t + ':' + ' ' + 'Device2: ' + '심박수= ' + Heartbeat + ', 걸음수= ' + Steps + ', 소모칼로리= ' + Cal + '\n'
        print(d)
        f.write(d)

f.close()
sock1.close()
sock2.close()
