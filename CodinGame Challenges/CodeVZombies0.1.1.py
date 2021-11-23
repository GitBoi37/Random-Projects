import sys
import math

# Save humans, destroy zombies!
def dist(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**.5

#where co is list of coords [[x,y]] p is player coords [x,y]
#TODO
def minDist(co, p):
    m = 999999999
    x = co[0]
    for c in co:
        d = dist(c[0],c[1],p[0],p[1])
        if(d < m):
            m = d
            x = c
    return m

#returns coords and dist
def minDistCoords(co, p):
    m = 999999999
    x = co[0]
    for c in co:
        d = dist(c[0],c[1],p[0],p[1])
        if(d < m):
            m = d
            x = c
    x.insert(0,m)
    #print(x, file=sys.stderr, flush=True)
    return x

#returns the coordinates and distance of the human who is closest to a zombie
def closestHumanToAZombie(humans, zombiePos, x, y):
    x = 0;  y = 0
    m = 999999
    zombieCloseCoords = [minDistCoords(zombiePos, [h[1],h[2]]) for h in humans] #gets the closest zombie coords to each human
    #zombieCloseCoords = [x for x in zombieCloseCoords if x[0] > dist(x,y,x[1],x[2])]    doesnt work lol
    zombieCloseCoords = [[dist(e[1], e[2], x, y), e[1], e[2]] for e in zombieCloseCoords]
    zombieCloseCoords.sort()
    zombieCloseCoords = [[round(float(i)) for i in nested] for nested in zombieCloseCoords]
    print(zombieCloseCoords, file=sys.stderr, flush=True)
    return zombieCloseCoords[0][1:3]

# game loop
while True:
    x, y = [int(i) for i in input().split()]
    humans = []
    zombies = []
    zombiePos = []
    human_count = int(input())
    for i in range(human_count):
        # human_id, human_x, human_y 
        humans.append([int(j) for j in input().split()]) 
    zombie_count = int(input())
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
        zombies.append([zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext])
        zombiePos.append([zombie_x, zombie_y])
    # Write an action using 
    # To debug: ("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates

    print(*closestHumanToAZombie(humans, zombiePos, x, y))
