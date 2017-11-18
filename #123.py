n = int(input())

i5 = n // 5
x = i5
       
while i5 > 0:
    i5 /= 5
    x += int(i5)

print(x)
