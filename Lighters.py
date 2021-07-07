l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
if l1 > l2:
    (l1, l2, r1, r2) = (l2, l1, r2, r1)
if l1 > l3:
    (l1, l3, r1, r3) = (l3, l1, r3, r1)
if l2 > l3:
    (l2, l3, r2, r3) = (l3, l2, r3, r2)
length1 = r1 - l1
length2 = r2 - l2
length3 = r3 - l3
if l2 <= l1 + length1 and (l3 <= l1 + length1 or l3 <= l2 + length2):
    print(0)
elif l2 > l1 + length1 and
