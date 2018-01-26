r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
n = int(r[0])
mass = [float(i) for i in r[1].split(" ")]
w.write(str(sum(mass)/n))

w.close()
