#

def nextMove(n,r,c,grid):
    pr = ()
    for x,j in enumerate(grid):
            if 'p' in j:
                pr = (x, j.index('p'))    
                      
    ver = r - pr[0]
    hor = c - pr [1]
                      
    if ver > 0:
        move = 'UP'
    elif ver < 0:
        move = 'DOWN'
                      
    elif hor > 0:
        move = 'LEFT'
    elif hor < 0:
        move = 'RIGHT'
    
    return move

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
