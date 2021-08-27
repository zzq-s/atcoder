n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if abs((l[j][1]-l[i][1]) / (l[j][0]-l[i][0])) <= 1:
            ans += 1
print(ans)
