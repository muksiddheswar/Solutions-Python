#!/usr/bin/python

# Head ends here

def next_move(posr, posc, board):
    dustx = []
    dusty = []
    for x,j in enumerate(board):
        if 'd' in j:
            dustx.append(x)
            dusty.append(j.index('d'))
    
    shortest = abs(posr-dustx[0]) + abs(posc-dusty[0])
    index = 0
    for i in range(len(dustx)):
        dist_x = abs(posr - dustx[i])
        dist_y = abs(posc - dusty[i])
        dist = dist_x + dist_y
        if (dist) < shortest:
            shortest = dist
            index = i
    
    row = posr - dustx[index] 
    col = posc - dusty[index]
    
    if row == 0 and col == 0:
        print("CLEAN")
        
    elif col > 0:
        print("LEFT")
    
    elif col < 0:
        print("RIGHT")
        
    elif row > 0:
        print("UP")
    
    elif row < 0:
        print("DOWN")
    
    return
    

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
