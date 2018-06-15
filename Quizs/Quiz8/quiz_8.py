# Randomly fills a grid of size 10 x 10 with 0s and 1s,
# in an estimated proportion of 1/2 for each,
# and computes the longest leftmost path that starts
# from the top left corner -- a path consisting of
# horizontally or vertically adjacent 1s --,
# visiting every point on the path once only.
#
# Written by Jiachen Li and Eric Martin for COMP9021


import sys
from random import seed, randrange


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(grid[i][j]) for j in range(len(grid[0]))))

def check(x,y,gridholder):
    global grid
    if x < 0 or x >= 10 or y < 0 or y >= 10:
        return 0
    if grid[x][y] == 0:
        return 0
    if gridholder[x][y] == 1:
        return 0
    gridholder1=[]
    for i in range(10):
        gridholder1.append([])
        for j in range(10):
            gridholder1[i].append(gridholder[i][j])
    gridholder1[x][y]=1
    return 1 + max(check(x,y+1,gridholder1),check(x,y-1,gridholder1),check(x+1,y,gridholder1),check(x-1,y,gridholder1))


def judgedirection(pi,i,pj,j):
    if i-pi==0 and j-pj==1:
        direction = 'East'
    if i-pi==0 and j-pj==-1:
        direction = 'West'
    if i-pi==1 and j-pj==0:
        direction = 'South'
    if i-pi==-1 and j-pj==0:
        direction = 'North'
    return direction


def leftmost_longest_path_from_top_left_corner():
    i=0
    j=0
    List=[]
    gridholder = [[0 for _ in range(10)] for _ in range(10)]
    t = check(0, 0, gridholder)
    while t >= 1:
        gridholder[i][j] = 1
        List.append((i ,j))
        z1=check(i,j+1,gridholder)
        z2=check(i+1,j,gridholder)
        z3=check(i,j-1,gridholder)
        z4=check(i-1,j,gridholder)
        if i==0 and j==0:
            if z1>=z2:
                x=i
                y=j+1
            else:
                x=i+1
                y=j
        else:
            direction = judgedirection(pi,i,pj,j)
            if direction == 'East':
                if (z4>=z1) and (z4>=z2):
                    x = i-1
                    y = j
                elif (z4<z1) and (z1>=z2):
                    x = i
                    y = j+1
                else:
                    x = i+1
                    y = j
            if direction == 'West':
                if (z2>=z3) and (z2>=z4):
                    x = i+1
                    y = j
                elif (z2<z3) and (z3>=z4):
                    x = i
                    y = j-1
                else:
                    x = i-1
                    y = j
            if direction == 'South':
                if (z1>=z2) and (z1>=z3):
                    x = i
                    y = j+1
                elif (z1<z2) and (z2>=z3):
                    x = i+1
                    y = j
                else:
                    x = i
                    y = j-1
            if direction == 'North':
                if (z3>=z4) and (z3>=z1):
                    x = i
                    y = j-1
                elif (z3<z4) and (z4>=z1):
                    x = i-1
                    y = j
                else:
                    x = i
                    y = j + 1
        pi = i
        pj = j
        i = x
        j = y
        t = check(i,j,gridholder)
    return List
provided_input = input('Enter one integer: ')
try:
    for_seed = int(provided_input)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(for_seed)
grid = [[randrange(2) for _ in range(10)] for _ in range(10)]
print('Here is the grid that has been generated:')
display_grid()
path = leftmost_longest_path_from_top_left_corner()
if not path:
    print('There is no path from the top left corner.')
else:
    print(f'The leftmost longest path from the top left corner is: {path}')