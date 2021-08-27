n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

t = 0
for i in range(n):
    t += a[i] * b[i]
print('Yes' if t == 0 else 'No')
