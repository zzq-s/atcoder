a, b, c, d = map(int, input().split())
r = 0
for i in range(10**5):
    a += b
    r += c
    if r * d >= a:
        print(i+1)
        exit(0)
print(-1)
