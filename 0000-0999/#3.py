import math
n = int(input())

c1 = int(math.pow(n,1.0/3) + 0.5)
c2 = int(math.sqrt(n/c1) + 0.5)
c3 = int(n/(c1*c2))
S = int(3*c1*c2*c3+2*(c1*c2+c1*c3+c2*c3)+(c1+c2+c3))
h = int(n-c1*c2*c3)

if h != 0:
    d1 = int(math.sqrt(h)+0.5)
    if(d1*d1>h):
        d1 -= 1
    d2 = int(h/d1)
    S += 3*d1*d2+2*(d1+d2)+1
    h -= d1*d2
    if h != 0:
        S += 3*h+2

print(S)