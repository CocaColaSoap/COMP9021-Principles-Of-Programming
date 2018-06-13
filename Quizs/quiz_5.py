# Randomly fills a grid of size 10 x 10 with 0s and 1s and computes:
# - the size of the largest homogenous region starting from the top left corner,
#   so the largest region consisting of connected cells all filled with 1s or
#   all filled with 0s, depending on the value stored in the top left corner;
# - the size of the largest area with a checkers pattern.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randint
from copy import deepcopy
dim = 10
grid = [[None] * dim for _ in range(dim)]


def display_grid():
    for i in range(dim):
        print('   ', ' '.join(str(int(grid[i][j]!=0)) for j in range(dim)))


# Possibly define other functions

try:
    arg_for_seed, density = input('Enter two nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, density = int(arg_for_seed), int(density)
    if arg_for_seed < 0 or density < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
# We fill the grid with randomly generated 0s and 1s,
# with for every cell, a probability of 1/(density + 1) to generate a 0.
for i in range(dim):
    for j in range(dim):
        grid[i][j] = int(randint(0, density) != 0)
print('Here is the grid that has been generated:')
display_grid()

size_of_largest_homogenous_region_from_top_left_corner = 0
# Replace this comment with your code
grid_backup = deepcopy(grid)

def replace_0_by_star(i,j):
    global grid
    if grid[i][j] == 0:
        grid[i][j] = '*'
        if i:
            replace_0_by_star(i - 1, j)
        if i < dim - 1:
            replace_0_by_star(i + 1, j)
        if j:
            replace_0_by_star(i, j - 1)
        if j < dim - 1:
            replace_0_by_star(i, j + 1)


def replace_1_by_star(i,j):
    global grid
    if grid[i][j] == 1:
        grid[i][j] = '*'
        if i:
            replace_1_by_star(i-1,j)
        if i < dim -1:
            replace_1_by_star(i+1,j)
        if j:
            replace_1_by_star(i,j-1)
        if j<dim-1:
            replace_1_by_star(i,j+1)


if grid[0][0] == 1:
    replace_1_by_star(0, 0)
else:
    replace_0_by_star(0, 0)

for i in range(dim):
    for j in range(dim):
        if grid[i][j] =='*':
            size_of_largest_homogenous_region_from_top_left_corner += 1

grid = deepcopy(grid_backup)
print('The size_of the largest homogenous region from the top left corner is '
      f'{size_of_largest_homogenous_region_from_top_left_corner}.'
      )



max_size_of_region_with_checkers_structure = 0
# Replace this comment with your code

def judge_value(value):
    if value:
        return 0
    else:
        return 1


def find_checker_area(i, j, grid, count, value):
    if grid[i][j] == value:
        grid[i][j] = '*'
        count += 1
        if i:
            count = find_checker_area(i - 1, j, grid, count, judge_value(value))

        if i < dim - 1:
            count = find_checker_area(i + 1, j, grid, count, judge_value(value))

        if j:
            count = find_checker_area(i, j - 1, grid, count, judge_value(value))

        if j < dim - 1:
            count = find_checker_area(i, j + 1, grid, count, judge_value(value))
    return count




max_count = 0
count = 0
for i in range(0, dim - 1):
    for j in range(0, dim - 1):
        current_count = find_checker_area(i, j, grid, count, grid[i][j])
        if current_count > max_count:
            max_count = current_count
        count = 0
        grid = grid_backup.copy()

max_size_of_region_with_checkers_structure = max_count

print('The size of the largest area with a checkers structure is '
      f'{max_size_of_region_with_checkers_structure}.'
      )






