w = 0
for i in open("input.txt", "r"):
    in_out = 0
    for j in i:
        if j != ' ' and in_out == 0:
            w += 1
            in_out = 1
        elif j == ' ':
            in_out = 0
 

f = open("output.txt", "w")
f.write(str(w))
f.close()
