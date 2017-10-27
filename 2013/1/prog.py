f = open("in.txt", "r").read().split(" ")

m = int(f[0])
n = int(f[1])

mass = m + m + 5

k = n - mass

w = open('out.txt', 'w')
w.write(str(k))
w.close()
