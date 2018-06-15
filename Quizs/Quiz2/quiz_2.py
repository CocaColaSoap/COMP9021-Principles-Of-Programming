# Written by Jiachen Li and Eric Martin for COMP9021


'''
Prompts the user for two strictly positive integers, numerator and denominator.

Determines whether the decimal expansion of numerator / denominator is finite or infinite.

Then computes integral_part, sigma and tau such that numerator / denominator is of the form
integral_part . sigma tau tau tau ...
where integral_part in an integer, sigma and tau are (possibly empty) strings of digits,
and sigma and tau are as short as possible.
'''


import sys
from math import gcd

try:
    numerator, denominator = input('Enter two strictly positive integers: ').split()
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    numerator, denominator = int(numerator), int(denominator)
    if numerator <= 0 or denominator <= 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

has_finite_expansion = False
integral_part = 0
sigma = ''
tau = ''
# Replace this comment with your code
greatest_common_diviso=gcd(numerator,denominator)
numerator_backup=numerator/greatest_common_diviso
denominator_backup=denominator/greatest_common_diviso

while True:
    if(denominator_backup%2==0):
        denominator_backup = denominator_backup / 2
    elif((denominator_backup%2==1)and(denominator_backup==1)):
        has_finite_expansion = True
        break
    elif((denominator_backup%2==1)and(denominator_backup!=1)):
        break
if(has_finite_expansion == True):
    pass
else:
    while True:
        if(denominator_backup % 5 == 0):
            denominator_backup = denominator_backup/5
        elif((denominator_backup%5==1)and(denominator_backup==1)):
            has_finite_expansion = True
            break
        elif((denominator_backup%5==1)or(denominator_backup%5==2)or(denominator_backup%5==3)or(denominator_backup%5==4)):
            break

L_remainder = []
remainder = numerator%denominator
integral_part = int(numerator/denominator)
while remainder!=0:
    if L_remainder.count(remainder)==1:
        for i in range(len(L_remainder)):
            if(L_remainder[i] == remainder):
                sigma = tau[0:i]
                tau = tau[i:len(L_remainder)]
                break
        break
    L_remainder.append(remainder)
    tau += str(int((remainder*10)/denominator))
    remainder = (remainder*10)%denominator

if has_finite_expansion:
    print(f'\n{numerator} / {denominator} has a finite expansion')
    if(numerator%denominator == 0):
        print(f'{numerator} / {denominator} =',numerator // denominator)
    else:
        print(f'{numerator} / {denominator} =', numerator / denominator)
else:
    print(f'\n{numerator} / {denominator} has no finite expansion')

    if not tau:
        if not sigma:
            integral_part = numerator / denominator
            print(f'{numerator} / {denominator} = {integral_part}')
        else:
            print(f'{numerator} / {denominator} = {integral_part}.{sigma}')
    else:
        print(f'{numerator} / {denominator} = {integral_part}.{sigma}({tau})*')