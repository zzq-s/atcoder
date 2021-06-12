n = int(input())
l = list(map(int, input().split()))

ans = 0
for i in l:
    if i > 10:
        ans += i - 10
print(ans)
