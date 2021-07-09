l1 = int(input())
r1 = int(input())
l2 = int(input())
r2 = int(input())
l3 = int(input())
r3 = int(input())
length1 = r1 - l1
length2 = r2 - l2
length3 = r3 - l3
if r1 < l2:
    distance12 = l2 - r1
elif r2 < l1:
    distance12 = l1 - r2
else:
    distance12 = 0
if r1 < l3:
    distance13 = l3 - r1
elif r3 < l1:
    distance13 = l1 - r3
else:
    distance13 = 0
if r2 < l3:
    distance23 = l3 - r2
elif r3 < l2:
    distance23 = l2 - r3
else:
    distance23 = 0
if (not distance12 and not distance13) or \
        (not distance12 and not distance23) or \
        (not distance13 and not distance23):
    print(0)
elif (distance12 > 0 and length1 >= distance23) or \
        (distance23 > 0 and length1 >= distance23):
    print(1)
elif (distance13 > 0 and length2 >= distance13):
    print(2)
elif distance12 > 0 and length3 >= distance12:
    print(3)
else:
    print(-1)
