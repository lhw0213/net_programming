from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    a = req[0].split()[1].strip('/')
    
    if a == 'index.html': 
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: text/html \r\n')
        c.send(b'\r\n')
        f = open('index.html', 'r', encoding='utf-8')
        html=f.read()
        c.send(html.encode('euc-kr'))
    elif a == 'iot.png':
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: image/png \r\n')
        c.send(b'\r\n')
        f = open('iot.png', 'rb')
        img = f.read()
        c.send(img)
    elif a == 'favicon.ico':
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: image/x-icon \r\n')
        c.send(b'\r\n')
        f = open('favicon.ico', 'rb')
        icon = f.read()
        c.send(icon)
    else : 
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')
    c.close()