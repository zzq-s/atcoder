s = input()

if s == 'RSR':
    print(1)
    exit(0)
ans = 0
for i in s:
    if i == 'R':
        ans += 1
print(ans)
