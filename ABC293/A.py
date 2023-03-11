S = list(input())


def swap(i):
    S[i], S[i+1] = S[i+1], S[i]


for i in range(len(S)//2):
    swap(2*i)

print(''.join(S))
