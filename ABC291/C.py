N = int(input())
S = input()

pos = [(0, 0)]
x, y = 0, 0
for i in range(N):
    if S[i] == 'R':
        x += 1
    elif S[i] == 'L':
        x -= 1
    elif S[i] == 'U':
        y += 1
    else:
        y -= 1
    pos.append((x, y))

if len(set(pos)) == len(pos):
    print('No')
else:
    print('Yes')
