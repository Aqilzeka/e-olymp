r = open("input.txt", "r").read().split("\n")
temp = r[0].split(" ")
n, s, f = int(temp[0]),int(temp[1]),int(temp[2])
g = []
for i in range(n):
    g.append([])
    temp = r[i + 1].split(" ")
    for j in range(n):
        g[i].append(int(temp[j]))
for i in range(n):
    for j in range(n):
        if i == j:
            g[i][j] = 0

arr = [0 for i in range(n)]
def bfs(j, h, f):
    for i in range(n):
        if g[j][i] == 1:
            if arr[i] == 0:
                arr[i] = h + 1
                bfs(i, h + 1, f)
            elif arr[i] > h + 1:
                arr[i] = h + 1
                bfs(i, h + 1, f)

bfs(s-1, 0, f)

w = open("output.txt","w")
w.write(str(arr[f - 1]))
w.close()
