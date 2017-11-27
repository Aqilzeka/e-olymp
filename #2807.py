from collections import Counter
f = open("input.txt", "r").read().split("\n")
w = open("output.txt", "w")

list = list(f[1])
c = Counter(list)
for key in c:
    if c[key] % 2 != 0:
        kub = key
    
if kub:
    w.write(kub)
else:
    w.write("Ok")

w.close()
