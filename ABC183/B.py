x1, y1, x2, y2 = map(int, input().split())
y2 = -y2
x = (-y1)/(y2-y1)*(x2-x1)+x1
print(x)
