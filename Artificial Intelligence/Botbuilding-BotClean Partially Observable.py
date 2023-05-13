#!/usr/bin/python3

def next_move(posx, posy, board):
    dimx = 5 # len(board)
    dimy = 5 # len(board[0])
    
    # dposx = posx + dimx
    # dposy = posy + dimy
    found = False
    for x in range(dimx):
        for y in range(dimy):
            if board[x][y] == 'd':
                # Es la mas cercana hasta el momento ?
                if not found or ((abs(posx - x) + abs(posy - y)) < (abs(posx - dposx) + abs(posy - dposy))):
                    dposx, dposy = x, y
                    found = True
                       
    if not found:
        if (posx == 1) and (posy < (dimy - 2)):
            dposy = posy + 1
            dposx = posx
        elif (posx == 3) and (posy > 2):
            dposy = posy - 1
            dposx = posx
        elif (posy == 3) and (posx < (dimx - 2)):
            dposx = posx + 1
            dposy = posy
        elif (posy == 1) and (posx > 2):
            dposx = posx - 1
            dposy = posy
        else:
            dposy = 1 if (posy <= 2) else 3
            dposx = 1 if (posx <= 2) else 3
                    
    if (posx < dposx):
        print('DOWN')
    elif (posx > dposx):
        print('UP')
    elif (posy < dposy):
        print('RIGHT')
    elif (posy > dposy):
        print('LEFT')
    else: # (posx == dposx) and (posy == dposy) <=> board[posx][posy] == 'd':
        print('CLEAN')

if __name__ == "__main__": 
    pos = [int(i) for i in input().strip().split()] 
    board = [[j for j in input().strip()] for i in range(5)]  
    next_move(pos[0], pos[1], board)