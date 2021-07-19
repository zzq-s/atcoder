n = int(input())
h = set(input() for _ in range(n))
for s in h:
    if "!" + s in h:
        print(s)
        exit()
print("satisfiable")
