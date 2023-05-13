

def next_move(posx, posy, dimx, dimy, board):
    # Buscar la 'd' mas "cercana"
    # Empezar desde la posicion "mas lejana posible".
    dposx = posx + dimx
    dposy = posy + dimy
    for x in range(dimx):
        for y in range(dimy):
            if board[x][y] == 'd':
                # Es la mas cercana hasta el momento ?
                if (abs(posx - x) + abs(posy - y)) < (abs(posx - dposx) + abs(posy - dposy)):
                    dposx, dposy = x, y
                        
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
    dim = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(dim[0])]
    next_move(pos[0], pos[1], dim[0], dim[1], board)