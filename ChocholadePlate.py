n = int(input())
m = int(input())
k = int(input())
if (n > 0) and (k > 0) and (n * m >= k) and (not(k % n) or not(k % m)):
    print("YES")
else:
    print("NO")
