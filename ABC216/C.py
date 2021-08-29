n = int(input())
l = ""
while n > 0:
    if n % 2 == 0:
        n = n // 2
        l += "B"
    else:
        n -= 1
        l += "A"
l = l[::-1]
print(l)
