r = open("input.txt", "r").read().split("\n")
n = int(r[0])

mass = {}

for i in range(n):
    temp =  r[i+1].split(" - ")
    for j in temp[1].split(", "):
        if mass.get(j) != None:
            mass[j].append(temp[0])
        else:
            mass.update({j:[temp[0]]})

sort_keys = sorted(mass)
#print(mass)
w = open("output.txt", "w")
w.write(str(len(sort_keys)))
for i in sort_keys:
    w.write("\n")
    w.write(i + " - ")
    for j in mass[i]:
        if mass[i].index(j) != 0:
            w.write(", " + j)
        else:
            w.write(j)

