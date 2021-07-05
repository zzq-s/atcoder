n, m, t = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]

battery = n
for i in range(m):
    if n - l[i][0] <= 0:
        print('No')
        exit()
    n = n - 2*l[i][0] + 2*l[i][1]
    if n > battery + l[i][1]:
        n = battery + l[i][1]
    print(n)

if n - t > 0:
    print('Yes')
else:
    print('No')
