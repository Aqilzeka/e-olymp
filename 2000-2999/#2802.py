f = open("input.txt", "r").read().split("\n")
o = open('output.txt', 'w')
for i in range(len(f)):
    if i!=0:  o.write("\n")
    o.write(str(bin(int(f[i]))).replace("0b",""))
o.close()
