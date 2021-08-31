n = int(input())
t = int(n**0.5)
h = set()

for i in range(2, t+1):
    num = i * i
    while num <= n:
        h.add(num)
        num *= i

print(n - len(h))
