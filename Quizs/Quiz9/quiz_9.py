# Randomly generates a binary search tree whose number of nodes
# is determined by user input, with labels ranging between 0 and 999,999,
# displays it, and outputs the maximum difference between consecutive leaves.
#
# Written by *** and Eric Martin for COMP9021

import sys
from random import seed, randrange
from Quizs.Quiz9.binary_tree_adt import *

# Possibly define some functions

List = []
def findleave(tree):
    if (tree.left_node.value is not None) and (tree.right_node.value is not None):
        return findleave(tree.left_node), findleave(tree.right_node)
    elif (tree.left_node.value is None) and (tree.right_node.value is not None):
        return findleave(tree.right_node)
    elif (tree.left_node.value is not None) and (tree.right_node.value is None):
        return findleave(tree.left_node)
    elif (tree.left_node.value is None) and (tree.right_node.value is None):
        List.append(tree.value)
def max_diff_in_consecutive_leaves(tree):
    findleave(tree)
    if len(List) <= 1:
        return 0
    else:
        max_diff = List[1]-List[0]
        for i in range(1,len(List)):
            if List[i]-List[i-1] > max_diff:
                max_diff = List[i]-List[i-1]
        return max_diff

provided_input = input('Enter two integers, the second one being positive: ')
try:
    arg_for_seed, nb_of_nodes = provided_input.split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, nb_of_nodes = int(arg_for_seed), int(nb_of_nodes)
    if nb_of_nodes < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
seed(arg_for_seed)
tree = BinaryTree()
for _ in range(nb_of_nodes):
    datum = randrange(1000000)
    tree.insert_in_bst(datum)
print('Here is the tree that has been generated:')
tree.print_binary_tree()
print('The maximum difference between consecutive leaves is: ', end = '')
print(max_diff_in_consecutive_leaves(tree))