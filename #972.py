import operator

f = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
mass = {}
for i in range(int(f[0])):
    temp = f[i+1].split(" ")
    temp = (int(temp[0])*60*60) + (int(temp[1])*60)+ int(temp[2])
    mass.update({temp:f[i+1]})

mass = sorted(mass.items(), key=operator.itemgetter(0))

for i in mass:
    w.write(i[1]+"\n")
w.close()
