a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == 0 and b != 0:
    print("NO")
elif a == 0 and b == 0:
    print("INF")
elif not(b % a):
    if c == 0:
        print(-b // a)
    elif c != 0 and (b // a != d // c):
        print(-b // a)
    elif c != 0 and (b // a == d // c):
        print("NO")
else:
    print("NO")
