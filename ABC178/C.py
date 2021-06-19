n = int(input())
mod = 10**9 + 7
a = 10**n % mod
b = 9**n % mod
c = 8**n % mod
print((a - 2*b % mod + c) % mod)
