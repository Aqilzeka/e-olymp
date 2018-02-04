f = open("input.txt", "r").read().split(" ")
w = open("output.txt", "w")

for i in range(len(f)): f[i] = float(f[i])
w.write(str(min(f)) + '0')

w.close()
