s, t = input().split()
num = min(len(s), len(t))
for i in range(num):
    if s[i] == t[i]:
        continue
    elif s[i] > t[i]:
        print('No')
        exit()
    elif s[i] < t[i]:
        print('Yes')
        exit()
print('Yes' if len(s) < len(t) else 'No')
