N = int(input())
A = list(map(int, input().split()))

t = [0] * N
A.sort()
h = set(A)

for i in range(N):
    if A[i] in h:
        h.remove(A[i])
    t[len(h)] += 1

for i in range(N):
    print(t[i])
