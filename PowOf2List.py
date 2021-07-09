num = int(input())
i = 0
curPow = 1
while num >= curPow * 2:
    print(curPow)
    i += 1
    curPow *= 2
print(curPow)
