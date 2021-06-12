x, y = map(int, input().split())
a = [0, 1, 2]
if x == y:
    print(x)
    exit(0)
else:
    a.remove(x)
    a.remove(y)
    print(a[0])
