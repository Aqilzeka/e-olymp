r = open("input.txt", "r").read().split("\n")
temp = r[0].split()
n, m = int(temp[0]), int(temp[1])
mass = [[] for i in range(n)]

for i in range(1,m + 1):
  temp = r[i].split()
  mass[int(temp[0]) - 1].append(int(temp[1]) - 1)
  mass[int(temp[1]) - 1].append(int(temp[0]) - 1)

level = [-1] * len(mass)
print(mass)
def bfs(s):
    level[s] = 0
    stack = [s]
    while stack:
        v = stack.pop(0)
        for w in mass[v]:
            if level[w] is -1:
                stack.append(w)
                level[w] = level[v] + 1

bfs(0)
print(level)
w = open("output.txt", "w")
if -1 in level:
    w.write("NO")
else:
    w.write("YES")
w.close()