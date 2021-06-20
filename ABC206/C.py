n = int(input())
l = list(map(int, input().split()))
h = dict()
ans = 0
for i in l:
    if i in h:
        h[i] += 1
    else:
        h[i] = 1
for i in h:
    n = n - h[i]
    if n != 0:
        ans += h[i] * n
print(ans)
