n = int(input())
k = 0

for i in range(10,100):
    c=int(i*n)
    a=int(i/10+i%10)
    b=int((c/10)%10+c%10+c/100)
    if (a==b):
        k += 1

print(k)
