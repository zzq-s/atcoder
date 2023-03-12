n, q = map(int, input().split())


N = [0] * n
for i in range(q):
    event, x = map(int, input().split())
    if event == 1:
        N[x - 1] += 1
    elif event == 2:
        N[x - 1] += 2
    else:
        print('Yes' if N[x - 1] >= 2 else 'No')
