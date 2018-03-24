import math

def function(x):
    if x == 1:
        return False
    if 2 <= x <= 4:
        return True
    if x % 2 == 0:
        return False

    return True

n = int(input())

if function(n):
    print("NO")
else:
    print("YES")