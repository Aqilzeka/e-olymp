def F(x):
 if D[x] == 0:
     D[x] = F(x-1)+F(x-2)+F(x-3)
 return D[x]
D = [0 for i in range(30)]
D[1], D[2], D[3] =1, 2, 4
n = int(input())
print(F(n))