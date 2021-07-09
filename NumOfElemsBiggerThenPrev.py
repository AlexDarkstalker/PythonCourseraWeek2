first = int(input())
num = 1
count = 0
while first and num:
    num = int(input())
    if num > first:
        count += 1
    first = num
print(count)
