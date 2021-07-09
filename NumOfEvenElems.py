new = int(input())
num = 0
if new:
    num = 1 - new % 2
while new:
    new = int(input())
    if new:
        num += 1 - new % 2
print(num)
