n = str(input())
n_1 = ""
n_2 = []

for i in n.split(" "):
    n_1 += str(i)
n_1 = list(n_1)

for i in range(len(n_1) - 1, -1, -1):
    n_2.append(n_1[i])

if n_1 == n_2:
    print("YES")
else:
    print("NO")
