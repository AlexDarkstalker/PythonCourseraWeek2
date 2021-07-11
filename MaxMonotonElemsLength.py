num = int(input())
if num:
    curLength = 1
    maxLength = 1
else:
    curLength = 0
    maxLength = 0
sequenceType = 0
while num:
    prevNum = num
    num = int(input())
    if not num:
        break
    if num > prevNum:
        if sequenceType == 1:
            curLength += 1
        else:
            sequenceType = 1
            curLength = 2
    elif num < prevNum:
        if sequenceType == -1:
            curLength += 1
        else:
            sequenceType = -1
            curLength = 2
    else:
        curLength = 1
        sequenceType = 0
    if curLength > maxLength:
        maxLength = curLength
print(maxLength)
