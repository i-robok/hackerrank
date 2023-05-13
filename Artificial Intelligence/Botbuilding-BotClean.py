#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    # Buscar la 'd' mas "cercana"
    # Empezar desde la posicion "mas lejana posible".
    dposr = posr + len(board)
    dposc = posc + len(board)
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'd':
                # Es la mas cercana hasta el momento ?
                if (abs(posr - i) + abs(posc - j)) < (abs(posr - dposr) + abs(posc - dposc)):
                    dposr, dposc = i, j
                        
    if (posr < dposr):
        print('DOWN')
    elif (posr > dposr):
        print('UP')
    elif (posc < dposc):
        print('RIGHT')
    elif (posc > dposc):
        print('LEFT')
    else: # (posr == dposr) and (posc == dposc) <=> board[posr][posc] == 'd':
        print('CLEAN')

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)