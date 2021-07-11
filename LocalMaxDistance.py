num = int(input())
curDistance = -1
minDistance = 10**100
greaterLeft = 0
isLocalMax = 0
countLocalMax = 0
while num:
    prevNum = num
    num = int(input())
    if not num:
        break
    if num > prevNum:
        greaterLeft = 1
        isLocalMax = 0
    elif num < prevNum:
        if greaterLeft:
            greaterLeft = 0
            isLocalMax = 1
            countLocalMax += 1
            if curDistance < minDistance and countLocalMax > 1:
                minDistance = curDistance
            curDistance = 1
        else:
            greaterLeft = 0
            isLocalMax = 0
    else:
        isLocalMax = 0
    if curDistance > -1 and not isLocalMax:
        curDistance += 1
if countLocalMax > 1:
    print(minDistance)
else:
    print(0)
