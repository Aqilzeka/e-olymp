n = int(input())
x = 0
temp = 0
temp_a = 0
for i in range(1, n+1):
    if ((i % 10) == 0):
        x += 1
    elif ((i % 2) == 0):
        temp = 1
        temp_a = i
    elif (temp == 1) and ((i % 5) == 0):
        if ((temp_a * i) % 100) == 0:
            x += 2
            temp_a = 0
            temp = 0
        elif ((temp_a * i) % 1000) == 0:
            x += 3
            temp_a = 0
            temp = 0
        else:
            x += 1
            temp = 0
            temp_a = 0
        
print(x)
