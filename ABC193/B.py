n = int(input())
ans = 10**9+1
for i in range(n):
    a, b, c = map(int, input().split())
    if a >= c:
        continue
    ans = min(ans, b)
if ans == 10**9+1:
    print(-1)
else:
    print(ans)
