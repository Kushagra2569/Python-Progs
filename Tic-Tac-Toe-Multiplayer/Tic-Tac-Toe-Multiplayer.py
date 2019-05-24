import socket
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',789))

print('server started and listening on port 789')

s.listen(5)
c,addr = s.accept()
print('client at '+str(addr)+'connected')
c.send('Thank you for connecting'.encode())
c.send('Press 1 whenever you are ready to play'.encode())
u = 0
while u != 1:
    time.sleep(1)
    print('enter response')
    u = int(c.recv(10).decode())
    

print('Game Start')



def p2Input():
    c.send('p2 enter a position'.encode())
    c.send('1'.encode())
    data = -1
    while data == -1:
        time.sleep(1)
        data = c.recv(10).decode()
        if not data:
            break

    return data

def p2close(message):
    c.send(message.encode())
    time.sleep(1)
    c.send('0'.encode())
        

def game():
    arr = [0] * 3
    for i in range(3):
        arr[i] = [0] * 3
    cFlag = 0
    posDict = {'0':[0,0] ,'1':[0,1] ,'2':[0,2] ,'3':[1,0] ,'4':[1,1] ,'5':[1,2] ,'6':[2,0] ,'7':[2,1] ,'8':[2,2]}

    while(cFlag == 0):
        if checkDraw(arr):
            cFlag = -1
            break
        a = input('p1 enter a position\n')
        if((arr[posDict[a][0]][posDict[a][1]]) != 0):
            print('this position is already taken')
            while True:
                a = input('p1 enter a position\n')
                if((arr[posDict[a][0]][posDict[a][1]]) != 0):
                    print('this position is already taken')
                else:
                    break
        else:
            arr[posDict[a][0]][posDict[a][1]] = 1
            if checkWin(arr):
                cFlag = 1
                break
        if checkDraw(arr):
            cFlag = -1
            break

        print('waiting for player 2 ...')
        b = p2Input()
        if((arr[posDict[b][0]][posDict[b][1]]) != 0):
            print('this position is already taken')
            while True:
                b = p2Input()
                if((arr[posDict[b][0]][posDict[b][1]]) != 0):
                    print('this position is already taken')
                else:
                    break
        else:
            arr[posDict[b][0]][posDict[b][1]] = 2
            if checkWin(arr):
                cFlag = 2
                break
    if cFlag == 1:
        print('player 1 won')
        p2close('player 1 won')
    elif cFlag == 2:
        print('player 2 won')
        p2close('You Won')
    elif cFlag == -1:
        print('its a draw')
        p2close('Its a Draw')
        
        
    print(arr)

def checkDraw(array):
    drawFlag = True
    for i in range(3):
        for j in range(3):
            if array[i][j] == 0:
                drawFlag = False
    return drawFlag


def checkWin(array):
    winFlag = False
    for i in range(3):
        if array[i][0] == array[i][1] == array[i][2] != 0:
            winFlag = True
        elif array[0][i] == array[1][i] == array[2][i] != 0:
            winFlag = True
        
    if array[0][0] == array[1][1] == array[2][2] != 0:
        winFlag = True
    if array[0][2] == array[1][1] == array[2][0] != 0:
        winFlag = True
    return winFlag

    
game()
