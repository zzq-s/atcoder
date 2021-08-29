n, x = map(int, input().split())
l = list(map(int, input().split()))
print(" ".join(str(i) for i in l if i != x))
