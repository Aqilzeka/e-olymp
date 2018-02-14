def s(x, y):
    if x - 1 >= 0 and y + 1 <= n - 1 :

        if mass[x][y + 1][0] < mass[x][y][0] + main_mass[x][y + 1]:
            mass[x][y + 1][0] = mass[x][y][0] + main_mass[x][y + 1]
            mass[x][y + 1][1] += mass[x][y][1] + "R"
            s(x, y + 1)

        if mass[x - 1][y][0] < mass[x][y][0] + main_mass[x - 1][y]:
            mass[x - 1][y][0] = mass[x][y][0] + main_mass[x - 1][y]
            mass[x - 1][y][1] = mass[x][y][1] + "F"
            s(x - 1, y)


    #else:
    #    return mass[0][n - 1][1]
    #print(mass)
    #if x == 0 and y == n - 1:
    #    return mass[0][n - 1][1]


r = open("input.txt", "r").read().split("\n")
temp = r[0].split()
m, n = int(temp[0]), int(temp[1])
main_mass, mass = [], []

for i in range(m):
    main_mass.append([])
    mass.append([])
    temp = r[i + 1].split(" ")
    for j in range(n):
        main_mass[i].append(int(temp[j]))
        mass[i].append([0, ""])

mass[len(main_mass) - 1][0][0] = main_mass[len(main_mass) - 1][0]

print(main_mass, mass)

print(s(len(main_mass) - 1, 0))

print(main_mass, mass)