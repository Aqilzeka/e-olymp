f = open("input.txt", "r").read().split(" ")
w = open("output.txt", "w")

m = int(f[0])
n = int(f[1])
k = int(f[2])
template = '{:.3f}'

w.write(template.format(float(m / n)))
w.close()
