r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
temp = r[0].split()
n, m = int(temp[0]), int(temp[1])
temp = r[1].split()
a, b = int(temp[0]),  int(temp[1])


g = [[] for i in range(n)]

for i in range(m):
  temp = r[i + 2].split()
  g[int(temp[0]) - 1].append(int(temp[1]) - 1)
  g[int(temp[1]) - 1].append(int(temp[0]) - 1)


level = [-1] * n
way = [""] * n
def bfs(s):
    level[s] = 0
    way[s] = str(s)
    stack = [s]
    while stack:
        v = stack.pop(0)
        for w in g[v]:
            if level[w] is -1:
                stack.append(w)
                level[w] = level[v] + 1
                way[w] = way[v] +" " + str(w)

#print(g, level)

for i in range(n):
    if level[i] is -1:
        bfs(i)
#print(way)
w.write(str(level[b - 1])+"\n")

road = way[b - 1].split()
for i in road:
    w.write(str(int(i)+1)+" ")
w.close()