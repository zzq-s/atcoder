n = int(input())
l = list(map(int, input().split()))
l.sort()

ans = 1
mod = 10**9 + 7
for i in range(n):
    if l[i] - i <= 0:
        print(0)
        exit()
    else:
        ans = ans * (l[i] - i) % mod
print(ans)
