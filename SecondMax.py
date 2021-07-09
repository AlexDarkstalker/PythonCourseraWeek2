num = int(input())
maxNum = num
secondMax = 0
while num:
    num = int(input())
    if secondMax < num < maxNum:
        secondMax = num
    elif num >= maxNum:
        secondMax = maxNum
        maxNum = num
print(secondMax)
