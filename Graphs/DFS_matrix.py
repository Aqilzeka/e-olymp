#DFS_matrix
g = [[0,1,1],  # матрица связности
     [1,1,1],
     [1,0,1]]

ex = set()       # множество посещенных вершин
def dfs(node):   # start - начальная вершина
    ex.add(node)
    for i in range(len(g)):
        if g[node][i] == 1 and i not in ex:
            print(i)
            dfs(i)
dfs(1)
