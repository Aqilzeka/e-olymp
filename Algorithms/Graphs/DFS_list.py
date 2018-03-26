#DFS_list

list_of_adjacency = [
    [],
    [],
    [],
    [],
    []
]
visited = [False for i in range(len(list_of_adjacency ))]

def dfs(v):
    visited[v] = True
    for vertex in list_of_adjacency[v]:
        if not visited[vertex]:
            dfs(vertex)

for c in range(len(list_of_adjacency )):
    if not visited[c]:
        dfs(c)

print(visited)