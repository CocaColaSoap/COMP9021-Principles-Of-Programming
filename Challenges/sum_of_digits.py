# Prompts the user for two numbers, say available_digits and desired_sum, and
# outputs the number of ways of selecting digits from available_digits
# that sum up to desired_sum.


import sys
def solve(available_digits, desired_sum):
    nb_of_solutions = 0
    list = []

    if desired_sum < 0:
        return 0
    elif available_digits == 0:
        return 0
    else:
        available_digits = str(available_digits)
        for i in range(len(available_digits)):
            list.append(int(available_digits[i]))
        for i in range(len(list)):
            for j in range(len(list)):
                if list[i] + list[j] == desired_sum:
                    nb_of_solutions += 1
        for i in range(len(list)):
            for j in range(2,len(list)):





# Insert your code here
try:
    available_digits = abs(int(input('Input a number that we will use as available digits: ')))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
try:
    desired_sum = int(input('Input a number that represents the desired sum: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
nb_of_solutions = solve(available_digits, desired_sum)
if nb_of_solutions == 0:
    print('There is no solution.')
elif nb_of_solutions == 1:
    print('There is a unique solution.')
else:
    print(f'There are {nb_of_solutions} solutions.')