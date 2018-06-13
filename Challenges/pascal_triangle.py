# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.


# Insert you code here
while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')

pascal_triangle = [[1] * (n + 1) for n in range(N + 1)]
for i in range(2,N+1):
    for j in range(1,len(pascal_triangle[i])-1):
        pascal_triangle[i][j]=pascal_triangle[i-1][j]+pascal_triangle[i-1][j-1]

width = len(str(pascal_triangle[N][N // 2]))
for n in range(N + 1):
    print(' ' * width * (N - n), end = '')
    print((' ' * width).join((f'{pascal_triangle[n][k]:{width}d}' for k in range(n + 1))))