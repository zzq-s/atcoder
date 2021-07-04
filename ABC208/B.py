import math
p = int(input())
l = [math.factorial(i) for i in range(1, 11)]
l.reverse()
ans = 0
for i in l:
    while p >= i:
        ans += 1
        p -= i
print(ans)
