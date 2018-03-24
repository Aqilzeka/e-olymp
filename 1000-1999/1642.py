import math
n = int(input())
#print(math.factorial(n), pow(n, 2))
if math.factorial(n) % pow(n, 2) == 0:
    print("YES")
else:
    print("NO")
