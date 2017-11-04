i = 0
j = 0
mas = []

for line in open("in.txt", "r").read().split("\n"):
    mas.append([])
    for unit in line.split(" "):
        mas[i].append(unit)
        j += 1
    i += 1
    
#print(mas)

f = open('out.txt', 'w')

for i in range(len(mas)):
    for j in range(len(mas[i])):
        f.write(mas[i][j] + ' ')
    f.write('\n')
f.close()
