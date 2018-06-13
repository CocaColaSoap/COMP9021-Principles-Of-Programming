# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.


# Insert you code here

def is_square(n):
    list = []
    for i in range(32):
        for j in range(i,32):
            if (i*i + j*j > 100) and (i*i + j*j < 1000):
                if n == i*i + j*j:
                    list=[n,i,j]
                    break
    return list

for i in range(100,997):
    list1=is_square(i)
    list2=is_square(i+1)
    list3=is_square(i+2)
    if(len(list1)!=0) and (len(list2)!=0) and (len(list3)!=0):
        print(f'({list1[0]}, {list2[0]}, {list3[0]}) (equal to ('
                                    f'{list1[1]}^2+{list1[2]}^2, '
                            f'{list2[1]}^2+{list2[2]}^2, '
                              f'{list3[1]}^2+{list3[2]}^2'')) is a solution.')


