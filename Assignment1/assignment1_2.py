# Written by *** for COMP9021


# Insert your code here
import sys

filename = input('Which data file do you want to use? ')
try:
    file = open(filename)
except FileNotFoundError:
    print('Incorrect input, giving up.')
    sys.exit()
List_Fish = []
count = 0
while True:
    line = file.readline()
    if not line:
        break
    else:
        line = line.split()
        LL = []
        for items in line:
            items = int(items)
            LL.append(items)
        List_Fish.append(LL)
        count += 1

def maximise_quantity(list):
    sum = 0
    distance =  0
    min = list[0][1]
    for items in list:
        if min > items[1]:
            min = items[1]
        sum += items[1]
    for i in range(len(list)-1):
        distance += list[i+1][0]-list[i][0]
    max = int(sum/count)
    while True:
        max_quantity = round((max + min) / 2)
        if count * max_quantity == (sum-distance):
            break
        elif count * max_quantity > (sum-distance):
            max = max_quantity
        elif count * max_quantity < (sum-distance):
            min = max_quantity
        if max == min or max-min == 1:
            max_quantity = min
            break
    return str(max_quantity)

print('The maximum quantity of fish that each town can have is '+maximise_quantity(List_Fish)+'.')