n, k = map(int, input().split())
l = list(map(int, input().split()))

h = dict()
for i in l:
    h[i] = 0

t = sorted(l)
a, b = divmod(k, n)
t = t[:b]

for i in t:
    h[i] = 1

for i in l:
    if h[i] == 1:
        print(a+1)
    else:
        print(a)
