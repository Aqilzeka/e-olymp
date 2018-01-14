f = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")

for i in range(len(f)):
    if "//" in f[i]:
        temp = f[i].split("//")
        if "->" in temp[0]:
                w.write(temp[0].replace("->", ".") + '//' +temp[1] + '\n')
        else:
            w.write('//' + temp[1] + '\n')
    else:
        if "->" in f[i]:
                w.write(f[i].replace("->", ".") + '\n')
        else:
            w.write(f[i] + '\n')

w.close()
