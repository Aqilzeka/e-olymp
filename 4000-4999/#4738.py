f = open("input.txt", "r").read().split("\n")
n = int(f[0])

temp = f[1].split(" ")
mass = [int(i) for i in temp]
mass.sort(reverse=True)
out = ""
for i in mass:
    out += str(i)+" "

w = open("output.txt", "w")
w.write(out)
w.close()
