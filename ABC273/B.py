from decimal import Decimal, ROUND_HALF_UP

X, K = map(int, input().split())
y = Decimal(str(X))
for t in range(K+1):
    y = y.quantize(Decimal('1E{i}'.format(i=t)), rounding=ROUND_HALF_UP)

print(int(y))
