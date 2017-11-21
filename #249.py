r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
n = int(r[0])
l = r[1].split(" ")

for i in range(n):
    N = int(l[i])
    x = len([i for i in range(1,N+1) if not N % i])

    if (x % 2) == 0:
        w.write('0 ')
    else:
        w.write('1 ')

w.close()
