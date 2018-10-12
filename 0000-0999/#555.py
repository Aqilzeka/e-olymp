import itertools


f = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
n = int(f[0])
temp = [int(i) for i in f[1].split()]
mass = []
for i in itertools.combinations(temp,2):
    temp_3 = i
    #print(temp[0], temp[1], end=" - ")
    #print(abs(temp[0] - temp[1]))
    mass.append([abs(temp_3[0] - temp_3[1]),temp_3[0], temp_3[1]])

#print(mass)
temp_1 = [i[0] for i in mass]
#print(mass[temp_1.index(min(temp_1))][0])
temp_2 = [mass[temp_1.index(min(temp_1))][0],mass[temp_1.index(min(temp_1))][1],mass[temp_1.index(min(temp_1))][2]]

w.write(str(mass[temp_1.index(min(temp_1))][0])+"\n")
w.write(str(temp.index(temp_2[1])+1)+" "+str(temp.index(temp_2[2])+1))
w.close()