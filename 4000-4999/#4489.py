r_file = open("input.txt", "r").read().split("\n")
w_file = open("output.txt", "w")
n = list(r_file[0])
m = int(r_file[1])
mass = []
for i in range(2, m + 2):
    mass.append([])
    temp = r_file[i].split()
    mass[i - 2].append(int(temp[0]))
    mass[i - 2].append(int(temp[1]))
    mass[i - 2].append(int(temp[2]))
#print(n,mass)
for i in range(m):
    #print("i = ",i, "type = ",mass[i][0])
    if i != 0:
        w_file.write("\n")
    if mass[i][0] == 1:
        temp = ""
        for j in range(mass[i][1] - 1, mass[i][2]):
            temp += n[j]
        #print("---------", temp)
        if int(temp) % 11 == 0:
            w_file.write("YES")
        else:
            w_file.write("NO")
    elif mass[i][0] == 2:
        if n[mass[i][1] - 1] == str(mass[i][2]):
            w_file.write("YES")
        else:
            w_file.write("NO")
    #print()

w_file.close()