n = int(input())
l = list(map(int, input().split()))
p = dict()

for i in range(1, n+1):
    p[i] = l[i-1]

q = {v: k for k, v in p.items()}

print(" ".join(str(q[i]) for i in range(1, n+1)))
