f = open("input.txt", "r").read().split("\n")
temp = f[0].split(" ")
mass = [int(i) for i in temp]
mass.sort()
out = ""
for i in mass:
    out += str(i)+" "

w = open("output.txt", "w")
w.write(out)
w.close()
