n = int(input())
for i in range(1, 10**5):
    if (i + 1) * i >= 2*n:
        print(i)
        exit(0)
