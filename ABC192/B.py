s = input()
cnt = 0
for i in s:
    cnt += 1
    if cnt % 2 != 0:
        if i.islower():
            continue
        else:
            print('No')
            exit()
    else:
        if i.isupper():
            continue
        else:
            print('No')
            exit()
print('Yes')
