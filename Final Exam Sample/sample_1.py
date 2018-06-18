
def remove_consecutive_duplicates(word):
    '''
    >>> remove_consecutive_duplicates('')
    ''
    >>> remove_consecutive_duplicates('a')
    'a'
    >>> remove_consecutive_duplicates('ab')
    'ab'
    >>> remove_consecutive_duplicates('aba')
    'aba'
    >>> remove_consecutive_duplicates('aaabbbbbaaa')
    'aba'
    >>> remove_consecutive_duplicates('abcaaabbbcccabc')
    'abcabcabc'
    >>> remove_consecutive_duplicates('aaabbbbbaaacaacdddd')
    'abacacd'
    '''
    # Insert your code here (the output is returned, not printed out)
    if len(word) == 1:
        return word
    L = list(word)
    LL = []
    flag  = True
    for i in range(len(L)-1):
        if L[i+1] != L[i]:
            LL.append(L[i])
            flag = False
        if i == len(L)-2:
            LL.append(L[i+1])
        if flag == True and  i == len(L) - 2 :
            LL.append(L[i])
    word = ''
    for i in range(len(LL)):
        word += str(LL[i])
    return word

if __name__ == '__main__':
    import doctest
    doctest.testmod()
