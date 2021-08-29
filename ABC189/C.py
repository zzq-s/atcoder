n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in range(n):
    num = l[i]
    for j in range(i, n):
        num = min(num, l[j])
        ans = max(ans, num * (j-i+1))
print(ans)
