x = int(input())
y = int(input())
curRun = x
i = 1
while y > curRun:
    curRun += curRun * 0.1
    i += 1
print(i)
