'''
Given a word w, a good subsequence of w is defined as a word w' such that
- all letters in w' are different;
- w' is obtained from w by deleting some letters in w.

Returns the list of all good subsequences, without duplicates, in lexicographic order
(recall that the sorted() function sorts strings in lexicographic order).

The number of good sequences grows exponentially in the number of distinct letters in w,
so the function will be tested only for cases where the latter is not too large.

'''


def good_subsequences(word):
    '''
    >>> good_subsequences('')
    ['']
    >>> good_subsequences('aaa')
    ['', 'a']
    >>> good_subsequences('aaabbb')
    ['', 'a', 'ab', 'b']
    >>> good_subsequences('aaabbc')
    ['', 'a', 'ab', 'abc', 'ac', 'b', 'bc', 'c']
    >>> good_subsequences('aaabbaaa')
    ['', 'a', 'ab', 'b', 'ba']
    >>> good_subsequences('abbbcaaabccc')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb']
    >>> good_subsequences('abbbcaaabcccaaa')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    >>> good_subsequences('abbbcaaabcccaaabbbbbccab')
    ['', 'a', 'ab', 'abc', 'ac', 'acb', 'b', 'ba', 'bac',\
 'bc', 'bca', 'c', 'ca', 'cab', 'cb', 'cba']
    '''
    # Insert your code here
    result =[]
    if len(word) == 0:
        return ['']
    L = list(word)
    LL = ['']
    flag  = True
    for i in range(len(L)-1):
        if L[i+1] != L[i]:
            LL.append(L[i])
            flag = False
        if i == len(L)-2:
            LL.append(L[i+1])
        if flag == True and  i == len(L) - 2 :
            LL.append(L[i])
    for i in range(len(LL)):
        if LL[i] not in result:
            result.append(LL[i])
    if len(result) > 1:
        for i in range(len(LL)):
            for j in range(i+1,len(LL)):
                if LL[i] == LL[j]:
                    pass
                elif LL[i] + LL[j] not in result:
                    result.append(LL[i]+LL[j])
    if len(result) > 2:
        for i in range(len(LL)):
            for j in range(i+1,len(LL)):
                for k in range(j+1,len(LL)):
                    if LL[i] == LL[j] or LL[i] == LL[k] or LL[k] == LL[j]:
                        pass
                    elif LL[i] + LL[j] + LL[k] not in result:
                        result.append(LL[i] + LL[j] + LL[k])
    return sorted(result)
# Possibly define another function
                

if __name__ == '__main__':
    import doctest
    doctest.testmod()
