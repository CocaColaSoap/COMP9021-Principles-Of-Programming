# Written by Jiachen Li for COMP9021


# Insert your code here
import sys

filename = input('Which data file do you want to use? ')
dictory_path={}
try:
    file = open(filename)
except FileNotFoundError:
    print('Incorrect input, giving up.')
    sys.exit()
List=[]
while True:
    line = file.readline()
    if not line:
        break
    else:
        line = line[2:5]
        line = line.split(',')
        LL = []
        for items in line:
            items = int(items)
            LL.append(items)
    List.append(LL)


def find_child(begin,end,list):
    for items in list:
        if items[0] == begin and items[1] == end:
            return True
        elif items[0] == begin:
            return find_child(items[1],end,list)
    return False

def find_parent(begin, end, list, up_list, down_list):
    for items in list:
        if items[1] == begin and begin != -1:
            up_list.append(items[0])
            find_parent(items[0], -1, list, up_list, down_list)
        if items[0] == end and end != -1:
            down_list.append(items[1])
            find_parent(-1, items[1], list, up_list, down_list)

    for i in up_list:
        for j in down_list:
            if list.count([i, j]) > 0:
                list.remove([i, j])

List_add = []

for items in List:
    if not find_child(items[0], items[1], List_add):
        up_list = [items[0]]
        down_list = [items[1]]
        find_parent(items[0], items[1], List_add, up_list, down_list)
        List_add.append(items)
print(f'The nonredundant facts are:')
for items in List_add:
    print(f'R({items[0]},{items[1]})')