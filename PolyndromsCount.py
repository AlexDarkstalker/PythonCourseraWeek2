num = int(input())
count = 0
i = 0
while i <= num:
    length = 0
    curNum = i
    polyndrom = 0
    numDigits = 0
    while curNum // 10:
        polyndrom = curNum % 10
        curNum //= 10

