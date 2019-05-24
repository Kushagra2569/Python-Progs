import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('',789))

print('server started and listening on port 789')


def game():
    arr = [0] * 3
    for i in range(3):
        arr[i] = [0] * 3
    c = 0
    posDict = {'0':[0,0] ,'1':[0,1] ,'2':[0,2] ,'3':[1,0] ,'4':[1,1] ,'5':[1,2] ,'6':[2,0] ,'7':[2,1] ,'8':[2,2]}

    while(c == 0):
        if checkDraw(arr):
            c = -1
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
                c = 1
                break
        if checkDraw(arr):
            c = -1
            break
        b = input('p2 enter a position\n')
        if((arr[posDict[b][0]][posDict[b][1]]) != 0):
            print('this position is already taken')
            while True:
                b = input('p2 enter a position\n')
                if((arr[posDict[b][0]][posDict[b][1]]) != 0):
                    print('this position is already taken')
                else:
                    break
        else:
            arr[posDict[b][0]][posDict[b][1]] = 2
            if checkWin(arr):
                c = 2
                break
    if c == 1:
        print('player 1 won')
    elif c == 2:
        print('player 2 won')
    elif c == -1:
        print('its a draw')
        
        
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
