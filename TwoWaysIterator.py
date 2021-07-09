a = int(input())
b = int(input())
curNum = a
while curNum > b:
    if not curNum % 2 and curNum // 2 >= b:
        print(":2")
        curNum //= 2
    else:
        print("-1")
        curNum -= 1
