import itertools

n_l = list(map(int, input()))
t = len(n_l)

for i in range(t):
    for j in itertools.combinations(n_l, t-i):
        if sum(j) % 3 == 0:
            print(i)
            exit(0)

print(-1)
