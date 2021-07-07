x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if y2 < y1 or ((x1 - x2) + (y2 - y1)) % 2:
    print("NO")
elif (x2 - x1) <= (y2 - y1):
    print("YES")
