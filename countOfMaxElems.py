num = int(input())
maxNum = num
countMax = 0
if num:
    countMax = 1
while num:
    num = int(input())
    if num > maxNum:
        maxNum = num
        countMax = 1
    elif num == maxNum:
        countMax += 1
print(countMax)
