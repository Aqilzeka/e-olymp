import itertools

f = open("input.txt", "r").read().split(" ")
w = open("output.txt", "w")
a = int(f[0])
b = int(f[1])
c = int(f[2])
temp_a = list(str(a))
temp_b = list(str(b))
for i in itertools.permutations(temp_a):
    for j in itertools.permutations(temp_b):
        aa = ""
        for q in i:
            aa += q
        aa = int(aa)
        bb = ""
        for q in j:
            bb += q
        bb = int(bb)
        if (aa + bb == c):
            w.write("YES\n")
            w.write(str(aa)+" "+str(bb))
            exit()
w.write("NO")


