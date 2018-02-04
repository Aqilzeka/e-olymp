import math
def reverse(a):
    for i in range(len(a)//2):
        b = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = b
    return a
    
def prime(n):
    if (math.factorial(n-1)+1) % n!=0:
        return False
    else:
        return True
        
r = open("input.txt", "r").read().split(" ")
a,b = int(r[0]), int(r[1])
sum = 0
for i in range(a,b):
    if list(str(i)) == reverse(list(str(i))):
        if prime(i):
            sum += 1


#exit()
            
w = open("output.txt", "w")
w.write(str(sum))
w.close()
#exit()
