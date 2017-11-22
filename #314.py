f = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")

n = int(f[0])

for i in range(1,n+1):
    if i != 1: w.write("\n")
    if "+" in f[i]:
        text = f[i].split("+")
        w.write(str(int(text[0])+int(text[1])))
    elif "-" in f[i]:
        text = f[i].split("-")
        w.write(str(int(text[0])-int(text[1])))

w.close()
