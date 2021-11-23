import sys
import math
import copy
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def getNumNeighbors(grid, gpos):
    #extract x and y from grid position
    x = gpos[0]
    y = gpos[1]
    n = 0
    #reminder: range(inclusive, exclusive)
    #check all values around but not on gpos
    for i in range(y-1,y+2):
        for j in range(x-1, x+2):
            #test if iterators equal to gpos or i and j below 0 (since -1 isn't technically out of bounds in python)
            if((j,i) != gpos and i >= 0 and j >= 0):
                #instead of doing all the ifs and stuff to check if out of bounds I used a try except, I wonder if I could just check if i < len(grid) and j < len(grid[0])?
                try:
                    if(grid[i][j] == 'O'):
                        n += 1
                except IndexError:
                    pass
    #print(f"node at {x}, {y} has {n} neighbors",file=sys.stderr,flush=True)
    return n

def simulateTurn(grid, alive, dead):
    #on today's episode of how many fucking times can I copy a list before it actually works, attempt number 77:
    newGrid = [i[:] for i in grid]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            g = grid[i][j]
            n = getNumNeighbors(grid, (j,i))
            #if grid member is an O it could die if alive == 0 else nothing
            #if grid member is an . it could resurrect if dead == 1 else nothing
            if(g == "O"):
                if(alive[n] == "0"):
                    newGrid[i][j] = "."
            else:
                if(dead[n] == "1"):
                    newGrid[i][j] = "O"
    return newGrid

#assemble input
h, w, n = [int(i) for i in input().split()]
alive = input()
dead = input()
grid = []
for i in range(h):
    line = input()
    grid.append(list(line))

#simulate life turn by turn
for x in range(n):
    grid = simulateTurn(grid, alive, dead)

#output answer
for x in grid:
    for i in x:
        print(i, end = "")
    print()

