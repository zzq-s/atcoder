n, x = map(int, input().split())
t = 0
x = x * 100
for i in range(n):
    v, p = map(int, input().split())
    t += v * p
    if t > x:
        print(i+1)
        exit()
print(-1)
