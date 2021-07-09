num = int(input())
numFib = 0
if not num:
    numFib = 0
elif num == 1:
    numFib = 1
else:
    i = 0
    fib_n_2 = 0
    fib_n_1 = 1
    while i < num - 1:
        fib_n = fib_n_2 + fib_n_1
        fib_n_2 = fib_n_1
        fib_n_1 = fib_n
        i += 1
    numFib = fib_n
print(numFib)
