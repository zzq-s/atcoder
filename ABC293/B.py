n = int(input())
A = list(map(int, input().split()))

called = [False] * n

for i in range(len(A)):
    if called[i] == False:
        called[A[i] - 1] = True

ans = []
for i in range(n):
    if not called[i]:
        ans.append(i+1)

print(len(ans))
print(*ans)
