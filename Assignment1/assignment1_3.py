# Written by *** for COMP9021


# Insert your code here
import sys

filename = input('Which data file do you want to use? ')
try:
    file = open(filename)
except FileNotFoundError:
    print('Incorrect input, giving up.')
    sys.exit()
List_Rectangle = []
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
        LL.append(False)
    List_Rectangle.append(LL)

def sum_perimeter(list):
    sum_perimetered = 0
    for i in range(len(list)):
        x=abs(list[i][0]-list[i][2])
        y=abs(list[i][1]-list[i][3])
        sum_perimetered += 2 * (x+y)
    return sum_perimetered


def sum_perimeter_repeat(list):
    sum_perimeter_repeated = 0
    for i in range(len(list)):
        for j in range(i+1,len(list)):
            if (list[i][0] < list[j][0]) and (list[i][2] < list[j][2]) and (list[j][0] < list[i][2])\
                    or (list[i][0] < list[j][0]) and (list[i][2] == list[j][2])\
                    or (list[i][0] == list[j][0]) and (list[i][2] < list[j][2]):
                x=abs(list[j][0]-list[i][2])

                if (list[i][1] < list[j][1]) and (list[i][3] < list[j][3]) and (list[j][1] < list[i][3]) \
                        or (list[i][1] < list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] < list[j][3]):
                    y=abs(list[j][1]-list[i][3])
                    sum_perimeter_repeated += 2 *(x+y)

                elif list[i][3] == list[j][1] or list[j][3] == list[i][1]:
                    y = 0
                    sum_perimeter_repeated += 2*(x+y)

                elif ((list[i][1] > list[j][1]) and (list[i][3] > list[j][3]) and (list[i][1] < list[j][3])) \
                        or (list[i][1] > list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[i][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] < list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[j][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] > list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] == list[j][1]) and (list[i][3] == list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

            elif list[i][2] == list[j][0] or list[j][2] == list[i][0]:
                x=0
                if (list[i][1] < list[j][1]) and (list[i][3] < list[j][3]) and (list[j][1] < list[i][3]) \
                        or (list[i][1] < list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[j][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif list[i][3] == list[j][1] or list[j][3] == list[i][1]:
                    y = 0
                    sum_perimeter_repeated += 2 * (x + y)

                elif ((list[i][1] > list[j][1]) and (list[i][3] > list[j][3]) and (list[i][1] < list[j][3])) \
                        or (list[i][1] > list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[i][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] < list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[j][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] > list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] == list[j][1]) and (list[i][3] == list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

            elif ((list[i][0] > list[j][0]) and (list[i][2] > list[j][2]) and (list[i][0] < list[j][2]))\
                    or (list[i][0] > list[j][0]) and (list[i][2] == list[j][2])\
                    or (list[i][0] == list[j][0]) and (list[i][2] > list[j][2]):
                x=abs(list[i][0]-list[j][2])
                if (list[i][1] < list[j][1]) and (list[i][3] < list[j][3]) and (list[j][1] < list[i][3]) \
                        or (list[i][1] < list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[j][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif list[i][3] == list[j][1] or list[j][3] == list[i][1]:
                    y = 0
                    sum_perimeter_repeated += 2 * (x + y)

                elif ((list[i][1] > list[j][1]) and (list[i][3] > list[j][3]) and (list[i][1] < list[j][3])) \
                        or (list[i][1] > list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[i][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] < list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[j][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] > list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] == list[j][1]) and (list[i][3] == list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

            elif(list[i][0] < list[j][0]) and (list[i][2] > list[j][2]):
                x=abs(list[j][0]-list[j][2])
                if (list[i][1] < list[j][1]) and (list[i][3] < list[j][3]) and (list[j][1] < list[i][3]) \
                        or (list[i][1] < list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[j][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)
                elif list[i][3] == list[j][1] or list[j][3] == list[i][1]:
                    y = 0
                    sum_perimeter_repeated += 2 * (x + y)
                elif ((list[i][1] > list[j][1]) and (list[i][3] > list[j][3]) and (list[i][1] < list[j][3])) \
                        or (list[i][1] > list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[i][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] < list[j][1]) and (list[i][3] > list[j][3]) and list[j][4] == False:
                    y = abs(list[j][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)
                    list[j][4] = True

                elif (list[i][1] > list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)
                elif (list[i][1] == list[j][1]) and (list[i][3] == list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

            elif(list[i][0] > list[j][0]) and (list[i][2] < list[j][2]):
                x = abs(list[i][0] - list[i][2])
                if (list[i][1] < list[j][1]) and (list[i][3] < list[j][3]) and (list[j][1] < list[i][3]) \
                        or (list[i][1] < list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[j][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif list[i][3] == list[j][1] or list[j][3] == list[i][1]:
                    y = 0
                    sum_perimeter_repeated += 2 * (x + y)

                elif ((list[i][1] > list[j][1]) and (list[i][3] > list[j][3]) and (list[i][1] < list[j][3])) \
                        or (list[i][1] > list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[i][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] < list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[j][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] > list[j][1]) and (list[i][3] < list[j][3]) and list[i][4] == False:
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)
                    list[i][4] = True

                elif (list[i][1] == list[j][1]) and (list[i][3] == list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

            elif (list[i][0] == list[j][0]) and (list[i][2] == list[j][2]):
                x = abs(list[i][0] - list[i][2])

                if (list[i][1] < list[j][1]) and (list[i][3] < list[j][3]) and (list[j][1] < list[i][3]) \
                        or (list[i][1] < list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[j][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif list[i][3] == list[j][1] or list[j][3] == list[i][1]:
                    y = 0
                    sum_perimeter_repeated += 2 * (x + y)

                elif ((list[i][1] > list[j][1]) and (list[i][3] > list[j][3]) and (list[i][1] < list[j][3])) \
                        or (list[i][1] > list[j][1]) and (list[i][3] == list[j][3]) \
                        or (list[i][1] == list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[i][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] < list[j][1]) and (list[i][3] > list[j][3]):
                    y = abs(list[j][1] - list[j][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] > list[j][1]) and (list[i][3] < list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)

                elif (list[i][1] == list[j][1]) and (list[i][3] == list[j][3]):
                    y = abs(list[i][1] - list[i][3])
                    sum_perimeter_repeated += 2 * (x + y)
    return sum_perimeter_repeated
print('The perimeter is:',sum_perimeter(List_Rectangle)-sum_perimeter_repeat(List_Rectangle))