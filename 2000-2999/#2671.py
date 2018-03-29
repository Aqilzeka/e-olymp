file_r = open("input.txt", "r").read().split("\n")
file_w = open("output.txt", "w")
temp = file_r[0].split()
n, m = int(temp[0]), int(temp[1])
w = int(file_r[1])
mass = []
for i in range(n):
    mass.append([])
    for j in range(m):
        mass[i].append(0)

for i in range(w):
    temp = file_r[i + 2].split()
    x, y = int(temp[0]), int(temp[1])
    mass[x - 1][y - 1] = -1

for i in range(n):
    for j in range(m):
        if mass[i][j] == -1:

            file_w.write("* ")
            #print("*", end=" ")
        else:
            if (i > 0 and  mass[i - 1][j] == -1):
                mass[i][j] += 1
            if (i < n - 1 and mass[i + 1][j] == -1):
                mass[i][j] += 1
            if (j > 0 and mass[i][j - 1] == -1):
                mass[i][j] += 1
            if (j < m - 1 and mass[i][j + 1] == -1):
                mass[i][j] += 1
            if (i > 0 and j > 0 and mass[i - 1][j - 1] == -1):
                mass[i][j] += 1
            if (i > 0 and j < m - 1 and mass[i - 1][j + 1] == -1):
                mass[i][j] += 1
            if (i < n - 1 and j > 0 and mass[i + 1][j - 1] == -1):
                mass[i][j] += 1
            if (i < n - 1 and j < m - 1 and mass[i + 1][j + 1] == -1):
                mass[i][j] += 1
            file_w.write(str(chr(mass[i][j] + 48)))
            #print(chr(mass[i][j] + 48), end="")
            if j < m - 1:
                file_w.write(" ")
                #print(" ", end="")
    if i != n -1:
        file_w.write("\n")
    #print()

w.close()