def g1(n):
    return int("".join(sorted(str(n))[::-1]))


def g2(n):
    return int("".join(sorted(str(n))))


n, k = map(int, input().split())
for i in range(1, k+1):
    n = g1(n) - g2(n)
print(n)
