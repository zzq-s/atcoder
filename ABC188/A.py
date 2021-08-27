a, b = map(int, input().split())
print('Yes' if min(a, b)+3 > max(a, b) else 'No')
