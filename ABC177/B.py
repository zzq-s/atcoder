s = input()
t = input()

ans = len(t)
sum = 0
for i in range(len(s)-len(t)+1):
    for j in range(len(t)):
        if s[i+j] != t[j]:
            sum += 1
    ans = min(ans, sum)
    sum = 0
print(ans)
