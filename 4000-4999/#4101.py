n = int(open("input.txt", "r").read())
w = open("output.txt", "w")
mass = []
for i in range(100,1000):
    temp = sum([int(j) for j in list(str(i))])
    if temp == n:
        mass.append(i)
w.write(str(len(mass))+"\n")
print(mass)
for i in range(len(mass)):
    if i == 0:
        w.write(str(mass[i]))
    else:
        w.write("\n" + str(mass[i]))

w.close()
