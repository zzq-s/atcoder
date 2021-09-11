s = "abcdefghijklmnopqrstuvwxyz"
l = list(map(int, input().split()))
ans = ""
for i in l:
    ans += s[i-1]
print(ans)
