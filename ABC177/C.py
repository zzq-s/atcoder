n = int(input())
l = list(map(int, input().split()))
ans = 0
s = sum(l)

for i in l:
    s -= i
    ans += s * i
print(ans % (10**9+7))
