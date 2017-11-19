f = open("input.txt", "r").read().split("\n")
w = open('output.txt', 'w')

for i in range(len(f)):
    if i != 0: w.write("\n")
    x = f[i].split(" ")
    n, m = int(x[0]), int(x[1])
    if (m > n):
        p = n
        n = m
        m = p

    while (m > 0):
        p = n % m
        if (p != 0):
            n = m
            m = p
        else:
            break

    if m==1:
        w.write("YES")
    else:
        w.write("NO")

w.close()
