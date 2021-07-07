A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
if A >= B and A >= C:
    if B <= C:
        if D <= E:
            if B <= D and C <= E:
                print("YES")
            else:
                print("NO")
        else:
            if B <= E and C <= D:
                print("YES")
            else:
                print("NO")
    else:
        if D <= E:
            if C <= D and B <= E:
                print("YES")
            else:
                print("NO")
        else:
            if C <= E and B <= D:
                print("YES")
            else:
                print("NO")
elif B >= A and B >= C:
    if A <= C:
        if D <= E:
            if A <= D and C <= E:
                print("YES")
            else:
                print("NO")
        else:
            if A <= E and C <= D:
                print("YES")
            else:
                print("NO")
    else:
        if D <= E:
            if C <= D and A <= E:
                print("YES")
            else:
                print("NO")
        else:
            if C <= E and A <= D:
                print("YES")
            else:
                print("NO")
elif C >= A and C >= B:
    if A <= B:
        if D <= E:
            if A <= D and B <= E:
                print("YES")
            else:
                print("NO")
        else:
            if A <= E and B <= D:
                print("YES")
            else:
                print("NO")
    else:
        if D <= E:
            if B <= D and A <= E:
                print("YES")
            else:
                print("NO")
        else:
            if B <= E and A <= D:
                print("YES")
            else:
                print("NO")
else:
    print("NO")
