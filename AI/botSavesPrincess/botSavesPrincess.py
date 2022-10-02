#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    bot = ()
    pr = ()
    for x,j in enumerate(grid):
        for y,l in enumerate(j):
            if l == 'm':
                bot = (x,y)
            if l == 'p':
                pr = (x,y)
                
    ver = bot[0] - pr[0]
    hor = bot[1] - pr [1]
    if ver > 0:
        move1 = 'UP'
    else:
        move1 = 'DOWN'

    if hor > 0:
        move2 = 'LEFT'
    else:
        move2 = 'RIGHT'

    for i in range(abs(hor)):
        print(move1)

    for i in range(abs(ver)):
        print(move2)

    return

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
