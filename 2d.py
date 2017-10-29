f = open("in.txt", "r").read().split("\n")
n = int(f[0])
A = []
for i in range(1, n+1):
    row = f[i].split()
    for i in range(len(row)):
        row[i] = int(row[i])
    A.append(row)
