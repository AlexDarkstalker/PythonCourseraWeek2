num = int(input())
print(num % 10, sep="", end="")
while num // 10:
    num //= 10
    print(num % 10, sep="", end="")
