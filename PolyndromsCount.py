num = int(input())
count = 0
i = 1
while i <= num:
    curNum = i
    polyndrom = 0
    length = 0
    while curNum:
        length += 1
        curNum //= 10
    curNum = i
    j = 0
    while curNum:
        polyndrom += curNum % 10 * 10**(length - j - 1)
        j += 1
        curNum //= 10
    if i == polyndrom:
        count += 1
    i += 1
print(count)
