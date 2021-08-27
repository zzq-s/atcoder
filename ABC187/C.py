n = int(input())
l = set(input() for _ in range(n))

for i in l:
    if '!' + i in l:
        print(i)
        exit()
print('satisfiable')
