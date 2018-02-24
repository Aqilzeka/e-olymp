def ROT(str, n):
    abc = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ_.")
    list_in = list(str)
    list_in.reverse()
    out = ""
    for i in list_in:
        out += abc[(abc.index(i) + n) % len(abc)]
    return out


r = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")
for i in r:
    if i == "0":
        break
    temp = i.split(" ")
    print(temp)
    w.write(ROT(temp[1], int(temp[0]))+"\n")
    
w.close()
