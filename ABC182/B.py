n = int(input())
l = list(map(int, input().split()))

ans = -1
cnt = 0
for i in range(2, 1001):
    a = sum(j % i == 0 for j in l)
    if a > cnt:
        cnt = a
        ans = i
print(ans)
