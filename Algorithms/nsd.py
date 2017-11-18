n = input().split(" ")

a, b = int(n[0]), int(n[1])

while a*b != 0:
    if a >= b:
            a = a % b
    else:
            b = b % a
            
print (a + b)
