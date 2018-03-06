def function(index):
    if index >= 2 * n:return 0

    min = function(index + 1)
    for i in range(2,k + 1):
        min = max([min, function(index + i)])

    mass[index] = main_mass[index] + min
    return mass[index]

r = open("input.txt", "r").read().split("\n")
n, k = int(r[0]), int(r[2])

main_mass = []
mass = []
main_mass.append(0)

temp = r[1].split(" ")
for i in range(n):
    main_mass.append(int(temp[i]))

for i in range(n):
    main_mass.append(0)
mass = []

for i in range(2000):
    mass.append(0)

w = open("output.txt", "w")
w.write(str(function(0)))
w.close()
