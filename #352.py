f = open("input.txt", "r").read().split(" ")

for i in range(len(f)): f[i] = float(f[i])

w = open("output.txt", "w")
w.write(str(min(f)) + '0')
w.close()
