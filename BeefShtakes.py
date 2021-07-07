k = int(input())
m = int(input())
n = int(input())
sides = n * 2
numTimes = (sides - 1) // k + 1
if sides <= k:
    numTimes = 2
print(numTimes * m)
