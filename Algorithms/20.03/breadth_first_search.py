g = [    
    [1,3],
    [0,3,4,5],
    [4,5],
    [0,1,5],
    [1,2],
    [1,2,3]
]

level = [-1] * len(g) 

def bfs(s):
    level[s] = 0
    stack = [s]
    while stack:
        v = stack.pop(0)
        for w in g[v]:
            if level[w] is -1: 
                stack.append(w) 
                level[w] = level[v] + 1 

for i in range(len(g)):
    if level[i] is -1:
        bfs(i)
print(level)
