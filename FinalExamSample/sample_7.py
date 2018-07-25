'''
Tries and find a word in a text file that represents a grid of words, all of the same length.
There is only one word per line in the file.
The letters that make up a word can possibly be separated by an arbitrary number of spaces,
and there can also be spaces at the beginning or at the end of a word,
and there can be lines consisting of nothing but spaces anywhere in the file.
Assume that the file stores data as expected.

A word can be read horizontally from left to right,
or vertically from top to bottom,
or diagonally from top left to bottom right
(this is more limited than the lab exercise).
The locations are represented as a pair (line number, column number),
starting the numbering with 1 (not 0).
'''


def find_word(filename, word):
    '''
    >>> find_word('word_search_1.txt', 'PLATINUM')
    PLATINUM was found horizontally (left to right) at position (10, 4)
    >>> find_word('word_search_1.txt', 'MANGANESE')
    MANGANESE was found horizontally (left to right) at position (11, 4)
    >>> find_word('word_search_1.txt', 'LITHIUM')
    LITHIUM was found vertically (top to bottom) at position (2, 14)
    >>> find_word('word_search_1.txt', 'SILVER')
    SILVER was found vertically (top to bottom) at position (2, 13)
    >>> find_word('word_search_1.txt', 'SODIUM')
    SODIUM was not found
    >>> find_word('word_search_1.txt', 'TITANIUM')
    TITANIUM was not found
    >>> find_word('word_search_2.txt', 'PAPAYA')
    PAPAYA was found diagonally (top left to bottom right) at position (1, 9)
    >>> find_word('word_search_2.txt', 'RASPBERRY')
    RASPBERRY was found vertically (top to bottom) at position (5, 14)
    >>> find_word('word_search_2.txt', 'BLUEBERRY')
    BLUEBERRY was found horizontally (left to right) at position (13, 5)
    >>> find_word('word_search_2.txt', 'LEMON')
    LEMON was not found
    '''
    with open(filename) as file:
        grid = None
        i = 0
        grid = []
        while True:
            line = file.readline()
            if not line:
                break
            else:
                L = line.split()
                LL = []
                if len(L) != 0:
                    for item in L:
                        for i in range(len(item)):
                            LL.append(item[i])
                if len(LL) != 0:
                    grid.append(LL)
        # A one liner that sets grid to the appropriate value is enough.
        location = find_word_horizontally(grid, word)
        found = False
        if location:
            found = True
            print(word, 'was found horizontally (left to right) at position', location)
        location = find_word_vertically(grid, word)
        if location:
            found = True
            print(word, 'was found vertically (top to bottom) at position', location)
        location = find_word_diagonally(grid, word)
        if location:
            found = True
            print(word, 'was found diagonally (top left to bottom right) at position', location)
        if not found:
            print(word, 'was not found')
    
    
def find_word_horizontally(grid, word):
    location =''
    size = len(word)
    for i in range(len(grid)):
        for j in range(len(grid[i])-size):
            word_back = grid[i][j:j+size]
            word_1 = ''
            for k in range (len(word_back)):
                word_1 += word_back[k]
            if word_1 == word:
                location = '('+str(i+1) +', ' +str(j+1)+')'
    return location


    # Replace pass above with your code


def find_word_vertically(grid, word):
    location =''

    size = len(word)
    for j in range(len(grid[0])):

        for k in range(0,len(grid)-size):
            word_back = ''
            for i in range(k,k+size):
                word_back += grid[i][j]
                if word_back == word:
                    location = '(' + str(k + 1) + ', ' + str(j + 1) + ')'
    return location
    # Replace pass above with your code


def find_word_diagonally(grid, word):
    location =''
    size = len(word)
    for i in range(len(grid)-size+1):
        flag = False
        for j in range(len(grid[i])-size+1):
            word_back = ''
            for k, h in zip(range(i,i+size),range(j,j+size)):
                word_back += str(grid[k][h])
            if word_back == word:
                flag = True
                location = '(' + str(i + 1) + ', ' + str(j + 1) + ')'
                break
        if flag is True:
            break
    return location






if __name__ == '__main__':
    import doctest
    doctest.testmod()   
