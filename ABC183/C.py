import itertools
n, k = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]

ans = 0
time = 0
t = [i for i in range(1, n)]

for i in itertools.permutations(t):
    j = [0] + list(i)
    for v in range(n):
        time += l[j[v]][j[(v+1) % n]]
    if time == k:
        ans += 1
    time = 0
print(ans)
