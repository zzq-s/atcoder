n = input()
x = n[:-2]
y = int(n[-1])
if y >= 0 and y <= 2:
    print(x+'-')
elif y >= 3 and y <= 6:
    print(x)
else:
    print(x+'+')
