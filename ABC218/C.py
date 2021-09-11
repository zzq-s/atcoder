def rotate(matrix):
    n = len(matrix)
    # Python 这里不能 matrix_new = matrix 或 matrix_new = matrix[:] 因为是引用拷贝
    matrix_new = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            matrix_new[j][n - i - 1] = matrix[i][j]
    # 不能写成 matrix = matrix_new
    matrix[:] = matrix_new
    return matrix


n = int(input())
l = list(input().split() for _ in range(n))
t = list(input().split() for _ in range(n))
a = [[0] * n for _ in range(n)]
b = [[0] * n for _ in range(n)]
v = []
k = []

for i in range(n):
    tmp = l[i][0]
    for j in range(n):
        if tmp[j] == '#':
            a[i][j] = 1
            v.append([i, j])

for i in range(n):
    tmp = t[i][0]
    for j in range(n):
        if tmp[j] == '#':
            b[i][j] = 1
            k.append([i, j])

if len(v) != len(k):
    print('No')
    exit()

for i in range(4):
    can = True
    for i in range(len(v)):
        x = v[0][0] - k[0][0]
        y = v[0][1] - k[0][1]
        if v[i][0] - k[i][0] == x and v[i][1] - k[i][1] == y:
            continue
        else:
            can = False

    if can == True:
        print('Yes')
        exit()
    rotate(a)
    v = []
    for i in range(n):
        for j in range(n):
            if a[i][j] == 1:
                v.append([i, j])
print('No')
