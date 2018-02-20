def comb(n):
    mass_c[0], mass_c[1] = 1, 1
    for y in range(2, n):
        for j in range(0, y):
            mass_c[y] += mass_c[j] * mass_c[y - j - 1]
    return mass_c


r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
mass_c = [0 for i in range(51)]
comb(50)
mass = [int(i) for i in r]
print(mass_c)
for i in range(len(mass)):
    if i == 0:
        w.write(str(mass_c[mass[i]/2]))
    else:
        w.write("\n" + str(mass_c[mass[i]/2]))
w.close()
