N = int(input())
X = list(map(int, input().split()))

for i in range(N):
    X.remove(max(X))
for i in range(N):
    X.remove(min(X))

avg = sum(X) / len(X)

print(avg)
