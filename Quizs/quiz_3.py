# Randomly generates a grid with 0s and 1s, whose dimension is controlled by user input,
# as well as the density of 1s in the grid, and finds out, for a given direction being
# one of N, E, S or W (for North, East, South or West) and for a given size greater than 1,
# the number of triangles pointing in that direction, and of that size.
#
# Triangles pointing North:
# - of size 2:
#   1
# 1 1 1
# - of size 3:
#     1
#   1 1 1
# 1 1 1 1 1
#
# Triangles pointing East:
# - of size 2:
# 1
# 1 1
# 1
# - of size 3:
# 1
# 1 1
# 1 1 1
# 1 1
# 1
#
# Triangles pointing South:
# - of size 2:
# 1 1 1
#   1
# - of size 3:
# 1 1 1 1 1
#   1 1 1
#     1
#
# Triangles pointing West:
# - of size 2:
#   1
# 1 1
#   1
# - of size 3:
#     1
#   1 1
# 1 1 1
#   1 1
#     1
#
# The output lists, for every direction and for every size, the number of triangles
# pointing in that direction and of that size, provided there is at least one such triangle.
# For a given direction, the possble sizes are listed from largest to smallest.
#
# We do not count triangles that are truncations of larger triangles, that is, obtained
# from the latter by ignoring at least one layer, starting from the base.
#
# Written by *** and Eric Martin for COMP9021


from random import seed, randint
import sys
from collections import defaultdict


def display_grid():
    for i in range(len(grid)):
        print('   ', ' '.join(str(int(grid[i][j] != 0)) for j in range(len(grid))))
#


def triangles_in_grid():
    triangles_backup={}
    triangles_backup1={}
    count = 0
    count_backup=0
    convert_grid = 0
    size = int((dim+1)/2)
    while True:
        for i in range(size-1 , dim):
            for j in range(size-1, dim-size+1):
                if(grid[i][j]!=0):
                    sum = 0
                    length = 0
                    for k in range(i,i-size,-1):
                        for l in range(j-size+1+length,j+size-length):
                            if(grid[k][l]!=0):
                                sum += 1
                        length+=1
                    if(sum == (size * size)):
                        count += 1
        if(count != 0 and convert_grid==0):
            triangles_backup.setdefault('N',[]).append((size, count-count_backup))

        elif(count != 0 and convert_grid == 90):
            triangles_backup.setdefault('W', []).append((size, count-count_backup))
            triangles_backup1.setdefault('W', []).append((size, count))
        elif (count != 0 and convert_grid == 180):
            triangles_backup.setdefault('S', []).append((size, count-count_backup))
            triangles_backup1.setdefault('S', []).append((size, count))
        elif (count != 0 and convert_grid == 270):
            triangles_backup.setdefault('E', []).append((size, count-count_backup))
            triangles_backup1.setdefault('E', []).append((size, count))
        elif (convert_grid == 360):
            break
        if(size==2):
            count=0
            count_backup=0
            convert_grid = convert_grid_90(convert_grid)
            size = int((dim+1)/2)
        else:
            size -=1
            count_backup=count
            count = 0
    print(triangles_backup1)
    return triangles_backup

    # Replace return {} above with your code

# Possibly define other functions
def convert_grid_90(convert_grid):
    global grid
    grid.reverse()
    grid = [[j[i] for j in grid] for i in range (len(grid[0]))]
    return convert_grid + 90

try:
    arg_for_seed, density, dim = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density, dim = int(arg_for_seed), int(density), int(dim)
    if arg_for_seed < 0 or density < 0 or dim < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
grid = [[randint(0, density) for _ in range(dim)] for _ in range(dim)]
print('Here is the grid that has been generated:')
display_grid()
# A dictionary whose keys are amongst 'N', 'E', 'S' and 'W',
# and whose values are pairs of the form (size, number_of_triangles_of_that_size),
# ordered from largest to smallest size.
triangles=triangles_in_grid()
for direction in sorted(triangles, key = lambda x: 'NESW'.index(x)):
    print(f'\nFor triangles pointing {direction}, we have:')
    for size, nb_of_triangles in triangles[direction]:
        triangle_or_triangles = 'triangle' if nb_of_triangles == 1 else 'triangles'
        print(f'     {nb_of_triangles} {triangle_or_triangles} of size {size}')