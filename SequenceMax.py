new = int(input())
curMax = new
while new:
    new = int(input())
    if new and curMax < new:
        curMax = new
print(curMax)
