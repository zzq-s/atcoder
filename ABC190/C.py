import itertools
n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(m)]
k = int(input())
cd = [list(map(int, input().split())) for _ in range(k)]

ans = 0
for i in itertools.product(*cd):
    i = set(i)
    cnt = 0
    for a, b in ab:
        if a in i and b in i:
            cnt += 1
    ans = max(ans, cnt)

print(ans)
