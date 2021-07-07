a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
if b < c:
    (b, c) = (c, b)
if a < c:
    (a, c) = (c, a)
if a < b:
    (a, b) = (b, a)
if y < z:
    (y, z) = (z, y)
if x < z:
    (x, z) = (z, x)
if x < y:
    (x, y) = (y, x)
d1 = (a // x) * (b // y) * (c // z)
d2 = (a // x) * (b // z) * (c // y)
d3 = (a // y) * (b // x) * (c // z)
d4 = (a // y) * (b // z) * (c // x)
d5 = (a // z) * (b // x) * (c // y)
d6 = (a // z) * (b // y) * (c // x)
if d1 <= d2:
    d1 = d2
if d3 <= d4:
    d3 = d4
if d5 <= d6:
    d5 = d6
if d1 >= d3 and d1 >= d5:
    print(d1)
elif d3 >= d1 and d3 >= d5:
    print(d3)
elif d5 >= d1 and d5 >= d3:
    print(d5)
