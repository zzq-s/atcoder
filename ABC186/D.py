n = int(input())
l = list(map(int, input().split()))

l.sort()
a = 0
b = 0
for i in range(n):
    a += l[i] * i
    b += l[i] * (n - i - 1)

print(a-b)
