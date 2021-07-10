n, x = map(int, input().split())
l = list(map(int, input().split()))
a = sum(l)
a -= n // 2
print('Yes' if a <= x else 'No')
