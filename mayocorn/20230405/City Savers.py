N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

ans = 0
for i in range(N):
    # i番目の勇者がi番目の街を襲う場合
    m = min(A[i], B[i])
    A[i] -= m
    B[i] -= m
    ans += m

    # i+1番目の勇者がi番目の街を襲う場合
    m = min(A[i+1], B[i])
    A[i+1] -= m
    B[i] -= m
    ans += m

print(ans)
