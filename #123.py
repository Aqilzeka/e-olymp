import math

n = list(str(math.factorial(int(input()))))
n.reverse()
x = 0
for i in n:
    if i == '0':
        x += 1
    else:
        break
    
print(x)
