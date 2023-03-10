n, k = map(int, input().split())
a = list(map(int, input().split()))
X, Y = [], []

for _ in range(n):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

R = 0
for i in range(n):
    r = 10**30
    for j in range(k):
        light = a[j] - 1
        d = (X[i] - X[light])**2 + (Y[i] - Y[light])**2
        r = min(r, d)
    R = max(R, r)

print(R**0.5)
