n = int(input())
if (n // 10) == 1 or (n % 10) >= 5 or not(n % 10):
    print(n, "korov")
elif (n % 10) > 1 and (n % 10 < 5):
    print(n, "korovy")
else:
    print(n, "korova")
