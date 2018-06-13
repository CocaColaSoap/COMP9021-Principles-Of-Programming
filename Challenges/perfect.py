# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys

# Insert your code here
try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
L_perfect = []
sum = 0
for i in range(2, N+1):
    for j in range(1,i-1):
        if(i%j == 0):
            L_perfect.append(j)
        else:
            pass
    for k in range(len(L_perfect)):
        sum += L_perfect[k]
    if(sum == i):
        print(f'{i} is a perfect number.')
        sum = 0
        L_perfect.clear()
    else:
        sum = 0
        L_perfect.clear()
