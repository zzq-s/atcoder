n = int(input())
N = int(n ** 0.5)
l = []
for i in range(1, N+1):
    if n % i == 0:
        l.append(i)
        if i != n // i:
            l.append(n//i)
l.sort()
print(l)
