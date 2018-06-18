
def is_heterosquare(square):
    '''
    A heterosquare of order n is an arrangement of the integers 1 to n**2 in a square,
    such that the rows, columns, and diagonals all sum to DIFFERENT values.
    In contrast, magic squares have all these sums equal.
    
    
    >>> is_heterosquare([[1, 2, 3],\
                         [8, 9, 4],\
                         [7, 6, 5]])
    True
    >>> is_heterosquare([[1, 2, 3],\
                         [9, 8, 4],\
                         [7, 6, 5]])
    False
    >>> is_heterosquare([[2, 1, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    True
    >>> is_heterosquare([[1, 2, 3, 4],\
                         [5, 6, 7, 8],\
                         [9, 10, 11, 12],\
                         [13, 14, 15, 16]])
    False
    '''
    n = len(square)
    if any(len(line) != n for line in square):
        return False
    # Insert your code here
    List =[]
    for i in range(len(square)):
        count = 0
        for j in range(len(square[i])):
            count += square[i][j]
        List.append(count)

    for j in range(len(square[0])):
        count = 0
        for i in range(len(square)):
            count += square[i][j]
        List.append(count)
    count = 0
    for i in range(len(square)):
        count += square[i][i]
    List.append(count)
    count = 0
    for i in range(len(square)):
        count += square[i][-(i+1)]
    List.append(count)
    for i in range(len(List)):
        for j in range(i+1,len(List)):
            if List[i] == List[j]:
                return False
    return True
# Possibly define other functions

    
if __name__ == '__main__':
    import doctest
    doctest.testmod()
