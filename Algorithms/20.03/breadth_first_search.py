g = [    
    [1,3], # 0
    [0,3,4,5], # 1
    [4,5], # 2
    [0,1,5], # 3
    [1,2], # 4
    [1,2,3] # 5
]

level = [-1] * len(g) 

def bfs(s):
    level[s] = 0
    stack = [s]
    while stack:
        v = stack.pop(0)
        for w in adj[v]: 
            if level[w] is -1: 
                stack.append(w) 
                level[w] = level[v] + 1 

for i in range(len(g)):
    if level[i] is -1:
        bfs(i)
print(level)
