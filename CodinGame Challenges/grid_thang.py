import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis
b = []
for i in range(height):
    line = input()  # width characters, each either 0 or .
    b.append(line)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)
graph = [(i, j) for i in range(width) for j in range(height) if b[j][i] == '0']
print(b, file=sys.stderr, flush=True)
print(graph, file=sys.stderr, flush=True)
for x,y in graph:
    rightNode = f"{-1} {-1}"
    downNode = f"{-1} {-1}"

    for i in range(x+1,width):
        if((i, y) in graph):
            print("Found!", file=sys.stderr, flush=True)
            rightNode = f"{i} {y}"
            break

    for i in range(y+1, height):
        if((x, i) in graph):
            downNode = f"{x} {i}"
            print("Found!", file=sys.stderr, flush=True)
            break
    print(f"{x} {y} {rightNode} {downNode}")