n = int(input())
l = list(map(int, input().split()))

half = len(l) // 2
t = min(max(l[:half]), max(l[half:]))
print(l.index(t)+1)
