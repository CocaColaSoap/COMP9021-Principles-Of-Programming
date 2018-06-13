# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys

# Insert your code here
word = input('Please input a string of lowercase letters: ')
for items in word:
    if not items.islower():
        print('Incorrect input.')
        sys.exit()

List = []
for items in word:
    List.append(ord(items))
List=list(set(List))
List.sort()

List_judge=[]
for size in range(len(List),0,-1):
    for i in range(len(List)):
        if i+size <= len(List):
            List_judge=List[i:i+size]
            Flag = True
            for k in range(len(List_judge)-1):
                if List_judge[k+1]-List_judge[k] != 1:
                    Flag = False
                    break
                else:
                    continue
        if Flag:
            break
    if Flag:
        break

print('The solution is: ', end = '')
for items in List_judge:
    print(chr(items),end='')