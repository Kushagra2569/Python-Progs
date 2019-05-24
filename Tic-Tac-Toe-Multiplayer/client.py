import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect(('127.0.0.1',789))

data = s.recv(1024).decode()
data1 = s.recv(1024).decode()

print(data)
print(data1)

nd = input('enter response\n')
s.send(nd.encode())
print('response sent')

flag = '1'
while flag == '1':
    msg = s.recv(1024).decode()
    print(msg)
    flag = s.recv(10).decode()
    if flag == '0':
        break
    pos = input()
    s.send(pos.encode())
    print('input sent')
    print('waiting for player 1')
