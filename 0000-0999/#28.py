n = int(input())
point = False
for i in range(1,1000):
    dob = i
    for j in range(1,1000):
        if i < j and i != j:
           dob = dob * j
        if dob == n:
            a = j
            b = i
            point = True
            break
    if point == True:
        break
mass = [a,b]
print(min(mass), max(mass))