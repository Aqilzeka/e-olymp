import math
def prime(x):
    for i in range(3, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False

def function(x):
    if x == 1:
        return False
    if 2 <= x <= 4:
        return True
    if x % 2 == 0:
        return False
    if prime(x) == False:
        return False
    return True

n = int(input())
#print(math.factorial(n), pow(n, 2))

if function(n):
    print("NO")
else:
    print("YES")