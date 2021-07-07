num = int(input())
if num < 3:
    print("NO")
elif not(num % 3):
    print("YES")
elif num < 5:
    print("NO")
elif not(num % 5):
    print("YES")
elif num < 8:
    print("NO")
else:
    print("YES")
