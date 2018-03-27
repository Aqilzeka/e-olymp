n = 4
g = [[0,5,9,100],
     [100,0,2,8],
     [100,100,0,7],
     [4,100,100,0]
    ]

d = g
for i in range(1, n + 1):
    for j in range(0, n - 1):
        for k in range(0, n - 1):
            d[j][k] = min(d[j][k], d[j][i - 1] + d[i - 1][k])

print(d)
