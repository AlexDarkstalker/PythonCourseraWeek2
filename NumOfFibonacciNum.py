num = int(input())
numFib = 0
if not num:
    numFib = 0
elif num == 1:
    numFib = 1
else:
    i = 1
    fib_n_2 = 0
    fib_n_1 = 1
    fib_n = 1
    while fib_n < num:
        fib_n = fib_n_2 + fib_n_1
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
        i += 1
    if fib_n != num:
        numFib = -1
    else:
        numFib = i
print(numFib)
