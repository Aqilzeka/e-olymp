n = list(input())
n_new = []
for i in range(len(n) - 1, -1, -1):
    n_new.append(n[i])

if n == n_new:
    print("Yes")
else:
    print("No")
