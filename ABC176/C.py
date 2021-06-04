n = int(input())
l = list(map(int, input().split()))

ans = 0
max_f = l[0]
for i in range(n):
    if l[i] < max_f:
        ans += max_f - l[i]
        l[i] = max_f
    max_f = l[i]
print(ans)
