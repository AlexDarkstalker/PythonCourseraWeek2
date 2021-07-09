num = int(input())
i = 1
sum = num
while num:
    num = int(input())
    if num:
        i += 1
    sum += num
print(sum / i)
