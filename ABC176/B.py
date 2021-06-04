n = input()
cnt = 0
for i in n:
    cnt += int(i)
print('Yes' if cnt % 9 == 0 else 'No')
