# Written by *** for COMP9021


# Insert your code here
import sys
filename = input('Which data file do you want to use?')
try:
	file = open(filename)
except FileNotFoundError:
    print('Incorrect input, giving up.')
    sys.exit()
L_triangle = []
count = 0
while True:
    line = file.readline()
    if not line:
        break
    else:
        L = line.split()
        LL = []
        for items in L:
            LL.append(int(items))
        L_triangle.append(LL)
        count += 1

path = 1
for i in range(count-1,-1,-1):
    for j in range(len(L_triangle[i])-1):
        if len(L_triangle[i]) == 1:
            continue
        else:
            if L_triangle[i][j] > L_triangle[i][j+1] :
                L_triangle[i-1][j] = L_triangle[i-1][j] + L_triangle[i][j]
            elif L_triangle[i][j] < L_triangle[i][j+1]:
                L_triangle[i-1][j] = L_triangle[i-1][j] + L_triangle[i][j+1]
            else:
                L_triangle[i - 1][j] = L_triangle[i - 1][j] + L_triangle[i][j]
list = []
for i in range (count-1):
    if len(L_triangle[i]) == 1:
        if L_triangle[i+1][0] > L_triangle[i+1][1]:
            list.append(L_triangle[i][0]-L_triangle[i+1][0])
            j = 0
        elif L_triangle[i+1][0] < L_triangle[i+1][1]:
            list.append((L_triangle[i][0])-L_triangle[i+1][1])
            j = 1
        else:
            list.append(L_triangle[i][0]-L_triangle[i+1][0])
            j = 0
    else:
        if L_triangle[i+1][j] > L_triangle[i+1][j+1]:
            list.append(L_triangle[i][j]-L_triangle[i+1][j])
            if len(L_triangle[i + 1]) == count:
                list.append(L_triangle[i+1][j])
        elif L_triangle[i+1][j] < L_triangle[i+1][j+1]:
            list.append(L_triangle[i][j]-L_triangle[i+1][j+1])
            j= j+1
            if len(L_triangle[i + 1]) == count:
                list.append(L_triangle[i+1][j+1])
        else:
            list.append(L_triangle[i][j] - L_triangle[i + 1][j])
            if len(L_triangle[i + 1]) == count:
                list.append(L_triangle[i+1][j])

list_equal=[[0]]
for i in range(count-1):
        xxx = []
        for j in range (len(list_equal[i])):
            if L_triangle[i+1][list_equal[i][j]]>L_triangle[i+1][list_equal[i][j]+1]:
                xxx.append(j)
            elif L_triangle[i+1][list_equal[i][j]]<L_triangle[i+1][list_equal[i][j]+1]:
                xxx.append(j+1)
            else:
                xxx.append(j)
                xxx.append(j+1)
                path += 1
        list_equal.append(xxx)
        if len(list_equal[i]) > len(L_triangle[i]):
            break

print('The largest sum is:',L_triangle[0][0])
print('The number of paths yielding this sum is:',path)
print('The leftmost path yielding this sum is:',list)