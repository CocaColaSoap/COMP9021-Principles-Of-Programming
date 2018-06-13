# Written by *** and Eric Martin for COMP9021


'''
Generates a list L of random nonnegative integers at most equal to a given upper bound,
of a given length, all controlled by user input.

Outputs four lists:
- elements_to_keep, consisting of L's smallest element, L's third smallest element,
  L's fifth smallest element, ...
  Hint: use sorted(), list slices, and set()
- L_1, consisting of all members of L which are part of elements_to_keep, preserving
  the original order
- L_2, consisting of the leftmost occurrences of the members of L which are part of
  elements_to_keep, preserving the original order
- L_3, consisting of the LONGEST, and in case there are more than one candidate, the
  LEFTMOST LONGEST sequence of CONSECUTIVE members of L that reduced to a set,
  is a set of integers without gaps.
'''

import sys
from random import seed, randint

try:
    arg_for_seed, upper_bound, length = input('Enter three nonnegative integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    arg_for_seed, upper_bound, length = int(arg_for_seed), int(upper_bound), int(length)
    if arg_for_seed < 0 or upper_bound < 0 or length < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randint(0, upper_bound) for _ in range(length)]
print('\nThe generated list L is:')
print('  ', L)
L_1 = []
L_2 = []
L_3 = []
elements_to_keep = []
# Replace this comment with your code
L_backup = L.copy()
L_backup = sorted(list(set(L_backup)))
for i in range(0,len(L_backup),2):
    elements_to_keep.append(L_backup[i])
print('\nThe elements to keep in L_1 and L_2 are:')
print('  ', elements_to_keep)
for i in range(len(L)):
    for j in range(len(elements_to_keep)):
        if(elements_to_keep[j] == L[i]):
            L_1.append(L[i])
print('\nHere is L_1:')
print('  ', L_1)
L_2= sorted(set(L_1), key=L_1.index)
print('\nHere is L_2:')
print('  ', L_2)
a=True
if(len(L)==1):
    L_3=L
else:
    for i in range(len(L), 1, -1):
        for j in range(0, len(L)):
            if((i+j) > len(L)):
                break
            else:
                L_3_backup=sorted(L[j:j+i])
                for k in range(1,len(L_3_backup)):
                    if((L_3_backup[k]-L_3_backup[k-1]<=1)):
                        a = True
                        continue
                    else:
                        L_3_backup.clear()
                        a = False
                        break
            if (a == True):
                break
        if(a == True):
            L_3=L[j:j+i]
            break
if(len(L_3)==0):
    L_3.append(L_backup[-1])
print('\nHere is L_3:')
print('  ', L_3)

