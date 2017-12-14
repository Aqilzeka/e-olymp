import math
n = int(input())
a = 0
for i in range(int(math.sqrt(n))):
    for j in range(int(math.sqrt(n))):
        for y in range(int(math.sqrt(n))):
            if (i**3 + j**3 + y ** 3) == n:
                a = [i,j,y]

if a != 0:
    print(a)
else:
    print(-1)
