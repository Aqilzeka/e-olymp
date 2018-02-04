

r = open("input.txt", "r").read().split("\n")
mass = [int(i) for i in r[1].split()]
mass.sort()
print(mass)

w = open("output.txt", "w")
for i in range(len(mass)):
    if i == 0: w.write(str(mass[i]))
    else: w.write(" " + str(mass[i]))

w.close()
#exit()
