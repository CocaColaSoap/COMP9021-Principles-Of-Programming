# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


# Insert your code here
from math import sqrt


def is_prime(n):
    Flag = True
    for i in range(3, round(sqrt(n)) + 1, 2):
        if n / i == n // i:
            Flag = False
            break
    return Flag


print('The solutions are:\n')

list = []
for i in range(10001, 99970, 2):
    Flag = True
    list = [i, i + 2, i + 6, i + 12, i + 20, i + 30]
    for j in range (i, i + 30, 2):
        x = False
        for items in list:
            if j == items:
                x = True
                break
        if is_prime(j) and x != True:
            list.clear()
            Flag = False
            break

    if Flag == True:
        for items in list:
            if is_prime(items) != True:
                list.clear()
    if len(list) != 0:
        for i in range (len(list)):
            if i == len(list)-1:
                print(list[i])
            else:
                print(list[i],' ',end='')



