h, w = map(int, input().split())

a = 0
b = 100
for i in range(h):
    l = list(map(int, input().split()))
    a += sum(l)
    b = min(b, min(l))

print(a - b*h*w)
