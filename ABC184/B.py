n, x = map(int, input().split())
s = input()

for i in s:
    if i == 'x' and x == 0:
        continue
    elif i == 'x':
        x -= 1
    elif i == 'o':
        x += 1
print(x)
