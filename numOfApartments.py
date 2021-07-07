a = int(input())
b = int(input())
if not((a - 1) % (b - a + 1)):
    print("YES")
else:
    print("NO")
