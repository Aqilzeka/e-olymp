f = open("input.txt", "r").read().split("\n")
temp = f[0].split(" ")
n, m = int(temp[0]), int(temp[1])
mass = []
for i in range(m):
    temp = f[i+1].split(" ")
    mass.append([int(temp[0]), int(temp[1])])

g = []
for i in range(n):
    g.append([])
    for j in range(n):
        g[i].append(0)
       # print(g[i][j], end=" ")
    #print()

for i in range(m):
    temp = mass[i]
    x = temp[0] - 1
    y = temp[1] - 1
    g[x][y] = 1
w = open("output.txt", "w")
for i in range(n):
    for j in range(n):
        w.write(str(g[i][j]))
        if j != n - 1:
            w.write(" ")
    if i != n - 1:
        w.write("\n")

