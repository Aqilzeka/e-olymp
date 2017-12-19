def is_int(n):
    try:
        return int(n) == float(n)
    except ValueError:
        return -1

def v(a):
    if a != 0:
        return a

n = int(input())
mass = []
first = n
for i in range(int(n**(1/3))):
    k_cub = n**(1/3)
    #print(i, int(k_cub), n )
    if is_int(k_cub) == False:
        mass.append(int(k_cub))

        n -= int(int(k_cub)**3)
    elif is_int(k_cub) == True:
        mass.append(int(k_cub))
        n -= int(int(k_cub)**3)


if sum([i**3 for i in mass]) == first:
    print(mass)
elif sum([i**3 for i in mass]) + 1 == first:
    mass.append(1)
    print(mass)
else:
    mass = -1
    print(mass)



    
