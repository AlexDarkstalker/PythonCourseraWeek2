num = int(input())
i = num
minDiv = num
while i > 1:
    if not num % i:
        minDiv = i
    i -= 1
print(minDiv)
