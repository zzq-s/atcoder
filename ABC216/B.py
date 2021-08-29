n = int(input())
h = dict()
for i in range(n):
    s, t = input().split()
    if s in h:
        if t in h[s]:
            print('Yes')
            exit()
        else:
            h[s].append(t)
    else:
        h[s] = [t]
print('No')
