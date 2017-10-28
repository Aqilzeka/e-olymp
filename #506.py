f = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
for i in range(len(f)):
    if "//" in f[i]:
        temp = f[i].split("//")
        w.write(temp[0].replace("->", ".") + '//' +temp[1] + '\n')
    else:
        w.write(f[i].replace("->", ".") + '\n')
w.close()


