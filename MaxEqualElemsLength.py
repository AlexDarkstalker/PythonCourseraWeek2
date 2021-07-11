num = int(input())
if num:
    curLength = 1
    maxLength = 1
else:
    curLength = 0
    maxLength = 0
while num:
    prevNum = num
    num = int(input())
    if num == prevNum:
        curLength += 1
    else:
        curLength = 1
    if curLength > maxLength:
        maxLength = curLength
print(maxLength)
