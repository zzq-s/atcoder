n = int(input())
l = list(map(int, input().split()))
print('Yes' if len(set(l)) == n else "No")
