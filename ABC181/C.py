n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(i):
        for k in range(j):
            x1, y1 = l[i]
            x2, y2 = l[j]
            x3, y3 = l[k]
            x1 -= x2
            y1 -= y2
            x3 -= x2
            y3 -= y2
            if x1*y3 == x3*y1:
                print("Yes")
                exit(0)

print("No")
