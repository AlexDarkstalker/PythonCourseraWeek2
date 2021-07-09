num = int(input())
curDel = num
i = 0
while curDel // 2:
    i += curDel % 2
    curDel = curDel // 2
if i:
    print("NO")
else:
    print("YES")
