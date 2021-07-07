a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    longest = a
    short1 = b
    short2 = c
elif b > a and b > c:
    longest = b
    short1 = a
    short2 = c
else:
    longest = c
    short1 = a
    short2 = b
if longest >= short1 + short2:
    print("impossible")
elif longest**2 > short1**2 + short2**2:
    print("obtuse")
elif longest**2 == short1**2 + short2**2:
    print("rectangular")
else:
    print("acute")
