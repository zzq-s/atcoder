x, k, d = map(int, input().split())
x = abs(x)
a, b = divmod(x, d)

if a >= k:
    print(abs(x-k*d))
else:
    if (k-a) % 2 == 0:
        print(abs(b))
    else:
        print(abs(b-d))
