

r = open("input.txt", "r").read().split("\n")
temp = r[0].split(" ")
n, s, f = int(temp[0]),int(temp[1]),int(temp[2])
g = []
for i in range(n):
    g.append([])
    temp = r[i + 1].split(" ")
    for j in range(n):
        g[i].append(int(temp[j]))
        
ex = set()
data = []
def dfs(node):
    ex.add(node)
    for i in range(len(g)):
        if g[node][i] == 1 and i not in ex:
            data.append(i)
            dfs(i)

dfs(s-1)
w = open("output.txt","w")
w.write(str(data[f-1]))
w.close()
