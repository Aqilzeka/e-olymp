def NSD(a, b): 
    while a*b != 0:
        if a >= b:
            a = a % b
        else:
            b = b % a
    return a + b

list = input().split(" ")
a, b, c, d = int(list[0]),int(list[1]),int(list[2]),int(list[3])

f = False
k = 0
while (not f) and (a/b < c/d):
    a += 1
    b += 1
    k += 1
    n = NSD(a, b)
    #print(n)
    if n > 1:
       a = int(a / n)
       b = int(b / n)
       #print(a, b)
    if a == c and b == d:
        f = True
if not f:
    k = 0

print(k)
