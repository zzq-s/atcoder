n = int(input())
l = list(map(int, input().split()))

ans = [0, 0, 0]
for i in l:
    ans[0] += abs(i)
    ans[1] += abs(i)**2
    ans[2] = max(ans[2], abs(i))
ans[1] = ans[1] ** 0.5

for i in ans:
    print(i)
